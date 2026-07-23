const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  // 是否对 node_modules 里的第三方库也做语法转译（把新语法转成老浏览器能跑的）
  transpileDependencies: true,
  // 里面写这个服务器该怎么工作（代理、端口、自动打开浏览器等）
  devServer: {
    // 挂载代理配置，告诉开发服务器：「某些请求别自己处理，转交给另一个服务器」。
    proxy: {
      // 所有以 /api 为开头的请求全部都代理到 Django 后端进行请求（http://localhost:8000）
      '/api': {
        target: 'http://localhost:8000',
        // 把请求头里的 Host/Origin 改成目标服务器地址（8000）。作用：让 Django 以为请求来自 8000 自己，避免某些后端按 Host 校验拒绝连接。开发联调基本都设成 true。
        changeOrigin: true
      }
    }
  }
})
