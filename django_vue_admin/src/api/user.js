import request from './request'

// 用户相关接口集中在此，组件只调用函数名，不感知具体 URL
export function login(data) {
  return request.post('/login/', data)
}

export function getUsers() {
  return request.get('/users/')
}

export function getProfile() {
  return request.get('/profile/')
}
