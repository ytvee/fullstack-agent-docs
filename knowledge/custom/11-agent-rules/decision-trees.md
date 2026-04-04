---
category: agent-rules
topic: decision-trees
status: draft
---

## Порядок extends в ESLint — строго соблюдать

1. airbnb
2. airbnb-typescript
3. airbnb/hooks
4. next/core-web-vitals
5. prettier              ← ВСЕГДА ПОСЛЕДНИМ

Нарушение порядка → конфликты правил форматирования.
Prettier должен отключить все Airbnb правила связанные
с форматированием, иначе они будут конфликтовать.
