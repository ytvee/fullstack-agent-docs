#### Step 6 - Setup `metro` config

Create a file `metro.config.js` in root folder and add this code inside:

```js copy filename="metro.config.js"
const { getDefaultConfig } = require('expo/metro-config');
/** @type {import('expo/metro-config').MetroConfig} */
const config = getDefaultConfig(__dirname);
config.resolver.sourceExts.push('sql');
module.exports = config;
```

