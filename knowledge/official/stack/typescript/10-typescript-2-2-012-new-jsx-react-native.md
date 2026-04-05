## New `jsx: react-native`

React-native build pipeline expects all files to have a `.js` extension even if the file contains JSX syntax.
The new [`jsx`](/tsconfig#jsx) value `react-native` will preserve the JSX syntax in the output file, but give it a `.js` extension.
