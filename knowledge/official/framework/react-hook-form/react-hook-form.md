# React Hook Form Documentation (aggregated)

> This file aggregates documentation sources from this repository without changing their content.



---

## Source: `README.md`

<div align="center">
    <p align="center">
        <a href="https://react-hook-form.com" title="React Hook Form - Simple React forms validation">
            <img src="https://raw.githubusercontent.com/bluebill1049/react-hook-form/master/docs/logo.png" alt="React Hook Form Logo - React hook custom hook for form validation"  />
        </a>
    </p>
</div>

<p align="center">Performant, flexible and extensible forms with easy to use validation.</p>

## Install

```shellscript
pnpm install && pnpm dev
```

## Backers

Thanks goes to all our backers! [[Become a backer](https://opencollective.com/react-hook-form#backer)].

<a href="https://opencollective.com/react-hook-form#backers">
    <img src="https://opencollective.com/react-hook-form/backers.svg?width=950" />
</a>

## Contributors

Thanks goes to these wonderful people. [[Become a contributor](https://github.com/react-hook-form/documentation/blob/master/CONTRIBUTING.md)].

<a href="https://github.com/react-hook-form/react-hook-form/graphs/contributors">
    <img src="https://opencollective.com/react-hook-form/contributors.svg?width=950" />
</a>


---

## Source: `src/content/advanced-usage.mdx`

---
title: Advanced Usage
description: Build complex and accessible forms
sidebar: advancedLinks
---

## Accessibility (A11y) {#AccessibilityA11y}

React Hook Form has support for native form validation, which lets you validate inputs with your own rules. Since most of us have to build forms with custom designs and layouts, it is our responsibility to make sure those are accessible (A11y).

The following code example works as intended for validation; however, it can be improved for accessibility.

```javascript copy
import { useForm } from "react-hook-form"

export default function App() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm()
  const onSubmit = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label htmlFor="name">Name</label>
      <input
        id="name"
        {...register("name", { required: true, maxLength: 30 })}
      />
      {errors.name && errors.name.type === "required" && (
        <span>This is required</span>
      )}
      {errors.name && errors.name.type === "maxLength" && (
        <span>Max length exceeded</span>
      )}
      <input type="submit" />
    </form>
  )
}
```

The following code example is an improved version by leveraging [ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA).

```javascript copy
import { useForm } from "react-hook-form"

export default function App() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm()
  const onSubmit = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label htmlFor="name">Name</label>

      {/* use aria-invalid to indicate field contain error */}
      <input
        id="name"
        aria-invalid={errors.name ? "true" : "false"}
        {...register("name", { required: true, maxLength: 30 })}
      />

      {/* use role="alert" to announce the error message */}
      {errors.name && errors.name.type === "required" && (
        <span role="alert">This is required</span>
      )}
      {errors.name && errors.name.type === "maxLength" && (
        <span role="alert">Max length exceeded</span>
      )}

      <input type="submit" />
    </form>
  )
}
```

After this improvement, the screen reader will say: _“Name, edit, invalid entry, This is required.”_

---

## Wizard Form / Funnel {#WizardFormFunnel}

It's pretty common to collect user information through different pages and sections. We recommend using a state management library to store user input through different pages or sections. In this example, we are going to use [little state machine](https://github.com/bluebill1049/little-state-machine) as our state management library (you can replace it with [redux](https://github.com/reduxjs/redux) if you are more familiar with it).

**Step 1:** Set up your routes and store.

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-wizard-form-9pg6j"
import { BrowserRouter as Router, Route } from "react-router-dom"
import { StateMachineProvider, createStore } from "little-state-machine"
import Step1 from "./Step1"
import Step2 from "./Step2"
import Result from "./Result"

createStore({
  data: {
    firstName: "",
    lastName: "",
  },
})

export default function App() {
  return (
    <StateMachineProvider>
      <Router>
        <Route exact path="/" component={Step1} />
        <Route path="/step2" component={Step2} />
        <Route path="/result" component={Result} />
      </Router>
    </StateMachineProvider>
  )
}
```

**Step 2:** Create your pages, collect and submit the data to the store and push to the next form/page.

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-wizard-form-9pg6j"
import { useForm } from "react-hook-form"
import { withRouter } from "react-router-dom"
import { useStateMachine } from "little-state-machine"
import updateAction from "./updateAction"

const Step1 = (props) => {
  const { register, handleSubmit } = useForm()
  const { actions } = useStateMachine({ updateAction })
  const onSubmit = (data) => {
    actions.updateAction(data)
    props.history.push("./step2")
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("firstName")} />
      <input {...register("lastName")} />
      <input type="submit" />
    </form>
  )
}

export default withRouter(Step1)
```

**Step 3:** Make your final submission with all the data in the store or display the resulting data.

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-wizard-form-9pg6j"
import { useStateMachine } from "little-state-machine"
import updateAction from "./updateAction"

const Result = (props) => {
  const { state } = useStateMachine(updateAction)

  return <pre>{JSON.stringify(state, null, 2)}</pre>
}
```

Following the above pattern, you should be able to build a wizard form/funnel to collect user input data from multiple pages.

---

## Smart Form Component {#SmartFormComponent}

This idea here is that you can easily compose your form with inputs. We are going to create a `Form` component to automatically collect form data.

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-smart-form-component-forked-iq89z"
import { Form, Input, Select } from "./Components"

export default function App() {
  const onSubmit = (data) => console.log(data)

  return (
    <Form onSubmit={onSubmit}>
      <Input name="firstName" />
      <Input name="lastName" />
      <Select name="gender" options={["female", "male", "other"]} />

      <Input type="submit" value="Submit" />
    </Form>
  )
}
```

Let's have a look what's in each of these components.

`</> Form`

The `Form` component's responsibility is to inject all `react-hook-form` methods into the child component.

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-smart-form-component-forked-iq89z"
import { Children, createElement } from "react"
import { useForm } from "react-hook-form"

export default function Form({ defaultValues, children, onSubmit }) {
  const methods = useForm({ defaultValues })
  const { handleSubmit } = methods

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {Children.map(children, (child) => {
        return child.props.name
          ? createElement(child.type, {
              ...{
                ...child.props,
                register: methods.register,
                key: child.props.name,
              },
            })
          : child
      })}
    </form>
  )
}
```

`</> Input / Select`

Those input components' responsibility is to register them into `react-hook-form`.

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-smart-form-component-forked-iq89z"
export function Input({ register, name, ...rest }) {
  return <input {...register(name)} {...rest} />
}

export function Select({ register, options, name, ...rest }) {
  return (
    <select {...register(name)} {...rest}>
      {options.map((value) => (
        <option key={value} value={value}>
          {value}
        </option>
      ))}
    </select>
  )
}
```

With the `Form` component injecting `react-hook-form`'s `props` into the child component, you can easily create and compose complex forms in your app.

---

## Error Messages {#ErrorMessages}

Error messages are visual feedback to our users when there are issues with their inputs. React Hook Form provides an `errors` object to let you retrieve errors easily. There are several different ways to improve error presentation on the screen.

- #### Register

  You can simply pass the error message to `register`, via the `message` attribute of the validation rule object, like this:

  `<input {...register('test', { maxLength: { value: 2, message: "error message" } })} />`

- #### Optional Chaining

  The `?.` [optional chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining) operator permits reading the `errors` object without worrying about causing another error due to `null` or `undefined`.

  `errors?.firstName?.message`

- #### Lodash `get`

  If your project is using [lodash](https://lodash.com), then you can leverage the lodash [get](https://lodash.com/docs/4.17.15#get) function. Eg:

  `get(errors, 'firstName.message')`

---

## Connect Form {#ConnectForm}

When we are building forms, there are times when our input lives inside of deeply nested component trees, and that's when [FormContext](/docs/useformcontext) comes in handy. However, we can further improve the Developer Experience by creating a `ConnectForm` component and leveraging React's [renderProps](https://reactjs.org/docs/render-props.html). The benefit is you can connect your input with React Hook Form much easier.

```javascript copy
import { FormProvider, useForm, useFormContext } from "react-hook-form"

export const ConnectForm = ({ children }) => {
  const methods = useFormContext()

  return children(methods)
}

export const DeepNest = () => (
  <ConnectForm>
    {({ register }) => <input {...register("deepNestedInput")} />}
  </ConnectForm>
)

export const App = () => {
  const methods = useForm()

  return (
    <FormProvider {...methods}>
      <form>
        <DeepNest />
      </form>
    </FormProvider>
  )
}
```

---

## FormProvider Performance {#FormProviderPerformance}

React Hook Form's [FormProvider](/docs/formprovider) is built upon [React's Context](https://react.dev/learn/passing-data-deeply-with-context) API. It solves the problem where data is passed through the component tree without having to pass props down manually at every level. This also causes the component tree to trigger a re-render when React Hook Form triggers a state update, but we can still optimise our App if required via the example below.

**Note:** Using React Hook Form's [Devtools](/dev-tools) alongside [FormProvider](/docs/formprovider) can cause performance issues in some situations. Before diving deep in performance optimizations, consider this bottleneck first.

```javascript copy sandbox="https://codesandbox.io/s/provider-perf-forked-r24ho"
import { memo } from "react"
import { useForm, FormProvider, useFormContext } from "react-hook-form"

// we can use React.memo to prevent re-render except isDirty state changed
const NestedInput = memo(
  ({ register, formState: { isDirty } }) => (
    <div>
      <input {...register("test")} />
      {isDirty && <p>This field is dirty</p>}
    </div>
  ),
  (prevProps, nextProps) =>
    prevProps.formState.isDirty === nextProps.formState.isDirty
)

export const NestedInputContainer = ({ children }) => {
  const methods = useFormContext()

  return <NestedInput {...methods} />
}

export default function App() {
  const methods = useForm()
  const onSubmit = (data) => console.log(data)
  console.log(methods.formState.isDirty) // make sure formState is read before render to enable the Proxy

  return (
    <FormProvider {...methods}>
      <form onSubmit={methods.handleSubmit(onSubmit)}>
        <NestedInputContainer />
        <input type="submit" />
      </form>
    </FormProvider>
  )
}
```

---

## Controlled mixed with Uncontrolled Components {#ControlledmixedwithUncontrolledComponents}

React Hook Form embraces uncontrolled components but is also compatible with controlled components. Most UI libraries are built to support only controlled components, such as [MUI](https://github.com/mui/material-ui) and [Antd](https://github.com/ant-design/ant-design). But with React Hook Form, the re-rendering of controlled components are also optimized. Here is an example that combines them both with validation.

<TabGroup buttonLabels={["Controller", "Custom Register"]}>

```javascript copy
import { Input, Select, MenuItem } from "@material-ui/core"
import { useForm, Controller } from "react-hook-form"

const defaultValues = {
  select: "",
  input: "",
}

function App() {
  const { handleSubmit, reset, control, register } = useForm({
    defaultValues,
  })
  const onSubmit = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <Controller
        render={({ field }) => (
          <Select {...field}>
            <MenuItem value={10}>Ten</MenuItem>
            <MenuItem value={20}>Twenty</MenuItem>
          </Select>
        )}
        control={control}
        name="select"
        defaultValue={10}
      />

      <Input {...register("input")} />

      <button type="button" onClick={() => reset({ ...defaultValues })}>
        Reset
      </button>
      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-controlled-mixed-with-uncontrolled-forked-c323j"
import { useEffect } from "react"
import { Input, Select, MenuItem } from "@material-ui/core"
import { useForm } from "react-hook-form"

const defaultValues = {
  select: "",
  input: "",
}

function App() {
  const { register, handleSubmit, setValue, reset, watch } = useForm({
    defaultValues,
  })
  const selectValue = watch("select")
  const onSubmit = (data) => console.log(data)

  useEffect(() => {
    register("select")
  }, [register])

  const handleChange = (e) => setValue("select", e.target.value)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <Select value={selectValue} onChange={handleChange}>
        <MenuItem value={10}>Ten</MenuItem>
        <MenuItem value={20}>Twenty</MenuItem>
      </Select>
      <Input {...register("input")} />

      <button type="button" onClick={() => reset({ ...defaultValues })}>
        Reset
      </button>
      <input type="submit" />
    </form>
  )
}
```

</TabGroup>

---

## Custom Hook with Resolver {#CustomHookwithResolver}

You can build a custom hook as a resolver. A custom hook can easily integrate with yup/Joi/Superstruct as a validation method, and to be used inside validation resolver.

- Define a memorized validation schema (or define it outside your component if you don't have any dependencies)
- Use the custom hook, by passing the validation schema
- Pass the validation resolver to the useForm hook

```javascript copy sandbox="https://codesandbox.io/s/custom-hook-with-resolver-v7-cwczk"
import { useCallback } from "react"
import { useForm } from "react-hook-form"
import * as yup from "yup"

const useYupValidationResolver = (validationSchema) =>
  useCallback(
    async (data) => {
      try {
        const values = await validationSchema.validate(data, {
          abortEarly: false,
        })

        return {
          values,
          errors: {},
        }
      } catch (errors) {
        return {
          values: {},
          errors: errors.inner.reduce(
            (allErrors, currentError) => ({
              ...allErrors,
              [currentError.path]: {
                type: currentError.type ?? "validation",
                message: currentError.message,
              },
            }),
            {}
          ),
        }
      }
    },
    [validationSchema]
  )

const validationSchema = yup.object({
  firstName: yup.string().required("Required"),
  lastName: yup.string().required("Required"),
})

export default function App() {
  const resolver = useYupValidationResolver(validationSchema)
  const { handleSubmit, register } = useForm({ resolver })

  return (
    <form onSubmit={handleSubmit((data) => console.log(data))}>
      <input {...register("firstName")} />
      <input {...register("lastName")} />
      <input type="submit" />
    </form>
  )
}
```

---

## Working with virtualized lists {#Workingwithvirtualizedlists}

Imagine a scenario where you have a table of data. This table might contain hundreds or thousands of rows, and each row will have inputs. A common practice is to only render the items that are in the viewport, however this will cause issues as the items are removed from the DOM when they are out of view and re-added. This will cause items to reset to their default values when they re-enter the viewport.

An example is shown below using [react-window](https://github.com/bvaughn/react-window).

<TabGroup buttonLabels={["Form", "Field Array"]}>

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-with-react-window-forked-3j3mq"
import { memo } from "react"
import { FormProvider, useForm, useFormContext } from "react-hook-form"
import { VariableSizeList as List } from "react-window"
import AutoSizer from "react-virtualized-auto-sizer"

const items = Array.from(Array(1000).keys()).map((i) => ({
  title: `List ${i}`,
  quantity: Math.floor(Math.random() * 10),
}))

const WindowedRow = memo(({ index, style, data }) => {
  const { register } = useFormContext()

  return (
    <div style={style}>
      <label>{data[index].title}</label>
      <input {...register(`${index}.quantity`)} />
    </div>
  )
})

export const App = () => {
  const onSubmit = (data) => console.log(data)
  const methods = useForm({ defaultValues: items })

  return (
    <form onSubmit={methods.handleSubmit(onSubmit)}>
      <FormProvider {...methods}>
        <AutoSizer>
          {({ height, width }) => (
            <List
              height={height}
              itemCount={items.length}
              itemSize={() => 100}
              width={width}
              itemData={items}
            >
              {WindowedRow}
            </List>
          )}
        </AutoSizer>
      </FormProvider>
      <button type="submit">Submit</button>
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-usefieldarray-virtual-inputs-ghrey"
import { FixedSizeList } from "react-window"
import { Controller, useFieldArray, useForm } from "react-hook-form"

const items = Array.from(Array(1000).keys()).map((i) => ({
  title: `List ${i}`,
  quantity: Math.floor(Math.random() * 10),
}))

function App() {
  const { control, getValues } = useForm({
    defaultValues: {
      test: items,
    },
  })
  const { fields } = useFieldArray({ control, name: "test" })

  return (
    <FixedSizeList
      width={400}
      height={500}
      itemSize={40}
      itemCount={fields.length}
      itemData={fields}
      itemKey={(i) => fields[i].id}
    >
      {({ style, index, data }) => {
        const defaultValue =
          getValues()["test"][index].quantity ?? data[index].quantity

        return (
          <form style={style}>
            <Controller
              render={({ field }) => <input {...field} />}
              name={`test[${index}].quantity`}
              defaultValue={defaultValue}
              control={control}
            />
          </form>
        )
      }}
    </FixedSizeList>
  )
}
```

</TabGroup>

---

## Testing Form {#TestingForm}

Testing is very important because it prevents your code from having bugs or mistakes. It also guarantees code safety when refactoring the codebase.

We recommend using [testing-library](https://testing-library.com/), because it is simple and tests are more focused on user behavior.

**Step 1:** Set up your testing environment.

Please install [@testing-library/jest-dom](https://github.com/testing-library/jest-dom) with the latest version of `jest`, because react-hook-form uses `MutationObserver` to detect inputs, and to get unmounted from the DOM.

**Note:** If you are using React Native, you don't need to install [@testing-library/jest-dom](https://github.com/testing-library/jest-dom).

```bash copy
npm install -D @testing-library/jest-dom
```

Create `setup.js` to import [@testing-library/jest-dom](https://github.com/testing-library/jest-dom).

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-unit-test-docs-066zk?file=/src/setupTests.js"
import "@testing-library/jest-dom"
```

**Note:** If you are using React Native, you need to create setup.js, define `window` object, and include the following lines in the setup file:

```javascript copy
global.window = {}
global.window = global
```

Finally, you have to update `setup.js` in `jest.config.js` to include the file.

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-unit-test-docs-066zk"
module.exports = {
  setupFilesAfterEnv: ["<rootDir>/setup.js"], // or .ts for TypeScript App
  // ...other settings
}
```

Additionally, you can set up [eslint-plugin-testing-library](https://github.com/testing-library/eslint-plugin-testing-library) and [eslint-plugin-jest-dom](https://github.com/testing-library/eslint-plugin-jest-dom) to follow best practices and anticipate common mistakes when writing your tests.

**Step 2:** Create login form.

We have set the role attribute accordingly. These attributes are helpful for when you write tests, and they improve accessibility. For more information, you can refer to the [testing-library](https://testing-library.com/) documentation.

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-unit-test-docs-066zk?file=/src/App.js"
import { useForm } from "react-hook-form"

export default function App({ login }) {
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm()
  const onSubmit = async (data) => {
    await login(data.email, data.password)
    reset()
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label htmlFor="email">email</label>
      <input
        id="email"
        {...register("email", {
          required: "required",
          pattern: {
            value: /\S+@\S+\.\S+/,
            message: "Entered value does not match email format",
          },
        })}
        type="email"
      />
      {errors.email && <span role="alert">{errors.email.message}</span>}
      <label htmlFor="password">password</label>
      <input
        id="password"
        {...register("password", {
          required: "required",
          minLength: {
            value: 5,
            message: "min length is 5",
          },
        })}
        type="password"
      />
      {errors.password && <span role="alert">{errors.password.message}</span>}
      <button type="submit">SUBMIT</button>
    </form>
  )
}
```

**Step 3:** Write tests.

The following criteria are what we try to cover with the tests:

- Test submission failure.

  We are using `waitFor` util and `find*` queries to detect submission feedback, because the `handleSubmit` method is executed asynchronously.

- Test validation associated with each inputs.

  We are using the `*ByRole` method when querying different elements because that's how users recognize your UI component.

- Test successful submission.

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-unit-test-docs-066zk?file=/src/App.test.js"
import { render, screen, fireEvent, waitFor } from "@testing-library/react"
import App from "./App"

const mockLogin = jest.fn((email, password) => {
  return Promise.resolve({ email, password })
})

it("should display required error when value is invalid", async () => {
  render(<App login={mockLogin} />)

  fireEvent.submit(screen.getByRole("button"))

  expect(await screen.findAllByRole("alert")).toHaveLength(2)
  expect(mockLogin).not.toBeCalled()
})

it("should display matching error when email is invalid", async () => {
  render(<App login={mockLogin} />)

  fireEvent.input(screen.getByRole("textbox", { name: /email/i }), {
    target: {
      value: "test",
    },
  })

  fireEvent.input(screen.getByLabelText("password"), {
    target: {
      value: "password",
    },
  })

  fireEvent.submit(screen.getByRole("button"))

  expect(await screen.findAllByRole("alert")).toHaveLength(1)
  expect(mockLogin).not.toBeCalled()
  expect(screen.getByRole("textbox", { name: /email/i })).toHaveValue("test")
  expect(screen.getByLabelText("password")).toHaveValue("password")
})

it("should display min length error when password is invalid", async () => {
  render(<App login={mockLogin} />)

  fireEvent.input(screen.getByRole("textbox", { name: /email/i }), {
    target: {
      value: "test@mail.com",
    },
  })

  fireEvent.input(screen.getByLabelText("password"), {
    target: {
      value: "pass",
    },
  })

  fireEvent.submit(screen.getByRole("button"))

  expect(await screen.findAllByRole("alert")).toHaveLength(1)
  expect(mockLogin).not.toBeCalled()
  expect(screen.getByRole("textbox", { name: /email/i })).toHaveValue(
    "test@mail.com"
  )
  expect(screen.getByLabelText("password")).toHaveValue("pass")
})

it("should not display error when value is valid", async () => {
  render(<App login={mockLogin} />)

  fireEvent.input(screen.getByRole("textbox", { name: /email/i }), {
    target: {
      value: "test@mail.com",
    },
  })

  fireEvent.input(screen.getByLabelText("password"), {
    target: {
      value: "password",
    },
  })

  fireEvent.submit(screen.getByRole("button"))

  await waitFor(() => expect(screen.queryAllByRole("alert")).toHaveLength(0))
  expect(mockLogin).toBeCalledWith("test@mail.com", "password")
  expect(screen.getByRole("textbox", { name: /email/i })).toHaveValue("")
  expect(screen.getByLabelText("password")).toHaveValue("")
})
```

#### Resolving act warning during test

If you test a component that uses react-hook-form, you might run into a warning like this, even if you didn't write any asynchronous code for that component:

> Warning: An update to MyComponent inside a test was not wrapped in act(...)

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-unit-test-act-warning-docs-yq7uj?file=/src/App.js"
import { useForm } from "react-hook-form"

export default function App() {
  const { register, handleSubmit } = useForm({
    mode: "onChange",
  })
  const onSubmit = (data) => {}

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input
        {...register("answer", {
          required: true,
        })}
      />
      <button type="submit">SUBMIT</button>
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-unit-test-act-warning-docs-yq7uj?file=/src/App.test.js"
import { render, screen } from "@testing-library/react"
import App from "./App"

it("should have a submit button", () => {
  render(<App />)

  expect(screen.getByText("SUBMIT")).toBeInTheDocument()
})
```

In this example, there is a simple form without any apparent async code, and the test merely renders the component and tests for the presence of a button. However, it still logs the warning about updates not being wrapped in `act()`.

This is because react-hook-form internally uses asynchronous validation handlers. In order to compute the formState, it has to initially validate the form, which is done asynchronously, resulting in another render. That update happens after the test function returns, which triggers the warning.

To solve this, wait until some element from your UI appears with `find*` queries. Note that you **must not** wrap your `render()` calls in `act()`. [You can read more about wrapping things in `act` unnecessarily here](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library#wrapping-things-in-act-unnecessarily).

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-unit-test-act-warning-docs-tcb7y?file=/src/App.test.js"
import { render, screen } from "@testing-library/react"
import App from "./App"

it("should have a submit button", async () => {
  render(<App />)

  expect(await screen.findByText("SUBMIT")).toBeInTheDocument()

  // Now that the UI was awaited until the async behavior was completed,
  // you can keep asserting with `get*` queries.
  expect(screen.getByRole("textbox")).toBeInTheDocument()
})
```

---

## Transform and Parse {#TransformandParse}

The native input returns the value in `string` format unless invoked with `valueAsNumber` or `valueAsDate`, you can read more under [this section](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement). However, it's not perfect. We still have to deal with `isNaN` or `null` values. So it's better to leave the transform at the custom hook level. In the following example, we are using the `Controller` to include the functionality of the transform value's input and output. You can also achieve a similar result with a custom `register`.

```javascript copy sandbox="https://codesandbox.io/s/transform-vt3tm"
import { Controller } from "react-hook-form"

const ControllerPlus = ({ control, transform, name, defaultValue }) => (
  <Controller
    defaultValue={defaultValue}
    control={control}
    name={name}
    render={({ field }) => (
      <input
        onChange={(e) => field.onChange(transform.output(e))}
        value={transform.input(field.value)}
      />
    )}
  />
)

// usage below:
<ControllerPlus
  transform={{
    input: (value) => (isNaN(value) || value === 0 ? "" : value.toString()),
    output: (e) => {
      const output = parseInt(e.target.value, 10)
      return isNaN(output) ? 0 : output
    },
  }}
  control={control}
  name="number"
  defaultValue=""
/>
```


---

## Source: `src/content/docs/createFormControl.mdx`

---
title: createFormControl
description: Create form state and ready to be subscribed
sidebar: apiLinks
---

This function create the entire form state subscription and allow you to subscribe update with or without react component. You can use this function without the need of React Context api.

### Props

---

| Name       | Type                        | Description    |
| ---------- | --------------------------- | -------------- |
| `...props` | <TypeText>Object</TypeText> | `UseFormProps` |

### Returns

---

| Name          | Type                           | Description                                                                           |
| ------------- | ------------------------------ | ------------------------------------------------------------------------------------- |
| `formControl` | <TypeText>Object</TypeText>    | control object for `useForm` hook                                                     |
| `control`     | <TypeText>Object</TypeText>    | control object for `useController`, `useFormState`, `useWatch`                        |
| `subscribe`   | <TypeText>Function</TypeText>  | function to [subscribe](/docs/useform/subscribe) for form state update without render |
| `...returns`  | <TypeText>Functions</TypeText> | `useForm` return methods                                                              |

<Admonition type="important" title="Notes">
  - This function is published at **v7.55.0** - This function is completely
  optional, you can consider to use this instead of `useFormContext` API. - You
  may find it useful if you would like to subscribe formsState by skipping react
  re-render.
</Admonition>

<Admonition type="important" title="Rules">
 - You should either use this API or context API
 ```tsx
 const props = createFormControl()

<FormProvider {...props} /> // ❌ You don't need provider

 <input {...props.register('name')} /> // ✅ Direct use method from createFormControl
 ```
</Admonition>

**Examples:**

---

<TabGroup buttonLabels={["Setup", "Subscribe"]}>

```javascript
const { formControl, control, handleSubmit, register } = createFormControl({
  mode: 'onChange',
  defaultValues: {
    firstName: 'Bill'
  }
}})

function App() {
  useForm({
    formControl,
  })

  return (
    <form onSubmit={handleSubmit(data => console.log)}>
      <input {...register('name')} />
      <FormState />
      <Controller />
    </form>
  );
}

function FormState() {
  useFormState({
    control // no longer need context api
  })
}

function Controller() {
  useFormState({
    control // no longer need context api
  })
}
```

```javascript
const { formControl, register } = createFormControl(props)

formControl.subscribe({
  formState: {
    isDirty: true,
    values: true,
  },
  callback: (formState) => {
    if (formState.isDirty) {
      // do something here
    }

    if (formState.values.test.length > 3) {
      // do something here
    }
  },
})

function App() {
  const { register } = useForm({
    formControl,
  })

  return (
    <form>
      <input {...register("test")} />
    </form>
  )
}
```

</TabGroup>


---

## Source: `src/content/docs/formprovider.mdx`

---
title: FormProvider
description: A component to provide React Context
sidebar: apiLinks
---

This component will host context object and allow consuming component to subscribe to context and use [useForm](/docs/useform) props and methods.

### Props

---

This following table applied to `FormProvider`, `useFormContext` accepts no argument.

| Name       | Type                        | Description                                    |
| ---------- | --------------------------- | ---------------------------------------------- |
| `...props` | <TypeText>Object</TypeText> | `FormProvider` requires all `useForm` methods. |

<Admonition type="important" title="Rules">

- Avoid using nested FormProvider

</Admonition>

**Examples:**

---

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-v7-form-context-ytudi"
import { useForm, FormProvider, useFormContext } from "react-hook-form"

export default function App() {
  const methods = useForm()

  const onSubmit = (data) => console.log(data)
  const { register, reset } = methods

  useEffect(() => {
    reset({
      name: "data",
    })
  }, [reset]) // ❌ never put `methods` as the deps

  return (
    <FormProvider {...methods}>
      // pass all methods into the context
      <form onSubmit={methods.handleSubmit(onSubmit)}>
        <NestedInput />
        <input {...register("name")} />
        <input type="submit" />
      </form>
    </FormProvider>
  )
}

function NestedInput() {
  const { register } = useFormContext() // retrieve all hook methods

  return <input {...register("test")} />
}
```


---

## Source: `src/content/docs/usecontroller/controller.mdx`

---
title: Controller
description: Wrapper component for controlled inputs
sidebar: apiLinks
---

## \</> `Controller`: <TypeText>Component</TypeText>

React Hook Form embraces uncontrolled components and native inputs, however it's hard to avoid working with external controlled component such as [React-Select](https://github.com/JedWatson/react-select), [AntD](https://github.com/ant-design/ant-design) and [MUI](https://mui.com/). This wrapper component will make it easier for you to work with them.

### Props

---

The following table contains information about the arguments for `Controller`.

| Name               | Type                                                               | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------ | ------------------------------------------------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`             | <TypeText>[`FieldPath`](/ts#FieldPath "FieldPath type")</TypeText> | ✓        | Unique name of your input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| control            | <TypeText>[`Control`](/ts#Control "Control type")</TypeText>       |          | [`control`](/docs/useform/control) object is from invoking `useForm`. Optional when using `FormProvider`.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `render`           | <TypeText>Function</TypeText>                                      |          | This is a [render prop](https://reactjs.org/docs/render-props.html). A function that returns a React element and provides the ability to attach events and value into the component. This simplifies integrating with external controlled components with non-standard prop names. Provides `onChange`, `onBlur`, `name`, `ref` and `value` to the child component, and also a `fieldState` object which contains specific input state.                                                                                                                        |
| `rules`            | <TypeText>Object</TypeText>                                        |          | Validation rules in the same format for [`register` options](/docs/useform/register#options), which includes:<br/><br/>required, min, max, minLength, maxLength, pattern, validate                                                                                                                                                                                                                                                                                                                                                                             |
| `shouldUnregister` | <TypeText>boolean = false`</TypeText>                              |          | Input will be unregistered after unmount and defaultValues will be removed as well.<br/><br/>**Note:** this prop should be avoided when using with `useFieldArray` as `unregister` function gets called after input unmount/remount and reorder.                                                                                                                                                                                                                                                                                                               |
| `disabled`         | <TypeText>boolean = false`</TypeText>                              |          | `disabled` prop will be returned from `field` prop. Controlled input will be disabled and its value will be omitted from the submission data.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `defaultValue`     | <TypeText>unknown</TypeText>                                       |          | **Important:** Can not apply `undefined` to `defaultValue` or `defaultValues` at `useForm`. <ul><li>You need to either set `defaultValue` at the field-level or `useForm`'s `defaultValues`. If you used <code>defaultValues</code> at <code>useForm</code>, skip using this prop.</li><li>If your form will invoke `reset` with default values, you will need to provide `useForm` with `defaultValues`.</li><li>Calling `onChange` with `undefined` is not valid. You should use `null` or the empty string as your default/cleared value instead.</li></ul> |
| `exact`            | <TypeText>boolean = false</TypeText>                               |          | This prop will enable an exact match for input name subscriptions, default to true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### Return

---

The following table contains information about properties which `Controller` produces.

| Object Name                            | Name                 | Type                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------- | -------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `field`                                | `onChange`           | <TypeText>`(value: any) => void`</TypeText> | A function which sends the input's value to the library.<br/><br/> _It should be assigned to the `onChange` prop of the input and value should **not be `undefined`**._ <br/>This prop update [formState](/docs/useform/formstate) and you should avoid manually invoke [setValue](/docs/useform/setvalue) or other API related to field update.                                                                                                                                                                                                               |
| `field`                                | `onBlur`             | <TypeText>`() => void`</TypeText>           | A function which sends the input's onBlur event to the library. It should be assigned to the input's `onBlur` prop.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `field`                                | `value`              | <TypeText>unknown</TypeText>                | The current value of the controlled component.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `field`                                | `disabled`           | <TypeText>boolean</TypeText>                | The disabled state of the input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `field`                                | `name`               | <TypeText>string</TypeText>                 | Input's name being registered.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `field`                                | `ref`                | <TypeText>React.ref</TypeText>              | A ref used to connect hook form to the input. Assign `ref` to component's input ref to allow hook form to focus the error input.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `fieldState`                           | `invalid`            | <TypeText>boolean</TypeText>                | Invalid state for current input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `fieldState`                           | `isTouched`          | <TypeText>boolean</TypeText>                | Touched state for current controlled input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `fieldState`                           | `isDirty`            | <TypeText>boolean</TypeText>                | Dirty state for current controlled input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `fieldState`                           | `error`              | <TypeText>object</TypeText>                 | error for this specific input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [`formState`](/docs/useform/formstate) | `isDirty`            | <TypeText>boolean</TypeText>                | Set to `true` after the user modifies any of the inputs. <ol><li>**Important:** Make sure to provide all inputs' defaultValues at the useForm, so hook form can have a single source of truth to compare whether the form is dirty.</li><li>File typed input will need to be managed at the app level due to the ability to cancel file selection and [FileList](https://developer.mozilla.org/en-US/docs/Web/API/FileList) object.</li></ol>                                                                                                                  |
| `formState`                            | `dirtyFields`        | <TypeText>object</TypeText>                 | An object with the user-modified fields. Make sure to provide all inputs' defaultValues via useForm, so the library can compare against the `defaultValues` <ol><li>**Important:** Make sure to provide defaultValues at the useForm, so hook form can have a single source of truth to compare each field's dirtiness.</li><li>Dirty fields will **not** represent as `isDirty` formState, because dirty fields are marked field dirty at field level rather the entire form. If you want to determine the entire form state use `isDirty` instead.</li></ol> |
| `formState`                            | `touchedFields`      | <TypeText>object</TypeText>                 | An object containing all the inputs the user has interacted with.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `formState`                            | `defaultValues`      | <TypeText>object</TypeText>                 | The value which has been set at [useForm](/docs/useform)'s defaultValues or updated defaultValues via [reset](/docs/useform/reset) API.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `formState`                            | `isSubmitted`        | <TypeText>boolean</TypeText>                | Set to `true` after the form is submitted. Will remain `true` until the `reset` method is invoked.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `formState`                            | `isSubmitSuccessful` | <TypeText>boolean</TypeText>                | Indicate the form was successfully submitted without any runtime error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `formState`                            | `isSubmitting`       | <TypeText>boolean</TypeText>                | `true` if the form is currently being submitted. `false` otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `formState`                            | `isLoading`          | <TypeText>boolean</TypeText>                | `true` if the form is currently loading async default values.<br/>**Important:** this prop is only applicable to async `defaultValues`                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `formState`                            | `submitCount`        | <TypeText>number</TypeText>                 | Number of times the form was submitted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `formState`                            | `isValid`            | <TypeText>boolean</TypeText>                | Set to `true` if the form doesn't have any errors.<br/><br/>`setError` has no effect on `isValid` formState, `isValid` will always derived via the entire form validation result.                                                                                                                                                                                                                                                                                                                                                                              |
| `formState`                            | `isValidating`       | <TypeText>boolean</TypeText>                | Set to `true` during validation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `formState`                            | `errors`             | <TypeText>object</TypeText>                 | An object with field errors. There is also an [ErrorMessage](/docs/useformstate/errormessage) component to retrieve error message easily.                                                                                                                                                                                                                                                                                                                                                                                                                      |

**Examples:**

---

**Web**

<TabGroup buttonLabels={["TS", "JS"]}>

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-v6-controller-ts-jwyzw"
import ReactDatePicker from "react-datepicker"
import { TextField } from "@material-ui/core"
import { useForm, Controller } from "react-hook-form"

type FormValues = {
  ReactDatepicker: string
}

function App() {
  const { handleSubmit, control } = useForm<FormValues>()

  return (
    <form onSubmit={handleSubmit((data) => console.log(data))}>
      <Controller
        control={control}
        name="ReactDatepicker"
        render={({ field: { onChange, onBlur, value, ref } }) => (
          <ReactDatePicker
            onChange={onChange} // send value to hook form
            onBlur={onBlur} // notify when input is touched/blur
            selected={value}
          />
        )}
      />

      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-v7-controller-5h1q5"
import ReactDatePicker from "react-datepicker"
import { TextField } from "@material-ui/core"
import { useForm, Controller } from "react-hook-form"

function App() {
  const { handleSubmit, control } = useForm()

  return (
    <form onSubmit={handleSubmit((data) => console.log(data))}>
      <Controller
        control={control}
        name="ReactDatepicker"
        render={({ field: { onChange, onBlur, value, ref } }) => (
          <ReactDatePicker
            onChange={onChange}
            onBlur={onBlur}
            selected={value}
          />
        )}
      />

      <input type="submit" />
    </form>
  )
}
```

</TabGroup>

**React Native**

```javascript copy sandbox="https://snack.expo.io/@bluebill1049/react-hook-form-v7---controller" expo
import { Text, View, TextInput, Button, Alert } from "react-native"
import { useForm, Controller } from "react-hook-form"

export default function App() {
  const {
    control,
    handleSubmit,
    formState: { errors },
  } = useForm({
    defaultValues: {
      firstName: "",
      lastName: "",
    },
  })
  const onSubmit = (data) => console.log(data)

  return (
    <View>
      <Controller
        control={control}
        rules={{
          required: true,
        }}
        render={({ field: { onChange, onBlur, value } }) => (
          <TextInput
            placeholder="First name"
            onBlur={onBlur}
            onChangeText={onChange}
            value={value}
          />
        )}
        name="firstName"
      />
      {errors.firstName && <Text>This is required.</Text>}

      <Controller
        control={control}
        rules={{
          maxLength: 100,
        }}
        render={({ field: { onChange, onBlur, value } }) => (
          <TextInput
            placeholder="Last name"
            onBlur={onBlur}
            onChangeText={onChange}
            value={value}
          />
        )}
        name="lastName"
      />

      <Button title="Submit" onPress={handleSubmit(onSubmit)} />
    </View>
  )
}
```

### Video

---

The following video showcases what's inside Controller and how its been built.

<YouTube youTubeId="N2UNk_UCVyA" />

<Admonition type="tip" >

- It's important to be aware of each prop's responsibility when working with external controlled components, such as MUI, AntD, Chakra UI. Controller acts as a "spy" on your input by reporting and setting value.
  - **onChange**: send data back to hook form
  - **onBlur**: report input has been interacted (focus and blur)
  - **value**: set up input initial and updated value
  - **ref**: allow input to be focused with error
  - **name**: give input an unique name
    The following codesandbox demonstrate the usages:
  - [MUI and other components](https://codesandbox.io/s/react-hook-form-v7-controller-5h1q5)
  - [Chakra UI components](https://codesandbox.io/s/chakra-ui-5mp8g)
- Do not `register` input again. This component is made to take care of the registration process.

  ```javascript
  <Controller
    name="test"
    render={({ field }) => {
      // return <input {...field} {...register('test')} />; ❌ double up the registration
      return <input {...field} /> // ✅
    }}
  />
  ```

- Customise what value gets sent to hook form by transforming the value during `onChange`.
  ```javascript
  <Controller
    name="test"
    render={({ field }) => {
      // sending integer instead of string.
      return (
        <input
          {...field}
          onChange={(e) => field.onChange(parseInt(e.target.value))}
        />
      )
    }}
  />
  ```

</Admonition>


---

## Source: `src/content/docs/useform/clearerrors.mdx`

---
title: clearErrors
description: Clear form errors
sidebar: apiLinks
---

## \</> `clearErrors:` <TypeText>(name?: string | string[]) => void</TypeText>

This function can manually clear errors in the form.

### Props

---

| Type                           | Description             | Example                                 |
| ------------------------------ | ----------------------- | --------------------------------------- |
| <TypeText>undefined</TypeText> | Remove all errors.      | `clearErrors()`                         |
| <TypeText>string</TypeText>    | Remove single error.    | `clearErrors("yourDetails.firstName")`  |
| <TypeText>string[]</TypeText>  | Remove multiple errors. | `clearErrors(["yourDetails.lastName"])` |

- `undefined`: reset all errors
- `string`: reset the error on a single field or by key name.

  ```javascript
  register("test.firstName", { required: true })
  register("test.lastName", { required: true })
  clearErrors("test") // will clear both errors from test.firstName and test.lastName
  clearErrors("test.firstName") // for clear single input error
  ```

- `string[]`: reset errors on the given fields

<Admonition type="important" title="Rules">

- This method does not affect the validation rules attached to inputs and does not
  impact <code>formState.isValid</code>.

</Admonition>

**Examples**

---

<TabGroup buttonLabels={["TS", "JS"]}>

```tsx sandbox="https://codesandbox.io/s/react-hook-form-v7-ts-clearerrors-w3ymx"
import * as React from "react"
import { useForm } from "react-hook-form"

type FormInputs = {
  firstName: string
  lastName: string
  username: string
}

const App = () => {
  const {
    register,
    formState: { errors },
    handleSubmit,
    clearErrors,
  } = useForm<FormInputs>()

  const onSubmit = (data: FormInputs) => {
    console.log(data)
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("firstName", { required: true })} />
      <input {...register("lastName", { required: true })} />
      <input {...register("username", { required: true })} />
      <button type="button" onClick={() => clearErrors("firstName")}>
        Clear First Name Errors
      </button>
      <button
        type="button"
        onClick={() => clearErrors(["firstName", "lastName"])}
      >
        Clear First and Last Name Errors
      </button>
      <button type="button" onClick={() => clearErrors()}>
        Clear All Errors
      </button>
      <input type="submit" />
    </form>
  )
}
```

```javascript sandbox="https://codesandbox.io/s/react-hook-form-v7-clearerrors-w5tl6"
import * as React from "react"
import { useForm } from "react-hook-form"

const App = () => {
  const {
    register,
    formState: { errors },
    handleSubmit,
    clearErrors,
  } = useForm()
  const onSubmit = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("firstName", { required: true })} />
      <input {...register("lastName", { required: true })} />
      <input {...register("username", { required: true })} />
      <button type="button" onClick={() => clearErrors("firstName")}>
        Clear First Name Errors
      </button>
      <button
        type="button"
        onClick={() => clearErrors(["firstName", "lastName"])}
      >
        Clear First and Last Name Errors
      </button>
      <button type="button" onClick={() => clearErrors()}>
        Clear All Errors
      </button>
      <input type="submit" />
    </form>
  )
}
```

</TabGroup>


---

## Source: `src/content/docs/useform/control.mdx`

---
title: control
description: Take control of the form
sidebar: apiLinks
---

## \</> `control:` <TypeText>Object</TypeText>

This object contains methods for registering components into React Hook Form.

<Admonition type="important" title="Rules">

**Important:** do not access any of the properties inside this object directly. It's for internal usage only.

</Admonition>

**Examples:**

---

<TabGroup buttonLabels={["TS", "JS"]}>

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-v6-controller-ts-jwyzw"
import { useForm, Controller } from "react-hook-form"
import { TextField } from "@material-ui/core"

type FormInputs = {
  firstName: string
}

function App() {
  const { control, handleSubmit } = useForm<FormInputs>()
  const onSubmit = (data: FormInputs) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <Controller
        render={({ field }) => <input {...field} />}
        name="firstName"
        control={control}
        defaultValue=""
      />

      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-v7-controller-5h1q5"
import { useForm, Controller } from "react-hook-form"

function App() {
  const { control } = useForm()

  return (
    <Controller
      render={({ field }) => <input {...field} />}
      name="firstName"
      control={control}
      defaultValue=""
    />
  )
}
```

</TabGroup>


---

## Source: `src/content/docs/useform/form.mdx`

---
title: Form
description: Take care of form submission
sidebar: apiLinks
---

## \</> `Form:` <TypeText>Component</TypeText>

**Note**: This component is currently in **BETA**

This component is optional and it takes care of the form submission by closely aligning with the standard native form.

By default, we will send a POST request with your form submission data as [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData). You can supply `headers` prop to avoid FormData to be submitted and use `application/json` instead.

- Progressively enhancement for your form.
- Support both React Web and React Native.
- Take care of form submission handling.

```javascript
<Form
  action="/api"
  method="post" // default to post
  onSubmit={() => {}} // function to be called before the request
  onSuccess={() => {}} // valid response
  onError={() => {}} // error response
  validateStatus={(status) => status >= 200} // validate status code
/>
```

### Props

---

All props are optional

| Name             | Type                                               | Description                                                                                                                                                      | Example                                                                                                            |
| ---------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `control`        | <TypeText>`Control`</TypeText>                     | [`control`](/docs/useform/control) object provided by invoking `useForm`. Optional when using `FormProvider`.                                                    | <CodeArea withOutCopy rawData="<Form control={control} />"/>                                                       |
| `children`       | <TypeText>`React.ReactNode`</TypeText>             |                                                                                                                                                                  |
| `render`         | <TypeText>`Function`</TypeText>                    | Render prop function suitable for headless component.                                                                                                            | <CodeArea withOutCopy rawData="<Form render={({ submit }) => <View/>} />" />                                       |
| `onSubmit`       | <TypeText>`Function`</TypeText>                    | Function invoked after successful validation.                                                                                                                    | <CodeArea withOutCopy rawData="<Form onSubmit={({ data }) => mutation(data)} />"/>                                 |
| `onSuccess`      | <TypeText>`Function`</TypeText>                    | Function called after successful request to the server.                                                                                                          | <CodeArea withOutCopy rawData="<Form onSuccess={({ response }) => {}} />" />                                       |
| `onError`        | <TypeText>`Function`</TypeText>                    | Function called after failed request to the server.<br/><br/>`setError` function will be called to update errors state. `root.server` will be used as error key. | <CodeArea withOutCopy rawData="<Form onError={({ response }) => {}} />" />                                         |
| `headers`        | <TypeText>`Record<string, string>`</TypeText>      | Request headers object.                                                                                                                                          | <CodeArea withOutCopy rawData="<Form headers={{ accessToken:  'xxx', 'Content-Type':  'application/json'  }} />"/> |
| `validateStatus` | <TypeText>`(status: number) => boolean`</TypeText> | Function to validate status code.                                                                                                                                | <CodeArea withOutCopy rawData="<Form validateStatus={status => status === 200} />" />                              |

<Admonition type="important" title="Rules">

- If want to prepare or omit submission data, please use [`handleSubmit`](/docs/useform/handlesubmit) or `onSubmit`.
  ```javascript
  const { handleSubmit, control } = useForm();
  const onSubmit =(data) => callback(prepareData(data))
  <form onSubmit={handleSubmit(onSubmit)} />
  // or
  <Form
    onSubmit={({ data }) => {
      console.log(data)
    }}
  />
  ```
- Progressive Enhancement only applicable for SSR framework.

  ```javascript
  const { handleSubmit, control } = useForm({
    progressive: true
  });

  <Form onSubmit={onSubmit} control={control} action="/api/test" method="post">
    <input {...register("test", { required: true })} />
  </Form>

  // Renders

  <form action="/api/test" method="post">
    <input required name="test" />
  </form>
  ```

</Admonition>
 
**Examples:**

---

**React Web**

```javascript copy
import { useForm, Form } from "react-hook-form"

function App() {
  const {
    control,

    register,

    formState: { isSubmitSuccessful, errors },
  } = useForm({
    // progressive: true, optional prop for progressive enhancement
  })

  return (
    <div>
      // Use action prop to make post submission with formData
      <Form
        action="/api"
        control={control}
        onSuccess={() => {
          alert("Success")
        }}
        onError={() => {
          alert("error")
        }}
      >
        {" "}
        <input {...register("name")} />
        {isSubmitSuccessful && <p>Form submit successful.</p>}
        {errors?.root?.server && <p>Form submit failed.</p>}
        <button>submit</button>
      </Form>
      // Manual form submission
      <Form
        onSubmit={async ({ formData, data, formDataJson, event }) => {
          await fetch("api", {
            method: "post",

            body: formData,
          })
        }}
      >
        {" "}
        <input {...register("test")} /> <button>submit</button>
      </Form>
    </div>
  )
}
```

**React Native**

```javascript copy
import { useForm, Form } from "react-hook-form"
function App() {
  const {
    control,
    register,
    formState: { isSubmitSuccessful, errors },
  } = useForm()
  return (
    <Form
      action="/api"
      control={control}
      render={({ submit }) => {
        ;<View>
          {isSubmitSuccessful && <Text>Form submit successful.</Text>}

          {errors?.root?.server && <Text>Form submit failed.</Text>}
          <Button onPress={() => submit()} />
        </View>
      }}
    />
  )
}
```


---

## Source: `src/content/docs/useform/formstate.mdx`

---
title: formState
description: State of the form
sidebar: apiLinks
---

import formStateUseEffect from "@/components/codeExamples/formStateUseEffect"
import formStateUseEffectTs from "@/components/codeExamples/formStateUseEffectTs"
import formState from "@/components/codeExamples/formState"
import formStateTs from "@/components/codeExamples/formStateTs"

## \</> `formState:` <TypeText>`Object`</TypeText>

This object contains information about the entire form state. It helps you to keep on track with the user's interaction with your form application.

### Return

---

| Name                 | Type                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `isDirty`            | <TypeText>boolean</TypeText> | Set to `true` after the user modifies any of the inputs.<ul><li>**Important:** make sure to provide all inputs' `defaultValues` at the `useForm`, so hook form can have a single source of truth to compare whether the form is dirty.<CodeArea withOutCopy rawData={`const {\n  formState: { isDirty, dirtyFields },\n  setValue\n} = useForm({ defaultValues: { test: "" } })\n\n// isDirty: true ✅\nsetValue('test', 'change')\n\n// isDirty: false because there getValues() === defaultValues ❌\nsetValue('test', '')`}/></li><li>File typed input will need to be managed at the app level due to the ability to cancel file selection and [FileList](https://developer.mozilla.org/en-US/docs/Web/API/FileList) object.</li><li>Do not support custom object, Class or File object.</li></ul> |
| `dirtyFields`        | <TypeText>object</TypeText>  | An object with the user-modified fields. Make sure to provide all inputs' `defaultValues` via `useForm`, so the library can compare against the `defaultValues.`<ul><li>**Important:** make sure to provide `defaultValues` at the `useForm`, so hook form can have a single source of truth to compare each field's dirtiness.</li><li>Dirty fields will **not** represent as `isDirty` `formState`, because dirty fields are marked field dirty at field level rather the entire form. If you want to determine the entire form state use `isDirty` instead.</li></ul>                                                                                                                                                                                                                               |
| `touchedFields`      | <TypeText>object</TypeText>  | An object containing all the inputs the user has interacted with.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `defaultValues`      | <TypeText>object</TypeText>  | The value which has been set at [useForm](/docs/useform)'s `defaultValues` or updated `defaultValues` via [reset](/docs/useform/reset) API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `isSubmitted`        | <TypeText>boolean</TypeText> | Set to `true` after the form is submitted. Will remain `true` until the `reset` method is invoked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `isSubmitSuccessful` | <TypeText>boolean</TypeText> | Indicate the form was successfully submitted without any runtime error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `isSubmitting`       | <TypeText>boolean</TypeText> | `true` if the form is currently being submitted. `false` otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `isLoading`          | <TypeText>boolean</TypeText> | `true` if the form is currently loading async default values.<ul><li>**Important:** this prop is only applicable to async `defaultValues`<CodeArea withOutCopy rawData={`const {\n  formState: { isLoading }\n} = useForm({\n  defaultValues: async () => await fetch('/api')\n})`}/></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `submitCount`        | <TypeText>number</TypeText>  | Number of times the form was submitted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `isValid`            | <TypeText>boolean</TypeText> | Set to `true` if the form doesn't have any errors.<ul><li>`setError` has no effect on `isValid` `formState`, `isValid` will always derived via the entire form validation result.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `isValidating`       | <TypeText>boolean</TypeText> | Set to `true` during validation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `validatingFields`   | <TypeText>object</TypeText>  | Capture fields which are getting async validation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `errors`             | <TypeText>object</TypeText>  | An object with field errors. There is also an [ErrorMessage](/docs/useformstate/errormessage) component to retrieve error message easily.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `disabled`           | <TypeText>boolean</TypeText> | Set to true if the form is disabled via the disabled prop in [useForm](/docs/useform).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `isReady`            | <TypeText>boolean</TypeText> | Set to true when `formState` subscription setup is ready. <ul><li><p>Renders children before the parent completes setup. If you're using `useForm` methods (eg. `setValue`) in a child before the subscription is ready, it can cause issues. Use an `isReady` flag to ensure the form is initialized before updating state from the child.</p><CodeArea withOutCopy rawData={`const {\n setValue,\n formState: { isReady }\n} = useForm();\n\n// Parent component: ✅ \nuseEffect(() => setValue('test', 'data'), []) \n\n// Children component: ✅ \nuseEffect(() => isReady && setValue('test', 'data'), [isReady])`}/></li></ul>                                                                                                                                                                   |

<Admonition type="important" title="Rules">

<ul>
  <li>
    Returned `formState` is wrapped with a
    [Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
    to improve render performance and skip extra logic if specific state is not
    subscribed to. Therefore make sure you invoke or read it before a render in
    order to enable the state update.
  </li>

  <li>
    `formState` is updated in batch. If you want to subscribe to `formState` via
    `useEffect`, make sure that you place the entire `formState` in the optional
    array.

    <TabGroup buttonLabels={["snippet", "example"]}>

    ```javascript
    useEffect(() => {
      if (formState.errors.firstName) {
        // do the your logic here
      }
    }, [formState]) // ✅
    // ❌ [formState.errors] will not trigger the useEffect
    ```

    <CodeArea rawData={formStateUseEffect} tsRawData={formStateUseEffectTs}/>

  </TabGroup>
  </li>

  <li>
    Pay attention to the logical operator when subscription to `formState`.

    <CodeArea
            rawData={`// ❌ formState.isValid is accessed conditionally,

// so the Proxy does not subscribe to changes of that state
return <button disabled={!formState.isDirty || !formState.isValid} />;

// ✅ read all formState values to subscribe to changes
const { isDirty, isValid } = formState;
return <button disabled={!isDirty || !isValid} />;
`}
/>

  </li>
</ul>

</Admonition>

**Examples**

---

<CodeArea
  rawData={formState}
  tsRawData={formStateTs}
  url="https://codesandbox.io/s/react-hook-form-v6-formstate-forked-tyqlp"
  tsUrl="https://codesandbox.io/s/react-hook-form-v6-ts-formstate-forked-5sxs3"
/>

### Video

---

<YouTube youTubeId="4kzd572NbkM" />


---

## Source: `src/content/docs/useform/getfieldstate.mdx`

---
title: getFieldState
description: State of the field
sidebar: apiLinks
---

## \</> `getFieldState:` <TypeText>`(name: string, formState?: Object) => ({isDirty, isTouched, invalid, error})`</TypeText>

This method is introduced in react-hook-form ([v7.25.0](https://github.com/react-hook-form/react-hook-form/releases/tag/v7.25.0)) to return individual field state. It's useful in case you are trying to retrieve nested field state in a typesafe way.

### Props

---

| Name      | Type                          | Description                                                                                                                                                                         |
| --------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`    | <TypeText>`string`</TypeText> | registered field name.                                                                                                                                                              |
| formState | <TypeText>`object`</TypeText> | This is an optional prop, which is only required if `formState` is not been read/subscribed from the `useForm`, `useFormContext` or `useFormState`. Read rules for more information |

### Return

---

| Name      | Type                                           | Description                                                                                 |
| --------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `isDirty` | <TypeText>`boolean`</TypeText>                 | field is modified.<br/>**Condition:** subscribe to `dirtyFields`.                           |
| isTouched | <TypeText>`boolean`</TypeText>                 | field has received a focus and blur event.<br/>**Condition:** subscribe to `touchedFields`. |
| invalid   | <TypeText>`boolean`</TypeText>                 | field is not valid.<br/>**Condition:** subscribe to `errors`.                               |
| error     | <TypeText>`undefined \| FieldError`</TypeText> | field error object.<br/>**Condition:** subscribe to `errors`.                               |

<Admonition type="important" title="Rules">

- name needs to match a registered field name.
  ```javascript
  getFieldState("test")
  getFieldState("test") // ✅ register input and return field state
  getFieldState("non-existent-name") // ❌ will return state as false and error as undefined
  ```
- `getFieldState` works by subscribing to the form state update, and you can subscribe to the formState in the following ways:
  - You can subscribe at the `useForm`, `useFormContext` or `useFormState`. This is will establish the form state subscription and `getFieldState` second argument will no longer be required.

    ```javascript
    const {
      register,
      formState: { isDirty },
    } = useForm()
    register("test")
    getFieldState("test") // ✅
    ```

    ```javascript
    const { isDirty } = useFormState()
    register("test")
    getFieldState("test") // ✅
    ```

    ```javascript
    const {
      register,
      formState: { isDirty },
    } = useFormContext()
    register("test")
    getFieldState("test") // ✅
    ```

  - When form state subscription is not setup, you can pass the entire `formState` as the second optional argument by following the example below:
    ```javascript
    const { register } = useForm()
    register("test")
    const { isDirty } = getFieldState("test") // ❌ formState isDirty is not subscribed at useForm
    const { register, formState } = useForm()
    const { isDirty } = getFieldState("test", formState) // ✅ formState.isDirty subscribed
    const { formState } = useFormContext()
    const { touchedFields } = getFieldState("test", formState) // ✅ formState.touchedFields subscribed
    ```

</Admonition>

**Examples**

---

```javascript copy sandbox="https://codesandbox.io/s/getfieldstate-jvekk"
import * as React from "react"

import { useForm } from "react-hook-form"

export default function App() {
  const {
    register,
    getFieldState,
    formState: { isDirty, isValid },
  } = useForm({
    mode: "onChange",

    defaultValues: {
      firstName: "",
    },
  })

  // you can invoke before render or within the render function

  const fieldState = getFieldState("firstName")

  return (
    <form>
      <input {...register("firstName", { required: true })} />{" "}
      <p>{getFieldState("firstName").isDirty && "dirty"}</p>{" "}
      <p>{getFieldState("firstName").isTouched && "touched"}</p>
      <button
        type="button"
        onClick={() => console.log(getFieldState("firstName"))}
      >
        field state
      </button>
    </form>
  )
}
```


---

## Source: `src/content/docs/useform/getvalues.mdx`

---
title: getValues
description: Get form values
sidebar: apiLinks
---

## \</> `getValues:` <TypeText>`(payload?: string | string[]) => Object`</TypeText>

An optimized helper for reading form values. The difference between `watch` and `getValues` is that `getValues` **will not** trigger re-renders or subscribe to input changes.

### Props

---

| Name         | Type            | Description                                               |
| ------------ | --------------- | --------------------------------------------------------- |
| `fieldNames` | `undefined`     | Returns the entire form values.                           |
|              | `string`        | Gets the value at path of the form values.                |
|              | `array`         | Returns an array of the value at path of the form values. |
| `config`     | `dirtyFields`   | Returns only dirty fields                                 |
|              | `touchedFields` | Return only touchedFields                                 |

**Examples:**

---

The example below shows what to expect when you invoke `getValues` method.

```jsx copy
<input {...register("root.test1")} />

<input {...register("root.test2")} />
```

| Name                                            | Output                              |
| ----------------------------------------------- | ----------------------------------- |
| `getValues()`                                   | `{ root: { test1: '', test2: ''} }` |
| `getValues("root")`                             | `{ test1: '', test2: ''}`           |
| `getValues("root.firstName")`                   | `''`                                |
| `getValues(["yourDetails.lastName"])`           | `['']`                              |
| `getValues(undefined, { dirtyFields: true })`   | `{ root: { test1: '', test2: ''} }` |
| `getValues(undefined, { touchedFields: true })` | `{ root: { test1: '', test2: ''} }` |

<Admonition type="important" title="Rules">

- It will return `defaultValues` from `useForm` before the **initial** render.

</Admonition>

**Examples:**

---

<TabGroup buttonLabels={["TS", "JS", "Types"]}>

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-v7-ts-getvalues-txsfg"
import { useForm } from "react-hook-form"

type FormInputs = {
  test: string
  test1: string
}

export default function App() {
  const { register, getValues } = useForm<FormInputs>()

  return (
    <form>
      <input {...register("test")} />
      <input {...register("test1")} />

      <button
        type="button"
        onClick={() => {
          const values = getValues() // { test: "test-input", test1: "test1-input" }
          const singleValue = getValues("test") // "test-input"
          const multipleValues = getValues(["test", "test1"]) // ["test-input", "test1-input"]
        }}
      >
        Get Values
      </button>
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-v7-getvalues-2eioh"
import { useForm } from "react-hook-form"

export default function App() {
  const { register, getValues } = useForm()

  return (
    <form>
      <input {...register("test")} />
      <input {...register("test1")} />

      <button
        type="button"
        onClick={() => {
          const values = getValues() // { test: "test-input", test1: "test1-input" }
          const singleValue = getValues("test") // "test-input"
          const multipleValues = getValues(["test", "test1"])
          // ["test-input", "test1-input"]
        }}
      >
        Get Values
      </button>
    </form>
  )
}
```

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-v7-ts-getvalues-txsfg"
import React from "react"
import { useForm } from "react-hook-form"

// Flat input values
type Inputs = {
  key1: string
  key2: number
  key3: boolean
  key4: Date
}

export default function App() {
  const { register, getValues } = useForm<Inputs>()

  getValues()

  return <form />
}

// Nested input values
type Inputs1 = {
  key1: string
  key2: number
  key3: {
    key1: number
    key2: boolean
  }
  key4: string[]
}

export default function Form() {
  const { register, getValues } = useForm<Inputs1>()

  getValues()
  // function getValues(): Record<string, unknown>
  getValues("key1")
  // function getValues<"key1", unknown>(payload: "key1"): string
  getValues("key2")
  // function getValues<"key2", unknown>(payload: "key2"): number
  getValues("key3.key1")
  // function getValues<"key3.key1", unknown>(payload: "key3.key1"): unknown
  getValues<string, number>("key3.key1")
  // function getValues<string, number>(payload: string): number
  getValues<string, boolean>("key3.key2")
  // function getValues<string, boolean>(payload: string): boolean
  getValues("key4")
  // function getValues<"key4", unknown>(payload: "key4"): string[]

  return <form />
}
```

</TabGroup>


---

## Source: `src/content/docs/useform/handlesubmit.mdx`

---
title: handleSubmit
description: Ready to send to the server
sidebar: apiLinks
---

## \</> `handleSubmit:` <TypeText>`((data: Object, e?: Event) => Promise<void>, (errors: Object, e?: Event) => Promise<void>) => Promise<void>`</TypeText>

This function will receive the form data if form validation is successful.

### Props

---

| Name               | Type                                                                | Description            |
| ------------------ | ------------------------------------------------------------------- | ---------------------- |
| SubmitHandler      | <TypeText>`(data: Object, e?: Event) => Promise<void>`</TypeText>   | A successful callback. |
| SubmitErrorHandler | <TypeText>`(errors: Object, e?: Event) => Promise<void>`</TypeText> | An error callback.     |

<Admonition type="important" title="Rules">

- `disabled` inputs will appear as `undefined` values in form values. If you want to prevent users from updating an input and wish to retain the form value, you can use `readOnly` or disable the entire &lt;fieldset /&gt;. Here is an [example](https://codesandbox.io/s/react-hook-form-disabled-inputs-oihxx).
- `handleSubmit` function will not swallow errors that occurred inside your onSubmit callback, so we recommend you to try and catch inside async request and handle those errors gracefully for your customers.

  ```javascript
  const onSubmit = async () => {
    // async request which may result error
    try {
      // await fetch()
    } catch (e) {
      // handle your error
    }
  }

  return <form onSubmit={handleSubmit(onSubmit)} />
  ```

</Admonition>

**Examples:**

---

**Sync**

<TabGroup buttonLabels={["TS", "JS"]}>

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-handlesubmit-ts-v7-lcrtu"
import { useForm, SubmitHandler, SubmitErrorHandler } from "react-hook-form"

type FormValues = {
  firstName: string
  lastName: string
  email: string
}

export default function App() {
  const { register, handleSubmit } = useForm<FormValues>()
  const onSubmit: SubmitHandler<FormValues> = (data) => console.log(data)
  const onError: SubmitErrorHandler<FormValues> = (errors) =>
    console.log(errors)

  return (
    <form onSubmit={handleSubmit(onSubmit, onError)}>
      <input {...register("firstName")} />
      <input {...register("lastName")} />
      <input type="email" {...register("email")} />

      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-handlesubmit-v7-uqmiy"
import { useForm } from "react-hook-form"

export default function App() {
  const { register, handleSubmit } = useForm()
  const onSubmit = (data, e) => console.log(data, e)
  const onError = (errors, e) => console.log(errors, e)

  return (
    <form onSubmit={handleSubmit(onSubmit, onError)}>
      <input {...register("firstName")} />
      <input {...register("lastName")} />
      <button type="submit">Submit</button>
    </form>
  )
}
```

</TabGroup>

**Async**

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-async-submit-validation-kpx0o"
import { useForm } from "react-hook-form";

const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

function App() {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const onSubmit = async data => {
    await sleep(2000);
    if (data.username === "bill") {
      alert(JSON.stringify(data));
    } else {
      alert("There is an error");
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label htmlFor="username">User Name</label>
      <input placeholder="Bill" {...register("username"} />

      <input type="submit" />
    </form>
  );
}
```

### Video

---

The following video tutorial explains the `handleSubmit` API in detail.

<YouTube youTubeId="KzcPKB9SOEk" />


---

## Source: `src/content/docs/useform/register.mdx`

---
title: register
description: Register uncontrolled/controlled inputs
sidebar: apiLinks
---

## \</> `register:` <TypeText>`(name: string, options?: RegisterOptions) => ({ ref, name, onChange, onBlur })`</TypeText>

This method allows you to register an input or select element and apply validation rules to React Hook Form. Validation rules are all based on the HTML standard and also allow for custom validation methods.

### Props

---

| Name      | Type                                 | Description       |
| --------- | ------------------------------------ | ----------------- |
| `name`    | <TypeText>string</TypeText>          | Input's name.     |
| `options` | <TypeText>RegisterOptions</TypeText> | Input's behavior. |

### Return

---

| Name       | Type                               | Description                                               |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| `ref`      | <TypeText>React.ref</TypeText>     | React element ref used to connect hook form to the input. |
| `name`     | <TypeText>string</TypeText>        | Input's name being registered.                            |
| `onChange` | <TypeText>ChangeHandler</TypeText> | `onChange` prop to subscribe the input change event.      |
| `onBlur`   | <TypeText>ChangeHandler</TypeText> | `onBlur` prop to subscribe the input blur event.          |

<Admonition type="note">

This is how submitted values will look like:

| Input Name                                        | Submit Result                                             |
| ------------------------------------------------- | --------------------------------------------------------- |
| <TypeText>register("firstName")</TypeText>        | <TypeText>`{ firstName: value }`</TypeText>               |
| <TypeText>register("name.firstName")</TypeText>   | <TypeText>`{ name: { firstName: value } }`</TypeText>     |
| <TypeText>register("name.firstName.0")</TypeText> | <TypeText>`{ name: { firstName: [ value ] } }`</TypeText> |

</Admonition>

### Options

---

By selecting the register option, the API table below will get updated.

<TabGroup buttonLabels={["validation", "validation and error message"]}>

<div style={{ background: 'var(--color-options)', padding: 20 }}>

| Name                                                                          | Description                                                                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ref`<TypeText pre>React.Ref</TypeText>                                       | React element `ref`                                                                                                                                                                                                                                                                                                            |
| `required`<TypeText pre>boolean</TypeText>                                    | Indicates that the input must have a value before the form can be submitted.<br/><br/>**Note:** This config aligns with web constrained API for required input validation, for object or array type of input use validate function instead.                                                                                    |
| `maxLength`<TypeText pre>number</TypeText>                                    | The maximum length of the value to accept for this input.                                                                                                                                                                                                                                                                      |
| `minLength`<TypeText pre>number</TypeText>                                    | The minimum length of the value to accept for this input.                                                                                                                                                                                                                                                                      |
| `max`<TypeText pre>number</TypeText>                                          | The maximum value to accept for this input.                                                                                                                                                                                                                                                                                    |
| `min`<TypeText pre>number</TypeText>                                          | The minimum value to accept for this input.                                                                                                                                                                                                                                                                                    |
| `pattern`<TypeText pre>RegExp</TypeText>                                      | The regex pattern for the input.<br/><br/>**Note:** `RegExp` with the `/g` flag keeps track of the last index where a match occurred.                                                                                                                                                                                          |
| `validate`<TypeText pre>Function \|<br/>`Record<string, Function>`</TypeText> | Validate function will be executed on its own without depending on other validation rules included in the required attribute.<br/><br/>**Note:** for object or array input data, it's recommended to use the validate function for validation as the other rules mostly apply to string, array of strings, number and boolean. |
| `valueAsNumber`<TypeText pre>boolean</TypeText>                               | Returns `Number` normally. If something goes wrong `NaN` will be returned.<br/><ul><li>`valueAs` process is happening **before** validation.</li><li>Only applies to number input, but without any data manipulation.</li><li>Does not transform `defaultValue` or `defaultValues`.</li></ul>                                  |
| `valueAsDate`<TypeText pre>boolean</TypeText>                                 | Returns `Date` normally. If something goes wrong `Invalid Date` will be returned.<br/><ul><li>`valueAs` process is happening **before** validation.</li><li>Only applies to input.</li><li>Does not transform `defaultValue` or `defaultValues`.</li></ul>                                                                     |
| `setValueAs`<TypeText pre>\<T\>(value: any) => T</TypeText>                   | Return input value by running through the function.<br/><ul><li>`valueAs` process is happening **before** validation. Also, `setValueAs` is ignored if either `valueAsNumber` or `valueAsDate` are true.</li><li>Only applies to text input.</li><li>Does not transform `defaultValue` or `defaultValues`.</li></ul>           |
| `disabled`<TypeText pre>boolean = false</TypeText>                            | Set `disabled` to `true` will lead input value to be `undefined` and input control to be disabled.<br/><ul><li>`disabled` prop will also omit built-in validation rules.</li><li>For schema validation, you can leverage the `undefined` value returned from input or context object.</li></ul>                                |
| `onChange`<TypeText pre>(e: SyntheticEvent) => void</TypeText>                | `onChange` function event to be invoked in the change event.                                                                                                                                                                                                                                                                   |
| `onBlur`<TypeText pre>(e: SyntheticEvent) => void</TypeText>                  | `onBlur` function event to be invoked in the blur event.                                                                                                                                                                                                                                                                       |
| `value`<TypeText pre>unknown</TypeText>                                       | Set up `value` for the registered input. This prop should be utilised inside `useEffect` or invoke once, each re-run will update or overwrite the input value which you have supplied.                                                                                                                                         |
| `shouldUnregister`<TypeText pre>boolean</TypeText>                            | Input will be unregistered after unmount and `defaultValues` will be removed as well.<br/><br/>**Note:** this prop should be avoided when using with `useFieldArray` as unregister function gets called after input unmount/remount and reorder.                                                                               |
| `deps`<TypeText pre>string \| string[]</TypeText>                             | Validation will be triggered for the dependent inputs, it only limited to register api not trigger.                                                                                                                                                                                                                            |

</div>

<div style={{ background: 'var(--color-options)', padding: 20 }}>

| Name                                                                                                           | Description                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ref`<TypeText pre>React.Ref</TypeText>                                                                        | React element `ref`                                                                                                                                                                                                                                                                                                            |
| `required`<TypeText pre>string \|<br/><PrettyObject value={{value: 'boolean', message: 'string'}}/></TypeText> | Indicates that the input must have a value before the form can be submitted. <br/><br/>**Note:** This config aligns with web constrained API for required input validation, for object or array type of input use validate function instead.                                                                                   |
| `maxLength`<TypeText pre><PrettyObject value={{value: 'number', message: 'string'}}/></TypeText>               | The maximum length of the value to accept for this input.                                                                                                                                                                                                                                                                      |
| `minLength`<TypeText pre><PrettyObject value={{value: 'number', message: 'string'}}/></TypeText>               | The minimum length of the value to accept for this input.                                                                                                                                                                                                                                                                      |
| `max`<TypeText pre><PrettyObject value={{value: 'number', message: 'string'}}/></TypeText>                     | The maximum value to accept for this input.                                                                                                                                                                                                                                                                                    |
| `min`<TypeText pre><PrettyObject value={{value: 'number', message: 'string'}}/></TypeText>                     | The minimum value to accept for this input.                                                                                                                                                                                                                                                                                    |
| `pattern`<TypeText pre><PrettyObject value={{value: 'RegExp', message: 'string'}}/></TypeText>                 | The regex pattern for the input.<br/><br/>**Note:** `RegExp` with the `/g` flag keeps track of the last index where a match occurred.                                                                                                                                                                                          |
| `validate`<TypeText pre>Function \|<br/>`Record<string, Function>`</TypeText>                                  | Validate function will be executed on its own without depending on other validation rules included in the required attribute.<br/><br/>**Note:** for object or array input data, it's recommended to use the validate function for validation as the other rules mostly apply to string, array of strings, number and boolean. |
| `valueAsNumber`<TypeText pre>boolean</TypeText>                                                                | Returns `Number` normally. If something goes wrong `NaN` will be returned.<br/><ul><li>`valueAs` process is happening **before** validation.</li><li>Only applies to number input, but without any data manipulation.</li><li>Does not transform `defaultValue` or `defaultValues`.</li></ul>                                  |
| `valueAsDate`<TypeText pre>boolean</TypeText>                                                                  | Returns `Date` normally. If something goes wrong `Invalid Date` will be returned.<br/><ul><li>`valueAs` process is happening **before** validation.</li><li>Only applies to input.</li><li>Does not transform `defaultValue` or `defaultValues`.</li></ul>                                                                     |
| `setValueAs`<TypeText pre>\<T\>(value: any) => T</TypeText>                                                    | Return input value by running through the function.<br/><ul><li>`valueAs` process is happening **before** validation. Also, `setValueAs` is ignored if either `valueAsNumber` or `valueAsDate` are true.</li><li>Only applies to text input.</li><li>Does not transform `defaultValue` or `defaultValues`.</li></ul>           |
| `disabled`<TypeText pre>boolean = false</TypeText>                                                             | Set `disabled` to `true` will lead input value to be `undefined` and input control to be disabled.<br/><ul><li>`disabled` prop will also omit built-in validation rules.</li><li>For schema validation, you can leverage the `undefined` value returned from input or context object.</li></ul>                                |
| `onChange`<TypeText pre>(e: SyntheticEvent) => void</TypeText>                                                 | `onChange` function event to be invoked in the change event.                                                                                                                                                                                                                                                                   |
| `onBlur`<TypeText pre>(e: SyntheticEvent) => void</TypeText>                                                   | `onBlur` function event to be invoked in the blur event.                                                                                                                                                                                                                                                                       |
| `value`<TypeText pre>unknown</TypeText>                                                                        | Set up `value` for the registered input. This prop should be utilised inside `useEffect` or invoke once, each re-run will update or overwrite the input value which you have supplied.                                                                                                                                         |
| `shouldUnregister`<TypeText pre>boolean</TypeText>                                                             | Input will be unregistered after unmount and `defaultValues` will be removed as well.<br/><br/>**Note:** this prop should be avoided when using with `useFieldArray` as unregister function gets called after input unmount/remount and reorder.                                                                               |
| `deps`<TypeText pre>string \| string[]</TypeText>                                                              | Validation will be triggered for the dependent inputs, it only limited to register api not trigger.                                                                                                                                                                                                                            |

</div>

</TabGroup>
 
<Admonition type="important" title="Rules">

<ul>
  <li>
    <strong>Name</strong> is <strong>required</strong> and must be <strong>unique</strong>
        (except for native radio and checkbox inputs).
  </li>
  <li>
    Name must not start with a number or use numbers as standalone keys, and should avoid special characters.
    For TypeScript consistency, only dot syntax is supported—bracket syntax (<code>[]</code>) will not work for array form values.

```javascript
register("test.0.firstName") // ✅
register("test[0].firstName") // ❌
```

  </li>
  
  <li> Disabled inputs return <code>undefined</code> as their form value.
        If you need to prevent user edits while preserving the value, use
        <code>readOnly</code> or disable the entire <code>fieldset</code>. Here is an [example](https://codesandbox.io/s/react-hook-form-disabled-inputs-oihxx).</li>
  
  <li>Changing an input’s <code>name</code> on each render causes it to be re-registered as a new field.
        To ensure consistent behavior, keep input names stable across renders.</li>
  
  <li>Input values and references are not automatically removed on unmount.
        Use <a href="/docs/useform/unregister"><code>unregister</code></a> to explicitly remove them when needed.</li>
  
  <li>
  Individual register option can't be removed by `undefined` or `{}`. You can update individual attribute instead.
  
```javascript
register('test', { required: true });
register('test', {}); // ❌
register('test', undefined); // ❌
register('test', { required: false });  // ✅
```
  
  </li>

    <li>There are certain keyword which need to avoid before conflicting with type check. They are `ref`, `_f`.</li>

</ul>

</Admonition>

**Examples**

---

**Register input or select**

```javascript sandbox="https://codesandbox.io/s/register-is0sfo"
import { useForm } from "react-hook-form"

export default function App() {
  const { register, handleSubmit } = useForm({
    defaultValues: {
      firstName: "",
      lastName: "",
      category: "",
      checkbox: [],
      radio: "",
    },
  })

  return (
    <form onSubmit={handleSubmit(console.log)}>
      <input
        {...register("firstName", { required: true })}
        placeholder="First name"
      />

      <input
        {...register("lastName", { minLength: 2 })}
        placeholder="Last name"
      />

      <select {...register("category")}>
        <option value="">Select...</option>
        <option value="A">Category A</option>
        <option value="B">Category B</option>
      </select>

      <input {...register("checkbox")} type="checkbox" value="A" />
      <input {...register("checkbox")} type="checkbox" value="B" />
      <input {...register("checkbox")} type="checkbox" value="C" />

      <input {...register("radio")} type="radio" value="A" />
      <input {...register("radio")} type="radio" value="B" />
      <input {...register("radio")} type="radio" value="C" />

      <input type="submit" />
    </form>
  )
}
```

**Custom async validation**

```javascript
import { useForm } from "react-hook-form"
import { checkProduct } from "./service"

export default function App() {
  const { register, handleSubmit } = useForm()

  return (
    <form onSubmit={handleSubmit(console.log)}>
      <select
        {...register("category", {
          required: true,
        })}
      >
        <option value="">Select...</option>
        <option value="A">Category A</option>
        <option value="B">Category B</option>
      </select>

      <input
        type="text"
        {...register("product", {
          validate: {
            checkAvailability: async (product, { category }) => {
              if (!category) return "Choose a category"
              if (!product) return "Specify your product"
              const isInStock = await checkProduct(category, product)
              return isInStock || "There is no such product"
            },
          },
        })}
      />

      <input type="submit" />
    </form>
  )
}
```

### Video

---

<YouTube youTubeId="JFIpCoajYkA" />

### Tips

---

#### Destructuring assignment

```javascript
const { onChange, onBlur, name, ref } = register('firstName');
// include type check against field path with the name you have supplied.

<input
  onChange={onChange} // assign onChange event
  onBlur={onBlur} // assign onBlur event
  name={name} // assign name prop
  ref={ref} // assign ref prop
/>
// same as above
<input {...register('firstName')} />
```

#### Custom Register

You can also register inputs with `useEffect` and treat them as virtual inputs. For controlled components, we provide a custom hook [useController](/docs/usecontroller) and [Controller](/docs/usecontroller/controller) component to take care this process for you.

If you choose to manually register fields, you will need to update the input value with [setValue](/docs/useform/setvalue).

```javascript
register('firstName', { required: true, min: 8 });

<TextInput onTextChange={(value) => setValue('lastChange', value))} />
```

#### How to work with `innerRef`, `inputRef`?

When the custom input component didn't expose ref correctly, you can get it working via the following.

```javascript
// not working, because ref is not assigned
<TextInput {...register('test')} />

const firstName = register('firstName', { required: true })
<TextInput
  name={firstName.name}
  onChange={firstName.onChange}
  onBlur={firstName.onBlur}
  inputRef={firstName.ref} // you can achieve the same for different ref name such as innerRef
/>
```


---

## Source: `src/content/docs/useform/reset.mdx`

---
title: reset
description: Reset form state and values
sidebar: apiLinks
---

## \</> `reset:` <TypeText>`<T>(values?: T | ResetAction<T>, options?: Record<string, boolean>) => void`</TypeText>

Reset the entire form state, fields reference, and subscriptions. There are optional arguments and will allow partial form state reset.

### Props

---

`Reset` has the ability to retain formState. Here are the options you may use:

| Name      |                     | Type                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------- | ------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `values`  |                     | <TypeText>object \| (values: Object) => Object </TypeText> | An optional object to reset form values, and it's recommended to provide the **entire** defaultValues when supplied.                                                                                                                                                                                                                                                                                                 |
| `options` | `keepErrors`        | <TypeText>boolean</TypeText>                               | All errors will remain. This will not guarantee with further user actions.                                                                                                                                                                                                                                                                                                                                           |
|           | `keepDirty`         | <TypeText>boolean</TypeText>                               | `DirtyFields` form state will remain, and `isDirty` will temporarily remain as the current state until further user's action.<br/><br/>**Important:** this keep option doesn't reflect form input values but only dirty fields form state.                                                                                                                                                                           |
|           | `keepDirtyValues`   | <TypeText>boolean</TypeText>                               | `DirtyFields` and `isDirty` will remained, and only none dirty fields will be updated to the latest rest value. [Check out the example.](https://codesandbox.io/s/react-keepdirtyvalues-o8to91)<br/><br/>**Important:** formState `dirtyFields` will need to be subscribed.                                                                                                                                          |
|           | `keepValues`        | <TypeText>boolean</TypeText>                               | Form input values will be unchanged.                                                                                                                                                                                                                                                                                                                                                                                 |
|           | `keepDefaultValues` | <TypeText>boolean</TypeText>                               | Keep the same defaultValues which are initialised via `useForm`.<ul><li>`isDirty` will be checked again: it is set to be the result of the comparison of any new values provided against the original `defaultValues`.</li> <li>`dirtyFields` will be updated again if values are provided: it is set to be result of the comparison between the new values provided against the original `defaultValues`.</li></ul> |
|           | `keepIsSubmitted`   | <TypeText>boolean</TypeText>                               | `isSubmitted` state will be unchanged.                                                                                                                                                                                                                                                                                                                                                                               |
|           | `keepTouched`       | <TypeText>boolean</TypeText>                               | `isTouched` state will be unchanged.                                                                                                                                                                                                                                                                                                                                                                                 |
|           | `keepIsValid`       | <TypeText>boolean</TypeText>                               | `isValid` will temporarily persist as the current state until additional user actions.                                                                                                                                                                                                                                                                                                                               |
|           | `keepSubmitCount`   | <TypeText>boolean</TypeText>                               | `submitCount` state will be unchanged.                                                                                                                                                                                                                                                                                                                                                                               |

<Admonition type="important" title="Rules">

- It is recommended to always provide <code>defaultValues</code> when resetting a form
  to ensure all inputs, especially controlled components, are restored correctly.

</Admonition>

**Examples:**

---

**Uncontrolled**

<TabGroup buttonLabels={["TS", "JS"]}>

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-reset-v7-ts-pu901"
import { useForm } from "react-hook-form"

interface UseFormInputs {
  firstName: string
  lastName: string
}

export default function Form() {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm<UseFormInputs>()
  const onSubmit = (data: UseFormInputs) => {
    console.log(data)
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>First name</label>
      <input {...register("firstName", { required: true })} />

      <label>Last name</label>
      <input {...register("lastName")} />

      <input type="submit" />
      <input type="reset" value="Standard Reset Field Values" />
      <input
        type="button"
        onClick={() => reset()}
        value="Custom Reset Field Values & Errors"
      />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-reset-v7-r7m5s"
import React, { useCallback } from "react"
import { useForm } from "react-hook-form"

export default function App() {
  const { register, handleSubmit, reset } = useForm()
  const resetAsyncForm = useCallback(async () => {
    const result = await fetch("./api/formValues.json") // result: { firstName: 'test', lastName: 'test2' }
    reset(result) // asynchronously reset your form values
  }, [reset])

  useEffect(() => {
    resetAsyncForm()
  }, [resetAsyncForm])

  return (
    <form onSubmit={handleSubmit((data) => {})}>
      <input {...register("firstName")} />
      <input {...register("lastName")} />

      <input
        type="button"
        onClick={() => {
          reset(
            {
              firstName: "bill",
            },
            {
              keepErrors: true,
              keepDirty: true,
            }
          )
        }}
      />

      <button
        onClick={() => {
          reset((formValues) => ({
            ...formValues,
            lastName: "test",
          }))
        }}
      >
        Reset partial
      </button>
    </form>
  )
}
```

</TabGroup>

**Controller**

<TabGroup buttonLabels={["TS", "JS"]}>

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-v6-controller-ts-jwyzw"
import { useForm, Controller } from "react-hook-form"
import { TextField } from "@material-ui/core"

interface IFormInputs {
  firstName: string
  lastName: string
}

export default function App() {
  const { register, handleSubmit, reset, setValue, control } =
    useForm<IFormInputs>()
  const onSubmit = (data: IFormInputs) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <Controller
        render={({ field }) => <TextField {...field} />}
        name="firstName"
        control={control}
        rules={{ required: true }}
        defaultValue=""
      />
      <Controller
        render={({ field }) => <TextField {...field} />}
        name="lastName"
        control={control}
        defaultValue=""
      />

      <input type="submit" />
      <input type="button" onClick={reset} />
      <input
        type="button"
        onClick={() => {
          reset({
            firstName: "bill",
            lastName: "luo",
          })
        }}
      />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-v7-controller-5h1q5"
import { useForm, Controller } from "react-hook-form"
import { TextField } from "@material-ui/core"

export default function App() {
  const { register, handleSubmit, reset, setValue, control } = useForm()
  const onSubmit = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <Controller
        render={({ field }) => <TextField {...field} />}
        name="firstName"
        control={control}
        rules={{ required: true }}
        defaultValue=""
      />
      <Controller
        render={({ field }) => <TextField {...field} />}
        name="lastName"
        control={control}
        defaultValue=""
      />

      <input type="submit" />
      <input type="button" onClick={reset} />
      <input
        type="button"
        onClick={() => {
          reset({
            firstName: "bill",
            lastName: "luo",
          })
        }}
      />
    </form>
  )
}
```

</TabGroup>

**Submit with Reset**

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-handlesubmit-with-reset-xu1zu"
import { useForm, useFieldArray, Controller } from "react-hook-form"

function App() {
  const {
    register,
    handleSubmit,
    reset,
    formState,
    formState: { isSubmitSuccessful },
  } = useForm({ defaultValues: { something: "anything" } })

  const onSubmit = (data) => {
    // It's recommended to reset in useEffect as execution order matters
    // reset({ ...data })
  }

  React.useEffect(() => {
    if (formState.isSubmitSuccessful) {
      reset({ something: "" })
    }
  }, [formState, submittedData, reset])

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("something")} />
      <input type="submit" />
    </form>
  )
}
```

**Field Array**

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-reset-usefieldarray-forked-kdh2s"
import React, { useEffect } from "react"
import { useForm, useFieldArray, Controller } from "react-hook-form"

function App() {
  const { register, control, handleSubmit, reset } = useForm({
    defaultValues: {
      loadState: "unloaded",
      names: [{ firstName: "Bill", lastName: "Luo" }],
    },
  })
  const { fields, remove } = useFieldArray({
    control,
    name: "names",
  })

  useEffect(() => {
    reset({
      names: [
        {
          firstName: "Bob",
          lastName: "Actually",
        },
        {
          firstName: "Jane",
          lastName: "Actually",
        },
      ],
    })
  }, [reset])

  const onSubmit = (data) => console.log("data", data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <ul>
        {fields.map((item, index) => (
          <li key={item.id}>
            <input {...register(`names.${index}.firstName`)} />

            <Controller
              render={({ field }) => <input {...field} />}
              name={`names.${index}.lastName`}
              control={control}
            />
            <button type="button" onClick={() => remove(index)}>
              Delete
            </button>
          </li>
        ))}
      </ul>

      <input type="submit" />
    </form>
  )
}
```

### Videos

---

<YouTube youTubeId="qmCLBjyPwVk" />


---

## Source: `src/content/docs/useform/resetfield.mdx`

---
title: resetField
description: Reset field state and value
sidebar: apiLinks
---

## \</> `resetField:` <TypeText>`(name: string, options?: Record<string, boolean | any>) => void`</TypeText>

Reset an individual field state.

### Props

---

After invoke this function.

- `isValid` form state will be reevaluated.
- `isDirty` form state will be reevaluated.

`ResetField` has the ability to retain field state. Here are the options you may want to use:

| Name    |                | Type                         | Description                                                                                                                                                                                                                                                                                                       |
| ------- | -------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`  |                | <TypeText>string</TypeText>  | registered field name.                                                                                                                                                                                                                                                                                            |
| options | `keepError`    | <TypeText>boolean</TypeText> | When set to `true`, field error will be retained.                                                                                                                                                                                                                                                                 |
|         | `keepDirty`    | <TypeText>boolean</TypeText> | When set to `true`, `dirtyFields` will be retained.                                                                                                                                                                                                                                                               |
|         | `keepTouched`  | <TypeText>boolean</TypeText> | When set to `true`, `touchedFields` state will be unchanged.                                                                                                                                                                                                                                                      |
|         | `defaultValue` | <TypeText>unknown</TypeText> | When this value is **not** provided, field will be revert back to it's defaultValue.<br/>When this value is provided:<br/><ul><li>field will be updated with the supplied value</li> <li>field's `defaultValue` will be updated to this value.</li> <li>Only support non <code>undefined</code> value.</li> </ul> |

<Admonition type="important" title="Rules">

- name need to match registered field name.

  ```javascript
  register("test")
  resetField("test") // ✅ register input and resetField works
  resetField("non-existent-name") // ❌ failed by input not found
  ```

</Admonition>

**Examples:**

---

**Reset Field State**

```javascript copy sandbox="https://codesandbox.io/s/priceless-firefly-d0kuv"
import * as React from "react"
import { useForm } from "react-hook-form"

export default function App() {
  const {
    register,
    resetField,
    formState: { isDirty, isValid },
  } = useForm({
    mode: "onChange",
    defaultValues: {
      firstName: "",
    },
  })
  const handleClick = () => resetField("firstName")

  return (
    <form>
      <input {...register("firstName", { required: true })} />

      <p>{isDirty && "dirty"}</p>
      <p>{isValid && "valid"}</p>

      <button type="button" onClick={handleClick}>
        Reset
      </button>
    </form>
  )
}
```

**Reset With Options**

```javascript copy sandbox="https://codesandbox.io/s/resetfield-with-options-iw4wd"
import * as React from "react"
import { useForm } from "react-hook-form"

export default function App() {
  const {
    register,
    resetField,
    formState: { isDirty, isValid, errors, touchedFields, dirtyFields },
  } = useForm({
    mode: "onChange",
    defaultValues: {
      firstName: "",
    },
  })

  return (
    <form>
      <input {...register("firstName", { required: true })} />

      <p>isDirty: {isDirty && "dirty"}</p>
      <p>touchedFields: {touchedFields.firstName && "touched field"}</p>
      <p>dirtyFields:{dirtyFields.firstName && "dirty field"}</p>
      <p>isValid: {isValid && "valid"}</p>
      <p>error: {errors.firstName && "error"}</p>

      <hr />

      <button
        type="button"
        onClick={() => resetField("firstName", { keepError: true })}
      >
        Reset keep error
      </button>
      <button
        type="button"
        onClick={() => resetField("firstName", { keepTouched: true })}
      >
        Reset keep touched fields
      </button>
      <button
        type="button"
        onClick={() => resetField("firstName", { keepDirty: true })}
      >
        Reset keep dirty fields
      </button>
      <button
        type="button"
        onClick={() => resetField("firstName", { defaultValue: "New" })}
      >
        update defaultValue
      </button>
    </form>
  )
}
```

### Video

---

The following video tutorial demonstrates `resetField` API.

<YouTube youTubeId="IdLFcNaEFEo" />


---

## Source: `src/content/docs/useform/seterror.mdx`

---
title: setError
description: Manually set an input error
sidebar: apiLinks
---

## \</> `setError:` <TypeText>`(name: string, error: FieldError, { shouldFocus?: boolean }) => void`</TypeText>

The function allows you to manually set one or more errors.

### Props

---

| Name    | Type                                                                                  | Description                                                                                                                                             |
| ------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`  | <TypeText>string</TypeText>                                                           | input's name.                                                                                                                                           |
| `error` | <TypeText>`{ type: string, message?: string, types: MultipleFieldErrors }`</TypeText> | Set an error with its type and message.                                                                                                                 |
| config  | <TypeText>`{ shouldFocus?: boolean }`</TypeText>                                      | Should focus the input during setting an error. This only works when the input's reference is registered, it will not work for custom register as well. |

<Admonition type="important" title="Rules">

- This method will not persist the associated input error if the input passes `register`'s associated rules.
  ```javascript
  register("registerInput", { minLength: 4 })
  setError("registerInput", { type: "custom", message: "custom message" })
  // validation will pass as long as minLength requirement pass
  ```
- An error that is not associated with an input field will be persisted until cleared with `clearErrors`. This behaviour is only applicable for built-in validation at field level.
  ```javascript
  setError("notRegisteredInput", { type: "custom", message: "custom message" })
  // clearErrors() need to invoked manually to remove that custom error
  ```
- You can set a server or global error with `root` as the key. This type of error will not persist with each submission.
  ```javascript
  setError("root.serverError", {
    type: "400",
  })
  ```
- `shouldFocus` doesn't work when an input has been disabled.
- This method will force <code>formState.isValid</code> to <code>false</code>.
  However, <code>isValid</code> is always derived from the validation results of your
  registered inputs or schema.
- There are certain keywords that need to be avoided to prevent conflicts with type checking.

</Admonition>

**Examples:**

---

**Single Error**

<TabGroup buttonLabels={["TS", "JS"]}>

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-v7-ts-seterror-nfxxu"
import * as React from "react"
import { useForm } from "react-hook-form"

type FormInputs = {
  username: string
}

const App = () => {
  const {
    register,
    handleSubmit,
    setError,
    formState: { errors },
  } = useForm<FormInputs>()
  const onSubmit = (data: FormInputs) => {
    console.log(data)
  }

  React.useEffect(() => {
    setError("username", {
      type: "manual",
      message: "Dont Forget Your Username Should Be Cool!",
    })
  }, [setError])

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("username")} />
      {errors.username && <p>{errors.username.message}</p>}

      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-v7-seterror-btbf8"
import { useForm } from "react-hook-form"

const App = () => {
  const {
    register,
    setError,
    formState: { errors },
  } = useForm()

  return (
    <form>
      <input {...register("test")} />
      {errors.test && <p>{errors.test.message}</p>}

      <button
        type="button"
        onClick={() => {
          setError("test", { type: "focus" }, { shouldFocus: true })
        }}
      >
        Set Error Focus
      </button>
      <input type="submit" />
    </form>
  )
}
```

</TabGroup>

**Multiple Errors**

<TabGroup buttonLabels={["TS", "JS"]}>

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-v7-ts-seterror-8h440"
import * as React from "react"
import { useForm } from "react-hook-form"

type FormInputs = {
  username: string
  firstName: string
}

const App = () => {
  const {
    register,
    handleSubmit,
    setError,
    formState: { errors },
  } = useForm<FormInputs>()

  const onSubmit = (data: FormInputs) => {
    console.log(data)
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>Username</label>
      <input {...register("username")} />
      {errors.username && <p>{errors.username.message}</p>}
      <label>First Name</label>
      <input {...register("firstName")} />
      {errors.firstName && <p>{errors.firstName.message}</p>}
      <button
        type="button"
        onClick={() => {
          const inputs = [
            {
              type: "manual",
              name: "username",
              message: "Double Check This",
            },
            {
              type: "manual",
              name: "firstName",
              message: "Triple Check This",
            },
          ]

          inputs.forEach(({ name, type, message }) => {
            setError(name, { type, message })
          })
        }}
      >
        Trigger Name Errors
      </button>
      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-v7-seterror-3y1op"
import * as React from "react"
import { useForm } from "react-hook-form"

const App = () => {
  const {
    register,
    handleSubmit,
    setError,
    formState: { errors },
  } = useForm()

  const onSubmit = (data) => {
    console.log(data)
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>Username</label>
      <input {...register("username")} />
      {errors.username && <p>{errors.username.message}</p>}
      <label>First Name</label>
      <input {...register("firstName")} />
      {errors.firstName && <p>{errors.firstName.message}</p>}
      <button
        type="button"
        onClick={() => {
          const inputs = [
            {
              type: "manual",
              name: "username",
              message: "Double Check This",
            },
            {
              type: "manual",
              name: "firstName",
              message: "Triple Check This",
            },
          ]

          inputs.forEach(({ name, type, message }) =>
            setError(name, { type, message })
          )
        }}
      >
        Trigger Name Errors
      </button>
      <input type="submit" />
    </form>
  )
}
```

</TabGroup>

**Single Field Errors**

<TabGroup buttonLabels={["TS", "JS"]}>

```tsx copy
import * as React from "react"
import { useForm } from "react-hook-form"

type FormInputs = {
  lastName: string
}

const App = () => {
  const {
    register,
    handleSubmit,
    setError,
    formState: { errors },
  } = useForm<FormInputs>({
    criteriaMode: "all",
  })

  const onSubmit = (data: FormInputs) => console.log(data)

  React.useEffect(() => {
    setError("lastName", {
      types: {
        required: "This is required",
        minLength: "This is minLength",
      },
    })
  }, [setError])

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>Last Name</label>
      <input {...register("lastName")} />
      {errors.lastName && errors.lastName.types && (
        <p>{errors.lastName.types.required}</p>
      )}
      {errors.lastName && errors.lastName.types && (
        <p>{errors.lastName.types.minLength}</p>
      )}
      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/seterror-single-field-errors-79wcr9"
import * as React from "react"
import { useForm } from "react-hook-form"

const App = () => {
  const {
    register,
    handleSubmit,
    setError,
    formState: { errors },
  } = useForm({
    criteriaMode: "all",
  })
  const onSubmit = (data) => {
    console.log(data)
  }

  React.useEffect(() => {
    setError("lastName", {
      types: {
        required: "This is required",
        minLength: "This is minLength",
      },
    })
  }, [setError])

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>Last Name</label>
      <input {...register("lastName")} />
      {errors.lastName && errors.lastName.types && (
        <p>{errors.lastName.types.required}</p>
      )}
      {errors.lastName && errors.lastName.types && (
        <p>{errors.lastName.types.minLength}</p>
      )}
      <input type="submit" />
    </form>
  )
}
```

</TabGroup>

**Server Error**

```javascript copy
import * as React from "react";
import { useForm } from "react-hook-form";

const App = () => {
  const { register, handleSubmit, setError, formState: { errors } } = useForm({
    criteriaMode: 'all',
  });
  const onSubmit = async () => {
    const response = await fetch(...)
    if (response.statusCode > 200) {
        setError('root.serverError', {
          type: response.statusCode,
        })
    }
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>Last Name</label>
      <input {...register("lastName")} />

      {errors.root.serverError.type === 400 && <p>server response message</p>}

      <button>submit</button>
    </form>
  );
};
```

### Video

---

The following video explain `setError` API in detail.

<YouTube youTubeId="raMqvE0YyIY" />


---

## Source: `src/content/docs/useform/setfocus.mdx`

---
title: setFocus
description: Manually set an input focus
sidebar: apiLinks
---

## `setFocus:` <TypeText>(name: string, options: SetFocusOptions) => void</TypeText>

This method will allow users to programmatically focus on input. Make sure input's ref is registered into the hook form.

### Props

---

| Name      |                | Type                         | Description                                   |
| --------- | -------------- | ---------------------------- | --------------------------------------------- |
| `name`    |                | <TypeText>string</TypeText>  | A input field name to focus                   |
| `options` | `shouldSelect` | <TypeText>boolean</TypeText> | Whether to select the input content on focus. |

<Admonition type="important" title="Rules">

- This API will invoke focus method from the ref, so it's important to provide `ref` during `register`.
- Avoid calling `setFocus` right after `reset` as all input references will be removed by `reset` API.

</Admonition>

### Examples

---

<TabGroup buttonLabels={["TS", "JS"]}>

```tsx copy sandbox="https://codesandbox.io/s/setfocus-rolus"
import * as React from "react"
import { useForm } from "react-hook-form"

type FormValues = {
  firstName: string
}

export default function App() {
  const { register, handleSubmit, setFocus } = useForm<FormValues>()
  const onSubmit = (data: FormValues) => console.log(data)
  renderCount++

  React.useEffect(() => {
    setFocus("firstName")
  }, [setFocus])

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("firstName")} placeholder="First Name" />
      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/setfocus-rolus"
import * as React from "react"
import { useForm } from "react-hook-form"

export default function App() {
  const { register, handleSubmit, setFocus } = useForm()
  const onSubmit = (data) => console.log(data)
  renderCount++

  React.useEffect(() => {
    setFocus("firstName")
  }, [setFocus])

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("firstName")} placeholder="First Name" />
      <input type="submit" />
    </form>
  )
}
```

</TabGroup>


---

## Source: `src/content/docs/useform/setvalue.mdx`

---
title: setValue
description: Update field value
sidebar: apiLinks
---

## \</> `setValue:` <TypeText>(name: string, value: unknown, config?: SetValueConfig) => void</TypeText>

This function allows you to dynamically set the value of a <strong>registered</strong> field and have the options to validate and update the form state. At the same time, it tries to avoid unnecessary rerender.

### Props

---

| Name                                     |                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`<br/><TypeText>string</TypeText>   |                                                   | Target a single field or field array by name.                                                                                                                                                                                                                                                                                                                                                            |
| `value`<br/><TypeText>unknown</TypeText> |                                                   | The value for the field. This argument is required and can not be `undefined`.                                                                                                                                                                                                                                                                                                                           |
| `options`                                | `shouldValidate`<br/><TypeText>boolean</TypeText> | <ul><li>Whether to compute if your input is valid or not (subscribed to <TypeText>errors</TypeText>).</li><li>Whether to compute if your entire form is valid or not (subscribed to <TypeText>isValid</TypeText>).</li>This option will update `touchedFields` at the specified field level not the entire form touched fields.</ul>                                                                     |
|                                          | `shouldDirty`<br/><TypeText>boolean</TypeText>    | <ul><li>Whether to compute if your input is dirty or not against your `defaultValues` (subscribed to <TypeText>dirtyFields</TypeText>).</li><li>Whether to compute if your entire form is dirty or not against your `defaultValues` (subscribed to <TypeText>isDirty</TypeText>).</li><li>This option will update `dirtyFields` at the specified field level not the entire form dirty fields.</li></ul> |
|                                          | `shouldTouch`<br/><TypeText>boolean</TypeText>    | Whether to set the input itself to be touched.                                                                                                                                                                                                                                                                                                                                                           |

<Admonition type="important" title="Rules">

- You can use methods such as [replace](/docs/usefieldarray#replace) or [update](/docs/usefieldarray#update) for field array, however, they will cause the component to unmount and remount for the targeted field array.

  ```javascript
  const { update } = useFieldArray({ name: "array" })

  // unmount fields and remount with updated value
  update(0, { test: "1", test1: "2" })

  // will directly update input value
  setValue("array.0.test1", "1")
  setValue("array.0.test2", "2")
  ```

- It's recommended to target the field's name rather than make the second argument a nested object.

  ```javascript
  setValue("yourDetails.firstName", "value") // ✅ performant
  setValue("yourDetails", { firstName: "value" }) ❌ // less performant

  register("nestedValue", { value: { test: "data" } }) // register a nested value input
  setValue("nestedValue.test", "updatedData") // ❌ failed to find the relevant field
  setValue("nestedValue", { test: "updatedData" }) // ✅ setValue find input and update
  ```

- It's recommended to register the input's name before invoking `setValue`. To update the entire `FieldArray`, make sure the `useFieldArray` hook is being executed first.

  **Important:** use `replace` from `useFieldArray` instead, update entire field array with `setValue` will be removed in the next major version.

  ```javascript
  // you can update an entire Field Array,
  setValue("fieldArray", [{ test: "1" }, { test: "2" }]) // ✅

  // you can setValue to a unregistered input
  setValue("notRegisteredInput", "value") // ✅ prefer to be registered

  // the following will register a single input (without register invoked)
  setValue("resultSingleNestedField", { test: "1", test2: "2" }) // 🤔

  // with registered inputs, the setValue will update both inputs correctly.
  register("notRegisteredInput.test", "1")
  register("notRegisteredInput.test2", "2")
  setValue("notRegisteredInput", { test: "1", test2: "2" }) // ✅ sugar syntax to setValue twice
  ```

</Admonition>

### Examples

---

**Basic**

```javascript sandbox="https://codesandbox.io/s/react-hook-form-v7-ts-setvalue-8z9hx"
import { useForm } from "react-hook-form"

const App = () => {
  const { register, setValue } = useForm({
    firstName: "",
  })

  return (
    <form>
      <input {...register("firstName", { required: true })} />
      <button onClick={() => setValue("firstName", "Bill")}>setValue</button>
      <button
        onClick={() =>
          setValue("firstName", "Luo", {
            shouldValidate: true,
            shouldDirty: true,
          })
        }
      >
        setValue options
      </button>
    </form>
  )
}
```

**Dependant Fields**

```tsx sandbox="https://codesandbox.io/s/dependant-field-dwin1"
import * as React from "react"
import { useForm } from "react-hook-form"

type FormValues = {
  a: string
  b: string
  c: string
}

export default function App() {
  const { watch, register, handleSubmit, setValue, formState } =
    useForm<FormValues>({
      defaultValues: {
        a: "",
        b: "",
        c: "",
      },
    })
  const onSubmit = (data: FormValues) => console.log(data)
  const [a, b] = watch(["a", "b"])

  React.useEffect(() => {
    if (formState.touchedFields.a && formState.touchedFields.b && a && b) {
      setValue("c", `${a} ${b}`)
    }
  }, [setValue, a, b, formState])

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("a")} placeholder="a" />
      <input {...register("b")} placeholder="b" />
      <input {...register("c")} placeholder="c" />
      <input type="submit" />

      <button
        type="button"
        onClick={() => {
          setValue("a", "what", { shouldTouch: true })
          setValue("b", "ever", { shouldTouch: true })
        }}
      >
        trigger value
      </button>
    </form>
  )
}
```

### Video

---

<YouTube youTubeId="qpv51sCH3fI" />


---

## Source: `src/content/docs/useform/subscribe.mdx`

---
title: subscribe
description: Subscribe to form state update without render
sidebar: apiLinks
---

## `subscribe:` <TypeText>`UseFormSubscribe<TFieldValues extends FieldValues>`</TypeText>

Subscribe to [`formState`](/docs/useform/formstate) changes and value updates. You can subscribe to individual fields or the entire form, while avoiding unnecessary re-renders caused by form changes.

### Props

---

| Name      | Type                                          | Description                                                         | Example                                                                                                                                                                                                                                                                  |
| --------- | --------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| name      | <TypeText>undefined</TypeText>                | Subscribe to the entire form                                        | `subscribe()`                                                                                                                                                                                                                                                            |
|           | <TypeText>string[]</TypeText>                 | Subscribe on multiple fields by **name**.                           | `subscribe({ name: ['firstName', 'lastName'] })`                                                                                                                                                                                                                         |
| formState | <TypeText>`Partial<ReadFormState>`</TypeText> | Pick which [`formState`](/docs/useform/formstate) to be subscribed. | <CodeArea withOutCopy rawData={`subscribe({ \n  formState: { \n    values: true, \n    isDirty: true, \n    dirtyFields: true, \n    touchedFields: true, \n    isValid: true, \n    errors: true, \n    validatingFields: true, \n    isValidating: true \n  } \n})`}/> |
| callback  | <TypeText>`Function`</TypeText>               | The callback function for the subscription.                         | <CodeArea withOutCopy rawData={`subscribe({ \n  formState: { \n    values: true \n  }, \n  callback: ({ values }) => { \n    console.log(values) \n  } \n})`}/>                                                                                                          |
| exact     | <TypeText>boolean</TypeText>                  | This prop will enable an exact match for input name subscriptions.  | `subscribe({ name: 'target', exact: true })`                                                                                                                                                                                                                             |

<Admonition type="important" title="Notes">

<ul>
  <li>
    <p>
      This function shares the same functionality as{" "}
      <code>createFormControl.subscribe</code>, with the key difference being
      that [createFormControl](/docs/createFormControl) can be initialized
      outside of a React component.
    </p>
  </li>
  <li>
    <p>
      This function is dedicated for subscribe form state without **render**,
      use this function for that instead of [watch](/docs/useform/watch)
      callback function.
    </p>
  </li>
</ul>

</Admonition>

**Examples:**

---

```tsx copy
import { useForm } from "react-hook-form"

type FormInputs = {
  firstName: string
  lastName: string
}

export default function App() {
  const { register, subscribe } = useForm<FormInputs>()

  useEffect(() => {
    // make sure to unsubscribe;
    const callback = subscribe({
      formState: {
        values: true,
      },
      callback: ({ values }) => {
        console.log(values)
      },
    })

    return () => callback()

    // You can also just return the subscribe
    // return subscribe();
  }, [subscribe])

  return (
    <form>
      <input {...register("firstName", { required: true })} />
      <input {...register("lastName", { required: true })} />
    </form>
  )
}
```


---

## Source: `src/content/docs/useform/trigger.mdx`

---
title: trigger
description: Trigger validation across the form
sidebar: apiLinks
---

## `trigger:` <TypeText>`(name?: string | string[]) => Promise<boolean>`</TypeText>

Manually triggers form or input validation. This method is also useful when you have dependant validation (input validation depends on another input's value).

### Props

---

| Name        | Type                           | Description                                                                                                                                             | Example                                  |
| ----------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| name        | <TypeText>undefined</TypeText> | Triggers validation on all fields.                                                                                                                      | `trigger()`                              |
|             | <TypeText>string</TypeText>    | Triggers validation on a specific field value by **name**                                                                                               | `trigger("yourDetails.firstName")`       |
|             | <TypeText>string[]</TypeText>  | Triggers validation on multiple fields by **name**.                                                                                                     | `trigger(["yourDetails.lastName"])`      |
| shouldFocus | <TypeText>boolean</TypeText>   | Should focus the input during setting an error. This only works when the input's reference is registered, it will not work for custom register as well. | `trigger('name', { shouldFocus: true })` |

<Admonition type="important" title="Rules">

Isolate render optimisation only applicable for targeting a single field name with `string` as payload, when supplied with `array` and `undefined` to trigger will re-render the entire formState.

</Admonition>

**Examples:**

---

<TabGroup buttonLabels={["TS", "JS"]} >

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-v6-ts-triggervalidation-forked-xs7hl"
import { useForm } from "react-hook-form"

type FormInputs = {
  firstName: string
  lastName: string
}

export default function App() {
  const {
    register,
    trigger,
    formState: { errors },
  } = useForm<FormInputs>()

  return (
    <form>
      <input {...register("firstName", { required: true })} />
      <input {...register("lastName", { required: true })} />
      <button
        type="button"
        onClick={() => {
          trigger("lastName")
        }}
      >
        Trigger
      </button>
      <button
        type="button"
        onClick={() => {
          trigger(["firstName", "lastName"])
        }}
      >
        Trigger Multiple
      </button>
      <button
        type="button"
        onClick={() => {
          trigger()
        }}
      >
        Trigger All
      </button>
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-v6-triggervalidation-forked-8w9tn"
import { useForm } from "react-hook-form"

export default function App() {
  const {
    register,
    trigger,
    formState: { errors },
  } = useForm()

  return (
    <form>
      <input {...register("firstName", { required: true })} />
      <input {...register("lastName", { required: true })} />
      <button
        type="button"
        onClick={async () => {
          const result = await trigger("lastName")
          // const result = await trigger("lastName", { shouldFocus: true }); allowed to focus input
        }}
      >
        Trigger
      </button>
      <button
        type="button"
        onClick={async () => {
          const result = await trigger(["firstName", "lastName"])
        }}
      >
        Trigger Multiple
      </button>
      <button
        type="button"
        onClick={() => {
          trigger()
        }}
      >
        Trigger All
      </button>
    </form>
  )
}
```

</TabGroup>

### Video

---

The following video explain `trigger` API in detail.

<YouTube youTubeId="-bcyJCDjksE" />


---

## Source: `src/content/docs/useform/unregister.mdx`

---
title: unregister
description: Unregister uncontrolled/controlled inputs
sidebar: apiLinks
---

## \</> `unregister:` <TypeText>(name: string | string[], options) => void</TypeText>

This method allows you to `unregister` a single input or an array of inputs. It also provides a second optional argument to keep state after unregistering an input.

### Props

---

The example below shows what to expect when you invoke the `unregister` method.

```javascript
<input {...register('yourDetails.firstName')} />
<input {...register('yourDetails.lastName')} />
```

| Type                          | Input Name                             | Value              |
| ----------------------------- | -------------------------------------- | ------------------ |
| <TypeText>string</TypeText>   | `unregister("yourDetails")`            | `{}`               |
| <TypeText>string</TypeText>   | `unregister("yourDetails.firstName")`  | `{ lastName: '' }` |
| <TypeText>string[]</TypeText> | `unregister(["yourDetails.lastName"])` | `''`               |

### Options

---

| Name               | Type                         | Description                                                                                                                                                                                                                   |
| ------------------ | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `keepDirty`        | <TypeText>boolean</TypeText> | `isDirty` and `dirtyFields` will be remained during this action. However, this is not going to guarantee the next user input will not update `isDirty` formState, because `isDirty` is measured against the `defaultValues`.  |
| `keepTouched`      | <TypeText>boolean</TypeText> | `touchedFields` will no longer remove that input after unregister.                                                                                                                                                            |
| `keepIsValid`      | <TypeText>boolean</TypeText> | `isValid` will be remained during this action. However, this is not going to guarantee the next user input will not update `isValid` for schema validation, you will have to adjust the schema according with the unregister. |
| `keepError`        | <TypeText>boolean</TypeText> | `errors` will not be updated.                                                                                                                                                                                                 |
| `keepValue`        | <TypeText>boolean</TypeText> | input's current `value` will not be updated.                                                                                                                                                                                  |
| `keepDefaultValue` | <TypeText>boolean</TypeText> | input's `defaultValue` which defined in `useForm` will be remained.                                                                                                                                                           |

<Admonition type="important" title="Rules">

- This method will remove input reference and its value, which means **built-in validation** rules will be removed as well.
- By `unregister` an input, it will not affect the schema validation.

  ```javascript
  const schema = yup
    .object()
    .shape({
      firstName: yup.string().required(),
    })
    .required()

  unregister("firstName") // this will not remove the validation against firstName input
  ```

- Make sure you unmount that input which has `register` callback or else the input will get registered again.

  ```javascript
  const [show, setShow] = React.useState(true)

  const onClick = () => {
    unregister("test")
    setShow(false) // make sure to unmount that input so register not invoked again.
  }

  {
    show && <input {...register("test")} />
  }
  ```

</Admonition>

**Examples:**

---

<TabGroup buttonLabels={["TS", "JS"]}>

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-unregister-v6-ts-forked-4k2ey"
import React, { useEffect } from "react"
import { useForm } from "react-hook-form"

interface IFormInputs {
  firstName: string
  lastName?: string
}

export default function App() {
  const { register, handleSubmit, unregister } = useForm<IFormInputs>()
  const onSubmit = (data: IFormInputs) => console.log(data)

  React.useEffect(() => {
    register("lastName")
  }, [register])

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <button type="button" onClick={() => unregister("lastName")}>
        unregister
      </button>
      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-unregister-v6-forked-qs8o6"
import React, { useEffect } from "react"
import { useForm } from "react-hook-form"

export default function App() {
  const { register, handleSubmit, unregister } = useForm()

  React.useEffect(() => {
    register("lastName")
  }, [register])

  return (
    <form>
      <button type="button" onClick={() => unregister("lastName")}>
        unregister
      </button>
      <input type="submit" />
    </form>
  )
}
```

</TabGroup>

### Video

---

<YouTube youTubeId="TM99g_NW5Gk" />


---

## Source: `src/content/docs/useform/watch.mdx`

---
title: watch
description: Subscribe to input changes
sidebar: apiLinks
---

## \</> `watch:` <TypeText>UseFormWatch</TypeText>

This method will watch specified inputs and return their values. It is useful to render input value and for determining what to render by condition.

### Overloads

This function mainly serves **two purposes**:

- <TypeText>`watch(name: string, defaultValue?: unknown): unknown`</TypeText>
- <TypeText>`watch(names: string[], defaultValue?: {[key:string]: unknown}): unknown[]`</TypeText>
- <TypeText>`watch(): {[key:string]: unknown}`</TypeText>

The explanation of each of these four overloads follows below.

#### 1-a. Watching single field <TypeText>`watch(name: string, defaultValue?: unknown): unknown`</TypeText>

---

Watch and subscribe to a single field used outside of render.

**Params**

| Name           | Type                           | Description                         |
| -------------- | ------------------------------ | ----------------------------------- |
| `name`         | <TypeText>`string`</TypeText>  | the field name                      |
| `defaultValue` | <TypeText>`unknown`</TypeText> | _optional_. default value for field |

**Returns** the single field value.

```tsx
const name = watch("name")
```

#### 1-b. Watching some fields <TypeText>`watch(names: string[], defaultValue?: {[key:string]: unknown}): unknown[]`</TypeText>

---

Watch and subscribe to an array of fields used outside of render.

**Params**

| Name           | Type                                           | Description                           |
| -------------- | ---------------------------------------------- | ------------------------------------- |
| `names`        | <TypeText>`string[]`</TypeText>                | the field names                       |
| `defaultValue` | <TypeText>`{[key:string]: unknown}`</TypeText> | _optional_. default values for fields |

**Returns** an array of field values.

```tsx
const [name, name1] = watch(["name", "name1"])
```

#### 1-c. Watching the entire form <TypeText>`watch(): {[key:string]: unknown}`</TypeText>

---

Watch and subscribe to the entire form update/change based on onChange and re-render at the useForm.

**Params** None

**Returns** the entire form values.

```tsx
const formValues = watch()
```

#### 2. <b>Deprecated:</b> consider use or migrate to [subscribe](/docs/useform/subscribe). Watching with callback fn <TypeText>`watch(callback: (data, { name, type }) => void, defaultValues?: {[key:string]: unknown}): { unsubscribe: () => void }`</TypeText>

---

Subscribe to field update/change without trigger re-render.

**Params**

| Name            | Type                                                  | Description                                          |
| --------------- | ----------------------------------------------------- | ---------------------------------------------------- |
| `callback`      | <TypeText>`(data, { name, type }) => void`</TypeText> | callback function to subscribe to all fields changes |
| `defaultValues` | <TypeText>`{[key:string]: unknown}`</TypeText>        | _optional_. defaultValues for the entire form        |

**Returns** object with `unsubscribe` function.

### Rules

---

- When `defaultValue` is not defined, the first render of `watch` will return `undefined` because it is called before `register`. It's **recommended** to provide `defaultValues` at `useForm` to avoid this behaviour, but you can set the inline `defaultValue` as the second argument.
- When both `defaultValue` and `defaultValues` are supplied, `defaultValue` will be returned.
- This API will trigger re-render at the root of your app or form, consider using a callback or the [useWatch](/docs/usewatch) api if you are experiencing performance issues.
- `watch` result is optimised for render phase instead of `useEffect`'s deps, to detect value update you may want to use an external custom hook for value comparison.

### Examples:

---

#### Watch in a Form

<TabGroup buttonLabels={["TS", "JS"]}>

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-watch-v7-ts-8et1d"
import { useForm } from "react-hook-form"

interface IFormInputs {
  name: string
  showAge: boolean
  age: number
}

function App() {
  const {
    register,
    watch,
    formState: { errors },
    handleSubmit,
  } = useForm<IFormInputs>()
  const watchShowAge = watch("showAge", false) // you can supply default value as second argument
  const watchAllFields = watch() // when pass nothing as argument, you are watching everything
  const watchFields = watch(["showAge", "age"]) // you can also target specific fields by their names

  const onSubmit = (data: IFormInputs) => console.log(data)

  return (
    <>
      <form onSubmit={handleSubmit(onSubmit)}>
        <input {...register("name", { required: true, maxLength: 50 })} />
        <input type="checkbox" {...register("showAge")} />
        {/* based on yes selection to display Age Input*/}
        {watchShowAge && (
          <input type="number" {...register("age", { min: 50 })} />
        )}
        <input type="submit" />
      </form>
    </>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-watch-v7-qbxd7"
import { useForm } from "react-hook-form"

function App() {
  const {
    register,
    watch,
    formState: { errors },
    handleSubmit,
  } = useForm()
  const watchShowAge = watch("showAge", false) // you can supply default value as second argument
  const watchAllFields = watch() // when pass nothing as argument, you are watching everything
  const watchFields = watch(["showAge", "number"]) // you can also target specific fields by their names

  const onSubmit = (data) => console.log(data)

  return (
    <>
      <form onSubmit={handleSubmit(onSubmit)}>
        <input type="checkbox" {...register("showAge")} />

        {/* based on yes selection to display Age Input*/}
        {watchShowAge && (
          <input type="number" {...register("age", { min: 50 })} />
        )}

        <input type="submit" />
      </form>
    </>
  )
}
```

</TabGroup>

#### Watch in Field Array

<TabGroup buttonLabels={["TS", "JS"]}>

```tsx copy sandbox="https://codesandbox.io/s/watch-with-usefieldarray-z54xwd"
import * as React from "react"
import { useForm, useFieldArray } from "react-hook-form"

type FormValues = {
  test: {
    firstName: string
    lastName: string
  }[]
}

function App() {
  const { register, control, handleSubmit, watch } = useForm<FormValues>()
  const { fields, remove, append } = useFieldArray({
    name: "test",
    control,
  })
  const onSubmit = (data: FormValues) => console.log(data)

  console.log(watch("test"))

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {fields.map((field, index) => {
        return (
          <div key={field.id}>
            <input
              defaultValue={field.firstName}
              {...register(`test.${index}.firstName`)}
            />
            <input
              defaultValue={field.lastName}
              {...register(`test.${index}.lastName`)}
            />
            <button type="button" onClick={() => remove(index)}>
              Remove
            </button>
          </div>
        )
      })}
      <button
        type="button"
        onClick={() =>
          append({
            firstName: "bill" + renderCount,
            lastName: "luo" + renderCount,
          })
        }
      >
        Append
      </button>
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/watch-with-usefieldarray-52yy3z"
import * as React from "react"
import { useForm, useFieldArray } from "react-hook-form"

function App() {
  const { register, control, handleSubmit, watch } = useForm()
  const { fields, remove, append } = useFieldArray({
    name: "test",
    control,
  })
  const onSubmit = (data) => console.log(data)

  console.log(watch("test"))

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {fields.map((field, index) => {
        return (
          <div key={field.id}>
            <input
              defaultValue={field.firstName}
              {...register(`test.${index}.firstName`)}
            />
            <input
              defaultValue={field.lastName}
              {...register(`test.${index}.lastName`)}
            />
            <button type="button" onClick={() => remove(index)}>
              Remove
            </button>
          </div>
        )
      })}
      <button
        type="button"
        onClick={() =>
          append({
            firstName: "bill" + renderCount,
            lastName: "luo" + renderCount,
          })
        }
      >
        Append
      </button>
    </form>
  )
}
```

</TabGroup>

## Video

---

<YouTube youTubeId="3qLd69WMqKk" />


---

## Source: `src/content/docs/useform.mdx`

---
title: useForm
description: React hooks for form validation
sidebar: apiLinks
---

<SelectNav
  options={[
    {
      label: "register",
      value: "/docs/useform/register",
    },
    {
      label: "unregister",
      value: "/docs/useform/unregister",
    },
    {
      label: "formstate",
      value: "/docs/useform/formstate",
    },
    {
      label: "watch",
      value: "/docs/useform/watch",
    },
    {
      label: "subscribe",
      value: "/docs/useform/subscribe",
    },
    {
      label: "handlesubmit",
      value: "/docs/useform/handlesubmit",
    },
    {
      label: "reset",
      value: "/docs/useform/reset",
    },
    {
      label: "resetField",
      value: "/docs/useform/resetfield",
    },
    {
      label: "setError",
      value: "/docs/useform/seterror",
    },
    {
      label: "clearErrors",
      value: "/docs/useform/clearerrors",
    },
    {
      label: "setValue",
      value: "/docs/useform/setvalue",
    },
    {
      label: "setFocus",
      value: "/docs/useform/setfocus",
    },
    {
      label: "getValues",
      value: "/docs/useform/getvalues",
    },
    {
      label: "getFieldState",
      value: "/docs/useform/getfieldstate",
    },
    {
      label: "trigger",
      value: "/docs/useform/trigger",
    },
    {
      label: "control",
      value: "/docs/useform/control",
    },
    {
      label: "Form",
      value: "/docs/useform/form",
    },
  ]}
/>

## \</> `useForm:` [`UseFormProps`](/ts#UseFormProps)

`useForm` is a custom hook for managing forms with ease. It takes one object as **optional** argument. The following example demonstrates all of its properties along with their default values.

**Generic props:**

| Option                                                  | Description                                                                                                                   |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| [mode](#mode)                                           | Validation strategy **before** submitting behaviour.                                                                          |
| [reValidateMode](#reValidateMode)                       | Validation strategy **after** submitting behaviour.                                                                           |
| [defaultValues](#defaultValues)                         | Default values for the form, this value will be cached.                                                                       |
| [values](#values)                                       | Reactive values to update the form values.                                                                                    |
| [errors](#errors)                                       | Server returns errors to update form. **⚠ Important:** Keep the errors object reference-stable to avoid infinite re-renders. |
| [resetOptions](#resetOptions)                           | Option to reset form state update while updating new form values.                                                             |
| [criteriaMode](#criteriaMode)                           | Display all validation errors or one at a time.                                                                               |
| [shouldFocusError](#shouldFocusError)                   | Enable or disable built-in focus management.                                                                                  |
| [delayError](#delayError)                               | Delay error from appearing instantly.                                                                                         |
| [validate](#validate)                                   | Form-level validation is limited to built-in validation methods.                                                              |
| [shouldUseNativeValidation](#shouldUseNativeValidation) | Use browser built-in form constraint API.                                                                                     |
| [shouldUnregister](#shouldUnregister)                   | Enable and disable input unregister after unmount.                                                                            |
| [progressive](/docs/useform/form)                       | Enable progressive enhancement for native form submission when using the `Form` component.                                    |
| [disabled](#disabled)                                   | Disable the entire form with all associated inputs.                                                                           |

**Schema validation props:**

| Option                | Description                                               |
| --------------------- | --------------------------------------------------------- |
| [resolver](#resolver) | Integrates with your preferred schema validation library. |
| [context](#context)   | A context object to supply for your schema validation.    |

### Props

---

#### mode: <TypeText>onChange | onBlur | onSubmit | onTouched | all = 'onSubmit'</TypeText> <Popup top={3} message="React Native: compatible with Controller" /> {#mode}

---

This option allows you to configure the validation strategy before a user submits the form. The validation occurs during the `onSubmit` event, which is triggered by invoking the [`handleSubmit`](/docs/useform/handlesubmit) function.

| Name      | Type                        | Description                                                                                                                                                                                                              |
| --------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| onSubmit  | <TypeText>string</TypeText> | Validation is triggered on the `submit` event, and inputs attach `onChange` event listeners to re-validate themselves.                                                                                                   |
| onBlur    | <TypeText>string</TypeText> | Validation is triggered on the `blur` event.                                                                                                                                                                             |
| onChange  | <TypeText>string</TypeText> | Validation is triggered on the `change`event for each input, leading to multiple re-renders. Warning: this often comes with a significant impact on performance.                                                         |
| onTouched | <TypeText>string</TypeText> | Validation is initially triggered on the first `blur` event. After that, it is triggered on every `change` event.<br/><br/>**Note:** when using with `Controller`, make sure to wire up `onBlur` with the `render` prop. |
| all       | <TypeText>string</TypeText> | Validation is triggered on both `blur` and `change` events.                                                                                                                                                              |

#### reValidateMode: <TypeText>onChange | onBlur | onSubmit = 'onChange' </TypeText> <Popup top={3} message="React Native: Custom register or using Controller" /> {#reValidateMode}

---

This option allows you to configure validation strategy when inputs with errors get re-validated **after** a user submits the form (`onSubmit` event and [`handleSubmit`](/docs/useform/handlesubmit) function executed). By default, re-validation occurs during the input change event.

#### defaultValues: <TypeText>`FieldValues | () => Promise<FieldValues>`</TypeText> {#defaultValues}

---

The `defaultValues` prop populates the entire form with default values. It supports both synchronous and asynchronous assignment of default values. While you can set an input's default value using `defaultValue` or `defaultChecked` [(as detailed in the official React documentation)](https://react.dev/reference/react-dom/components/input), it is **recommended** to use `defaultValues` for the entire form.

```javascript copy
useForm({
  defaultValues: {
    firstName: '',
    lastName: ''
  }
})

// set default value async
useForm({
  defaultValues: async () => fetch('/api-endpoint');
})
```

<Admonition type="important" title="Rules">

- You **should avoid** providing `undefined` as a default value, as it conflicts with the default state of a controlled component.
- `defaultValues` are cached. To reset them, use the [reset](/docs/useform/reset) API.
- `defaultValues` will be included in the submission result by default.
- It's recommended to avoid using custom objects containing prototype methods, such as `Moment` or `Luxon`, as `defaultValues`.
- There are other options for including form data:

  ```javascript
  // adding a hidden input
  <input {...register("hidden", { value: "data" })} type="hidden" />
  ```

  ```javascript
  // include data onSubmit
  const onSubmit = (data) => {
    const output = {
      ...data,
      others: "others",
    }
  }
  ```

</Admonition>

#### values: <TypeText>FieldValues</TypeText> {#values}

---

The `values` prop will react to changes and update the form values, which is useful when your form needs to be updated by external state or server data. The `values` prop will overwrite the `defaultValues` prop, unless `resetOptions: { keepDefaultValues: true }` is also set for `useForm`.

```javascript copy
// set default value sync
function App({ values }) {
  useForm({
    values, // will get updated when values props updates
  })
}

function App() {
  const values = useFetch("/api")

  useForm({
    defaultValues: {
      firstName: "",
      lastName: "",
    },
    values, // will get updated once values returns
  })
}
```

#### errors: <TypeText>FieldErrors</TypeText> {#errors}

---

The `errors` props will react to changes and update the server errors state, which is useful when your form needs to be updated by external server returned errors.

```javascript copy
function App() {
  const { errors, data } = useFetch("/api")

  useForm({
    errors, // will get updated once errors returns
  })
}
```

#### resetOptions: <TypeText>KeepStateOptions</TypeText> {#resetOptions}

---

This property is related to value update behaviors. When `values` or `defaultValues` are updated, the `reset` API is invoked internally. It's important to specify the desired behavior after `values` or `defaultValues` are asynchronously updated. The configuration option itself is a reference to the [reset](/docs/useform/reset) method's options.

```javascript copy
// by default asynchronously value or defaultValues update will reset the form values
useForm({ values })
useForm({ defaultValues: async () => await fetch() })

// options to config the behaviour
// eg: I want to keep user interacted/dirty value and not remove any user errors
useForm({
  values,
  resetOptions: {
    keepDirtyValues: true, // user-interacted input will be retained
    keepErrors: true, // input errors will be retained with value update
  },
})
```

#### context: <TypeText>object</TypeText> {#context}

---

|                                                                                                                                                                   |                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| This context `object` is mutable and will be injected into the `resolver`'s second argument or [Yup](https://github.com/jquense/yup) validation's context object. | <CodeSandbox url="https://codesandbox.io/s/resolver-context-d9jqy"/> |

#### criteriaMode: <TypeText>firstError | all</TypeText> {#criteriaMode}

---

|                                                                                                                                                                                          |                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| <ul><li> When set to `firstError` (default), only the first error from each field will be gathered.</li> <li> When set to `all`, all errors from each field will be gathered. </li></ul> | <CodeSandbox url="https://codesandbox.io/s/react-hook-form-v6-errors-validatecriteriamode-all-p9xm6" /> |

#### shouldFocusError: <TypeText>boolean = true</TypeText> {#shouldFocusError}

---

When set to `true` (default), and the user submits a form that fails validation, focus is set on the first field with an error.

<Admonition type="note">

- Only registered fields with a `ref` will work. Custom registered inputs do not
  apply. For example: `register('test') // doesn't work`
- The focus order is based on the `register` order.

</Admonition>

#### delayError: <TypeText>number</TypeText> {#delayError}

---

|                                                                                                                                                                                                                  |                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| This configuration delays the display of error states to the end-user by a specified number of milliseconds. If the user corrects the error input, the error is removed instantly, and the delay is not applied. | <CodeSandbox url="https://codesandbox.io/s/useform-delayerror-q6c2d"/> |

#### validate: <TypeText>Function</TypeText> {#validate}

---

This example demonstrates how to use the **new `validate` API** in combination with `useForm` to perform **form-level validation** in a React application.

The `validate` function receives the entire form object and allows you to return a **structured error** that integrates with `formState.errors`.

**Examples:**

---

```javascript copy
const {
  register,
  formState: { errors },
} = useForm({
  validate: async ({ formValues }: FormValidateResult) => {
    if (formValues.test1.length > formValues.test.length) {
      return {
        type: "formError",
        message: "something is wrong here",
      }
    }

    if (formValue.test === "test") {
      return "direct error message"
    }

    return true
  },
})
```

#### shouldUnregister: <TypeText>boolean = false</TypeText> {#shouldUnregister}

---

By default, an input value will be retained when input is removed. However, you can set `shouldUnregister` to `true` to `unregister` input during unmount.

- This is a global configuration that overrides child-level configurations. To have individual behavior, set the configuration at the component or hook level, not at `useForm`.
- By default, `shouldUnregister: false` means unmounted fields are **not validated** by built-in validation.
- By setting `shouldUnregister` to true at `useForm` level, `defaultValues` will **not** be merged against submission result.
- Setting `shouldUnregister: true` makes your form behave more closely to native forms.
  - Form values are stored within the inputs themselves.
  - Unmounting an input removes its value.
  - Hidden inputs should use the `hidden` attribute for storing hidden data.
  - Only registered inputs are included as submission data.
  - Unmounted inputs must be notified at either `useForm` or `useWatch`'s `useEffect` for the hook form to verify that the input is unmounted from the DOM.

    ```javascript
    const NotWork = () => {
      const [show, setShow] = React.useState(false)
      // ❌ won't get notified, need to invoke unregister
      return show && <input {...register("test")} />
    }

    const Work = ({ control }) => {
      const { show } = useWatch({ control })
      // ✅ get notified at useEffect
      return show && <input {...register("test1")} />
    }

    const App = () => {
      const [show, setShow] = React.useState(false)
      const { control } = useForm({ shouldUnregister: true })
      return (
        <div>
          // ✅ get notified at useForm's useEffect
          {show && <input {...register("test2")} />}
          <NotWork />
          <Work control={control} />
        </div>
      )
    }
    ```

#### shouldUseNativeValidation: <TypeText>boolean = false</TypeText> {#shouldUseNativeValidation}

---

This config will enable [browser native validation](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation). It will also enable CSS selectors `:valid` and`:invalid` making styling inputs easier. You can still use these selectors even when client-side validation is disabled.

- Only works with `onSubmit` and `onChange` modes, as the `reportValidity` execution will focus the error input.
- Each registered field's validation message is required to be string to display them natively.
- This feature only works with the `register` API and&nbsp; `useController/Controller` that are connected with actual DOM references.

**Examples:**

---

```javascript copy
import { useForm } from "react-hook-form"

export default function App() {
  const { register, handleSubmit } = useForm({
    shouldUseNativeValidation: true,
  })
  const onSubmit = async (data) => {
    console.log(data)
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input
        {...register("firstName", {
          required: "Please enter your first name.",
        })} // custom message
      />
      <input type="submit" />
    </form>
  )
}
```

#### disabled: <TypeText>boolean = false</TypeText> {#disabled}

---

This config allows you to disable the entire form and all associated inputs when set to `true`.<br />
This can be useful for preventing user interaction during asynchronous tasks or other
situations where inputs should be temporarily unresponsive.

**Examples:**

---

```javascript copy
import { useForm, Controller } from "react-hook-form"

const App = () => {
  const [disabled, setDisabled] = useState(false)
  const { register, handleSubmit, control } = useForm({
    disabled,
  })

  return (
    <form
      onSubmit={handleSubmit(async () => {
        setDisabled(true)
        await sleep(100)
        setDisabled(false)
      })}
    >
      <input
        type={"checkbox"}
        {...register("checkbox")}
        data-testid={"checkbox"}
      />
      <select {...register("select")} data-testid={"select"} />

      <Controller
        control={control}
        render={({ field }) => <input disabled={field.disabled} />}
        name="test"
      />

      <button type="submit">Submit</button>
    </form>
  )
}
```

#### resolver: [Resolver](/ts#Resolver) {#resolver}

---

This function allows you to use any external validation library such as [Yup](https://github.com/jquense/yup), [Zod](https://github.com/vriad/zod), [Joi](https://github.com/hapijs/joi), [Vest](https://github.com/ealush/vest), [Ajv](https://github.com/ajv-validator/ajv) and many others. The goal is to make sure you can seamlessly integrate whichever validation library you prefer. If you're not using a library, you can always write your own logic to validate your forms.

```bash copy
npm install @hookform/resolvers
```

##### Props

---

| Name      | Type                                                                                                                      | Description                                                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `values`  | <TypeText>object</TypeText>                                                                                               | This object contains the entire form values.                                                                                                |
| `context` | <TypeText>object</TypeText>                                                                                               | This is the `context` object which you can provide to the `useForm` config. It is a mutable `object` that can be changed on each re-render. |
| `options` | <TypeText><pre>{JSON.stringify({ criteriaMode: "string", fields: "object", names: "string[]" }, null,2)}</pre></TypeText> | This is the option object containing information about the validated fields, names and `criteriaMode` from `useForm`.                       |

<Admonition type="important" title="Rules">

- Schema validation focuses on field-level error reporting. Parent-level error checking is limited to the direct parent level, which is applicable for components such as group checkboxes.
- This function will be cached.
- Re-validation of an input will only occur one field at time during a user’s interaction. The lib itself will evaluate the `error` object to trigger a re-render accordingly.
- A resolver can not be used with the built-in validators (e.g.: required, min, etc.)
- When building a custom resolver:
  - Make sure that you return an object with both `values` and `errors` properties. Their default values should be an empty object. For example: `{}`.
  - The keys of the `errors` object should match the `name` values of your fields, but they _must_ be hierarchical rather than a single key for deep errors:
    `❌ { "participants.1.name": someErr }` will not set or clear properly - instead, use `✅ { participants: [null, { name: someErr } ] }` as this is reachable
    as `errors.participants[1].name` - you can still prepare your errors using flat keys, and then use a function like this one from the zod resolver:
    [toNestErrors(flatErrs, resolverOptions)](https://github.com/react-hook-form/resolvers/blob/master/src/toNestErrors.ts)

</Admonition>

**Examples:**

---

<TabGroup buttonLabels={["Yup","Zod","Joi","Ajv","Vest", "Custom"]}>

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-apply-validation-ts-forked-nmbyh"
import { useForm } from "react-hook-form"
import { yupResolver } from "@hookform/resolvers/yup"
import * as yup from "yup"

const schema = yup
  .object()
  .shape({
    name: yup.string().required(),
    age: yup.number().required(),
  })
  .required()

const App = () => {
  const { register, handleSubmit } = useForm({
    resolver: yupResolver(schema), // yup, joi and even your own.
  })

  return (
    <form onSubmit={handleSubmit((d) => console.log(d))}>
      <input {...register("name")} />
      <input type="number" {...register("age")} />
      <input type="submit" />
    </form>
  )
}
```

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-zod-resolver-ts-example-forked-w72vp"
import { useForm } from "react-hook-form"
import { zodResolver } from "@hookform/resolvers/zod"
import * as z from "zod"

const schema = z.object({
  name: z.string(),
  age: z.number(),
})

type Schema = z.infer<typeof schema>

const App = () => {
  const { register, handleSubmit } = useForm({
    resolver: zodResolver(schema),
  })

  return (
    <form
      onSubmit={handleSubmit((data) => {
        // handle inputs
        console.log(data)
      })}
    >
      <input {...register("name")} />
      <input {...register("age", { valueAsNumber: true })} type="number" />
      <input type="submit" />
    </form>
  )
}
```

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-joiresolver-v6-ts-forked-5pseh"
import { useForm } from "react-hook-form"
import { joiResolver } from "@hookform/resolvers/joi"
import Joi from "joi"

interface IFormInput {
  name: string
  age: number
}

const schema = Joi.object({
  name: Joi.string().required(),
  age: Joi.number().required(),
})

const App = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<IFormInput>({
    resolver: joiResolver(schema),
  })
  const onSubmit = (data: IFormInput) => {
    console.log(data)
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("name")} />
      <input type="number" {...register("age")} />
      <input type="submit" />
    </form>
  )
}
```

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-ajvresolver-vr3imc"
import { useForm } from "react-hook-form"
import { ajvResolver } from "@hookform/resolvers/ajv"

// must use `minLength: 1` to implement required field
const schema = {
  type: "object",
  properties: {
    username: {
      type: "string",
      minLength: 1,
      errorMessage: { minLength: "username field is required" },
    },
    password: {
      type: "string",
      minLength: 1,
      errorMessage: { minLength: "password field is required" },
    },
  },
  required: ["username", "password"],
  additionalProperties: false,
}

const App = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: ajvResolver(schema),
  })

  return (
    <form onSubmit={handleSubmit((data) => console.log(data))}>
      <input {...register("username")} />
      {errors.username && <p>{errors.username.message}</p>}
      <input {...register("password")} />
      {errors.password && <p>{errors.password.message}</p>}
      <button type="submit">submit</button>
    </form>
  )
}
```

```tsx copy sandbox="https://codesandbox.io/s/vest-8q874"
import * as React from "react"
import { useForm } from "react-hook-form"
import { vestResolver } from "@hookform/resolvers/vest"
import vest, { test, enforce } from "vest"

const validationSuite = vest.create((data = {}) => {
  test("username", "Username is required", () => {
    enforce(data.username).isNotEmpty()
  })

  test("username", "Must be longer than 3 chars", () => {
    enforce(data.username).longerThan(3)
  })

  test("password", "Password is required", () => {
    enforce(data.password).isNotEmpty()
  })

  test("password", "Password must be at least 5 chars", () => {
    enforce(data.password).longerThanOrEquals(5)
  })

  test("password", "Password must contain a digit", () => {
    enforce(data.password).matches(/[0-9]/)
  })

  test("password", "Password must contain a symbol", () => {
    enforce(data.password).matches(/[^A-Za-z0-9]/)
  })
})

const App = () => {
  const { register, handleSubmit } = useForm({
    resolver: vestResolver(validationSuite),
  })

  return (
    <form onSubmit={handleSubmit((data) => console.log(data))}>
      <input {...register("username")} />
      <input {...register("password")} />
      <input type="submit" />
    </form>
  )
}
```

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-customresoliver-ts-v7-juc63"
import * as React from "react"
import { useForm } from "react-hook-form"
import * as Joi from "joi"

interface IFormInputs {
  username: string
}

const validationSchema = Joi.object({
  username: Joi.string().alphanum().min(3).max(30).required(),
})

const App = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<IFormInputs>({
    resolver: async (data) => {
      const { error, value: values } = validationSchema.validate(data, {
        abortEarly: false,
      })

      return {
        values: error ? {} : values,
        errors: error
          ? error.details.reduce((previous, currentError) => {
              return {
                ...previous,
                [currentError.path[0]]: currentError,
              }
            }, {})
          : {},
      }
    },
  })

  const onSubmit = (data: IFormInputs) => console.log(data)

  return (
    <div className="App">
      <h1>resolver</h1>

      <form onSubmit={handleSubmit(onSubmit)}>
        <label>Username</label>
        <input {...register("username")} />
        {errors.username && <p>errors.username.message</p>}
        <input type="submit" />
      </form>
    </div>
  )
}
```

</TabGroup>

Need more? See [Resolver Documentation](https://github.com/react-hook-form/resolvers#quickstart)

<Admonition type="tip" >

You can debug your schema via the following code snippet:

```javascript copy
resolver: async (data, context, options) => {
  // you can debug your validation schema here
  console.log("formData", data)
  console.log(
    "validation result",
    await anyResolver(schema)(data, context, options)
  )
  return anyResolver(schema)(data, context, options)
}
```

</Admonition>

#### `useForm` return and `useEffect` dependencies

In a future major release, `useForm` return will be memoized to optimize performance and reflect changes in `formState`.
As a result, adding the entire return value of `useForm` to a `useEffect` dependency list may lead to infinite loops.

<Admonition type="warning" >

The following code is likely to create this situation:

```javascript
const methods = useForm()

useEffect(() => {
  methods.reset({ ... })
}, [methods])
```

</Admonition>

Passing only the relevant methods, as showed below, should avoid this kind of issue:

```javascript
const methods = useForm()

useEffect(() => {
  methods.reset({ ... })
}, [methods.reset])
```

<Admonition type="tip" >

The recommended way is to pass destructured methods to the dependencies of an `useEffect`

```javascript
const { reset } = useForm()

useEffect(() => {
  reset({ ... })
}, [reset])
```

</Admonition>

[More info can be found on this issue](https://github.com/react-hook-form/react-hook-form/issues/12463)

#### Return

---

The following list contains reference to `useForm` return props.

- [register](/docs/useform/register)
- [unregister](/docs/useform/unregister)
- [formState](/docs/useform/formstate)
- [watch](/docs/useform/watch)
- [handleSubmit](/docs/useform/handlesubmit)
- [reset](/docs/useform/reset)
- [resetField](/docs/useform/resetfield)
- [setError](/docs/useform/seterror)
- [clearErrors](/docs/useform/clearerrors)
- [setValue](/docs/useform/setvalue)
- [setFocus](/docs/useform/setfocus)
- [getValues](/docs/useform/getvalues)
- [getFieldState](/docs/useform/getfieldstate)
- [trigger](/docs/useform/trigger)
- [control](/docs/useform/control)
- [Form](/docs/useform/form)


---

## Source: `src/content/docs/useformcontext.mdx`

---
title: useFormContext
description: React Context API for hook form
sidebar: apiLinks
---

<SelectNav
  options={[
    {
      label: "FormProvider",
      value: "/docs/formprovider",
    },
  ]}
/>

## \</> `useFormContext:` <TypeText>Function</TypeText>

This custom hook allows you to access the form context. `useFormContext` is intended to be used in deeply nested structures, where it would become inconvenient to pass the context as a prop.

### Return

---

This hook will return all the useForm return methods and props.

```javascript
const methods = useForm()

<FormProvider {...methods} /> // all the useForm return props

const methods = useFormContext() // retrieve those props
```

<Admonition type="important" title="Rules">
  You need to wrap your form with the [`FormProvider`](/docs/formprovider)
  component for `useFormContext` to work properly.
</Admonition>

**Example:**

```javascript copy codesandbox="https://codesandbox.io/s/react-hook-form-v7-form-context-ytudi"
import { useForm, FormProvider, useFormContext } from "react-hook-form"

export default function App() {
  const methods = useForm()
  const onSubmit = (data) => console.log(data)
  const { register, reset } = methods

  useEffect(() => {
    reset({
      name: "data",
    })
  }, [reset]) // ❌ never put `methods` as the deps

  return (
    <FormProvider {...methods}>
      // pass all methods into the context
      <form onSubmit={methods.handleSubmit(onSubmit)}>
        <NestedInput />
        <input {...register("name")} />
        <input type="submit" />
      </form>
    </FormProvider>
  )
}

function NestedInput() {
  const { register } = useFormContext() // retrieve all hook methods
  return <input {...register("test")} />
}
```


---

## Source: `src/content/docs/useformstate/errormessage.mdx`

---
title: ErrorMessage
description: An error message component to handle errors
sidebar: apiLinks
---

## \</> `ErrorMessage:` <TypeText>Component</TypeText>

A simple component to render associated input's error message.

```bash
npm install @hookform/error-message
```

### Props

---

| Name      | Type                                                                                        | Required | Description                                                                                                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`    | <TypeText>string</TypeText>                                                                 | ✓        | Name of the field.                                                                                                                                                                            |
| `errors`  | <TypeText>object</TypeText>                                                                 |          | `errors` object from React Hook Form. Optional if you are using `FormProvider`.                                                                                                               |
| `message` | <TypeText>string \| React.ReactElement</TypeText>                                           |          | Inline error message.                                                                                                                                                                         |
| `as`      | <TypeText>React.ElementType \| string</TypeText>                                            |          | Wrapper component or HTML tag. For example: `as="span"` or `as={<Text />}`                                                                                                                    |
| `render`  | <TypeText>`({ message: string \| React.ReactElement, messages?: Object}) => any`</TypeText> |          | This is a [render prop](https://reactjs.org/docs/render-props.html) for rendering error message or messages.<br/><br/>**Note:** you need to set `criteriaMode` to 'all' for using `messages`. |

**Examples:**

---

**Single Error Message**

<TabGroup buttonLabels={["TS", "JS"]} >

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-v7-ts-errormessage-d1ues"
import { useForm } from "react-hook-form"
import { ErrorMessage } from "@hookform/error-message"

interface FormInputs {
  singleErrorInput: string
}

export default function App() {
  const {
    register,
    formState: { errors },
    handleSubmit,
  } = useForm<FormInputs>()
  const onSubmit = (data: FormInputs) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input
        {...register("singleErrorInput", { required: "This is required." })}
      />
      <ErrorMessage errors={errors} name="singleErrorInput" />

      <ErrorMessage
        errors={errors}
        name="singleErrorInput"
        render={({ message }) => <p>{message}</p>}
      />

      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-v7-errormessage-jufsl"
import { useForm } from "react-hook-form"
import { ErrorMessage } from "@hookform/error-message"

export default function App() {
  const {
    register,
    formState: { errors },
    handleSubmit,
  } = useForm()
  const onSubmit = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input
        {...register("singleErrorInput", { required: "This is required." })}
      />
      <ErrorMessage errors={errors} name="singleErrorInput" />

      <ErrorMessage
        errors={errors}
        name="singleErrorInput"
        render={({ message }) => <p>{message}</p>}
      />

      <input type="submit" />
    </form>
  )
}
```

</TabGroup>

**Multiple Error Messages**

<TabGroup buttonLabels={["TS", "JS"]}>

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-v6-ts-errormessage-multiple-error-messages-forked-sy5f0"
import { useForm } from "react-hook-form"
import { ErrorMessage } from "@hookform/error-message"

interface FormInputs {
  multipleErrorInput: string
}

export default function App() {
  const {
    register,
    formState: { errors },
    handleSubmit,
  } = useForm<FormInputs>({
    criteriaMode: "all",
  })
  const onSubmit = (data: FormInputs) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input
        {...register("multipleErrorInput", {
          required: "This is required.",
          pattern: {
            value: /d+/,
            message: "This input is number only.",
          },
          maxLength: {
            value: 10,
            message: "This input exceed maxLength.",
          },
        })}
      />
      <ErrorMessage
        errors={errors}
        name="multipleErrorInput"
        render={({ messages }) =>
          messages &&
          Object.entries(messages).map(([type, message]) => (
            <p key={type}>{message}</p>
          ))
        }
      />

      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-v7-errormessage-multiple-error-messages-lnvkt"
import { useForm } from "react-hook-form"
import { ErrorMessage } from "@hookform/error-message"

export default function App() {
  const {
    register,
    formState: { errors },
    handleSubmit,
  } = useForm({
    criteriaMode: "all",
  })
  const onSubmit = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input
        {...register("multipleErrorInput", {
          required: "This is required.",
          pattern: {
            value: /d+/,
            message: "This input is number only.",
          },
          maxLength: {
            value: 10,
            message: "This input exceed maxLength.",
          },
        })}
      />
      <ErrorMessage
        errors={errors}
        name="multipleErrorInput"
        render={({ messages }) =>
          messages &&
          Object.entries(messages).map(([type, message]) => (
            <p key={type}>{message}</p>
          ))
        }
      />

      <input type="submit" />
    </form>
  )
}
```

</TabGroup>


---

## Source: `src/content/docs/useformstate/formstatesubscribe.mdx`

---
title: FormStateSubscribe
description: Component to subscribe to form state update
sidebar: apiLinks
---

## \</> `FormStateSubscribe:` <TypeText>Component</TypeText>

A React Hook Form component that provides the same functionality as `uesFormState`, but in component form. Instead of using the hook inside another component, you can use `<FormStateSubscribe />` directly in your JSX to subscribe to and render form state.

### Props

---

| Name       | Type                                     | Description                                                                                                                                                                                                         |
| ---------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `control`  | <TypeText>Object</TypeText>              | [`control`](/docs/useform/control) object provided by `useForm`. It's optional if you are using `FormProvider`.                                                                                                     |
| `name`     | <TypeText>string \| string[] </TypeText> | Provide a single input name, an array of them, or subscribe to all inputs' formState update.                                                                                                                        |
| `disabled` | <TypeText>boolean = false</TypeText>     | Option to disable the subscription.                                                                                                                                                                                 |
| `exact`    | <TypeText>boolean = false</TypeText>     | This prop will enable an exact match for input name subscriptions.                                                                                                                                                  |
| `render`   | <TypeText>Function</TypeText>            | Subscribes to form state of specified form field(s) and re-renders its child function whenever the form state changes. This allows you to declaratively consume form state in JSX without manually wiring up state. |

**Examples:**

---

```tsx copy sandbox=""
import { useForm, FormStateSubscribe } from "react-hook-form"

const App = () => {
  const { register, control } = useForm()

  return (
    <div>
      <form>
        <input {...register("foo", { min: 3 })} />
        <input {...register("bar")} />
        {/* re-render only when form state of `foo` changes */}
        <FormStateSubscribe
          control={control}
          name="foo"
          render={({ errors }) => <span>{errors.foo?.message}</span>}
        />
      </form>
    </div>
  )
}
```

```

```


---

## Source: `src/content/docs/useformstate.mdx`

---
title: useFormState
description: Subscribe to form state update
sidebar: apiLinks
---

<SelectNav
  options={[
    {
      label: "FormStateSubscribe",
      value: "/docs/useformstate/formstatesubscribe",
    },
    {
      label: "ErrorMessage",
      value: "/docs/useformstate/errormessage",
    },
  ]}
/>

## \</> `useFormState:` <TypeText>`({ control: Control }) => FormState`</TypeText>

This custom hook allows you to subscribe to each form state, and isolate the re-render at the custom hook level. It has its scope in terms of form state subscription, so it would not affect other useFormState and useForm. Using this hook can reduce the re-render impact on large and complex form application.

### Props

---

| Name       | Type                                     | Description                                                                                                     |
| ---------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `control`  | <TypeText>Object</TypeText>              | [`control`](/docs/useform/control) object provided by `useForm`. It's optional if you are using `FormProvider`. |
| `name`     | <TypeText>string \| string[] </TypeText> | Provide a single input name, an array of them, or subscribe to all inputs' formState update.                    |
| `disabled` | <TypeText>boolean = false</TypeText>     | Option to disable the subscription.                                                                             |
| `exact`    | <TypeText>boolean = false</TypeText>     | This prop will enable an exact match for input name subscriptions.                                              |

### Return

---

| Name                 | Type                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `isDirty`            | <TypeText>boolean</TypeText> | Set to `true` after the user modifies any of the inputs.<ul><li>**Important:** make sure to provide all inputs' `defaultValues` at the `useForm`, so hook form can have a single source of truth to compare whether the form is dirty.<CodeArea withOutCopy rawData={`const {\n  formState: { isDirty, dirtyFields },\n  setValue\n} = useForm({ defaultValues: { test: "" } })\n\n// isDirty: true ✅\nsetValue('test', 'change')\n\n// isDirty: false because there getValues() === defaultValues ❌\nsetValue('test', '')`}/></li><li>File typed input will need to be managed at the app level due to the ability to cancel file selection and [FileList](https://developer.mozilla.org/en-US/docs/Web/API/FileList) object.</li><li>Do not support custom object, Class or File object.</li></ul> |
| `dirtyFields`        | <TypeText>object</TypeText>  | An object with the user-modified fields. Make sure to provide all inputs' `defaultValues` via `useForm`, so the library can compare against the `defaultValues.`<ul><li>**Important:** make sure to provide `defaultValues` at the `useForm`, so hook form can have a single source of truth to compare each field's dirtiness.</li><li>Dirty fields will **not** represent as `isDirty` `formState`, because dirty fields are marked field dirty at field level rather the entire form. If you want to determine the entire form state use `isDirty` instead.</li></ul>                                                                                                                                                                                                                               |
| `touchedFields`      | <TypeText>object</TypeText>  | An object containing all the inputs the user has interacted with.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `defaultValues`      | <TypeText>object</TypeText>  | The value which has been set at [useForm](/docs/useform)'s `defaultValues` or updated `defaultValues` via [reset](/docs/useform/reset) API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `isSubmitted`        | <TypeText>boolean</TypeText> | Set to `true` after the form is submitted. Will remain `true` until the `reset` method is invoked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `isSubmitSuccessful` | <TypeText>boolean</TypeText> | Indicate the form was successfully submitted without any runtime error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `isSubmitting`       | <TypeText>boolean</TypeText> | `true` if the form is currently being submitted. `false` otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `isLoading`          | <TypeText>boolean</TypeText> | `true` if the form is currently loading async default values.<ul><li>**Important:** this prop is only applicable to async `defaultValues`<CodeArea withOutCopy rawData={`const {\n  formState: { isLoading }\n} = useForm({\n  defaultValues: async () => await fetch('/api')\n})`}/></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `submitCount`        | <TypeText>number</TypeText>  | Number of times the form was submitted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `isValid`            | <TypeText>boolean</TypeText> | Set to `true` if the form doesn't have any errors.<ul><li>`setError` has no effect on `isValid` `formState`, `isValid` will always derived via the entire form validation result.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `isValidating`       | <TypeText>boolean</TypeText> | Set to `true` during validation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `validatingFields`   | <TypeText>object</TypeText>  | Capture fields which are getting async validation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `errors`             | <TypeText>object</TypeText>  | An object with field errors. There is also an [ErrorMessage](/docs/useformstate/errormessage) component to retrieve error message easily.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `disabled`           | <TypeText>boolean</TypeText> | Set to true if the form is disabled via the disabled prop in [useForm](/docs/useform).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

<Admonition type="important" title="Rules">

Returned `formState` is wrapped with Proxy to improve render performance and skip extra computation if specific state is not subscribed, so make sure you deconstruct or read it before render in order to enable the subscription.

```javascript
const { isDirty } = useFormState() // ✅
const formState = useFormState() // ❌ should deconstruct the formState
```

</Admonition>

**Examples**

---

```javascript copy sandbox="https://codesandbox.io/s/useformstate-75xly"
import { useForm, useFormState } from "react-hook-form"

function Child({ control }) {
  const { dirtyFields } = useFormState({ control })

  return dirtyFields.firstName ? <p>Field is dirty.</p> : null
}

export default function App() {
  const { register, handleSubmit, control } = useForm({
    defaultValues: {
      firstName: "firstName",
    },
  })
  const onSubmit = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("firstName")} placeholder="First Name" />
      <Child control={control} />

      <input type="submit" />
    </form>
  )
}
```


---

## Source: `src/content/docs/uselens.mdx`

---
title: useLens
description: Type-safe functional lenses for React Hook Form
sidebar: apiLinks
---

## \</> `useLens`

React Hook Form Lenses is a powerful TypeScript-first library that brings the elegance of functional lenses to form development. It provides type-safe manipulation of nested structures, enabling developers to precisely control and transform complex data with ease.

`useLens` is a custom hook that creates a lens instance connected to your React Hook Form control, enabling type-safe focusing, transformation, and manipulation of deeply nested form data structures through functional programming concepts.

### Installation

```bash copy
npm install @hookform/lenses
```

### Features

- **Type-Safe Form State**: Focus on specific parts of your data with full TypeScript support and precise type inference
- **Functional Lenses**: Build complex transformations through composable lens operations
- **Deep Structure Support**: Handle deeply nested structures and arrays elegantly with specialized operations
- **Seamless Integration**: Work smoothly with React Hook Form's Control API and existing functionality
- **Optimized Performance**: Each lens is cached and reused for optimal efficiency
- **Array Handling**: Specialized support for dynamic fields with type-safe mapping
- **Composable API**: Build complex transformations through elegant lens composition

### Props

---

The `useLens` hook accepts the following configuration:

#### `control`: <TypeText>Control\<TFieldValues></TypeText>

**Required.** The control object from React Hook Form's `useForm` hook. This connects your lens to the form management system.

```tsx copy
const { control } = useForm<MyFormData>()
const lens = useLens({ control })
```

#### Dependencies Array (Optional)

You can optionally pass a dependency array as the second parameter to clear the lens cache and re-create all lenses when dependencies change:

```tsx copy
const lens = useLens({ control }, [dependencies])
```

This is useful when you need to reset the entire lens cache based on external state changes.

### Return

---

The following table contains information about the main types and operations available on lens instances:

**Core Types:**

`Lens<T>` - The main lens type that provides different operations based on the field type you're working with:

```ts
type LensWithArray = Lens<string[]>
type LensWithObject = Lens<{ name: string; age: number }>
type LensWithPrimitive = Lens<string>
```

**Main Operations:**

These are the core methods available on every lens instance:

| Method                | Description                                    | Returns              |
| --------------------- | ---------------------------------------------- | -------------------- |
| [`focus`](#focus)     | Focuses on a specific field path               | `Lens<PathValue>`    |
| [`reflect`](#reflect) | Transform and reshape lens structure           | `Lens<NewStructure>` |
| [`map`](#map)         | Iterate over array fields (with useFieldArray) | `R[]`                |
| [`interop`](#interop) | Connect to React Hook Form's control system    | `{ control, name }`  |
| [`narrow`](#narrow)   | Type-safe narrowing of union types             | `Lens<SubType>`      |
| [`assert`](#assert)   | Runtime type assertion for type narrowing      | `void`               |
| [`defined`](#defined) | Exclude null and undefined from lens type      | `Lens<NonNullable>`  |
| [`cast`](#cast)       | Force type change (unsafe)                     | `Lens<NewType>`      |

---

### focus {#focus}

Creates a new lens focused on a specific path. This is the primary method for drilling down into your data structure.

```tsx copy
// Type-safe path focusing
const profileLens = lens.focus("profile")
const emailLens = lens.focus("profile.email")
const arrayItemLens = lens.focus("users.0.name")
```

**Array focusing:**

```tsx copy
function ContactsList({ lens }: { lens: Lens<Contact[]> }) {
  // Focus on specific array index
  const firstContact = lens.focus("0")
  const secondContactName = lens.focus("1.name")

  return (
    <div>
      <ContactForm lens={firstContact} />
      <input
        {...secondContactName.interop((ctrl, name) => ctrl.register(name))}
      />
    </div>
  )
}
```

<Admonition type="important" title="TypeScript Support">

The `focus` method provides full TypeScript support with autocompletion and type checking:

- Autocomplete available field paths
- Type errors for non-existent paths
- Inferred return types based on focused field

</Admonition>

### reflect {#reflect}

Transforms the lens structure with complete type inference. This is useful when you want to create a new lens from an existing one with a different shape to pass to a shared component.

The first argument is a proxy with a dictionary of lenses. Note that lens instantiation happens only on property access. The second argument is the original lens.

#### Object Reflection

```tsx copy
const contactLens = lens.reflect(({ profile }) => ({
  name: profile.focus("contact.firstName"),
  phoneNumber: profile.focus("contact.phone"),
}))

<SharedComponent lens={contactLens} />

function SharedComponent({
  lens,
}: {
  lens: Lens<{ name: string; phoneNumber: string }>
}) {
  return (
    <div>
      <input
        {...lens.focus("name").interop((ctrl, name) => ctrl.register(name))}
      />
      <input
        {...lens
          .focus("phoneNumber")
          .interop((ctrl, name) => ctrl.register(name))}
      />
    </div>
  )
}
```

**Alternative syntax using the lens parameter:**

You can also use the second parameter (the original lens) directly:

```tsx
const contactLens = lens.reflect((_, l) => ({
  name: l.focus("profile.contact.firstName"),
  phoneNumber: l.focus("profile.contact.phone"),
}))

<SharedComponent lens={contactLens} />

function SharedComponent({
  lens,
}: {
  lens: Lens<{ name: string; phoneNumber: string }>
}) {
  // ...
}
```

#### Array Reflection

You can restructure array lenses:

```tsx
function ArrayComponent({ lens }: { lens: Lens<{ value: string }[]> }) {
  return (
    <AnotherComponent lens={lens.reflect(({ value }) => [{ data: value }])} />
  )
}

function AnotherComponent({ lens }: { lens: Lens<{ data: string }[]> }) {
  // ...
}
```

<Admonition type="important">

Note that for array reflection, you must pass an array with a single item as the template.

</Admonition>

#### Merging Lenses

You can use `reflect` to merge two lenses into one:

```tsx
function Component({
  lensA,
  lensB,
}: {
  lensA: Lens<{ firstName: string }>
  lensB: Lens<{ lastName: string }>
}) {
  const combined = lensA.reflect((_, l) => ({
    firstName: l.focus("firstName"),
    lastName: lensB.focus("lastName"),
  }))

  return <PersonForm lens={combined} />
}
```

Keep in mind that in such cases, the function passed to `reflect` is no longer pure.

#### Spread Operator Support

You can use spread in reflect if you want to leave other properties as is. At runtime, the first argument is just a proxy that calls `focus` on the original lens. This is useful for proper typing when you need to change the property names for only a few fields and leave the rest unchanged:

```tsx
function Component({
  lens,
}: {
  lens: Lens<{ firstName: string; lastName: string; age: number }>
}) {
  return (
    <PersonForm
      lens={lens.reflect(({ firstName, lastName, ...rest }) => ({
        ...rest,
        name: firstName,
        surname: lastName,
      }))}
    />
  )
}
```

### map {#map}

Maps over array fields with `useFieldArray` integration. This method requires the `fields` property from `useFieldArray`.

```tsx copy
import { useFieldArray } from "@hookform/lenses/rhf"

function ContactsList({ lens }: { lens: Lens<Contact[]> }) {
  const { fields, append, remove } = useFieldArray(lens.interop())

  return (
    <div>
      <button onClick={() => append({ name: "", email: "" })}>
        Add Contact
      </button>

      {lens.map(fields, (value, l, index) => (
        <div key={value.id}>
          <button onClick={() => remove(index)}>Remove</button>
          <ContactForm lens={l} />
        </div>
      ))}
    </div>
  )
}

function ContactForm({
  lens,
}: {
  lens: Lens<{ name: string; email: string }>
}) {
  return (
    <div>
      <input
        {...lens.focus("name").interop((ctrl, name) => ctrl.register(name))}
      />
      <input
        {...lens.focus("email").interop((ctrl, name) => ctrl.register(name))}
      />
    </div>
  )
}
```

**Map callback parameters:**

| Parameter    | Type        | Description                            |
| ------------ | ----------- | -------------------------------------- |
| `value`      | `T`         | The current field value with `id`      |
| `lens`       | `Lens<T>`   | Lens focused on the current array item |
| `index`      | `number`    | Current array index                    |
| `array`      | `T[]`       | The complete array                     |
| `originLens` | `Lens<T[]>` | The original array lens                |

### interop {#interop}

The `interop` method provides seamless integration with React Hook Form by exposing the underlying `control` and `name` properties. This allows you to connect your lens to React Hook Form's control API.

#### First Variant: Object Return

The first variant involves calling `interop()` without arguments, which returns an object containing the `control` and `name` properties for React Hook Form:

```tsx
const { control, name } = lens.interop()

return <input {...control.register(name)} />
```

#### Second Variant: Callback Function

The second variant passes a callback function to `interop` which receives the `control` and `name` properties as arguments. This allows you to work with these properties directly within the callback scope:

```tsx
return (
  <form onSubmit={handleSubmit(console.log)}>
    <input {...lens.interop((ctrl, name) => ctrl.register(name))} />
    <input type="submit" />
  </form>
)
```

#### Integration with useController

The `interop` method's return value can be passed directly to the `useController` hook from React Hook Form, providing seamless integration:

```tsx
import { useController } from "react-hook-form"

function ControlledInput({ lens }: { lens: Lens<string> }) {
  const { field, fieldState } = useController(lens.interop())

  return (
    <div>
      <input {...field} />
      {fieldState.error && <p>{fieldState.error.message}</p>}
    </div>
  )
}
```

<Admonition type="info" title="Type System Escape Hatches">

The `narrow`, `assert`, `defined`, and `cast` methods serve as escape hatches for current TypeScript limitations with lens type compatibility. These methods address scenarios where you need to pass lenses with wider types to components expecting narrower types.

These workarounds will become less necessary once [issue #38](https://github.com/react-hook-form/lenses/issues/38) is resolved, which aims to improve lens type variance to allow more natural type narrowing and component composition.

</Admonition>

### narrow {#narrow}

The `narrow` method provides type-safe narrowing of union types, allowing you to tell the type system which branch of a union you want to work with. This is particularly useful when working with discriminated unions or optional values.

#### Manual Type Narrowing

Use the single generic parameter to manually narrow the type when you know (by external logic) what the value should be:

```tsx copy
// Lens<string | number>
const unionLens = lens.focus("optionalField")

// Narrow to string when you know it's a string
const stringLens = unionLens.narrow<string>()
// Now: Lens<string>
```

#### Discriminated Union Narrowing

Use the discriminant overload to narrow based on a specific property value:

```tsx copy
type Animal = { type: "dog"; breed: string } | { type: "cat"; indoor: boolean }

const animalLens: Lens<Animal> = lens.focus("pet")

// Narrow to Dog type using discriminant
const dogLens = animalLens.narrow("type", "dog")
// Now: Lens<{ type: 'dog'; breed: string }>

const breedLens = dogLens.focus("breed")
// Type-safe access to dog-specific properties
```

<Admonition type="important" title="Type Safety">

The `narrow` method performs type-level operations only. It doesn't validate the runtime value - use it when you have external guarantees about the value's type (e.g., from validation, conditional rendering, or runtime checks).

</Admonition>

### assert {#assert}

The `assert` method provides runtime type assertions that convince TypeScript the current lens is already the desired subtype. Unlike `narrow`, this is a type assertion that modifies the current lens instance.

#### Manual Type Assertion

Use the generic parameter to assert the lens is already the desired type:

```tsx copy
function processString(lens: Lens<string>) {
  // Work with string lens
}

const maybeLens: Lens<string | undefined> = lens.focus("optional")

// After your runtime check
if (value !== undefined) {
  maybeLens.assert<string>()
  processString(maybeLens) // Now TypeScript knows it's Lens<string>
}
```

#### Discriminant-Based Assertion

Use the discriminant overload when you're in a conditional branch:

```tsx copy
type Status =
  | { type: "loading" }
  | { type: "success"; data: string }
  | { type: "error"; message: string }

const statusLens: Lens<Status> = lens.focus("status")

// In a conditional branch
if (selected.type === "success") {
  statusLens.assert("type", "success")
  // Within this block, statusLens is Lens<{ type: 'success'; data: string }>
  const dataLens = statusLens.focus("data") // Type-safe access
}
```

<Admonition type="warning" title="Runtime Safety">

`assert` is a type-only operation that doesn't perform runtime validation. Ensure your assertions are backed by proper runtime checks to avoid type safety violations.

</Admonition>

### defined {#defined}

The `defined` method is a convenience function that narrows the lens type to exclude `null` and `undefined` values. This is equivalent to using `narrow<NonNullable<T>>()` but provides a more expressive API.

```tsx copy
const optionalLens: Lens<string | null | undefined> = lens.focus("optional")

// Remove null and undefined from the type
const definedLens = optionalLens.defined()
// Now: Lens<string>

// Use after validation
if (value != null) {
  const safeLens = optionalLens.defined()
  // Work with guaranteed non-null value
}
```

**Common use cases:**

```tsx copy
// Form validation
const emailLens = lens.focus("email") // Lens<string | undefined>

function validateEmail(email: string) {
  // validation logic
}

// After confirming value exists
if (formState.isValid) {
  const validEmailLens = emailLens.defined()
  // Pass to functions expecting non-null values
  validateEmail(validEmailLens.interop().control.getValues())
}
```

### cast {#cast}

The `cast` method forcefully changes the lens type to a new type, regardless of compatibility with the original type. This is a powerful but potentially **unsafe** operation that should be used with extreme caution.

```tsx copy
// Cast from unknown/any to specific type
const unknownLens: Lens<unknown> = lens.focus("dynamicData")
const stringLens = unknownLens.cast<string>()
// Now: Lens<string>

// Cast between incompatible types (dangerous!)
const numberLens: Lens<number> = lens.focus("count")
const stringLens = numberLens.cast<string>()
// Type system now thinks it's Lens<string>, but runtime value is still number
```

**Safe usage patterns:**

```tsx copy
// Working with external APIs returning 'any'
function processApiData(data: any) {
  const apiLens = LensCore.create(data)

  // Cast after runtime validation
  if (typeof data.user === "object" && data.user !== null) {
    const userLens = apiLens.focus("user").cast<User>()
    return <UserProfile lens={userLens} />
  }
}

// Type narrowing when you have more information
interface BaseConfig {
  type: string
}

interface DatabaseConfig extends BaseConfig {
  type: "database"
  connectionString: string
}

const configLens: Lens<BaseConfig> = lens.focus("config")

// After checking the type at runtime
if (config.type === "database") {
  const dbConfigLens = configLens.cast<DatabaseConfig>()
  // Now can access database-specific properties
}
```

<Admonition type="danger" title="Use with Extreme Caution">

`cast` bypasses TypeScript's type system entirely. It can lead to runtime errors if the underlying data doesn't match the asserted type. Always validate data at runtime before using `cast`, or prefer safer alternatives like `narrow` when possible.

</Admonition>

### useFieldArray

Import the enhanced `useFieldArray` from `@hookform/lenses/rhf` for seamless array handling with lenses.

```tsx copy
import { useFieldArray } from "@hookform/lenses/rhf"

function DynamicForm({
  lens,
}: {
  lens: Lens<{ items: { name: string; value: number }[] }>
}) {
  const itemsLens = lens.focus("items")
  const { fields, append, remove, move } = useFieldArray(itemsLens.interop())

  return (
    <div>
      <button onClick={() => append({ name: "", value: 0 })}>Add Item</button>

      {itemsLens.map(fields, (field, itemLens, index) => (
        <div key={field.id}>
          <input
            {...itemLens
              .focus("name")
              .interop((ctrl, name) => ctrl.register(name))}
          />
          <input
            type="number"
            {...itemLens
              .focus("value")
              .interop((ctrl, name) =>
                ctrl.register(name, { valueAsNumber: true })
              )}
          />
          <button onClick={() => remove(index)}>Remove</button>
          {index > 0 && (
            <button onClick={() => move(index, index - 1)}>Move Up</button>
          )}
        </div>
      ))}
    </div>
  )
}
```

<Admonition type="important" title="Rules">

- The `control` parameter is required and must be from React Hook Form's `useForm` hook
- Each lens is cached and reused for optimal performance - focusing on the same path multiple times returns the identical lens instance
- When using functions with methods like `reflect`, memoize the function to maintain caching benefits
- Dependencies array is optional but useful for clearing lens cache based on external state changes
- All lens operations maintain full TypeScript type safety and inference

</Admonition>

### Examples

#### Basic Usage

```tsx copy sandbox="https://codesandbox.io/p/sandbox/keen-herschel-y5h2ft"
import { useForm } from "react-hook-form"
import { Lens, useLens } from "@hookform/lenses"
import { useFieldArray } from "@hookform/lenses/rhf"

function FormComponent() {
  const { handleSubmit, control } = useForm<{
    firstName: string
    lastName: string
    children: {
      name: string
      surname: string
    }[]
  }>({})

  const lens = useLens({ control })

  return (
    <form onSubmit={handleSubmit(console.log)}>
      <PersonForm
        lens={lens.reflect(({ firstName, lastName }) => ({
          name: firstName,
          surname: lastName,
        }))}
      />
      <ChildForm lens={lens.focus("children")} />
      <input type="submit" />
    </form>
  )
}

function ChildForm({
  lens,
}: {
  lens: Lens<{ name: string; surname: string }[]>
}) {
  const { fields, append } = useFieldArray(lens.interop())

  return (
    <>
      <button type="button" onClick={() => append({ name: "", surname: "" })}>
        Add child
      </button>
      {lens.map(fields, (value, l) => (
        <PersonForm key={value.id} lens={l} />
      ))}
    </>
  )
}

// PersonForm is used twice with different sources
function PersonForm({
  lens,
}: {
  lens: Lens<{ name: string; surname: string }>
}) {
  return (
    <div>
      <StringInput lens={lens.focus("name")} />
      <StringInput lens={lens.focus("surname")} />
    </div>
  )
}

function StringInput({ lens }: { lens: Lens<string> }) {
  return <input {...lens.interop((ctrl, name) => ctrl.register(name))} />
}
```

### Motivation

Working with complex, deeply nested forms in React Hook Form can quickly become challenging. Traditional approaches often lead to common problems that make development more difficult and error-prone:

#### 1. Type-Safe Name Props Are Nearly Impossible

Creating reusable form components requires accepting a `name` prop to specify which field to control. However, making this type-safe in TypeScript is extremely challenging:

```tsx
// ❌ Loses type safety - no way to ensure name matches the form schema
interface InputProps<T> {
  name: string // Could be any string, even invalid field paths
  control: Control<T>
}

// ❌ Attempting proper typing leads to complex, unmaintainable generics
interface InputProps<T, TName extends Path<T>> {
  name: TName
  control: Control<T>
}
// This becomes unwieldy and breaks down with nested objects
```

#### 2. `useFormContext()` Creates Tight Coupling

Using `useFormContext()` in reusable components tightly couples them to specific form schemas, making them less portable and harder to share:

```tsx
// ❌ Tightly coupled to parent form structure
function AddressForm() {
  const { control } = useFormContext<UserForm>() // Locked to UserForm type

  return (
    <div>
      <input {...control.register("address.street")} />{" "}
      {/* Fixed field paths */}
      <input {...control.register("address.city")} />
    </div>
  )
}
// Can't reuse this component with different form schemas
```

#### 3. String-Based Field Paths Are Error-Prone

Building reusable components with string concatenation for field paths is fragile and difficult to maintain:

```tsx
// ❌ String concatenation is error-prone and hard to refactor
function PersonForm({ basePath }: { basePath: string }) {
  const { register } = useForm();

  return (
    <div>
      {/* No type safety, prone to typos */}
      <input {...register(`${basePath}.firstName`)} />
      <input {...register(`${basePath}.lastName`)} />
      <input {...register(`${basePath}.email`)} />
    </div>
  );
}

// Usage becomes unwieldy and error-prone
<PersonForm basePath="user.profile.owner" />
<PersonForm basePath="user.profile.emergency_contact" />
```

### Performance Optimization

#### Built-in Caching System

Lenses are automatically cached to prevent unnecessary component re-renders when using `React.memo`. This means that focusing on the same path multiple times will return the identical lens instance:

```tsx
assert(lens.focus("firstName") === lens.focus("firstName"))
```

#### Function Memoization

When using functions with methods like `reflect`, you need to be careful about function identity to maintain caching benefits:

```tsx
// ❌ Creates a new function on every render, breaking the cache
lens.reflect((l) => l.focus("firstName"))
```

To maintain caching, memoize the function you pass:

```tsx
// ✅ Memoized function preserves the cache
lens.reflect(useCallback((l) => l.focus("firstName"), []))
```

<Admonition type="tip" title="React Compiler Optimization">

[React Compiler](https://react.dev/learn/react-compiler) can automatically optimize these functions for you! Since functions passed to `reflect` have no side effects, React Compiler will automatically hoist them to module scope, ensuring lens caching works perfectly without manual memoization.

</Admonition>

### Advanced Usage

#### Manual Lens Creation

For advanced use cases or when you need more control, you can create lenses manually without the `useLens` hook using the `LensCore` class:

```tsx
import { useMemo } from "react"
import { useForm } from "react-hook-form"
import { LensCore, LensesStorage } from "@hookform/lenses"

function App() {
  const { control } = useForm<{ firstName: string; lastName: string }>()

  const lens = useMemo(() => {
    const cache = new LensesStorage(control)
    return LensCore.create(control, cache)
  }, [control])

  return (
    <div>
      <input
        {...lens
          .focus("firstName")
          .interop((ctrl, name) => ctrl.register(name))}
      />
      <input
        {...lens.focus("lastName").interop((ctrl, name) => ctrl.register(name))}
      />
    </div>
  )
}
```

#### Extending lenses

You can extend the basic lens functionality by adding custom methods to the `LensBase` interface. This is useful when you need additional methods that aren't available in the default lens API.

For example, let's add a `getValue` method to the lens that allows you to easily retrieve the current form values.

**Step 1: Create the type declarations file**

Create a `lenses.d.ts` file to extend the basic interface with the methods you want:

```typescript
declare module "@hookform/lenses" {
  interface LensBase<T> {
    getValue(): T
  }
}

export {}
```

**Step 2: Create the custom lens core implementation**

Create a `MyLensCore.ts` file with the actual runtime implementation:

```typescript
import type { FieldValues } from "react-hook-form"
import { LensCore } from "@hookform/lenses"

export class MyLensCore<T extends FieldValues> extends LensCore<T> {
  public getValue() {
    return this.control._formValues
  }
}
```

**Step 3: Create the custom hook**

Create a `useMyLens.ts` file that accepts control and returns the lens as usual:

```typescript
import { type DependencyList, useMemo } from "react"
import type { FieldValues } from "react-hook-form"

import { LensesStorage, type Lens, type UseLensProps } from "@hookform/lenses"
import { MyLensCore } from "./MyLensCore"

export function useMyLens<TFieldValues extends FieldValues = FieldValues>(
  props: UseLensProps<TFieldValues>,
  deps: DependencyList = []
): Lens<TFieldValues> {
  return useMemo(() => {
    const cache = new LensesStorage(props.control)
    const lens = new MyLensCore<TFieldValues>(
      props.control,
      "",
      cache
    ) as unknown as Lens<TFieldValues>

    return lens
  }, [props.control, ...deps])
}
```

**Step 4: Use your extended lens**

Now you can use this hook as usual and you have the new method with correct TypeScript support:

```typescript
const lens = useMyLens(form)
lens.getValue() // Your custom method is now available with full type support
```

This pattern allows you to add any custom functionality to lenses while maintaining full type safety and compatibility with the existing lens API.

<Admonition type="tip" title="Questions or Feedback?">

Found a bug or have a feature request? Check out the [GitHub repository](https://github.com/react-hook-form/lenses) to report issues or contribute to the project.

</Admonition>


---

## Source: `src/content/docs/usewatch/watch.mdx`

---
title: Watch
description: Watch component for subscribing to input changes
sidebar: apiLinks
---

## \</> `Watch:` <TypeText>Component</TypeText>

A React Hook Form component that provides the same functionality as `useWatch`, but in component form. Instead of using the hook inside another component, you can use `<Watch />` directly in your JSX to subscribe to and render form values.

### Props

---

| Name           | Type                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`         | <TypeText>string \| string[] \| undefined</TypeText> | Name of the field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `control`      | <TypeText>Object</TypeText>                          | [`control`](/docs/useform/control) object provided by `useForm`. It's optional if you are using `FormProvider`.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `compute`      | <TypeText>function</TypeText>                        | <p>Subscribe to selective and computed form values.</p><ul><li>Subscribe to the entire form but only return updated value with certain condition<CodeArea withOutCopy rawData={`const watchedValue = useWatch({\n  compute: (data: FormValue) => { \n    if (data.test?.length) return data.test; \n\n    return ''; \n  }, \n});`}/></li><li>Subscribe to a specific form value state<CodeArea withOutCopy rawData={`const watchedValue = useWatch({\n  name: 'test', \n  compute: (data: string) => { \n    return data.length ? data : ''; \n  }, \n});`}/></li></ul> |
| `defaultValue` | <TypeText>unknown</TypeText>                         | default value for `useWatch` to return before the initial render.<br/><br/>**Note:** the first render will always return `defaultValue` when it's supplied.                                                                                                                                                                                                                                                                                                                                                                                                              |
| `disabled`     | <TypeText>boolean = false</TypeText>                 | Option to disable the subscription.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `exact`        | <TypeText>boolean = false</TypeText>                 | This prop will enable an exact match for input name subscriptions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `render`       | <TypeText>Function</TypeText>                        | Subscribes to specified form field(s) and re-renders its child function whenever the values change. This allows you to declaratively consume form values in JSX without manually wiring up state.                                                                                                                                                                                                                                                                                                                                                                        |

**Examples:**

---

```tsx copy sandbox=""
import { useForm, Watch } from "react-hook-form"

const App = () => {
  const { register, control } = useForm()

  return (
    <div>
      <form>
        <input {...register("foo")} />
        <input {...register("bar")} />
      </form>
      {/* re-render only when value of `foo` changes */}
      <Watch
        control={control}
        names={["foo"]}
        render={([foo]) => <span>{foo}</span>}
      />
    </div>
  )
}
```


---

## Source: `src/content/docs/usewatch.mdx`

---
title: useWatch
description: React Hook for subscribing to input changes
sidebar: apiLinks
---

<SelectNav
  options={[
    {
      label: "Watch",
      value: "/docs/usewatch/watch",
    },
  ]}
/>

## \</> `useWatch:` <TypeText>`({ control?: Control, name?: string, defaultValue?: unknown, disabled?: boolean }) => object`</TypeText>

Behaves similarly to the `watch` API, however, this will isolate re-rendering at the custom hook level and potentially result in better performance for your application.

### Props

---

| Name           | Type                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`         | <TypeText>string \| string[] \| undefined</TypeText> | Name of the field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `control`      | <TypeText>Object</TypeText>                          | [`control`](/docs/useform/control) object provided by `useForm`. It's optional if you are using `FormProvider`.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `compute`      | <TypeText>function</TypeText>                        | <p>Subscribe to selective and computed form values.</p><ul><li>Subscribe to the entire form but only return updated value with certain condition<CodeArea withOutCopy rawData={`const watchedValue = useWatch({\n  compute: (data: FormValue) => { \n    if (data.test?.length) return data.test; \n\n    return ''; \n  }, \n});`}/></li><li>Subscribe to a specific form value state<CodeArea withOutCopy rawData={`const watchedValue = useWatch({\n  name: 'test', \n  compute: (data: string) => { \n    return data.length ? data : ''; \n  }, \n});`}/></li></ul> |
| `defaultValue` | <TypeText>unknown</TypeText>                         | default value for `useWatch` to return before the initial render.<br/><br/>**Note:** the first render will always return `defaultValue` when it's supplied.                                                                                                                                                                                                                                                                                                                                                                                                              |
| `disabled`     | <TypeText>boolean = false</TypeText>                 | Option to disable the subscription.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `exact`        | <TypeText>boolean = false</TypeText>                 | This prop will enable an exact match for input name subscriptions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### Return

---

| Example                              | Return                                         |
| ------------------------------------ | ---------------------------------------------- |
| `useWatch({ name: 'inputName' })`    | <TypeText>unknown</TypeText>                   |
| `useWatch({ name: ['inputName1'] })` | <TypeText>unknown[]</TypeText>                 |
| `useWatch()`                         | <TypeText>`{[key:string]: unknown}`</TypeText> |

<Admonition type="important" title="Rules">

- The initial return value from `useWatch` will always return what's inside of `defaultValue` or `defaultValues` from `useForm`.
- The only difference between `useWatch` and `watch` is at the root ([`useForm`](/docs/useform)) level or the custom hook level update.
- `useWatch`'s execution order matters, which means if you update a form value before the subscription is in place, then the value updated will be ignored.

  ```javascript copy
  setValue("test", "data")
  useWatch({ name: "test" }) // ❌ subscription is happened after value update, no update received
  useWatch({ name: "example" }) // ✅ input value update will be received and trigger re-render
  setValue("example", "data")
  ```

  You can overcome the above issue with a simple custom hook as below:

  ```javascript copy
  const useFormValues = () => {
    const { getValues } = useFormContext()

    return {
      ...useWatch(), // subscribe to form value updates

      ...getValues(), // always merge with latest form values
    }
  }
  ```

- `useWatch`'s result is optimised for render phase instead of `useEffect`'s deps, to detect value updates you may want to use an external custom hook for value comparison.

</Admonition>

**Examples:**

---

**Form**

<TabGroup buttonLabels={["TS", "JS"]} >

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-v7-ts-usewatch-h9i5e"
import { useForm, useWatch } from "react-hook-form"

interface FormInputs {
  firstName: string
  lastName: string
}

function FirstNameWatched({ control }: { control: Control<FormInputs> }) {
  const firstName = useWatch({
    control,
    name: "firstName", // without supply name will watch the entire form, or ['firstName', 'lastName'] to watch both
    defaultValue: "default", // default value before the render
  })

  return <p>Watch: {firstName}</p> // only re-render at the custom hook level, when firstName changes
}

function App() {
  const { register, control, handleSubmit } = useForm<FormInputs>()

  const onSubmit = (data: FormInputs) => {
    console.log(data)
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>First Name:</label>
      <input {...register("firstName")} />
      <input {...register("lastName")} />
      <input type="submit" />

      <FirstNameWatched control={control} />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-v7-usewatch-forked-9872t"
import { useForm, useWatch } from "react-hook-form"

function Child({ control }) {
  const firstName = useWatch({
    control,
    name: "firstName",
  })

  return <p>Watch: {firstName}</p>
}

function App() {
  const { register, control } = useForm({
    defaultValues: {
      firstName: "test",
    },
  })

  return (
    <form>
      <input {...register("firstName")} />
      <Child control={control} />
    </form>
  )
}
```

</TabGroup>

**Advanced Field Array**

```javascript copy sandbox="https://codesandbox.io/s/watchusewatch-calc-4tpnh"
import { useWatch } from "react-hook-form"

function totalCal(results) {
  let totalValue = 0

  for (const key in results) {
    for (const value in results[key]) {
      if (typeof results[key][value] === "string") {
        const output = parseInt(results[key][value], 10)
        totalValue = totalValue + (Number.isNaN(output) ? 0 : output)
      } else {
        totalValue = totalValue + totalCal(results[key][value], totalValue)
      }
    }
  }

  return totalValue
}

export const Calc = ({ control, setValue }) => {
  const results = useWatch({ control, name: "test" })
  const output = totalCal(results)

  // isolated re-render to calc the result with Field Array
  console.log(results)

  setValue("total", output)

  return <p>{output}</p>
}
```


---

## Source: `src/content/faqs.mdx`

---
title: FAQs
description: Frequently asked questions
sidebar: faqLinks
---

## Performance of React Hook Form {#PerformanceofReactHookForm}

Performance is one of the primary reasons why this library was created. React Hook Form relies on an uncontrolled form, which is the reason why the `register` function captures `ref` and the controlled component has its re-rendering scope with `Controller` or `useController`. This approach reduces the amount of re-rendering that occurs due to a user typing in an input or other form values changing at the root of your form or applications. Components mount to the page faster than controlled components because they have less overhead. As a reference, there is a quick comparison test that you can refer to at [this repo link](https://github.com/bluebill1049/react-hook-form-performance-compare).

---

## How to create an accessible input error and message? {#Howtocreateanaccessibleinputerrorandmessage}

React Hook Form is based on Uncontrolled Components, which gives you the ability to easily build an accessible custom form.
_(For more information about Uncontrolled Components, read [Sharing State Between Components](https://react.dev/learn/sharing-state-between-components))_

```javascript copy
import { useForm } from "react-hook-form"

export default function App() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm()
  const onSubmit = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label htmlFor="firstName">First name</label>
      <input
        id="firstName"
        aria-invalid={errors.firstName ? "true" : "false"}
        {...register("firstName", { required: true })}
      />
      {errors.firstName && <span role="alert">This field is required</span>}

      <input type="submit" />
    </form>
  )
}
```

---

## Does it work with Class Components? {#DoesitworkwithClassComponents}

No, not out of the box. If you want to do this, you can build a wrapper around it and use it in your Class Component.

> You can’t use Hooks inside of a class component, but you can definitely mix classes and function components with Hooks in a single tree. Whether a component is a class or a function that uses Hooks is simply an implementation detail of that component. In the longer term, we expect Hooks to be the primary way people write React components.

---

## How to reset the form? {#Howtoresettheform}

There are two methods to clear the form:

- **HTMLFormElement.reset()**

  This method does the same thing as clicking a form's reset button. It only clears `input/select/checkbox` values.

- **React Hook Form API: `reset()`**

  React Hook Form's `reset` method will reset all field values, and will also clear all `errors` within the form.

---

## How to initialize form values? {#Howtoinitializeformvalues}

Being that React Hook Form relies on an uncontrolled form, you can specify a `defaultValue` or `defaultChecked` to an individual field. However, it is more common and recommended to initialize a form by passing `defaultValues` to `useForm`.

```javascript copy
function App() {
  const { register, handleSubmit } = useForm({
    defaultValues: {
      firstName: "bill",
      lastName: "luo",
    },
  })

  return (
    <form onSubmit={handleSubmit((data) => console.log(data))}>
      <input {...register("firstName")} />
      <input {...register("lastName")} />
      <button type="submit">Submit</button>
    </form>
  )
}
```

For async default values, you can use the following methods:

- Async `defaultValues`

  ```javascript copy
  function App() {
    const { register, handleSubmit } = useForm({
      defaultValues: async () => {
        const response = await fetch("/api")
        return await response.json() // return { firstName: '', lastName: '' }
      },
    })
  }
  ```

- Reactive `values`

  ```javascript copy
  function App() {
    const { data } = useQuery() // data returns { firstName: '', lastName: '' }
    const { register, handleSubmit } = useForm({
      values: data,
      resetOptions: {
        keepDirtyValues: true, // keep dirty fields unchanged, but update defaultValues
      },
    })
  }
  ```

---

## How to share ref usage? {#Howtosharerefusage}

React Hook Form needs a `ref` to collect the input value. However, you may want to use `ref` for other purposes (e.g. scroll into the view, or focus).

<TabGroup buttonLabels={["TS", "JS"]}>

```tsx copy
import { useRef, useImperativeHandle } from "react"
import { useForm } from "react-hook-form"

type Inputs = {
  firstName: string
  lastName: string
}

export default function App() {
  const { register, handleSubmit } = useForm<Inputs>()
  const firstNameRef = useRef<HTMLInputElement>(null)
  const onSubmit = (data: Inputs) => console.log(data)
  const { ref, ...rest } = register("firstName")
  const onClick = () => {
    firstNameRef.current!.value = ""
  }

  useImperativeHandle(ref, () => firstNameRef.current)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...rest} ref={firstNameRef} />
      <button type="button" onClick={onClick}>
        clear
      </button>
      <button>Submit</button>
    </form>
  )
}
```

```javascript copy
import { useRef, useImperativeHandle } from "react"
import { useForm } from "react-hook-form"

export default function App() {
  const { register, handleSubmit } = useForm()
  const firstNameRef = useRef(null)
  const onSubmit = (data) => console.log(data)
  const { ref, ...rest } = register("firstName")
  const onClick = () => {
    firstNameRef.current.value = ""
  }

  useImperativeHandle(ref, () => firstNameRef.current)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...rest} ref={firstNameRef} />
      <button type="button" onClick={onClick}>
        clear
      </button>
      <button>Submit</button>
    </form>
  )
}
```

</TabGroup>

---

## What if you don't have access to ref? {#Whatifyoudonthaveaccesstoref}

You can actually `register` an input without a `ref`. In fact, you can manually `setValue`, `setError` and `trigger`.

**Note:** Because `ref` has not been registered, React Hook Form won't be able to register event listeners to the inputs. This means you will have to manually update value and error.

```javascript copy
import React, { useEffect } from "react"
import { useForm } from "react-hook-form"

export default function App() {
  const { register, handleSubmit, setValue, setError } = useForm()
  const onSubmit = (data) => console.log(data)

  useEffect(() => {
    register("firstName", { required: true })
    register("lastName")
  }, [register])

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input
        name="firstName"
        onChange={(e) => setValue("firstName", e.target.value)}
      />
      <input
        name="lastName"
        onChange={(e) => {
          const value = e.target.value
          if (value === "test") {
            setError("lastName", "notMatch")
          } else {
            setValue("lastName", e.target.value)
          }
        }}
      />
      <button>Submit</button>
    </form>
  )
}
```

---

## Why is the first keystroke not working? {#Whyisthefirstkeystrokenotworking}

Make sure you are not using `value`. The correct property is `defaultValue`.

React Hook Form is focusing on uncontrolled inputs, which means you don't need to change the input `value` via `state` via `onChange`. In fact, you don't need `value` at all. You only need to set `defaultValue` for the initial input value.

---

## React Hook Form, Formik or Redux Form? {#ReactHookFormFormikorReduxForm}

First of all, all libs try to solve the same problem: make the form building experience as easy as possible. However, there are some fundamental differences between these three. `react-hook-form` is built with uncontrolled inputs in mind and tries to provide your form with the best performance and least amount of re-renders possible. Additionally, `react-hook-form` is built with React Hooks and used as a hook, which means there is no Component for you to import. Here are some of the detailed differences:

|                    | React Hook Form                                                                                                                                                                                              | Formik                                                                 | Redux Form                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Component**      | [uncontrolled](https://reactjs.org/docs/uncontrolled-components.html) & [controlled](https://reactjs.org/docs/forms.html)                                                                                    | [controlled](https://reactjs.org/docs/forms.html)                      | [controlled](https://reactjs.org/docs/forms.html)                                       |
| **Rendering**      | minimum re-render and optimise computation                                                                                                                                                                   | re-render according to local state changes (As you type in the input.) | re-render according to state management lib (Redux) changes (As you type in the input.) |
| **API**            | Hooks                                                                                                                                                                                                        | Component (RenderProps, Form, Field) + Hooks                           | Component (RenderProps, Form, Field)                                                    |
| **Package size**   | Small <br/> `react-hook-form@7.27.0` <br/> **8.5KB**                                                                                                                                                         | Medium <br />`formik@2.1.4` <br/>**15KB**                              | Large <br/>`redux-form@8.3.6` <br/>**26.4KB**                                           |
| **Validation**     | Built-in, [Yup](https://github.com/jquense/yup), [Zod](https://github.com/vriad/zod), [Joi](https://github.com/hapijs/joi), [Superstruct](https://github.com/ianstormtaylor/superstruct) and build your own. | Build yourself or [Yup](https://github.com/jquense/yup)                | Build yourself or Plugins                                                               |
| **Learning curve** | Low to Medium                                                                                                                                                                                                | Medium                                                                 | Medium                                                                                  |

---

## watch vs getValues vs state {#watchvsgetValuesvsstate}

- **watch:** subscribe to either all inputs or a specified input's changes via an event listener and re-render based on which fields are subscribed to. Check out [this codesandbox](https://codesandbox.io/s/react-hook-form-watch-with-radio-buttons-and-select-examples-ovfus) for actual behaviour.
- **getValues**: get values that are stored inside the custom hook as reference, fast and cheap. This method doesn’t trigger a re-render.
- **local state**: React local state represents more than just an input’s state and also decides what to render. This will trigger on each input’s change.

---

## Why is default value not changing correctly with ternary operator? {#Whyisdefaultvaluenotchangingcorrectlywithternaryoperator}

React Hook Form doesn't control your entire form and inputs, which is why React wouldn't recognize that the actual input has been exchanged or swapped. As a solution, you can resolve this problem by giving a unique `key` prop to your input. You can also read more about the key props from [this article written by Kent C. Dodds](https://kentcdodds.com/blog/understanding-reacts-key-prop).

```javascript sandbox="https://codesandbox.io/s/react-hook-form-faq-toggle-fields-3htr6" copy
import { useForm } from "react-hook-form"

export default function App() {
  const { register } = useForm()

  return (
    <div>
      {watchChecked ? (
        <input {...register("input3")} key="key1" defaultValue="1" />
      ) : (
        <input {...register("input4")} key="key2" defaultValue="2" />
      )}
    </div>
  )
}
```

---

## How to work with modal or tab forms? {#Howtoworkwithmodalortabforms}

It's important to understand that React Hook Form embraces native form behavior by storing input state inside each input (except custom `register` at `useEffect`). A common misconception is that input state remains with mounted or unmounted inputs. Such as when working with a modal or tab forms. Instead, the correct solution is to build a new form for your form inside each modal or tab and capture your submission data in local or global state and then do something with the combined data.

- [Modal form and toggle inputs example](https://codesandbox.io/s/react-hook-form-modal-form-conditional-inputs-c7n0r)
- [Tab form example](https://codesandbox.io/s/tabs-760h9)

Alternatively you can use the deprecated option `shouldUnregister: false` when calling `useForm`.

<TabGroup buttonLabels={["Controller", "Custom Register"]}>

```javascript copy
import { useForm, Controller } from "react-hook-form"

function App() {
  const { control } = useForm()

  return (
    <Controller
      render={({ field }) => <input {...field} />}
      name="firstName"
      control={control}
      defaultValue=""
    />
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-controlled-input-forked-rl2v1"
import React, { useEffect } from "react"
import { useForm } from "react-hook-form"

function App() {
  const { register, watch, setValue, handleSubmit } = useForm({
    defaultValues: {
      firstName: "",
      lastName: "",
    },
  })
  const { firstName, lastName } = watch()

  useEffect(() => {
    register("firstName")
    register("lastName")
  }, [register])

  const handleChange = (e, name) => {
    setValue(name, e.target.value)
  }

  const onSubmit = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input onChange={(e) => handleChange(e, "firstName")} value={firstName} />

      <input onChange={(e) => handleChange(e, "lastName")} value={lastName} />
      <input type="submit" />
    </form>
  )
}
```

</TabGroup>


---

## Source: `src/content/get-started.mdx`

---
title: Get Started
description: Simple form validation with React Hook Form.
sidebar: getStartedLinks
---

## Installation {#Quickstart}

Installing React Hook Form only takes a single command and you're ready to roll.

```bash copy
npm install react-hook-form
```

## Example

The following code excerpt demonstrates a basic usage example:

<TabGroup buttonLabels={["TS", "JS"]}>

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-get-started-ts-5ksmm"
import { useForm, SubmitHandler } from "react-hook-form"

type Inputs = {
  example: string
  exampleRequired: string
}

export default function App() {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<Inputs>()
  const onSubmit: SubmitHandler<Inputs> = (data) => console.log(data)

  console.log(watch("example")) // watch input value by passing the name of it

  return (
    /* "handleSubmit" will validate your inputs before invoking "onSubmit" */
    <form onSubmit={handleSubmit(onSubmit)}>
      {/* register your input into the hook by invoking the "register" function */}
      <input defaultValue="test" {...register("example")} />

      {/* include validation with required or other standard HTML validation rules */}
      <input {...register("exampleRequired", { required: true })} />
      {/* errors will return when field validation fails  */}
      {errors.exampleRequired && <span>This field is required</span>}

      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-get-started-j5wxo"
import { useForm } from "react-hook-form"

export default function App() {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm()

  const onSubmit = (data) => console.log(data)

  console.log(watch("example")) // watch input value by passing the name of it

  return (
    /* "handleSubmit" will validate your inputs before invoking "onSubmit" */
    <form onSubmit={handleSubmit(onSubmit)}>
      {/* register your input into the hook by invoking the "register" function */}
      <input defaultValue="test" {...register("example")} />

      {/* include validation with required or other standard HTML validation rules */}
      <input {...register("exampleRequired", { required: true })} />
      {/* errors will return when field validation fails  */}
      {errors.exampleRequired && <span>This field is required</span>}

      <input type="submit" />
    </form>
  )
}
```

</TabGroup>

## React Web Video Tutorial {#ReactWebVideoTutorial}

This video tutorial illustrates the basic usage and concepts of React Hook Form.

<YouTube youTubeId="RkXv4AXXC_4" />

## Register fields {#Registerfields}

One of the key concepts in React Hook Form is to **`register`** your component into the hook. This will make its value available for both the form validation and submission.

**Note:** Each field is **required** to have a `name` as a key for the registration process.

{/* JSTSCopy [CodeSandbox JS](https://codesandbox.io/s/react-hook-form-get-started-smspp) */}

<TabGroup buttonLabels={["TS", "JS"]} >

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-get-started-ts-5ksmm"
import ReactDOM from "react-dom"
import { useForm, SubmitHandler } from "react-hook-form"

enum GenderEnum {
  female = "female",
  male = "male",
  other = "other",
}

interface IFormInput {
  firstName: string
  gender: GenderEnum
}

export default function App() {
  const { register, handleSubmit } = useForm<IFormInput>()
  const onSubmit: SubmitHandler<IFormInput> = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>First Name</label>
      <input {...register("firstName")} />
      <label>Gender Selection</label>
      <select {...register("gender")}>
        <option value="female">female</option>
        <option value="male">male</option>
        <option value="other">other</option>
      </select>
      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-get-started-j5wxo"
import { useForm } from "react-hook-form"

export default function App() {
  const { register, handleSubmit } = useForm()
  const onSubmit = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("firstName")} />
      <select {...register("gender")}>
        <option value="female">female</option>
        <option value="male">male</option>
        <option value="other">other</option>
      </select>
      <input type="submit" />
    </form>
  )
}
```

</ TabGroup>

## Apply validation {#Applyvalidation}

React Hook Form makes form validation easy by aligning with the existing [HTML standard for form validation](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Form_validation).

List of validation rules supported:

- required
- min
- max
- minLength
- maxLength
- pattern
- validate

You can read more detail on each rule in the [register section](/docs#register).

<TabGroup buttonLabels={["TS", "JS"]} >

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-apply-validation-ts-forked-nmbyh"
import { useForm, SubmitHandler } from "react-hook-form"

interface IFormInput {
  firstName: string
  lastName: string
  age: number
}

export default function App() {
  const { register, handleSubmit } = useForm<IFormInput>()
  const onSubmit: SubmitHandler<IFormInput> = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("firstName", { required: true, maxLength: 20 })} />
      <input {...register("lastName", { pattern: /^[A-Za-z]+$/i })} />
      <input type="number" {...register("age", { min: 18, max: 99 })} />
      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-apply-validation-q5m00"
import { useForm } from "react-hook-form"

export default function App() {
  const { register, handleSubmit } = useForm()
  const onSubmit = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("firstName", { required: true, maxLength: 20 })} />
      <input {...register("lastName", { pattern: /^[A-Za-z]+$/i })} />
      <input type="number" {...register("age", { min: 18, max: 99 })} />
      <input type="submit" />
    </form>
  )
}
```

</TabGroup>

## Integrating an existing form {#Integratinganexistingform}

Integrating an existing form should be simple. The important step is to `register` the component's `ref` and assign relevant props to your input.

<TabGroup buttonLabels={["TS", "JS"]} >

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-adapting-existing-form-ts-uzfxm"
import { Path, useForm, UseFormRegister, SubmitHandler } from "react-hook-form"

interface IFormValues {
  "First Name": string
  Age: number
}

type InputProps = {
  label: Path<IFormValues>
  register: UseFormRegister<IFormValues>
  required: boolean
}

// The following component is an example of your existing Input Component
const Input = ({ label, register, required }: InputProps) => (
  <>
    <label>{label}</label>
    <input {...register(label, { required })} />
  </>
)

// you can use React.forwardRef to pass the ref too
const Select = React.forwardRef<
  HTMLSelectElement,
  { label: string } & ReturnType<UseFormRegister<IFormValues>>
>(({ onChange, onBlur, name, label }, ref) => (
  <>
    <label>{label}</label>
    <select name={name} ref={ref} onChange={onChange} onBlur={onBlur}>
      <option value="20">20</option>
      <option value="30">30</option>
    </select>
  </>
))

const App = () => {
  const { register, handleSubmit } = useForm<IFormValues>()

  const onSubmit: SubmitHandler<IFormValues> = (data) => {
    alert(JSON.stringify(data))
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <Input label="First Name" register={register} required />
      <Select label="Age" {...register("Age")} />
      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-adapting-existing-form-llbnn"
import { useForm } from "react-hook-form"

// The following component is an example of your existing Input Component
const Input = ({ label, register, required }) => (
  <>
    <label>{label}</label>
    <input {...register(label, { required })} />
  </>
)

// you can use React.forwardRef to pass the ref too
const Select = React.forwardRef(({ onChange, onBlur, name, label }, ref) => (
  <>
    <label>{label}</label>
    <select name={name} ref={ref} onChange={onChange} onBlur={onBlur}>
      <option value="20">20</option>
      <option value="30">30</option>
    </select>
  </>
))

const App = () => {
  const { register, handleSubmit } = useForm()

  const onSubmit = (data) => {
    alert(JSON.stringify(data))
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <Input label="First Name" register={register} required />
      <Select label="Age" {...register("Age")} />
      <input type="submit" />
    </form>
  )
}
```

</TabGroup>

## Integrating with UI libraries {#IntegratingwithUIlibraries}

React Hook Form has made it easy to integrate with external UI component libraries. If the component doesn't expose input's `ref`, then you should use the [Controller](/docs#Controller) component, which will take care of the registration process.

<TabGroup buttonLabels={["TS", "JS"]} >

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-with-ui-library-ts-forked-qjgkx"
import Select from "react-select"
import { useForm, Controller, SubmitHandler } from "react-hook-form"
import { Input } from "@material-ui/core"

interface IFormInput {
  firstName: string
  lastName: string
  iceCreamType: { label: string; value: string }
}

const App = () => {
  const { control, handleSubmit } = useForm({
    defaultValues: {
      firstName: "",
      lastName: "",
      iceCreamType: {},
    },
  })

  const onSubmit: SubmitHandler<IFormInput> = (data) => {
    console.log(data)
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <Controller
        name="firstName"
        control={control}
        render={({ field }) => <Input {...field} />}
      />
      <Controller
        name="iceCreamType"
        control={control}
        render={({ field }) => (
          <Select
            {...field}
            options={[
              { value: "chocolate", label: "Chocolate" },
              { value: "strawberry", label: "Strawberry" },
              { value: "vanilla", label: "Vanilla" },
            ]}
          />
        )}
      />
      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-with-ui-library-forked-fp5r3"
import Select from "react-select"
import { useForm, Controller } from "react-hook-form"
import { Input } from "@material-ui/core"

const App = () => {
  const { control, handleSubmit } = useForm({
    defaultValues: {
      firstName: "",
      select: {},
    },
  })
  const onSubmit = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <Controller
        name="firstName"
        control={control}
        render={({ field }) => <Input {...field} />}
      />
      <Controller
        name="select"
        control={control}
        render={({ field }) => (
          <Select
            {...field}
            options={[
              { value: "chocolate", label: "Chocolate" },
              { value: "strawberry", label: "Strawberry" },
              { value: "vanilla", label: "Vanilla" },
            ]}
          />
        )}
      />
      <input type="submit" />
    </form>
  )
}
```

</TabGroup>

## Integrating Controlled Inputs {#IntegratingControlledInputs}

This library embraces uncontrolled components and native HTML inputs. However, it's hard to avoid working with external controlled components such as [shadcn/ui](https://ui.shadcn.com/docs/components/form), [React-Select](https://github.com/JedWatson/react-select), [AntD](https://github.com/ant-design/ant-design) and [MUI](https://mui.com/). To make this simple, we provide a wrapper component, [Controller](/docs#Controller), to streamline the integration process while still giving you the freedom to use a custom register.

#### Using Component API

<TabGroup buttonLabels={["TS", "JS", 'shadcn/ui']} >

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-v6-controller-ts-jwyzw"
import { useForm, Controller, SubmitHandler } from "react-hook-form"
import { TextField, Checkbox } from "@material-ui/core"

interface IFormInputs {
  TextField: string
  MyCheckbox: boolean
}

function App() {
  const { handleSubmit, control, reset } = useForm<IFormInputs>({
    defaultValues: {
      MyCheckbox: false,
    },
  })
  const onSubmit: SubmitHandler<IFormInputs> = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <Controller
        name="MyCheckbox"
        control={control}
        rules={{ required: true }}
        render={({ field }) => <Checkbox {...field} />}
      />
      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-v7-controller-5h1q5"
import { TextField } from "@material-ui/core"
import { useController, useForm } from "react-hook-form"

function Input({ control, name }) {
  const {
    field,
    fieldState: { invalid, isTouched, isDirty },
    formState: { touchedFields, dirtyFields },
  } = useController({
    name,
    control,
    rules: { required: true },
  })

  return (
    <TextField
      onChange={field.onChange} // send value to hook form
      onBlur={field.onBlur} // notify when input is touched/blur
      value={field.value} // input value
      name={field.name} // send down the input name
      inputRef={field.ref} // send input ref, so we can focus on input when error appear
    />
  )
}
```

```javascript copy
import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"
import { Form, FormControl, FormField } from "@/components/ui/form"
import { Input } from "@/components/ui/input"

const FormSchema = z.object({
  username: z.string().min(2, {
    message: "Username must be at least 2 characters.",
  }),
})

export function InputForm() {
  const form = useForm({
    resolver: zodResolver(FormSchema),
    defaultValues: {
      username: "",
    },
  })

  function onSubmit(data: z.output<typeof FormSchema>) {
    console.log(data);
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)}>
        <FormField
          control={form.control}
          name="username"
          render={({ field }) => (
            <FormControl><Input {...field} /></FormControl>
          )}
        />
        <button type="submit">Submit</button>
      </form>
    </Form>
  )
}
```

</TabGroup>

#### Using Hooks API

<TabGroup buttonLabels={["TS", "JS"]} >

```tsx copy sandbox="https://codesandbox.io/s/usecontroller-forked-4t8cx"
import * as React from "react"
import { useForm, useController, UseControllerProps } from "react-hook-form"

type FormValues = {
  FirstName: string
}

function Input(props: UseControllerProps<FormValues>) {
  const { field, fieldState } = useController(props)

  return (
    <div>
      <input {...field} placeholder={props.name} />
      <p>{fieldState.isTouched && "Touched"}</p>
      <p>{fieldState.isDirty && "Dirty"}</p>
      <p>{fieldState.invalid ? "invalid" : "valid"}</p>
    </div>
  )
}

export default function App() {
  const { handleSubmit, control } = useForm<FormValues>({
    defaultValues: {
      FirstName: "",
    },
    mode: "onChange",
  })
  const onSubmit = (data: FormValues) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <Input control={control} name="FirstName" rules={{ required: true }} />
      <input type="submit" />
    </form>
  )
}
```

```javascript copy sandbox="https://codesandbox.io/s/usecontroller-tefsc"
import { TextField } from "@material-ui/core"
import { useController, useForm } from "react-hook-form"

function Input({ control, name }) {
  const {
    field,
    fieldState: { invalid, isTouched, isDirty },
    formState: { touchedFields, dirtyFields },
  } = useController({
    name,
    control,
    rules: { required: true },
  })

  return (
    <TextField
      onChange={field.onChange} // send value to hook form
      onBlur={field.onBlur} // notify when input is touched/blur
      value={field.value} // input value
      name={field.name} // send down the input name
      inputRef={field.ref} // send input ref, so we can focus on input when error appear
    />
  )
}
```

</TabGroup>

## Integrating with global state {#Integratingwithglobalstate}

This library doesn't require you to rely on a state management library, but you can easily integrate with them.

```javascript copy
import { useForm } from "react-hook-form"
import { connect } from "react-redux"
import updateAction from "./actions"

export default function App(props) {
  const { register, handleSubmit, setValue } = useForm({
    defaultValues: {
      firstName: "",
      lastName: "",
    },
  })
  // Submit your data into Redux store
  const onSubmit = (data) => props.updateAction(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("firstName")} />
      <input {...register("lastName")} />
      <input type="submit" />
    </form>
  )
}

// Connect your component with redux
connect(
  ({ firstName, lastName }) => ({ firstName, lastName }),
  updateAction
)(YourForm)
```

## Handle errors {#Handleerrors}

React Hook Form provides an `errors` object to show you the errors in the form. `errors`' type will return given validation constraints. The following example showcases a required validation rule.

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-v7-errormessage-multiple-error-messages-3ur2z"
import { useForm } from "react-hook-form"

export default function App() {
  const {
    register,
    formState: { errors },
    handleSubmit,
  } = useForm()
  const onSubmit = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input
        {...register("firstName", { required: true })}
        aria-invalid={errors.firstName ? "true" : "false"}
      />
      {errors.firstName?.type === "required" && (
        <p role="alert">First name is required</p>
      )}

      <input
        {...register("mail", { required: "Email Address is required" })}
        aria-invalid={errors.mail ? "true" : "false"}
      />
      {errors.mail && <p role="alert">{errors.mail.message}</p>}

      <input type="submit" />
    </form>
  )
}
```

## Integrating with services {#Integratingwithservices}

To integrate React Hook Form with a service, you can use the library's built-in submission handling. `<Form />` component allow you to easily send form data to an API endpoint or other service. [Find out more about Form component](/docs/useform/form).

```javascript
import { Form } from "react-hook-form"

function App() {
  const { register, control } = useForm()

  return (
    <Form
      action="/api/save" // Send post request with the FormData
      // encType={'application/json'} you can also switch to json object
      onSuccess={() => {
        alert("Your application is updated.")
      }}
      onError={() => {
        alert("Submission has failed.")
      }}
      control={control}
    >
      <input {...register("firstName", { required: true })} />
      <input {...register("lastName", { required: true })} />
      <button>Submit</button>
    </Form>
  )
}
```

## Schema Validation {#SchemaValidation}

We also support schema-based form validation with [Yup](https://github.com/jquense/yup), [Zod](https://github.com/vriad/zod) , [Superstruct](https://github.com/ianstormtaylor/superstruct) & [Joi](https://github.com/hapijs/joi), where you can pass your `schema` to [useForm](/docs#useForm) as an optional config. It will validate your input data against the schema and return with either [errors](/docs#errors) or a valid result.

**Step 1:** Install `Yup` into your project.

```bash copy
npm install @hookform/resolvers yup
```

**Step 2:** Prepare your schema for validation and register inputs with React Hook Form.

```javascript copy sandbox="https://codesandbox.io/s/react-hook-form-v7-validationschema-rm35t"
import { useForm } from "react-hook-form"
import { yupResolver } from "@hookform/resolvers/yup"
import * as yup from "yup"

const schema = yup
  .object({
    firstName: yup.string().required(),
    age: yup.number().positive().integer().required(),
  })
  .required()

export default function App() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: yupResolver(schema),
  })
  const onSubmit = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("firstName")} />
      <p>{errors.firstName?.message}</p>

      <input {...register("age")} />
      <p>{errors.age?.message}</p>

      <input type="submit" />
    </form>
  )
}
```

## React Native {#ReactNative}

You will get the same performance boost and enhancement in React Native. To integrate with input component, you can wrap it with `Controller`.

```javascript copy sandbox="https://snack.expo.io/@bluebill1049/react-hook-form-v7---controller" expo
import { Text, View, TextInput, Button, Alert } from "react-native"
import { useForm, Controller } from "react-hook-form"

export default function App() {
  const {
    control,
    handleSubmit,
    formState: { errors },
  } = useForm({
    defaultValues: {
      firstName: "",
      lastName: "",
    },
  })
  const onSubmit = (data) => console.log(data)

  return (
    <View>
      <Controller
        control={control}
        rules={{
          required: true,
        }}
        render={({ field: { onChange, onBlur, value } }) => (
          <TextInput
            placeholder="First name"
            onBlur={onBlur}
            onChangeText={onChange}
            value={value}
          />
        )}
        name="firstName"
      />
      {errors.firstName && <Text>This is required.</Text>}

      <Controller
        control={control}
        rules={{
          maxLength: 100,
        }}
        render={({ field: { onChange, onBlur, value } }) => (
          <TextInput
            placeholder="Last name"
            onBlur={onBlur}
            onChangeText={onChange}
            value={value}
          />
        )}
        name="lastName"
      />

      <Button title="Submit" onPress={handleSubmit(onSubmit)} />
    </View>
  )
}
```

## TypeScript {#TypeScript}

React Hook Form is built with `TypeScript`, and you can define a `FormData` type to support form values.

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-typescript-qwk7b"
import * as React from "react"
import { useForm } from "react-hook-form"

type FormData = {
  firstName: string
  lastName: string
}

export default function App() {
  const {
    register,
    setValue,
    handleSubmit,
    formState: { errors },
  } = useForm<FormData>()
  const onSubmit = handleSubmit((data) => console.log(data))
  // firstName and lastName will have correct type

  return (
    <form onSubmit={onSubmit}>
      <label>First Name</label>
      <input {...register("firstName")} />
      <label>Last Name</label>
      <input {...register("lastName")} />
      <button
        type="button"
        onClick={() => {
          setValue("lastName", "luo") // ✅
          setValue("firstName", true) // ❌: true is not string
          errors.bill // ❌: property bill does not exist
        }}
      >
        SetValue
      </button>
    </form>
  )
}
```

## Design and philosophy {#Designandphilosophy}

React Hook Form's design and philosophy focus on user and developer experience. The library aims to provide users with a smoother interaction experience by fine-tuning the performance and improving accessibility. Some of the performance enhancements include:

- Introducing form state subscription model through the proxy
- Avoiding unnecessary computation
- Isolating component re-rendering when required

Overall, it improves the user experience while users interact with the application. As for the developers, we introduce built-in validation and are closely aligned with HTML standards allowing further extension with powerful validation methods and integration with schema validation natively. In addition, having a strongly type-checked form with the help of typescript provides early build-time feedback to help and guide the developer to build a robust form solution.

The following talk given by [Bill](https://twitter.com/bluebill1049) showcased some of the ideas and design patterns:

<YouTube youTubeId="ZFxHdpzaEmM" />


---

## Source: `src/content/ts.mdx`

---
title: Typescript Support
description: List of exported Typescript Types.
sidebar: tsLinks
---

**Important:** Typescript ^4.3 above is the recommended version to work with react hook form.

## \</> Resolver {#Resolver}

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-resolver-forked-mjsx7"
import { useForm, Resolver } from "react-hook-form"

type FormValues = {
  firstName: string
  lastName: string
}

const resolver: Resolver<FormValues> = async (values) => {
  return {
    values: values.firstName ? values : {},
    errors: !values.firstName
      ? {
          firstName: {
            type: "required",
            message: "This is required.",
          },
        }
      : {},
  }
}

export default function App() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormValues>({ resolver })
  const onSubmit = handleSubmit((data) => console.log(data))

  return (
    <form onSubmit={onSubmit}>
      <input {...register("firstName")} placeholder="Bill" />
      {errors?.firstName && <p>{errors.firstName.message}</p>}

      <input {...register("lastName")} placeholder="Luo" />

      <input type="submit" />
    </form>
  )
}
```

---

## \</> SubmitHandler {#SubmitHandler}

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-handlesubmit-ts-v7-z9z0g"
import { useForm, SubmitHandler } from "react-hook-form"

type FormValues = {
  firstName: string
  lastName: string
  email: string
}

export default function App() {
  const { register, handleSubmit } = useForm<FormValues>()
  const onSubmit: SubmitHandler<FormValues> = (data) => console.log(data)

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("firstName")} />
      <input {...register("lastName")} />
      <input type="email" {...register("email")} />

      <input type="submit" />
    </form>
  )
}
```

---

## \</> SubmitErrorHandler {#SubmitErrorHandler}

```tsx copy
import { useForm, SubmitHandler, SubmitErrorHandler } from "react-hook-form"

type FormValues = {
  firstName: string
  lastName: string
  email: string
}

export default function App() {
  const { register, handleSubmit } = useForm<FormValues>()
  const onSubmit: SubmitHandler<FormValues> = (data) => console.log(data)
  const onError: SubmitErrorHandler<FormValues> = (errors) =>
    console.log(errors)

  return (
    <form onSubmit={handleSubmit(onSubmit, onError)}>
      <input {...register("firstName", { required: true })} />
      <input {...register("lastName", { minLength: 2 })} />
      <input type="email" {...register("email")} />

      <input type="submit" />
    </form>
  )
}
```

---

## \</> Control {#Control}

```tsx copy sandbox="https://codesandbox.io/s/control-2mg07"
import { useForm, useWatch, Control } from "react-hook-form"

type FormValues = {
  firstName: string
  lastName: string
}

function IsolateReRender({ control }: { control: Control<FormValues> }) {
  const firstName = useWatch({
    control,
    name: "firstName",
    defaultValue: "default",
  })

  return <div>{firstName}</div>
}

export default function App() {
  const { register, control, handleSubmit } = useForm<FormValues>()
  const onSubmit = handleSubmit((data) => console.log(data))

  return (
    <form onSubmit={onSubmit}>
      <input {...register("firstName")} />
      <input {...register("lastName")} />
      <IsolateReRender control={control} />

      <input type="submit" />
    </form>
  )
}
```

---

## \</> UseFormReturn {#UseFormReturn}

<TabGroup buttonLabels={["Type", "Code Example"]}>

```tsx copy
export type UseFormReturn<
  TFieldValues extends FieldValues = FieldValues,
  TContext = any,
  TTransformedValues extends FieldValues | undefined = undefined,
> = {
  watch: UseFormWatch<TFieldValues>
  getValues: UseFormGetValues<TFieldValues>
  getFieldState: UseFormGetFieldState<TFieldValues>
  setError: UseFormSetError<TFieldValues>
  clearErrors: UseFormClearErrors<TFieldValues>
  setValue: UseFormSetValue<TFieldValues>
  trigger: UseFormTrigger<TFieldValues>
  formState: FormState<TFieldValues>
  resetField: UseFormResetField<TFieldValues>
  reset: UseFormReset<TFieldValues>
  handleSubmit: UseFormHandleSubmit<TFieldValues>
  unregister: UseFormUnregister<TFieldValues>
  control: Control<TFieldValues, TContext>
  register: UseFormRegister<TFieldValues>
  setFocus: UseFormSetFocus<TFieldValues>
}
```

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-UseFormReturn-forked-yl40u"
import type { FieldValues, UseFormReturn, SubmitHandler } from "react-hook-form"
import { useForm } from "react-hook-form"

type InputProps = React.DetailedHTMLProps<
  React.InputHTMLAttributes<HTMLInputElement>,
  HTMLInputElement
>

const Input = React.forwardRef<HTMLInputElement, InputProps>((props, ref) => (
  <input ref={ref} {...props} />
))

type Option = {
  label: React.ReactNode
  value: string | number | string[]
}

type SelectProps = React.DetailedHTMLProps<
  React.SelectHTMLAttributes<HTMLSelectElement>,
  HTMLSelectElement
> & { options: Option[] }

const Select = React.forwardRef<HTMLSelectElement, SelectProps>(
  ({ options, ...props }, ref) => (
    <select ref={ref} {...props}>
      {options.map(({ label, value }) => (
        <option value={value}>{label}</option>
      ))}
    </select>
  )
)

type FormProps<TFormValues extends FieldValues> = {
  onSubmit: SubmitHandler<TFormValues>
  children: (methods: UseFormReturn<TFormValues>) => React.ReactNode
}

const Form = <TFormValues extends FieldValues>({
  onSubmit,
  children,
}: FormProps<TFormValues>) => {
  const methods = useForm<TFormValues>()
  return (
    <form onSubmit={methods.handleSubmit(onSubmit)}>{children(methods)}</form>
  )
}

type FormValues = {
  firstName: string
  lastName: string
  sex: string
}

export default function App() {
  const onSubmit = (data: FormValues) => console.log(data)

  return (
    <Form<FormValues> onSubmit={onSubmit}>
      {({ register }) => (
        <>
          <Input {...register("firstName")} />
          <Input {...register("lastName")} />
          <Select
            {...register("sex")}
            options={[
              { label: "Female", value: "female" },
              { label: "Male", value: "male" },
              { label: "Other", value: "other" },
            ]}
          />
          <Input type="submit" />
        </>
      )}
    </Form>
  )
}
```

</TabGroup>

---

## \</> UseFormProps {#UseFormProps}

```tsx copy
export type UseFormProps<
  TFieldValues extends FieldValues = FieldValues,
  TContext extends object = object,
  TTransformedValues extends FieldValues | undefined = undefined,
> = Partial<{
  mode: Mode
  disabled: boolean
  reValidateMode: Exclude<Mode, "onTouched" | "all">
  defaultValues: DefaultValues<TFieldValues> | AsyncDefaultValues<TFieldValues>
  values: TFieldValues
  errors: FieldErrors<TFieldValues>
  resetOptions: Parameters<UseFormReset<TFieldValues>>[1]
  resolver: Resolver<TFieldValues, TContext>
  context: TContext
  shouldFocusError: boolean
  shouldUnregister: boolean
  shouldUseNativeValidation: boolean
  progressive: boolean
  criteriaMode: CriteriaMode
  delayError: number
}>
```

---

## \</> UseFieldArrayReturn {#UseFieldArrayReturn}

```tsx copy
export type UseFieldArrayReturn<
  TFieldValues extends FieldValues = FieldValues,
  TFieldArrayName extends
    FieldArrayPath<TFieldValues> = FieldArrayPath<TFieldValues>,
  TKeyName extends string = "id",
> = {
  swap: UseFieldArraySwap
  move: UseFieldArrayMove
  prepend: UseFieldArrayPrepend<TFieldValues, TFieldArrayName>
  append: UseFieldArrayAppend<TFieldValues, TFieldArrayName>
  remove: UseFieldArrayRemove
  insert: UseFieldArrayInsert<TFieldValues, TFieldArrayName>
  update: UseFieldArrayUpdate<TFieldValues, TFieldArrayName>
  replace: UseFieldArrayReplace<TFieldValues, TFieldArrayName>
  fields: FieldArrayWithId<TFieldValues, TFieldArrayName, TKeyName>[]
}
```

---

## \</> UseFieldArrayProps {#UseFieldArrayProps}

```tsx copy
export type UseFieldArrayProps<
  TFieldValues extends FieldValues = FieldValues,
  TFieldArrayName extends FieldArrayPath<TFieldValues> = FieldArrayPath<TFieldValues>,
  TKeyName extends string = 'id',
> = {
  name: TFieldArrayName
  keyName?: TKeyName
  control?: Control<TFieldValues>
  rules?: {
    validate?
      | Validate<FieldArray<TFieldValues, TFieldArrayName>[], TFieldValues>
      | Record<
          string,
          Validate<FieldArray<TFieldValues, TFieldArrayName>[], TFieldValues>
        >
  } & Pick<
    RegisterOptions<TFieldValues>,
    'maxLength' | 'minLength' | 'required'
  >
  shouldUnregister?: boolean
}
```

---

## \</> UseControllerReturn {#UseControllerReturn}

```tsx copy
export type UseControllerReturn<
  TFieldValues extends FieldValues = FieldValues,
  TName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>,
> = {
  field: ControllerRenderProps<TFieldValues, TName>
  formState: UseFormStateReturn<TFieldValues>
  fieldState: ControllerFieldState
}
```

---

## \</> UseControllerProps {#UseControllerProps}

```tsx copy
export type UseControllerProps<
  TFieldValues extends FieldValues = FieldValues,
  TName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>,
> = {
  name: TName
  rules?: Omit<
    RegisterOptions<TFieldValues, TName>,
    "valueAsNumber" | "valueAsDate" | "setValueAs" | "disabled"
  >
  shouldUnregister?: boolean
  defaultValue?: FieldPathValue<TFieldValues, TName>
  control?: Control<TFieldValues>
  disabled?: boolean
}
```

---

## \</> FieldError {#FieldError}

```tsx copy
export type FieldError = {
  type: LiteralUnion<keyof RegisterOptions, string>
  root?: FieldError
  ref?: Ref
  types?: MultipleFieldErrors
  message?: Message
}
```

---

## \</> FieldErrors {#FieldErrors}

```tsx copy
export type FieldErrors<T extends FieldValues = FieldValues> = Partial<
  FieldValues extends IsAny<FieldValues>
    ? any
    : FieldErrorsImpl<DeepRequired<T>>
> & {
  root?: Record<string, GlobalError> & GlobalError
}
```

---

## \</> Field {#Field}

```tsx copy
export type Field = {
  _f: {
    ref: Ref
    name: InternalFieldName
    refs?: HTMLInputElement[]
    mount?: boolean
  } & RegisterOptions
}
```

---

## \</> FieldPath {#FieldPath}

This type is useful when you define custom component's `name` prop, and it will type check against your field path.

```tsx copy
export type FieldPath<TFieldValues extends FieldValues> = Path<TFieldValues>
```

---

## \</> FieldPathByValue {#FieldPathByValue}

This type will return union with all available paths that match the passed value

```tsx copy
export type FieldPathByValue<TFieldValues extends FieldValues, TValue> = {
  [Key in FieldPath<TFieldValues>]: FieldPathValue<
    TFieldValues,
    Key
  > extends TValue
    ? Key
    : never
}[FieldPath<TFieldValues>]
```

---

## \</> FieldValues {#FieldValues}

```tsx copy
export type FieldValues = Record<string, any>
```

---

## \</> FieldArrayWithId {#FieldArrayWithId}

```tsx copy
export type FieldArrayWithId<
  TFieldValues extends FieldValues = FieldValues,
  TFieldArrayName extends
    FieldArrayPath<TFieldValues> = FieldArrayPath<TFieldValues>,
  TKeyName extends string = "id",
> = FieldArray<TFieldValues, TFieldArrayName> & Record<TKeyName, string>
```

---

## \</> Mode {#Mode}

```tsx copy
export type ValidationMode = typeof VALIDATION_MODE

export type Mode = keyof ValidationMode
```

---

## \</> RegisterOptions {#RegisterOptions}

```tsx copy
export type RegisterOptions<
  TFieldValues extends FieldValues = FieldValues,
  TFieldName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>,
> = Partial<{
  required: Message | ValidationRule<boolean>
  min: ValidationRule<number | string>
  max: ValidationRule<number | string>
  maxLength: ValidationRule<number>
  minLength: ValidationRule<number>
  validate:
    | Validate<FieldPathValue<TFieldValues, TFieldName>, TFieldValues>
    | Record<
        string,
        Validate<FieldPathValue<TFieldValues, TFieldName>, TFieldValues>
      >
  value: FieldPathValue<TFieldValues, TFieldName>
  setValueAs: (value: any) => any
  shouldUnregister?: boolean
  onChange?: (event: any) => void
  onBlur?: (event: any) => void
  disabled: boolean
  deps: FieldPath<TFieldValues> | FieldPath<TFieldValues>[]
}> &
  (
    | {
        pattern?: ValidationRule<RegExp>
        valueAsNumber?: false
        valueAsDate?: false
      }
    | {
        pattern?: undefined
        valueAsNumber?: false
        valueAsDate?: true
      }
    | {
        pattern?: undefined
        valueAsNumber?: true
        valueAsDate?: false
      }
  )
```

---

## \</> FormStateProxy {#FormStateProxy}

```tsx copy
export type FormStateProxy<TFieldValues extends FieldValues = FieldValues> = {
  isDirty: boolean
  isValidating: boolean
  dirtyFields: FieldNamesMarkedBoolean<TFieldValues>
  touchedFields: FieldNamesMarkedBoolean<TFieldValues>
  validatingFields: FieldNamesMarkedBoolean<TFieldValues>
  errors: boolean
  isValid: boolean
}
```

---

## \</> NestedValue (**Deprecated** at 7.33.0) {#NestedValue}

<TabGroup buttonLabels={["Code Example", "Type"]}>

```tsx copy sandbox="https://codesandbox.io/s/react-hook-form-nestedvalue-lskdv"
import { useForm, NestedValue } from "react-hook-form"
import { TextField, Select } from "@material-ui/core"
import { Autocomplete } from "@material-ui/lab"

type Option = {
  label: string
  value: string
}

const options = [
  { label: "Chocolate", value: "chocolate" },
  { label: "Strawberry", value: "strawberry" },
  { label: "Vanilla", value: "vanilla" },
]

export default function App() {
  const {
    register,
    handleSubmit,
    watch,
    setValue,
    formState: { errors },
  } = useForm<{
    autocomplete: NestedValue<Option[]>
    select: NestedValue<number[]>
  }>({
    defaultValues: { autocomplete: [], select: [] },
  })
  const onSubmit = handleSubmit((data) => console.log(data))

  React.useEffect(() => {
    register("autocomplete", {
      validate: (value) => value.length || "This is required.",
    })
    register("select", {
      validate: (value) => value.length || "This is required.",
    })
  }, [register])

  return (
    <form onSubmit={onSubmit}>
      <Autocomplete
        options={options}
        getOptionLabel={(option: Option) => option.label}
        onChange={(e, options) => setValue("autocomplete", options)}
        renderInput={(params) => (
          <TextField
            {...params}
            error={Boolean(errors?.autocomplete)}
            helperText={errors?.autocomplete?.message}
          />
        )}
      />

      <Select
        value=""
        onChange={(e) => setValue("select", e.target.value as number[])}
      >
        <MenuItem value={10}>Ten</MenuItem>
        <MenuItem value={20}>Twenty</MenuItem>
      </Select>

      <input type="submit" />
    </form>
  )
}
```

```tsx copy
import { useForm, NestedValue } from "react-hook-form"

type FormValues = {
  key1: string
  key2: number
  key3: NestedValue<{
    key1: string
    key2: number
  }>
  key4: NestedValue<string[]>
}

const {
  formState: { errors },
} = useForm<FormValues>()

errors?.key1?.message // no type error
errors?.key2?.message // no type error
errors?.key3?.message // no type error
errors?.key4?.message // no type error
```

</TabGroup>
