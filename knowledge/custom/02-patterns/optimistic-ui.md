---
category: patterns
topic: optimistic-ui
status: draft
---

## Проблема / Контекст

Without optimistic updates, every user interaction that triggers a mutation (delete, toggle, reorder) requires waiting for a server round-trip before the UI reflects the change. For a list of 20 items with a delete button on each, this means a 200–500ms freeze on every delete — visible lag that degrades perceived performance.

React 19 ships `useOptimistic` as a first-class hook specifically designed for this pattern. Unlike manual state management approaches (cloning state, rolling back on error), `useOptimistic` is designed to work alongside Server Actions: the optimistic state is shown immediately, and when the action settles, the component automatically returns to the actual server state (which `revalidatePath` ensures is fresh).

Common mistakes:
- Using `useState` to clone the list and manually manage rollback — verbose and error-prone
- Forgetting to wrap the action call in `startTransition` — `useOptimistic` requires this
- Not providing user feedback when the action fails and the optimistic update reverts
- Using optimistic updates for creates (where you don't know the server-generated ID) without a temporary ID strategy

## Решение

### How `useOptimistic` Works

```
User Action (e.g., click Delete)
         │
         ▼
startTransition(() => {
  applyOptimistic(payload)   ← UI updates IMMEDIATELY with optimistic state
  await serverAction()       ← server call happens concurrently
})
         │
         ▼
Server Action settles:
  - SUCCESS: revalidatePath → server re-renders with real data
             useOptimistic state replaced by server state
  - FAILURE: optimistic state reverts to original
             show error toast
```

The hook signature:
```typescript
const [optimisticState, applyOptimistic] = useOptimistic(
  actualState,           // The real data (from server props)
  reducerFn              // (currentState, payload) => newOptimisticState
)
```

`optimisticState` is what you render. `applyOptimistic` is called synchronously to trigger the optimistic change. `actualState` is the fallback that `useOptimistic` returns to after the transition completes.

### Pattern 1: Optimistic List Delete

The most common use case. Remove item from list immediately; restore it if delete fails.

```typescript
// src/features/projects/ui/project-list.tsx
'use client'

import { useOptimistic, useTransition } from 'react'
import { deleteProject } from '../actions'
import { ProjectCard } from '@/entities/project/ui/project-card'
import { toast } from 'sonner'
import type { Project } from '@/server/db/schema'

interface ProjectListProps {
  projects: Project[]
}

export function ProjectList({ projects }: ProjectListProps) {
  const [isPending, startTransition] = useTransition()
  const [optimisticProjects, removeProject] = useOptimistic(
    projects,
    (state: Project[], idToRemove: string) =>
      state.filter((p) => p.id !== idToRemove)
  )

  function handleDelete(projectId: string) {
    startTransition(async () => {
      removeProject(projectId)

      const result = await deleteProject(projectId)

      if (!result.success) {
        // useOptimistic automatically reverts to `projects` after transition
        // so we just show the error — the item will reappear
        toast.error(result.error ?? 'Failed to delete project')
      } else {
        toast.success('Project deleted')
      }
    })
  }

  return (
    <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
      {optimisticProjects.map((project) => (
        <ProjectCard
          key={project.id}
          project={project}
          onDelete={() => handleDelete(project.id)}
          isDeleting={isPending}
        />
      ))}
      {optimisticProjects.length === 0 && (
        <p className="col-span-full py-8 text-center text-muted-foreground">
          No projects
        </p>
      )}
    </div>
  )
}
```

### Pattern 2: Optimistic Create (with Temporary ID)

For creates, you don't have the server-generated ID. Use a temporary client-side ID. The optimistic item is replaced by the real item after `revalidatePath` triggers a server re-render.

```typescript
// src/features/tasks/ui/task-input.tsx
'use client'

import { useOptimistic, useTransition, useRef } from 'react'
import { createTask } from '../actions'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { toast } from 'sonner'
import type { Task } from '@/server/db/schema'

interface TaskInputProps {
  projectId: string
  tasks: Task[]
}

export function TaskInput({ projectId, tasks }: TaskInputProps) {
  const [isPending, startTransition] = useTransition()
  const inputRef = useRef<HTMLInputElement>(null)

  const [optimisticTasks, addOptimisticTask] = useOptimistic(
    tasks,
    (state: Task[], newTask: Task) => [newTask, ...state]
  )

  function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault()
    const name = inputRef.current?.value.trim()
    if (!name) return

    // Clear input immediately for snappy UX
    if (inputRef.current) inputRef.current.value = ''

    const tempTask: Task = {
      id: `temp-${Date.now()}`,        // Temporary ID — replaced after revalidation
      name,
      projectId,
      completed: false,
      createdAt: new Date(),
      updatedAt: new Date(),
      userId: 'optimistic',             // Will be replaced by server data
    }

    startTransition(async () => {
      addOptimisticTask(tempTask)

      const result = await createTask({ name, projectId })

      if (!result.success) {
        // Restore the input value so user doesn't lose their text
        if (inputRef.current) inputRef.current.value = name
        toast.error(result.error)
      }
    })
  }

  return (
    <div className="space-y-4">
      <form onSubmit={handleSubmit} className="flex gap-2">
        <Input
          ref={inputRef}
          placeholder="Add a task…"
          disabled={isPending}
          className="flex-1"
        />
        <Button type="submit" disabled={isPending}>
          {isPending ? 'Adding…' : 'Add'}
        </Button>
      </form>

      <ul className="space-y-2">
        {optimisticTasks.map((task) => (
          <li
            key={task.id}
            className={task.id.startsWith('temp-') ? 'opacity-60' : 'opacity-100'}
          >
            {task.name}
          </li>
        ))}
      </ul>
    </div>
  )
}
```

### Pattern 3: Optimistic Toggle (Like / Bookmark / Complete)

Toggle state needs to handle the boolean flip and revert correctly.

```typescript
// src/features/tasks/ui/task-item.tsx
'use client'

import { useOptimistic, useTransition } from 'react'
import { toggleTaskComplete } from '../actions'
import { Checkbox } from '@/components/ui/checkbox'
import { cn } from '@/lib/utils'
import { toast } from 'sonner'
import type { Task } from '@/server/db/schema'

interface TaskItemProps {
  task: Task
}

export function TaskItem({ task }: TaskItemProps) {
  const [isPending, startTransition] = useTransition()
  const [optimisticCompleted, setOptimisticCompleted] = useOptimistic(task.completed)

  function handleToggle() {
    startTransition(async () => {
      setOptimisticCompleted(!optimisticCompleted)

      const result = await toggleTaskComplete(task.id, !task.completed)

      if (!result.success) {
        toast.error('Failed to update task')
        // useOptimistic reverts to task.completed automatically
      }
    })
  }

  return (
    <div className="flex items-center gap-3 rounded-md border p-3">
      <Checkbox
        checked={optimisticCompleted}
        onCheckedChange={handleToggle}
        disabled={isPending}
        aria-label={optimisticCompleted ? 'Mark incomplete' : 'Mark complete'}
      />
      <span
        className={cn(
          'text-sm',
          optimisticCompleted && 'text-muted-foreground line-through'
        )}
      >
        {task.name}
      </span>
    </div>
  )
}
```

```typescript
// src/features/tasks/actions.ts
'use server'

import { auth } from '@/server/auth'
import { db } from '@/server/db'
import { tasks } from '@/server/db/schema'
import { eq, and } from 'drizzle-orm'
import { revalidatePath } from 'next/cache'
import type { ActionResult } from '@/types/api'

export async function toggleTaskComplete(
  taskId: string,
  completed: boolean
): Promise<ActionResult> {
  const session = await auth()
  if (!session?.user?.id) return { success: false, error: 'Unauthorized' }

  const task = await db.query.tasks.findFirst({
    where: and(eq(tasks.id, taskId), eq(tasks.userId, session.user.id)),
    columns: { id: true, projectId: true },
  })
  if (!task) return { success: false, error: 'Task not found' }

  await db
    .update(tasks)
    .set({ completed, updatedAt: new Date() })
    .where(eq(tasks.id, taskId))

  revalidatePath(`/projects/${task.projectId}`)
  return { success: true, data: undefined }
}
```

### Pattern 4: Optimistic Reorder (Drag and Drop)

For drag-to-reorder, apply the new order optimistically and persist asynchronously.

```typescript
// src/features/projects/ui/sortable-project-list.tsx
'use client'

import { useOptimistic, useTransition } from 'react'
import { reorderProjects } from '../actions'
import { toast } from 'sonner'
import type { Project } from '@/server/db/schema'

interface SortableProjectListProps {
  projects: Project[]
}

function reorder<T>(list: T[], fromIndex: number, toIndex: number): T[] {
  const result = [...list]
  const [removed] = result.splice(fromIndex, 1)
  result.splice(toIndex, 0, removed)
  return result
}

export function SortableProjectList({ projects }: SortableProjectListProps) {
  const [isPending, startTransition] = useTransition()
  const [optimisticProjects, applyReorder] = useOptimistic(
    projects,
    (state: Project[], { from, to }: { from: number; to: number }) =>
      reorder(state, from, to)
  )

  function handleDrop(fromIndex: number, toIndex: number) {
    if (fromIndex === toIndex) return

    const newOrder = reorder(projects, fromIndex, toIndex)
    const orderedIds = newOrder.map((p) => p.id)

    startTransition(async () => {
      applyReorder({ from: fromIndex, to: toIndex })

      const result = await reorderProjects(orderedIds)

      if (!result.success) {
        toast.error('Failed to save new order')
      }
    })
  }

  return (
    <ul className="space-y-2">
      {optimisticProjects.map((project, index) => (
        <DraggableProjectItem
          key={project.id}
          project={project}
          index={index}
          onDrop={handleDrop}
        />
      ))}
    </ul>
  )
}
```

### Pattern 5: Multiple Independent Optimistic Updates

When a list item needs both toggle and delete, keep separate `useOptimistic` calls or handle both in a single reducer:

```typescript
// Single reducer handling multiple action types
type OptimisticAction =
  | { type: 'delete'; id: string }
  | { type: 'toggle'; id: string; completed: boolean }

const [optimisticTasks, dispatch] = useOptimistic(
  tasks,
  (state: Task[], action: OptimisticAction): Task[] => {
    switch (action.type) {
      case 'delete':
        return state.filter((t) => t.id !== action.id)
      case 'toggle':
        return state.map((t) =>
          t.id === action.id ? { ...t, completed: action.completed } : t
        )
    }
  }
)

// Usage
function handleDelete(id: string) {
  startTransition(async () => {
    dispatch({ type: 'delete', id })
    const result = await deleteTask(id)
    if (!result.success) toast.error(result.error)
  })
}

function handleToggle(id: string, completed: boolean) {
  startTransition(async () => {
    dispatch({ type: 'toggle', id, completed })
    const result = await toggleTaskComplete(id, completed)
    if (!result.success) toast.error(result.error)
  })
}
```

### Loading Indicators with `useTransition`

Use `isPending` from `useTransition` for subtle in-progress feedback without full loading spinners:

```typescript
'use client'
import { useTransition } from 'react'

export function DeleteButton({ projectId }: { projectId: string }) {
  const [isPending, startTransition] = useTransition()

  return (
    <button
      onClick={() =>
        startTransition(async () => {
          await deleteProject(projectId)
        })
      }
      disabled={isPending}
      className="relative"
      aria-label="Delete project"
    >
      {isPending ? (
        <span className="h-4 w-4 animate-spin rounded-full border-2 border-current border-t-transparent" />
      ) : (
        <TrashIcon className="h-4 w-4" />
      )}
    </button>
  )
}
```

## Антипаттерн

```typescript
// BAD 1: Using useState for optimistic state — manual rollback is error-prone
const [localProjects, setLocalProjects] = useState(projects)

async function handleDelete(id: string) {
  const backup = localProjects
  setLocalProjects(prev => prev.filter(p => p.id !== id))

  const result = await deleteProject(id)
  if (!result.success) {
    setLocalProjects(backup)  // Manual rollback — works but verbose
    // Also: backup is stale if another delete happened concurrently
  }
}
// useOptimistic handles this automatically and correctly

// BAD 2: Not wrapping in startTransition — useOptimistic requires it
function handleDelete(id: string) {
  applyOptimistic(id)         // ❌ Must be inside startTransition
  deleteProject(id)
}

// BAD 3: Optimistic state that's too complex — optimistic updates for creates
// with server-generated sequential IDs (will cause key conflicts)
const tempId = Math.random()  // ❌ Not stable — use Date.now() or crypto.randomUUID()

// BAD 4: Showing loading spinner instead of optimistic update — defeats the purpose
async function handleDelete(id: string) {
  setIsDeleting(true)
  await deleteProject(id)     // User waits 300ms seeing nothing
  setIsDeleting(false)
}
// The item should disappear immediately, not after the round-trip

// BAD 5: Forgetting to handle the failure case
startTransition(async () => {
  removeProject(id)
  await deleteProject(id)     // If this fails, useOptimistic reverts but user sees no feedback
  // Always check result and toast on failure
})
```

## Связанные документы

- `02-patterns/crud-pattern.md` — Full CRUD with optimistic delete integrated
- `01-architecture/data-flow.md` — How revalidatePath syncs server state after actions
- `01-architecture/api-design.md` — Server Action patterns called by these hooks
