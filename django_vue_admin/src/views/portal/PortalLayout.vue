<template>
  <div class="dashboard-wrapper">
    <!-- 大屏系统的子路由出口（大屏首页 Dashboard / 子页面 SubModule） -->
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'DashboardLayout'
}
</script>

<style scoped>
.dashboard-wrapper {
  width: 100vw;
  height: 100vh;
}
</style>
