<template>
  <div class="login-page">
    <form class="login-box" @submit.prevent="handleLogin">
      <h2>系统登录</h2>
      <input v-model="form.username" placeholder="用户名" />
      <input v-model="form.password" type="password" placeholder="密码" />
      <button type="submit" :disabled="loading">登录</button>
      <p class="tip">演示账号：admin / 123456</p>
      <p v-if="error" class="error">{{ error }}</p>
    </form>
  </div>
</template>

<script>
import { login } from '@/api/user'

export default {
  name: 'LoginPage',
  data() {
    return {
      form: { username: '', password: '' },
      loading: false,
      error: ''
    }
  },
  methods: {
    async handleLogin() {
      this.error = ''
      this.loading = true
      try {
        const res = await login(this.form)
        const { token, user } = res.data.data
        localStorage.setItem('token', token)
        localStorage.setItem('user', JSON.stringify(user))
        this.$router.push('/')
      } catch (e) {
        this.error = (e.response && e.response.data && e.response.data.msg) || e.message || '登录失败'
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.login-page { display: flex; justify-content: center; align-items: center; min-height: 100vh; background: #f0f2f5; }
.login-box { background: #fff; padding: 32px; border-radius: 8px; width: 300px; box-shadow: 0 2px 8px rgba(0, 0, 0, .1); display: flex; flex-direction: column; gap: 12px; }
.login-box input { padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
.login-box button { padding: 8px; background: #409eff; color: #fff; border: none; border-radius: 4px; cursor: pointer; }
.login-box button:disabled { opacity: .6; cursor: not-allowed; }
.tip { font-size: 12px; color: #999; margin: 0; }
.error { color: #f56c6c; font-size: 13px; margin: 0; }
</style>
