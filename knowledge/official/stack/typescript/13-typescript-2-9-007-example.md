##### Example

```ts
class GenericComponent<P> extends React.Component<P> {
  internalProp: P;
}

type Props = { a: number; b: string };

const x = <GenericComponent<Props> a={10} b="hi" />; // OK

const y = <GenericComponent<Props> a={10} b={20} />; // Error
```
