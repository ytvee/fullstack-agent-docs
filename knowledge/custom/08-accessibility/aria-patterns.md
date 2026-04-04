---
category: accessibility
topic: aria-patterns
status: draft
---

## Проблема / Контекст

ARIA (Accessible Rich Internet Applications) is a set of attributes that modify how elements are exposed to assistive technology. The fundamental rule of ARIA is: **no ARIA is better than bad ARIA**. Incorrect ARIA creates a worse experience than plain HTML. shadcn/ui's Radix UI foundation handles most interactive patterns correctly — the patterns below cover what's not automatic, edge cases, and when to use native HTML instead.

---

## Решение

### When NOT to use ARIA (use native HTML instead)

```typescript
// These native elements are accessible for FREE — never replace with ARIA divs:

// Buttons (activatable with Enter + Space, announces "button" role)
<button onClick={fn}>Submit</button>
// NOT: <div role="button" tabIndex={0} onClick={fn} onKeyDown={...}>Submit</div>

// Links (activatable with Enter, announces "link" role)
<a href="/about">About</a>
// NOT: <span role="link" tabIndex={0}>About</span>

// Form controls
<input type="checkbox" id="agree" />
<label htmlFor="agree">I agree</label>
// NOT: <div role="checkbox" aria-checked="false" tabIndex={0}>I agree</div>

// Headings
<h2>Section title</h2>
// NOT: <div role="heading" aria-level={2}>Section title</div>

// Lists
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>
// NOT: <div role="list"><div role="listitem">Item 1</div></div>

// RULE: If a native HTML element does what you need, use it.
// ARIA is for custom widgets that have no native HTML equivalent.
```

---

### Modal / Dialog

```typescript
// shadcn/ui Dialog (Radix UI) handles ALL of this automatically:
// - role="dialog" or role="alertdialog"
// - aria-modal="true"
// - aria-labelledby pointing to the title
// - aria-describedby pointing to the description
// - Focus trap (Tab cycles within the dialog)
// - Escape key closes the dialog
// - Focus returns to trigger on close

import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";

export function DeleteConfirmDialog({ onConfirm }: { onConfirm: () => void }) {
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="destructive">Delete account</Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Delete account</DialogTitle>
          {/* DialogDescription is optional but improves context for screen reader users */}
          <DialogDescription>
            This action cannot be undone. All your data will be permanently deleted.
          </DialogDescription>
        </DialogHeader>
        <DialogFooter>
          {/* First focusable element gets focus when dialog opens */}
          <Button variant="outline">Cancel</Button>
          <Button variant="destructive" onClick={onConfirm}>
            Delete permanently
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}

// For ALERT dialogs (urgent, must be acknowledged): use role="alertdialog"
// In Radix: Dialog doesn't expose role, use AlertDialog component instead
import { AlertDialog, AlertDialogContent, AlertDialogTitle } from "@/components/ui/alert-dialog";
// AlertDialog automatically uses role="alertdialog" + aria-modal="true"
```

---

### Loading states (aria-busy, aria-live)

```typescript
// Pattern 1: aria-busy on the container being loaded
"use client";
import { useState, useTransition } from "react";

export function UserList() {
  const [isPending, startTransition] = useTransition();
  const [users, setUsers] = useState<User[]>([]);

  function refresh() {
    startTransition(async () => {
      const data = await fetchUsers();
      setUsers(data);
    });
  }

  return (
    <div>
      <button onClick={refresh} disabled={isPending}>
        {isPending ? "Loading..." : "Refresh"}
      </button>

      {/* aria-busy tells screen readers "this region is updating" */}
      {/* aria-live="polite" announces changes after the current speech finishes */}
      <div
        role="region"
        aria-label="User list"
        aria-busy={isPending}
        aria-live="polite"
      >
        {isPending ? (
          <p className="sr-only">Loading users...</p>  // audible status for screen readers
        ) : (
          <ul>
            {users.map((u) => <li key={u.id}>{u.name}</li>)}
          </ul>
        )}
      </div>
    </div>
  );
}

// Pattern 2: Status announcements with aria-live
export function FormStatus({ status }: { status: "idle" | "loading" | "success" | "error"; message?: string }) {
  return (
    // aria-live="assertive": interrupts screen reader immediately (for errors)
    // aria-live="polite": waits for current speech to finish (for success)
    // aria-atomic="true": reads the entire content when it changes, not just the diff
    <div
      role="status"
      aria-live={status === "error" ? "assertive" : "polite"}
      aria-atomic="true"
      className="sr-only"  // visually hidden but read by screen readers
    >
      {status === "loading" && "Saving..."}
      {status === "success" && "Saved successfully."}
      {status === "error" && "Error: Failed to save. Please try again."}
    </div>
  );
}
```

---

### Form errors with aria-describedby

```typescript
// src/components/ui/form-field.tsx
// This pattern is already implemented by shadcn/ui FormField + FormMessage
// but here's the underlying ARIA pattern for custom implementations:

"use client";
import { useId } from "react";
import type { FieldError } from "react-hook-form";

interface AccessibleInputProps {
  label: string;
  error?: FieldError;
  required?: boolean;
  description?: string;
}

export function AccessibleInput({
  label,
  error,
  required,
  description,
  ...inputProps
}: AccessibleInputProps & React.InputHTMLAttributes<HTMLInputElement>) {
  const inputId = useId();
  const errorId = useId();
  const descriptionId = useId();

  // Build aria-describedby: include description and/or error ID if they exist
  const describedBy = [
    description ? descriptionId : null,
    error ? errorId : null,
  ]
    .filter(Boolean)
    .join(" ") || undefined;

  return (
    <div className="space-y-1">
      <label htmlFor={inputId} className="text-sm font-medium">
        {label}
        {required && (
          <>
            <span aria-hidden="true" className="text-red-500 ml-1">*</span>
            <span className="sr-only"> (required)</span>
          </>
        )}
      </label>

      {description && (
        <p id={descriptionId} className="text-sm text-muted-foreground">
          {description}
        </p>
      )}

      <input
        id={inputId}
        aria-required={required}
        aria-invalid={!!error}         // tells screen readers the field has an error
        aria-describedby={describedBy} // links to both description and error
        className={cn("input", error && "border-red-500")}
        {...inputProps}
      />

      {error && (
        <p
          id={errorId}
          role="alert"               // announces immediately when it appears
          className="text-sm text-red-600"
        >
          {error.message}
        </p>
      )}
    </div>
  );
}
```

---

### Navigation with aria-current

```typescript
// src/components/nav.tsx
"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";

const navItems = [
  { href: "/dashboard", label: "Dashboard" },
  { href: "/products", label: "Products" },
  { href: "/orders", label: "Orders" },
  { href: "/settings", label: "Settings" },
];

export function Sidebar() {
  const pathname = usePathname();

  return (
    <nav aria-label="Main navigation">
      <ul role="list">  {/* role="list" because CSS might remove list semantics */}
        {navItems.map((item) => {
          const isActive = pathname === item.href || pathname.startsWith(`${item.href}/`);
          return (
            <li key={item.href}>
              <Link
                href={item.href}
                aria-current={isActive ? "page" : undefined}
                // aria-current="page" is the correct value for the current page in a nav
                // Screen readers announce "Dashboard, current page, link"
                className={cn(
                  "nav-link",
                  isActive && "nav-link--active"
                )}
              >
                {item.label}
              </Link>
            </li>
          );
        })}
      </ul>
    </nav>
  );
}
```

---

### Toast notifications

```typescript
// shadcn/ui Toast / Sonner already handles aria-live correctly
// For custom toast implementations:

// src/components/toast-container.tsx
export function ToastContainer({ toasts }: { toasts: Toast[] }) {
  return (
    // role="region" + aria-label for landmark navigation
    // aria-live="polite" so toasts don't interrupt reading
    // For error toasts: use aria-live="assertive"
    <div
      role="region"
      aria-label="Notifications"
      aria-live="polite"
      aria-relevant="additions"  // only announce when items are ADDED (not removed)
      className="fixed bottom-4 right-4 z-50 space-y-2"
    >
      {toasts.map((toast) => (
        <div
          key={toast.id}
          role="status"
          aria-live={toast.variant === "error" ? "assertive" : "polite"}
          className={cn("toast", `toast--${toast.variant}`)}
        >
          {/* Screen reader summary first, then visual content */}
          <span className="sr-only">
            {toast.variant === "error" ? "Error: " : ""}
            {toast.variant === "success" ? "Success: " : ""}
          </span>
          {toast.message}
          <button
            onClick={() => dismissToast(toast.id)}
            aria-label="Dismiss notification"
          >
            <X className="h-4 w-4" aria-hidden="true" />
          </button>
        </div>
      ))}
    </div>
  );
}
```

---

### Combobox / Autocomplete

```typescript
// shadcn/ui Combobox (uses Command + Popover under the hood)
// Radix handles: aria-expanded, aria-haspopup, role="combobox", role="listbox", role="option"

import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "@/components/ui/command";
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";

// For a custom autocomplete, here's the ARIA pattern:
export function CountryAutocomplete({
  value,
  onChange,
  options,
}: {
  value: string;
  onChange: (value: string) => void;
  options: { value: string; label: string }[];
}) {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");
  const inputId = useId();
  const listId = useId();

  const filtered = options.filter((o) =>
    o.label.toLowerCase().includes(query.toLowerCase())
  );

  return (
    <div>
      <label htmlFor={inputId}>Country</label>
      <input
        id={inputId}
        type="text"
        role="combobox"
        aria-expanded={open}
        aria-autocomplete="list"
        aria-controls={listId}  // points to the dropdown list
        aria-activedescendant={value ? `option-${value}` : undefined}
        value={query}
        onChange={(e) => { setQuery(e.target.value); setOpen(true); }}
        onFocus={() => setOpen(true)}
      />
      {open && filtered.length > 0 && (
        <ul
          id={listId}
          role="listbox"
          aria-label="Countries"
          className="dropdown-list"
        >
          {filtered.map((option) => (
            <li
              key={option.value}
              id={`option-${option.value}`}
              role="option"
              aria-selected={value === option.value}
              onClick={() => { onChange(option.value); setOpen(false); }}
              className={cn("dropdown-item", value === option.value && "selected")}
            >
              {option.label}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

---

### Tabs

```typescript
// shadcn/ui Tabs (Radix) handles all ARIA automatically:
// role="tablist", role="tab", role="tabpanel"
// aria-selected, aria-controls, aria-labelledby
// Arrow key navigation between tabs

import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

export function ProductTabs() {
  return (
    <Tabs defaultValue="description">
      {/* TabsList has role="tablist" */}
      <TabsList aria-label="Product information">
        {/* TabsTrigger has role="tab", aria-selected, aria-controls */}
        <TabsTrigger value="description">Description</TabsTrigger>
        <TabsTrigger value="specs">Specifications</TabsTrigger>
        <TabsTrigger value="reviews">Reviews</TabsTrigger>
      </TabsList>

      {/* TabsContent has role="tabpanel", aria-labelledby, tabIndex={0} */}
      <TabsContent value="description">
        <p>Product description here...</p>
      </TabsContent>
      <TabsContent value="specs">
        <dl>...</dl>
      </TabsContent>
      <TabsContent value="reviews">
        <ReviewList />
      </TabsContent>
    </Tabs>
  );
}
```

---

### Accordion

```typescript
// shadcn/ui Accordion (Radix) handles:
// role="button" on trigger, aria-expanded, aria-controls
// Arrow key navigation, Enter/Space activation

// What you still need to provide:
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";

export function FAQAccordion() {
  return (
    // The wrapping element should identify the region
    <section aria-label="Frequently asked questions">
      <h2>FAQ</h2>
      <Accordion type="single" collapsible>
        <AccordionItem value="item-1">
          {/* AccordionTrigger renders as <h3><button> by default in shadcn */}
          <AccordionTrigger>What is your return policy?</AccordionTrigger>
          <AccordionContent>
            {/* Meaningful content — don't put interactive elements inside accordion content
                that would confuse the navigation hierarchy */}
            We accept returns within 30 days of purchase.
          </AccordionContent>
        </AccordionItem>
      </Accordion>
    </section>
  );
}
```

---

## Антипаттерн

```typescript
// BAD 1: Misusing aria-label to "fix" poor design
// If sighted users can't understand it, neither can non-sighted users
<button aria-label="Go to the next page in the product listing">›</button>
// The label is too verbose AND the design is unclear — fix the design instead:
<button>
  <span aria-hidden="true">›</span>
  <span className="sr-only">Next page</span>
</button>

// BAD 2: Duplicate content in aria-label
<img src="/warning.png" alt="Warning" aria-label="Warning icon" />
// alt already provides the text — aria-label creates duplicate announcement

// BAD 3: aria-label on non-interactive elements without a role
<p aria-label="Introduction section">Welcome to our app</p>
// aria-label on a <p> tag does nothing — <p> has no interactive role

// BAD 4: role="presentation" on interactive elements
<button role="presentation">Submit</button>
// This hides the button from assistive technology completely

// BAD 5: Dynamic content without aria-live
const [count, setCount] = useState(0);
// Counter changes but screen reader users never hear the new value
<span>{count} items in cart</span>
// FIX:
<span aria-live="polite" aria-atomic="true">{count} items in cart</span>

// BAD 6: Opening links in a new tab without warning
<a href="/docs" target="_blank">Documentation</a>
// Screen reader users don't know a new tab will open — disorienting
// FIX:
<a href="/docs" target="_blank" rel="noopener noreferrer">
  Documentation
  <span className="sr-only"> (opens in new tab)</span>
  <ExternalLinkIcon className="h-3 w-3" aria-hidden="true" />
</a>
```

---

## Связанные документы

- `knowledge/custom/08-accessibility/wcag-checklist.md` — WCAG 2.2 AA requirements
- `knowledge/custom/05-testing/test-strategy.md` — axe-playwright automated testing
