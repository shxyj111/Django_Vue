import request from './request'

// 智能管理系统相关接口（baseURL 已是 /api，故此处只写模块路径）
// 主页面：系统总览
export function getOverview() {
  return request.get('/portal/')
}

// 六个子页面：按 key 取对应模块数据
// key ∈ tpm | facility | quality | spare | motor | energy
export function getModule(key) {
  return request.get(`/${key}/`)
}
