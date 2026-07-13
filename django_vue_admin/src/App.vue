<template>
  <div id="app">
    <header class="nav" v-if="showNav">
      <span class="logo">Admin</span>
      <router-link to="/">控制台</router-link>
      <router-link to="/users">用户管理</router-link>
      <router-link to="/about">关于</router-link>
      <span class="spacer"></span>
      <span v-if="user" class="user">{{ user.nickname }}</span>
      <a href="#" @click.prevent="logout">退出</a>
    </header>
    <main class="content">
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
  computed: {
    showNav() {
      return this.$route.path !== '/login'
    },
    user() {
      try { return JSON.parse(localStorage.getItem('user') || 'null') } catch { return null }
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      this.$router.push('/login')
    }
  }
}
</script>

<style>
* { box-sizing: border-box; }
body { margin: 0; font-family: Avenir, Helvetica, Arial, sans-serif; background: #f0f2f5; color: #2c3e50; }
.nav { display: flex; align-items: center; gap: 16px; padding: 0 24px; height: 56px; background: #001529; color: #fff; }
.nav a { color: #fff; text-decoration: none; }
.nav a.router-link-active { color: #409eff; font-weight: bold; }
.nav .logo { font-weight: bold; font-size: 18px; }
.nav .spacer { flex: 1; }
.nav .user { color: #409eff; }
.content { padding: 0; }
</style>
