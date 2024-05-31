# fontend

- Reference - org

  [React org](https://react.dev/), 

- Reference - course

  [React Brief Course (bilibili)](https://www.bilibili.com/video/BV1qK421x79b/?), [React Brief Course (github)](https://github.com/13RTK/React-Concise-Course), 

  [React Project!!!](https://www.bilibili.com/video/BV1Z34y1A7Tn/), 

  [React Chat App Full Tutorial 2024 | Realtime Chat Application Project with Firebase (Lama Dev)](https://www.youtube.com/watch?v=domt_Sx-wTY), [fireship-io / react-firebase-chat](https://github.com/fireship-io/react-firebase-chat), [safak / react-firebase-chat](https://github.com/safak/react-firebase-chat), 

  [VS Code Tutorial – Become More Productive (freeCodeCamp.org)](https://www.youtube.com/watch?v=heXQnM99oAI), 

  [Note Taking App using Next.js 14 | Auth.js](https://www.youtube.com/watch?v=Ha5SvXMr468), 

  Reference - recommend

  [Fullstack React](https://www.bilibili.com/video/BV1JC4y1H7jv/), 

  [shangyang](https://www.bilibili.com/video/BV18m4y1y7gy), [shangyang FlowUs](https://flowus.cn/share/0b1dace8-0291-4430-952e-1553b667854b?promotionChannel=BZ_syqd_01), [shangyang board_leave_message](https://flowus.cn/share/95ca872b-eec4-417c-84ed-1602b3b12b39)
  
  [social media](https://www.bilibili.com/video/BV1tz421r7bC/), 
  
- Reference - dev

  [apache / echarts](https://echarts.apache.org/zh/index.html), 





## vscode

- shortcut key

  Formatted code: `shift + alt + f`

  



- plug-in

  fitcode, 

  Live Server, 

  console ninja, 
  
- Java: `extension pack for java`, `spring boot extension pack`, 

- Fontend: `live server`, 



- go 格式化 保存时优化导入

  settings.json 

  ```json
    "[go]": {
      "editor.defaultFormatter": "golang.go"
    },
    "editor.codeActionsOnSave": { "source.organizeImports": true },
  ```

  





# HTML























# CSS









## Bootstrap

- 参考：[bootstrap官网](https://getbootstrap.com/)、[bootstrap3.4.1](https://getbootstrap.com/docs/3.4/components/)









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

  











# Echarts

- Reference

  [echarts docs](https://echarts.apache.org/handbook/zh/get-started/), [echarts example](https://echarts.apache.org/examples/zh/index.html), [echarts feature](https://echarts.apache.org/zh/feature.html), [echarts options](https://echarts.apache.org/zh/option.html#title), 



- Overview

  基本概念：

  基本使用：七个表

  高级使用：主题、动态效果、常用API

  项目实战：电商平台数据可视化监控 (后台 vue图表组件 websocket 扩展功能)





## 基本概念

- 数据可视化

  数据 -> 图表 (直观表达信息)

- 实现方式

  简单报表：Excel、水晶报表

  商业智能BI：Microsoft BI、Power-BI

  动态表格：Echarts.js、D3.js (编码类 灵活度)



- echarts

  数据支持：kv、二维表、typedArray；流数据、增量渲染

  多种图表：柱状图、折线图、折柱混合图、散点图；饼状图、地图、仪表盘图、玫瑰图、气泡图、条形图、雷达图....

- 代码实操

  引入echarts.js文件、准备呈现图表的盒子、

  初始化echarts实例对象、**准备配置项**、将配置项设置给echarts实例对象

  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Document</title>
      <script src="lib/echarts.min.js"></script>
    </head>
    <body>
      <div style="width: 600px; height: 400px"></div>
      <script>
        var myChart = echarts.init(document.querySelector("div"));
        var option = {
          xAxis: {
            type: "category",
            data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
          },
  
          yAxis: {
            type: "value",
          },
  
          series: [
            {
              data: [820, 932, 901, 934, 1290, 1330, 1320],
              type: "line",
            },
          ],
        };
        myChart.setOption(option);
      </script>
    </body>
  </html>
  
  ```

  [echarts options](https://echarts.apache.org/zh/option.html#title) 

  ```
  option = {
    xAxis  直角坐标系中x轴
    yAxis  直角坐标系中y轴
    series  序列列表 每个序列通过type决定自己的图表类型
  }
  
  
  xAxis.type：分类变量category、数值value
  xAxis.data：具体数据
  series.type：折线图line、条形图bar、饼图pie
  
  ```

  









## 基本使用

### 柱状图

- demo 期末语文成绩

  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Document</title>
      <script src="lib/echarts.min.js"></script>
    </head>
    <body>
      <div style="width: 600px; height: 400px"></div>
      <script>
        var myChart = echarts.init(document.querySelector("div"));
        var option = {
          title: {
            text: "期末语文数学英语成绩",
          },
          legend: {
            data: ["语文成绩", "数学成绩", "英语成绩"],
            right: 0,
          },
  
          xAxis: {
            type: "category",
            data: ["张三", "李四", "王五", "赵六", "钱七"],
          },
          yAxis: {
            type: "value",
          },
  
          series: [
            {
              name: "语文成绩",
              type: "bar",
              data: [80, 90, 75, 85, 95],
            },
            {
              name: "数学成绩",
              type: "bar",
              data: [90, 85, 95, 80, 90],
            },
            {
              name: "英语成绩",
              type: "bar",
              data: [75, 80, 85, 90, 80],
            },
          ],
        };
        myChart.setOption(option);
      </script>
    </body>
  </html>
  
  ```

  









### 折线图











折柱混合图





### 散点图





### 饼状图



### 地图





### 仪表盘图





### 玫瑰图





### 气泡图





### 条形图





### 雷达图















## 高级使用



主题、动态效果、常用API















## 项目实战

- 主题

  电商平台 数据可视化监控 

- 启动

  ```bash
  cd koa2-server
  npm install
  node app.js
  
  cd ../vision
  npm install
  npm run serve
  
  ```

  

## 后台 





## vue图表组件 







## websocket 











## 扩展功能

- 扩展功能

  主题切换、页面合并、全屏切换













































