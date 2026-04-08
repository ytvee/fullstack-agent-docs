repo-root/
│
├── AGENTS.md                        # Нативно распознаётся Cline
├── .clineignore                     # Исключения из контекста агента
│
├── .clinerules/                     # Rules — всегда активны
│   ├── 00-context.md
│   ├── 10-nextjs-conventions.md
│   ├── 20-quality-gates.md
│   ├── 30-security.md
│   │
│   ├── workflows/                   # Вызов: /имя-файла.md в чате
│   │   ├── new-feature.md
│   │   ├── pr-review.md
│   │   └── release-prep.md
│   │
│   └── hooks/                       # Скрипты-guardrails на события Cline
│       └── PreToolUse               # macOS/Linux: extensionless + chmod +x
│                                    # Windows: PreToolUse.ps1
│
└── .cline/
└── skills/                      # Skills — on-demand по триггеру
├── nextjs-app-router/
│   ├── SKILL.md
│   ├── docs/
│   │   ├── routing.md
│   │   └── error-handling.md
│   ├── templates/
│   │   └── page.tsx
│   └── scripts/
│       └── verify-build.sh
│
└── nextjs-pr-review/
├── SKILL.md
└── docs/
└── checklist.md

repo-root/
│
├── AGENTS.md                        # Нативно распознаётся Cline
├── .clineignore                     # Исключения из контекста агента
│
├── .clinerules/                     # Rules — всегда активны
│   ├── 00-context.md
│   ├── 10-nextjs-conventions.md
│   ├── 20-quality-gates.md
│   ├── 30-security.md
│   │
│   ├── workflows/                   # Вызов: /имя-файла.md в чате
│   │   ├── new-feature.md
│   │   ├── pr-review.md
│   │   └── release-prep.md
│   │
│   └── hooks/                       # Скрипты-guardrails на события Cline
│       └── PreToolUse               # macOS/Linux: extensionless + chmod +x
│                                    # Windows: PreToolUse.ps1
│
└── .cline/
└── skills/                      # Skills — on-demand по триггеру
├── nextjs-app-router/
│   ├── SKILL.md
│   ├── docs/
│   │   ├── routing.md
│   │   └── error-handling.md
│   ├── templates/
│   │   └── page.tsx
│   └── scripts/
│       └── verify-build.sh
│
└── nextjs-pr-review/
├── SKILL.md
└── docs/
└── checklist.md
