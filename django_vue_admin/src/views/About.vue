<template>
  <div class="page">
    <h2>关于</h2>
    <p>这是一个 Vue3 + Django 前后端分离示例项目，按企业级目录结构组织。</p>
    <ul>
      <li>前端：Vue3 + vue-router + axios 封装（请求/响应拦截器）</li>
      <li>后端：Django 提供 JSON API</li>
      <li>开发代理：vue.config.js 将 /api 转发到 Django</li>
      <li>目录分层：api/ 服务层、views/ 页面层、router/ 路由层</li>
    </ul>
  </div>
</template>

<script>
export default { name: 'AboutPage' }
</script>

<style scoped>
.page { padding: 24px; }
</style>
