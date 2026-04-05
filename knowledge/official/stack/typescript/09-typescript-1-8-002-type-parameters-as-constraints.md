## Type parameters as constraints

With TypeScript 1.8 it becomes possible for a type parameter constraint to reference type parameters from the same type parameter list.
Previously this was an error.
This capability is usually referred to as [F-Bounded Polymorphism](https://wikipedia.org/wiki/Bounded_quantification#F-bounded_quantification).
