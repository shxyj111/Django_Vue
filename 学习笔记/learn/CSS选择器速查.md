# CSS 选择器（Selector）速查表

> 来源：`learn/test04.html` 中实际演示过的所有选择器类型。
> 回顾原问题「CSS 是不是只有靠 class 才能绑定元素？」——答案：**不是**。CSS 用「选择器」来匹配元素，class 只是其中一种。

## 一句话概念

- **选择器（Selector）**：一段 CSS 规则开头的模式，用来「挑出」要加样式的元素。
- **规则（Rule）**：`选择器 { 属性: 值; }`，浏览器把样式应用到所有被选中的元素上。
- 不是"绑定"，而是"匹配"：写得对，元素自动命中；写错就不生效。

## 一、基础 / 简单选择器（Simple Selectors）

| 选择器 | 写法 | 作用 | 演示 |
|--------|------|------|------|
| 通配符 | `*` | 选中所有元素（常用于重置） | `.scope-universal *` |
| 类型(标签) | `div` / `p` / `h1` | 按标签名命中 | `.scope-type p` |
| 类 | `.class` | 命中带该 class 的元素（可重复、可多个） | `.highlight` |
| ID | `#id` | 命中唯一 id（页面内应不重复，权重最高） | `#only-one` |

> ID 与 class 区别：id 全页唯一（`#`）；class 可复用（`.`）。ID 权重远高于 class。

## 二、组合器（Combinators：表达元素间关系）

| 选择器 | 写法 | 作用 | 演示 |
|--------|------|------|------|
| 后代 | `A B` | A 内部**任意层级**的 B | `.descendant li` |
| 子代 | `A > B` | A 的**直接子元素** B | `.child > li` |
| 相邻兄弟 | `A + B` | 紧跟在 A 后面的**第一个**同级 B | `h4 + p` |
| 通用兄弟 | `A ~ B` | A 之后的**所有**同级 B | `h4 ~ p` |

> 空格是"后代"，`>` 是"子代"，别混淆：`.box li` 会命中嵌套再嵌套的 li；`.box > li` 只命中第一层。

## 三、属性选择器（Attribute Selectors）

| 选择器 | 写法 | 作用 | 演示 |
|--------|------|------|------|
| 存在 | `[attr]` | 元素有该属性即命中 | `[data-flag]` |
| 精确等于 | `[attr="val"]` | 属性值完全等于 val | `[data-role="admin"]` |
| 列表含词 | `[attr~="val"]` | 以空格分隔的列表中含 val | `[data-tags~="vue"]` |
| 开头 | `[attr^="val"]` | 值以 val 开头 | `a[href^="https"]` |
| 结尾 | `[attr$="val"]` | 值以 val 结尾 | `a[href$=".pdf"]` |
| 包含 | `[attr*="val"]` | 值包含 val 子串 | `[data-note*="重要"]` |
| 前缀 | `[attr\|="val"]` | 等于 val 或以 val- 开头（多语言 lang） | `[lang\|="zh"]` |

## 四、伪类（Pseudo-class，单冒号 `:`）

用来命中「某种状态 / 位置」的元素，多数**不需要 class**，元素进入该状态自动命中。

- 交互类：`:hover` `:active` `:focus` `:focus-within` `:link` `:visited`
- 结构类：`:first-child` `:last-child` `:nth-child(n)` `:only-child` `:empty` `:root`
- 表单类：`:checked` `:disabled` `:required` `:valid` `:invalid` `:placeholder-shown`
- 逻辑类：`:not()` `:is()` `:has()`

> 完整清单见 `状态速查.md` / `test03.html`。test04 中只做代表演示（`:hover` `:first-child` `:focus`）。

## 五、伪元素（Pseudo-element，双冒号 `::`）

命中元素的「某个部分」，如同在元素内部插入一个虚拟节点（不在真实 DOM 里）。

| 伪元素 | 作用 | 演示 |
|--------|------|------|
| `::before` | 在元素内容**前**插入 | `p::before` 加『 |
| `::after` | 在元素内容**后**插入 | `p::after` 加』 |
| `::first-letter` | 第一个字母 / 汉字 | 首字放大变蓝 |
| `::first-line` | 第一行文字 | 首行黄底 |
| `::selection` | 用户选中的文字 | 拖选高亮 |
| `::placeholder` | 输入框占位符 | 红斜体占位 |

> 记忆：伪类 `:` 选"状态的元素"，伪元素 `::` 选"元素的部件"。

## 六、分组 & 复合选择器

| 写法 | 名称 | 作用 | 演示 |
|------|------|------|------|
| `A, B, C` | 分组 | 逗号并列，多者共用一套样式 | `h3, .box, > span` |
| `tag.class` | 复合 | 连写不空格，命中"同时满足"的元素 | `p.note.active` |

> `p.note` 表示"既是 p 标签、又带 note 类"；少写一个条件就匹配不到。

## 七、Vue scoped（编译期语法糖，非原生选择器）

在 `.vue` 文件里写 `<style scoped>`，Vue 编译时会：

1. 给该组件模板的**每个元素**自动加一个属性，如 `data-v-7a9e1f`；
2. 把你的每条规则自动改写成带该属性的属性选择器，例如
   `.scoped-p` → `.scoped-p[data-v-7a9e1f]`。

效果：样式**只作用于本组件**，不会泄漏到全局——这正是"不靠 class 也能精确隔离"的例子。
test04 第七节用普通 HTML 的 `[data-v-demo] .scoped-p` 模拟了这个编译结果。

## 速记口诀

- 选「谁」：`*` 通配 / `标签` / `.类` / `#id`
- 选「关系」：`空格`后代 / `>`子代 / `+`相邻兄弟 / `~`通用兄弟
- 选「属性」：`[attr]` 存在 / `[=]`等于 / `[^=]`开头 / `[$=]`结尾 / `[*=]`包含
- 选「状态」：`:hover` `:checked` `:first-child`
- 选「部件」：`::before` `::after` `::first-letter`
- 多者共样式：`,` 分组；同时满足：`连写`复合
