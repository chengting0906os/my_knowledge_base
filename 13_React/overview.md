# React Overview

## What is React?

- React is a **JavaScript UI library** developed by Meta, focused on the **view layer** only (not a full framework like Angular)
- It is an **external library**, not built into browsers or JavaScript natively
- Can be used for web apps (ReactDOM) and mobile apps (React Native)

## Core Ideas

- **Component-based**: UI is broken into reusable, composable components that look like custom HTML tags in JSX
- **Declarative**: You describe *what* the UI should look like given the current state; React handles DOM updates automatically
- **Unidirectional data flow**: Data flows down from parent to child via props; state changes trigger re-renders

## Why React?

- Avoids direct DOM manipulation — React syncs the DOM efficiently via the **Virtual DOM**
- Components are reusable and easier to test and maintain
- Large ecosystem and community support
