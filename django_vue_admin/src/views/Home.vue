<template>
  <div class="page">
    <h2>控制台</h2>
    <p>欢迎，{{ user ? user.nickname : '访客' }}！</p>
    <div class="cards">
      <div class="card"><div class="num">{{ stats.users }}</div><div>用户数</div></div>
      <div class="card"><div class="num">8</div><div>今日订单</div></div>
      <div class="card"><div class="num">¥1,280</div><div>今日营收</div></div>
    </div>
    <p class="hint">这是演示首页，统计数字可对接真实接口。</p>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return { stats: { users: '-' } }
  },
  computed: {
    user() {
      try { return JSON.parse(localStorage.getItem('user') || 'null') } catch { return null }
    }
  }
}
</script>

<style scoped>
.page { padding: 24px; }
.cards { display: flex; gap: 16px; margin-top: 16px; }
.card { flex: 1; background: #fff; padding: 20px; border-radius: 8px; text-align: center; box-shadow: 0 1px 4px rgba(0, 0, 0, .08); }
.num { font-size: 28px; font-weight: bold; color: #409eff; }
.hint { color: #999; font-size: 13px; margin-top: 16px; }
</style>
