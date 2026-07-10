<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <div class="demo">
    <button @click="testLogin">测试连接后端</button>
    <p>后端返回：{{ message }}</p>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import request from './api/request'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data() {
    return {
      message: ''
    }
  },
  methods: {
    async testLogin() {
      try {
        // 实际请求地址：/api/login/  （经代理转发到 Django 的 /api/login/）
        const res = await request.get('/login/')
        this.message = typeof res.data === 'string' ? res.data : JSON.stringify(res.data)
      } catch (err) {
        this.message = '请求失败：' + err.message
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
