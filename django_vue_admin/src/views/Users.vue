// HTML代码注释
<template>
  <div class="page">
    <h2>用户列表</h2>
    <table>
      <thead>
        <tr><th>ID</th><th>用户名</th><th>昵称</th><th>角色</th></tr>
      </thead>
      <tbody>
        <tr v-for="u in list" :key="u.id">
          <td>{{ u.id }}</td>
          <td>{{ u.username }}</td>
          <td>{{ u.nickname }}</td>
          <td>{{ u.role }}</td>
        </tr>
      </tbody>
    </table>
    <p v-if="loading">加载中...</p>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

// JS代码注释
<script>
import { getUsers } from '@/api/user'

export default {
  name: 'UserListPage',
  data() {
    return { list: [], loading: false, error: '' }
  },
  async created() {
    this.loading = true
    try {
      const res = await getUsers()
      this.list = res.data.data.list
    } catch (e) {
      this.error = (e.response && e.response.data && e.response.data.msg) || e.message
    } finally {
      this.loading = false
    }
  }
}
</script>
// 加上这个scoped后这个Css代码就只对这个文件内的HTML代码有效
<style scoped>
.page { padding: 24px; }
table { width: 100%; border-collapse: collapse; background: #fff; }
th, td { border: 1px solid #eee; padding: 10px; text-align: left; }
th { background: #fafafa; }
.error { color: #f56c6c; }
</style>
