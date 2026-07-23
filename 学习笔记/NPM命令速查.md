# NPM 命令速查（django_vue_admin）

> 本文件用于说明本项目里 `npm install`、`npm run serve` 这类命令都是干什么的。
> 对应 `package.json` 中 `scripts` 字段（第 5–9 行）定义的内容。

---

## 一、前提：npm 是什么

**npm = Node 的包管理器（Package Manager）**。Node.js 装好就自带 npm。它干两件事：

1. 从网上的「npm 仓库」**下载别人写好的代码库**（比如 vue、axios），省得你手写；
2. 运行项目里定义的**脚本命令**（就是 `npm run xxx`）。

> 类比：npm 像「应用商店 + 启动器」。
> - `npm install` = 去商店把要用的库下载到本地；
> - `npm run xxx` = 按项目里写好的「快捷方式」启动某个功能。

---

## 二、本项目定义的脚本（package.json:5-9）

```json
"scripts": {
  "serve": "vue-cli-service serve",
  "build": "vue-cli-service build",
  "lint":  "vue-cli-service lint"
}
```

`npm run <名字>` 就是去执行 `scripts` 里对应的那行命令。

---

## 三、逐个命令详解

### 1. `npm install` —— 安装依赖（第一次 / 加库必跑）

```bash
npm install
```

**作用**：读 `package.json`，把里面列出的所有库下载到项目里的 `node_modules/` 文件夹。

**为什么需要它**：`git clone` 或新建项目后，`node_modules/` **默认不提交到 git**（太大）。所以换台机器、或刚拉下代码，必须先 `npm install` 把 vue、axios、vue-router、cli-service 这些全部装回来，项目才能跑。

对应 `package.json` 的两类：

| 分类 | 字段 | 这里的库 | 何时需要 |
|------|------|---------|---------|
| 运行时依赖 | `dependencies`（10–14 行） | vue、vue-router、axios | **运行项目**必须，线上也要 |
| 开发依赖 | `devDependencies`（16–24 行） | @vue/cli-service、babel、eslint | **只在开发 / 构建时**用，线上部署后不用 |

执行完会：
- 生成 / 更新 `node_modules/`（所有库的实体代码）；
- 更新 `package-lock.json`（锁定每个库的具体版本，保证别人装出来跟你一致）。

**带参数的变体**（以后会用到）：

```bash
npm install axios        # 装一个新库，并自动写进 dependencies
npm install -D eslint    # 装开发依赖（写进 devDependencies）
npm install              # 无参：按 package.json 装全部
```

---

### 2. `npm run serve` —— 启动开发服务器（你最常敲的）

```bash
npm run serve
```

背后执行（package.json:6）：`vue-cli-service serve`。

**这个命令干的事**：

1. 启动一个**本地开发服务器**，默认地址 `http://localhost:8080`；
2. **实时热更新（HMR）**：改 `src/` 里的代码，浏览器自动刷新，不用手动重启；
3. 在 `localhost:8080` 端做 `vue.config.js` 里配的 `/api` **代理**到 Django `:8000`；
4. 把 Vue 单文件组件、ES6+ 语法**实时编译**成浏览器能懂的 JS。

> 注意：它是**开发用**的，代码「边编译边跑」，不会生成最终文件。

---

### 3. `npm run build` —— 打包生产版本（上线用）

```bash
npm run build
```

背后执行（package.json:7）：`vue-cli-service build`。

**作用**：把 `src/` 所有源码**一次性编译、压缩、合并**，生成纯静态文件，输出到 `dist/` 文件夹（HTML / CSS / JS）。
- 这些是**可以直接部署**到 Nginx / 任何静态服务器的文件；
- 体积被压缩、代码被混淆，适合生产环境。

> `serve` vs `build` 区别：**serve 是「开发时边改边看」，build 是「最终打包成可上线文件」**。平时本地学习用 `serve` 就够了。

---

### 4. `npm run lint` —— 代码格式检查（可选）

```bash
npm run lint
```

背后执行（package.json:8）：`vue-cli-service lint`。

**作用**：按 ESLint 规则（package.json:25-38 的 `eslintConfig`）**扫描代码里的格式 / 潜在错误**，比如缩进不对、未使用的变量、不规范写法。

> 对初学者：报错一般是「代码风格不优雅」，大多不影响运行；可以先不纠结。

---

## 四、一张表记住

| 命令 | 何时用 | 结果 |
|------|--------|------|
| `npm install` | 拉下代码后、加新库后 | 装好 `node_modules/` |
| `npm run serve` | **平时开发 / 学习** | 起 `:8080` 开发服务器，热更新 |
| `npm run build` | 准备部署上线 | 生成 `dist/` 静态文件 |
| `npm run lint` | 想查代码规范问题 | 输出格式检查结果 |

---

## 五、本项目的典型启动顺序

```bash
cd django_vue_admin      # 进入前端目录
npm install              # 第一次：装依赖（之后一般不用重复）
npm run serve            # 起前端开发服务器 → 浏览器开 localhost:8080
```

同时另开一个终端跑 Django（`python manage.py runserver 8000`），前后端就通了
（前端 `:8080` 的 `/api` 请求经 webpack 代理转发到 Django `:8000`）。
