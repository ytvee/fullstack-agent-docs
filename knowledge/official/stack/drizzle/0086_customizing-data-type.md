### Customizing data type
Every column builder has a `.$type()` method, which allows you to customize the data type of the column. 

This is useful, for example, with unknown or branded types:
```ts
type UserId = number & { __brand: 'user_id' };
type Data = {
	foo: string;
	bar: number;
};

const users = mssqlTable('users', {
  id: int().$type<UserId>().primaryKey(),
  jsonField: json().$type<Data>(),
});
```

