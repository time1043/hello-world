# fontend

- Reference - org

  [React org](https://react.dev/), 

- Reference - course

  [React Brief Course (HDAlex_John bilibili)](https://www.bilibili.com/video/BV1qK421x79b/?), [React Brief Course (github)](https://github.com/13RTK/React-Concise-Course)

- Reference - recommend

  [Fullstack React](https://www.bilibili.com/video/BV1JC4y1H7jv/), 

  [shangyang](https://www.bilibili.com/video/BV18m4y1y7gy), [shangyang FlowUs](https://flowus.cn/share/0b1dace8-0291-4430-952e-1553b667854b?promotionChannel=BZ_syqd_01), [shangyang board_leave_message](https://flowus.cn/share/95ca872b-eec4-417c-84ed-1602b3b12b39)

  [social media](https://www.bilibili.com/video/BV1tz421r7bC/), 





## vscode

- shortcut key

  Formatted code: `shift + alt + f`

  



- plug-in

  fitcode, 

  Live Server, 

  console ninja, 
  
- Java: `extension pack for java`, `spring boot extension pack`, 

- Fontend: `live server`, 







# HTML























# CSS













# JavaScript













# TypeScript

















# fontend native demo

## board leave message















# React Brief Course (Alex)

- Question: `React` + Brief 

  In China, `Vue` ecology is better

  The training institution courses are too long

  



- Course Content

- Part 1: 

  from `html + css + js` to `React`

  *demo*: dynamic circle editortodo list (simple)

- Part 2: 

  `nodejs`, `vite scaffolding` (The real way to develop react)

  component, `Props`, `children` (Partition components and component communication)

  data request, lifecycle (`useEffect` usage)

  *project*: abstract

  Custom `Hock` (Abstract Operation Logic)

  *project*: weather forecast

  *project deployment*: `Vercel`, `Netify`

- Part 3: 

  state sharing, context API (Global state management)

  React Router

  introduction of `TailwindCSS` (The most popular atomic CSS library)

  performance optimization (useMemo, memo, useCallback)

  *project*: student management system (fontend + Saas tool)



- Without

  long time -> brief course

  full content -> retrieval capability (where)

  for job -> knowledge guidance





## Prepare the Environment

- Online environment

  [stackblitz](https://stackblitz.com/edit/stackblitz-starters-opcydc?file=index.html)

- Local environment

  ```bash
  npm install -g create-react-app
  
  ```

  



### Online environment

- Native js 

  index.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <title>Home</title>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width" />
      <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
      <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
      <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    </head>
    <body>
      <div id="vanilla">
        <h1>Title</h1>
        <input class="vanilla-input" type="text" />
        <p class="vanilla-p"></p>
      </div>
      <hr />
  
      <div id="app"></div>
  
      <!-- <script src="main-react.js" type="text/babel"></sczript> -->
      <script src="main.js"></script>
    </body>
  </html>
  
  ```

  main.js

  ```js
  const inputEl = document.querySelector('.vanilla-input');
  const pEl = document.querySelector('.vanilla-p');
  
  inputEl.addEventListener('input', (event) => {
    pEl.textContent = event.target.value;
  });
  
  ```

- React

  index.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <title>Home</title>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width" />
      <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
      <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
      <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    </head>
    <body>
      <!-- <div id="vanilla">
        <h1>Title</h1>
        <input class="vanilla-input" type="text" />
        <p class="vanilla-p"></p>
      </div>
      <hr /> -->
  
      <div id="app"></div>
  
      <script src="main-react.js" type="text/babel"></script>
      <!-- <script src="main.js"></script> -->
    </body>
  </html>
  
  ```

  main-react.js

  ```js
  function MyApp() {
    const [textInput, setTextInput] = React.useState('');
  
    return (
      <main>
        <h1>Title</h1>
        <input
          type="text"
          onChange={(event) => setTextInput(event.target.value)}
        />
        <p>{textInput}</p>
      </main>
    );
  }
  
  const appEl = document.querySelector('#app');
  const root = ReactDOM.createRoot(appEl);
  
  root.render(<MyApp />);
  
  ```

  



### Local environment (vscode)

- Introduction

  简单导入React库文件：[react CDN](https://legacy.reactjs.org/docs/cdn-links.html)

  在原生js实现jsx：[import babel (Very old front-end build tool)](https://dev.to/jeetvora331/write-react-code-with-cdn-in-html-56i9)

  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  
      <script
        crossorigin
        src="https://unpkg.com/react@18/umd/react.production.min.js"
      ></script>
      <script
        crossorigin
        src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"
      ></script>
      <script
        type="text/javascript"
        src="https://unpkg.com/babel-standalone@6.26.0/babel.js"
      ></script>
  
      <title>Document</title>
    </head>
  
    <body>
      <div id="app"></div>
      <script type="text/babel" src="./main.js"></script>
    </body>
  </html>
  
  ```

  离线文件

  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  
      <script crossorigin src="./static/js/react.production.min.js"></script>
      <script crossorigin src="./static/js/react-dom.production.min.js"></script>
      <script type="text/javascript" src="./static/js/babel.js"></script>
  
      <title>Document</title>
    </head>
  
    <body>
      <div id="app"></div>
      <script type="text/babel" src="./main.js"></script>
    </body>
  </html>
  
  ```

  选中 (id `#` 或 class `.`)

  `useState` 变量实时更新

  ```js
  function AppContent() {
    const [text, setText] = React.useState("");
    return (
      <main>
        <input onChange={(event) => setText(event.target.value)} />
        <p> {text} </p>
      </main>
    );
  }
  
  const appEl = document.querySelector("#app");
  const root = ReactDOM.createRoot(appEl);
  
  root.render(<AppContent />);
  
  ```

  



































