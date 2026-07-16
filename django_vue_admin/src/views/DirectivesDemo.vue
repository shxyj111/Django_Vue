<template>
  <div class="demo-page">
    <h1>Vue 指令演示</h1>

    <!-- 1. v-bind：动态绑定 HTML 属性 / class / style -->
    <section class="card">
      <h2>1. v-bind（动态绑定属性）</h2>
      <p>下面按钮的 <code>:class</code> 与 <code>:disabled</code> 都由数据驱动：</p>
      <button :class="{ active: isActive }" :disabled="isActive" @click="toggleActive">
        {{ isActive ? '已激活（按钮被禁用）' : '点击激活' }}
      </button>
      <p>动态绑定图片地址 <code>:src</code>：</p>
      <img :src="logoUrl" alt="logo" class="logo" />
      <p>动态绑定行内样式 <code>:style</code>：
        <span :style="{ color: textColor, fontWeight: 'bold' }">这段文字颜色由数据控制</span>
      </p>
    </section>

    <!-- 2. v-model：表单双向绑定 -->
    <section class="card">
      <h2>2. v-model（表单双向绑定）</h2>
      <input v-model="message" placeholder="输入点什么..." />
      <p>你输入的是：<b>{{ message }}</b></p>

      <label class="inline">
        <input type="checkbox" v-model="agreed" /> 我同意（checkbox 双向绑定）
      </label>
      <p>同意状态：{{ agreed ? '已同意' : '未同意' }}</p>

      <select v-model="fruit">
        <option disabled value="">请选择水果</option>
        <option v-for="f in fruits" :key="f" :value="f">{{ f }}</option>
      </select>
      <p>选中的水果：{{ fruit }}</p>
    </section>

    <!-- 3. v-for：列表渲染 -->
    <section class="card">
      <h2>3. v-for（列表渲染）</h2>
      <ul>
        <li v-for="(item, index) in items" :key="item.id">
          #{{ index + 1 }} {{ item.name }} - {{ item.price }} 元
          <button class="mini" @click="removeItem(item.id)">删除</button>
        </li>
      </ul>
      <input v-model="newItem" placeholder="新增商品名" />
      <button @click="addItem">添加商品</button>
    </section>

    <!-- 4. v-on：事件监听 -->
    <section class="card">
      <h2>4. v-on（事件监听）</h2>
      <button @click="count++">点我 +1（@click 内联表达式）</button>
      <button @click="increment">点我 +1（调用方法）</button>
      <button @click.once="sayHi">只触发一次（事件修饰符 .once）</button>
      <p>当前计数：{{ count }}</p>
    </section>

    <!-- 5 & 6. v-if vs v-show -->
    <section class="card">
      <h2>5. v-if / v-else（真正增删 DOM 节点）</h2>
      <button @click="showIf = !showIf">切换 v-if 显示</button>
      <p v-if="showIf">我在 DOM 里（v-if 为 true 才渲染此节点）</p>
      <p v-else>我替换了上面的内容（v-else 分支）</p>

      <h2>6. v-show（切换 CSS display 属性）</h2>
      <button @click="showBox = !showBox">切换 v-show 显示</button>
      <p v-show="showBox">我始终在 DOM 里，只是 display 被切换</p>
    </section>

    <!-- 7. axios：发起 HTTP 请求 -->
    <section class="card">
      <h2>7. axios（发起 HTTP 请求）</h2>

      <!-- 7a. GET 请求：获取用户列表 -->
      <h3>7a. GET 请求（复用封装层）</h3>
      <p>复用项目封装的 <code>@/api</code> 接口层，请求会自动带 token 并经 <code>/api</code> 代理到 Django 后端。</p>
      <button @click="fetchUsers" :disabled="userLoading">
        {{ userLoading ? '请求中...' : 'GET /api/users/ 获取用户列表' }}
      </button>
      <button @click="clearUsers">清空结果</button>

      <!-- 用 v-if 处理加载/错误/成功三种状态 -->
      <p v-if="userLoading" class="tip">正在向后端请求数据...</p>
      <p v-else-if="userError" class="error">请求失败：{{ userError }}</p>
      <ul v-else-if="users.length">
        <li v-for="u in users" :key="u.id">
          {{ u.id }} - {{ u.username }}（{{ u.nickname }}）角色：{{ u.role }}
        </li>
      </ul>
      <p v-else class="tip">暂无数据，点击上方按钮发起请求。</p>

      <hr class="divider" />

      <!-- 7b. POST 请求：登录（原始 axios vs 封装后 对比） -->
      <h3>7b. POST 请求 — 登录（两种写法对比）</h3>
      <p class="tip">下方表单同时驱动两种调用方式：<b>原始 axios()</b> 与 <b>项目封装的 api/user.js</b>。</p>

      <!-- v-model 双向绑定登录表单 -->
      <div class="login-form">
        <input v-model="loginForm.username" placeholder="用户名" />
        <input v-model="loginForm.password" type="password" placeholder="密码" />
      </div>

      <div class="btn-row">
        <button class="btn-raw" @click="loginRawAxios" :disabled="loginLoadingRaw">
          {{ loginLoadingRaw ? '请求中...' : '原始 axios() 调用' }}
        </button>
        <button class="btn-wrapped" @click="loginWrappedApi" :disabled="loginLoadingWrap">
          {{ loginLoadingWrap ? '请求中...' : '封装后 login() 调用' }}
        </button>
      </div>

      <!-- 用 v-if / v-else 展示两种调用的返回结果 -->
      <div class="result-box">
        <div v-if="loginLoadingRaw || loginLoadingWrap" class="tip">正在请求 /api/login/ ...</div>
        <div v-else-if="loginResultRaw" class="result-panel result-raw">
          <strong>原始 axios() 返回：</strong><pre>{{ loginResultRaw }}</pre>
        </div>
        <div v-else-if="loginResultWrap" class="result-panel result-wrap">
          <strong>封装后 login() 返回：</strong><pre>{{ loginResultWrap }}</pre>
        </div>
        <div v-else-if="loginError" class="error">{{ loginError }}</div>
        <div v-else class="tip">输入账号密码后点击上方按钮测试。（演示账号：admin / 123456）</div>
      </div>

      <p class="tip code-compare">
        <strong>代码对比：</strong><br>
        原始写法 → <code>axios({method:'post',url,params,data,headers}).then().catch()</code><br>
        封装写法 → <code>const res = await login(form);  // 只需一行</code>
      </p>
    </section>

    <p class="tip">提示：打开浏览器开发者工具的 Elements 面板，对比切换 v-if 与 v-show 时 DOM 节点的增删差异。</p>
  </div>
</template>

<script>
// 采用与项目一致的 Options API 写法
// 复用项目封装的接口层（axios 实例 + 拦截器）
import { getUsers, login } from '@/api/user'
import axios from 'axios'

export default {
  name: 'DirectivesDemo',
  data() {
    return {
      // —— axios 演示数据 ——
      users: [],
      userLoading: false,
      userError: '',

      // —— axios POST 登录演示数据 ——
      loginForm: { username: '', password: '' },
      loginResultRaw: '',
      loginResultWrap: '',
      loginLoadingRaw: false,
      loginLoadingWrap: false,
      loginError: '',

      // —— v-bind 演示数据 ——
      isActive: false,
      logoUrl: 'https://vuejs.org/logo.svg',
      textColor: '#409eff',

      // —— v-model 演示数据 ——
      message: '',
      agreed: false,
      fruit: '',
      fruits: ['苹果', '香蕉', '橙子'],

      // —— v-for 演示数据 ——
      items: [
        { id: 1, name: '键盘', price: 199 },
        { id: 2, name: '鼠标', price: 99 },
        { id: 3, name: '显示器', price: 999 }
      ],
      newItem: '',
      nextId: 4,

      // —— v-on 演示数据 ——
      count: 0,

      // —— v-if / v-show 演示数据 ——
      showIf: true,
      showBox: true
    }
  },
  methods: {
    toggleActive() {
      this.isActive = !this.isActive
    },
    increment() {
      this.count++
    },
    sayHi() {
      alert('你好！这个按钮通过 .once 修饰符只会触发一次')
    },
    addItem() {
      const name = this.newItem.trim()
      if (!name) return
      this.items.push({ id: this.nextId++, name, price: 0 })
      this.newItem = ''
    },
    removeItem(id) {
      this.items = this.items.filter(i => i.id !== id)
    },
    // —— axios 请求：GET 用户列表 ——
    async fetchUsers() {
      this.userError = ''
      this.userLoading = true
      try {
        // getUsers 内部即 request.get('/users/')，走 axios 实例与拦截器
        const res = await getUsers()
        // 后端约定返回 { code, msg, data: { list, total } }
        this.users = res.data.data.list
      } catch (e) {
        this.userError = (e.response && e.response.data && e.response.data.msg) || e.message || '请求异常'
      } finally {
        this.userLoading = false
      }
    },
    clearUsers() {
      this.users = []
      this.userError = ''
    },
    // —— 7b-1：原始 axios() POST 登录（对应图片中的用例）——
    // 图片原写法：axios({ method:'post', url, params:{v1,v2}, data, headers })
    // 这里适配项目实际后端：POST /api/login/，body 为 JSON {username,password}
    async loginRawAxios() {
      this.loginResultRaw = ''
      this.loginResultWrap = ''
      this.loginError = ''
      this.loginLoadingRaw = true
      try {
        const res = await axios({
          method: 'post',
          url: '/api/login/',          // 走 vue.config.js 代理到 Django
          params: { v1: 123, v2: 456 },// 查询参数（URL ?v1=123&v2=456），演示图片用法
          data: {                       // 请求体（JSON body）
            name: this.loginForm.username,
            pwd: this.loginForm.password
          },
          headers: {
            'Content-Type': 'application/json'
          }
        }).then(function (res) {
          return res
        }).catch(function (error) {
          return Promise.reject(error)
        })
        this.loginResultRaw = JSON.stringify(res.data, null, 2)
      } catch (e) {
        this.loginError = (e.response && e.response.data && e.response.data.msg) || e.message || '原始 axios 登录失败'
      } finally {
        this.loginLoadingRaw = false
      }
    },
    // —— 7b-2：封装后的 login() 调用（对比展示）——
    async loginWrappedApi() {
      if (!this.loginForm.username || !this.loginForm.password) {
        this.loginError = '请输入用户名和密码'
        return
      }
      this.loginResultRaw = ''
      this.loginResultWrap = ''
      this.loginError = ''
      this.loginLoadingWrap = true
      try {
        // 封装层内部即 request.post('/login/', data)，自动带 token、统一拦截错误
        const res = await login({
          username: this.loginForm.username,
          password: this.loginForm.password
        })
        this.loginResultWrap = JSON.stringify(res.data, null, 2)
      } catch (e) {
        this.loginError = (e.response && e.response.data && e.response.data.msg) || e.message || '封装登录失败'
      } finally {
        this.loginLoadingWrap = false
      }
    }
  }
}
</script>

<style scoped>
.demo-page { padding: 24px; max-width: 760px; margin: 0 auto; }
.card { background: #fff; border: 1px solid #eee; border-radius: 8px; padding: 16px 20px; margin-bottom: 16px; }
h1 { color: #001529; }
h2 { font-size: 16px; color: #409eff; margin-top: 0; }
button { padding: 6px 14px; margin: 4px 6px 4px 0; border: none; border-radius: 4px; background: #409eff; color: #fff; cursor: pointer; }
button:disabled { opacity: .5; cursor: not-allowed; }
button.active { background: #67c23a; }
button.mini { padding: 2px 8px; font-size: 12px; background: #f56c6c; }
input, select { padding: 6px 10px; border: 1px solid #ccc; border-radius: 4px; margin: 4px 6px 4px 0; }
.inline { display: inline-flex; align-items: center; gap: 6px; }
.logo { width: 40px; vertical-align: middle; }
.tip { color: #999; font-size: 13px; }
code { background: #f5f5f5; padding: 1px 4px; border-radius: 3px; }
/* —— 登录演示区样式 —— */
h3 { font-size: 14px; color: #333; margin: 16px 0 8px; }
hr.divider { border: none; border-top: 1px solid #eee; margin: 20px 0; }
.login-form { display: flex; gap: 8px; margin-bottom: 10px; }
.login-form input { width: 160px; }
.btn-row { display: flex; gap: 8px; margin-bottom: 12px; }
.btn-raw { background: #e6a23c; }
.btn-wrapped { background: #67c23a; }
.result-box { min-height: 40px; }
.result-panel { background: #f9f9f9; border-radius: 4px; padding: 10px; margin-top: 8px; overflow-x: auto; }
.result-raw { border-left: 3px solid #e6a23c; }
.result-wrap { border-left: 3px solid #67c23a; }
.result-panel pre { margin: 4px 0 0; white-space: pre-wrap; word-break: break-all; font-size: 13px; color: #555; }
.code-compare { line-height: 1.8; }
</style>
