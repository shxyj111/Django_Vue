import axios from 'axios'

// baseURL 优先读环境变量（.env.development / .env.production），否则回退 /api
const request = axios.create({
  baseURL: process.env.VUE_APP_BASE_API || '/api',
  timeout: 5000
})

// 请求拦截器：自动附带登录 token
request.interceptors.request.use(
  config => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  error => Promise.reject(error)
)

// 响应拦截器：统一处理业务错误 / 鉴权失效
request.interceptors.response.use(
  response => {
    const res = response.data
    // 约定：后端返回 { code, msg, data }，code !== 0 视为业务错误
    if (res.code !== undefined && res.code !== 0) {
      console.error('[API]', res.msg)
      return Promise.reject(new Error(res.msg || '业务错误'))
    }
    return response
  },
  error => {
    if (error.response && error.response.status === 401) {
      // 登录失效：清理本地状态并跳回登录页
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      if (window.location.hash !== '#/login') {
        window.location.href = '/#/login'
      }
    }
    return Promise.reject(error)
  }
)

export default request
