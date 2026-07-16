import { createRouter, createWebHashHistory } from 'vue-router'
import Login from '@/views/Login.vue'
import Home from '@/views/Home.vue'
import Users from '@/views/Users.vue'
import About from '@/views/About.vue'
import DirectivesDemo from '@/views/DirectivesDemo.vue'
import PortalLayout from '@/views/portal/PortalLayout.vue'
import Dashboard from '@/views/portal/Dashboard.vue'
import SubModule from '@/views/portal/SubModule.vue'

const routes = [
  { path: '/login', name: 'Login', component: Login },
  { path: '/', name: 'Home', component: Home, meta: { requiresAuth: true } },
  { path: '/users', name: 'Users', component: Users, meta: { requiresAuth: true } },
  { path: '/about', name: 'About', component: About },
  { path: '/directives', name: 'DirectivesDemo', component: DirectivesDemo },
  // 大屏智能管理系统：独立全屏布局，新标签页打开
  {
    path: '/portal',
    component: PortalLayout,
    children: [
      // 系统总览：大屏主页面（工厂俯瞰图 + 6 个悬浮卡片）
      { path: '', name: 'Dashboard', component: Dashboard },
      // 六个子页面：点击卡片后跳转到对应子系统
      { path: 'tpm', name: 'PortalTpm', component: SubModule, meta: { moduleKey: 'tpm' } },
      { path: 'facility', name: 'PortalFacility', component: SubModule, meta: { moduleKey: 'facility' } },
      { path: 'quality', name: 'PortalQuality', component: SubModule, meta: { moduleKey: 'quality' } },
      { path: 'spare', name: 'PortalSpare', component: SubModule, meta: { moduleKey: 'spare' } },
      { path: 'motor', name: 'PortalMotor', component: SubModule, meta: { moduleKey: 'motor' } },
      { path: 'energy', name: 'PortalEnergy', component: SubModule, meta: { moduleKey: 'energy' } }
    ]
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

// 全局前置守卫：需要登录的页面，若没有 token 则强制跳登录
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !localStorage.getItem('token')) {
    next('/login')
  } else {
    next()
  }
})

export default router
