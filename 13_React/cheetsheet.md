# React Cheatsheet

---

## English Version

- **Component** — The smallest UI unit; a reusable, composable piece that works like a custom HTML tag
- **JSX (JavaScript XML)** — Syntax that lets you write HTML-like code inside JS; compiled by Babel into `React.createElement()`
- **Props (Properties)** — Data passed from parent to child component; read-only, cannot be modified by the child
- **State** — Data managed inside a component; changing state triggers a re-render
- **Virtual DOM** — An in-memory copy of the DOM; React diffs old vs new to minimize real DOM updates
- **Rendering / Re-render** — React re-executes the component function when state or props change to produce a new UI
- **Reconciliation** — The process React uses to diff old and new Virtual DOM and decide the minimum updates needed
- **Hook** — Introduced in React 16.8; lets function components use state and lifecycle features
- **useState** — Hook to declare state in a function component; returns `[value, setter]`
- **useEffect** — Hook to handle side effects (API calls, subscriptions, DOM operations); runs after render
- **useRef** — Hook to get a reference to a DOM element, or store a value that doesn't trigger re-render
- **useContext** — Hook to read a Context value without prop drilling
- **useMemo** — Hook to cache a computed value; recalculates only when dependencies change
- **useCallback** — Hook to cache a function reference; prevents child re-renders caused by new function references
- **Context** — A mechanism to share data across component tree without passing props at every level
- **Provider** — The Context component that wraps the tree and supplies the shared data
- **Prop Drilling** — The problem of passing props through many layers; solved by Context or state management
- **Side Effect** — Any operation outside of rendering: API requests, timers, event subscriptions
- **Controlled Component** — Form element whose value is controlled by React state (`value` + `onChange`)
- **Uncontrolled Component** — Form element whose value is managed by the DOM itself; accessed via `ref`
- **Key** — A unique identifier given to list items so React can track which items changed
- **React.memo** — HOC that skips re-rendering a component when its props haven't changed
- **Lifecycle** — The stages a component goes through: mount → update → unmount
- **Fragment** — `<>...</>` or `<React.Fragment>`; groups elements without adding extra DOM nodes
- **Lazy / Suspense** — Dynamically load a component to reduce bundle size; `<Suspense>` shows a fallback while loading
- **Error Boundary** — Catches render errors in child components to prevent the whole app from crashing (class component only)

---

## 中文版

- **Component 元件** — UI 的最小單位，可重複使用，像自訂的 HTML 標籤
- **JSX** — 在 JS 裡寫類似 HTML 的語法，需經 Babel 編譯成 `React.createElement()`
- **Props 屬性** — 父元件傳給子元件的參數，唯讀，子元件不能修改
- **State 狀態** — 元件內部管理的資料，state 改變會觸發重新渲染
- **Virtual DOM 虛擬 DOM** — 記憶體中的 DOM 副本，React 比較差異後只更新有變化的真實 DOM
- **Rendering / Re-render 渲染 / 重新渲染** — state 或 props 改變時，React 重新執行 component function 產生新畫面
- **Reconciliation 協調** — React 比較新舊 Virtual DOM 差異（diffing）並決定最小更新範圍的過程
- **Hook** — React 16.8 引入，讓 function component 也能使用 state 和生命週期功能
- **useState** — 在 function component 中宣告 state，回傳 `[值, setter]`
- **useEffect** — 處理 side effect（API 呼叫、訂閱、操作 DOM），在 render 後執行
- **useRef** — 取得 DOM 元素的參考，或儲存不觸發重新渲染的值
- **useContext** — 讀取 Context 的值，不需要層層傳遞 props
- **useMemo** — 快取計算結果，只在依賴改變時重新計算，避免不必要的重複運算
- **useCallback** — 快取 function 本身，避免子元件因 function 參考改變而重新渲染
- **Context 上下文** — 跨層傳遞資料的機制，避免 prop drilling
- **Provider 提供者** — Context 的資料來源元件，包住需要共享資料的元件樹
- **Prop Drilling Props 鑽取** — 資料需要一層一層往下傳 props 的問題，Context 或狀態管理可解決
- **Side Effect 副作用** — 不屬於純渲染的操作，例如 API 請求、setTimeout、訂閱事件
- **Controlled Component 受控元件** — 表單值由 React state 控制（`value` + `onChange`）
- **Uncontrolled Component 非受控元件** — 表單值由 DOM 自己管理，透過 `ref` 取值
- **Key 鍵值** — 渲染列表時給每個元素的唯一識別，幫助 React 辨識哪個元素改變了
- **React.memo** — HOC，當 props 沒變時跳過重新渲染
- **Lifecycle 生命週期** — 元件從掛載、更新到卸載的各個階段
- **Fragment 片段** — `<>...</>` 或 `<React.Fragment>`，包住多個元素但不產生額外 DOM 節點
- **Lazy / Suspense 懶加載** — 動態載入元件減少 bundle 大小，搭配 `<Suspense>` 顯示 loading 畫面
- **Error Boundary 錯誤邊界** — 捕捉子元件 render 錯誤，避免整個應用崩潰（只能用 class component 實作）
