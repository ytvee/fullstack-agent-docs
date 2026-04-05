### `abstract` Members Can't Be Marked `async`

Members marked as `abstract` can no longer be marked as `async`.
The fix here is to remove the `async` keyword, since callers are only concerned with the return type.
