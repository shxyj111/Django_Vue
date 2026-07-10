const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      // 将以 /api 开头的请求代理到 Django 后端（http://localhost:8000）
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
})
