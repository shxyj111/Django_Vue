import axios from 'axios'

// 统一的 axios 实例，所有请求自动带上 /api 前缀
// 配合 vue.config.js 的 devServer.proxy，开发时会被转发到 Django 后端
const request = axios.create({
  baseURL: '/api',
  timeout: 5000
})

export default request
