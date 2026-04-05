#### Update config files.
You will need to update `babel.config.js`, `metro.config.js` and `drizzle.config.ts` files
```js filename='babel.config.js'
module.exports = {
  presets: ['module:@react-native/babel-preset'],
  plugins: [
    [
      'inline-import',
      {
        extensions: ['.sql'],
      },
    ],
  ],
};
```

```js filename="metro.config.js"
const { getDefaultConfig } = require('@react-native/metro-config');

const config = getDefaultConfig(__dirname);

config.resolver.sourceExts.push('sql');

module.exports = config;
```

Make sure to have `dialect: 'sqlite'` and `driver: 'expo'` in Drizzle Kit config
```ts filename="drizzle.config.ts"
import { defineConfig } from 'drizzle-kit';

export default defineConfig({
	schema: './db/schema.ts',
	out: './drizzle',
  dialect: 'sqlite',
	driver: 'expo', // <--- very important
});
```

