# Boundary Validation

- Validate as close to the input boundary as possible.
- Return structured validation output when the UI needs field-level feedback.
- Use `parse` only when invalid input is a developer bug or startup failure.
- Reuse schemas instead of rebuilding equivalent validation in multiple places.
