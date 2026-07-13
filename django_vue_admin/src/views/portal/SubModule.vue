<template>
  <div class="sub-dashboard">
    <!-- ===== Header ===== -->
    <header class="header">
      <div class="header-left">
        <span class="logo">康师傅饮品事业</span><span class="logo-sub">KSF Beverage</span>
        <nav class="nav-links">
          <router-link to="/portal">首页</router-link>
          <router-link to="/portal/tpm">TPM管理系统</router-link>
          <router-link to="/portal/facility">厂务管理数位化</router-link>
          <router-link to="/portal/quality">品质分析系统</router-link>
          <router-link to="/portal/spare">备品备件系统</router-link>
          <router-link to="/portal/motor">电机监控系统</router-link>
          <router-link to="/portal/energy">能源管理系统</router-link>
        </nav>
      </div>
      <div class="header-center"><h1>欢迎进入{{ data.name }}</h1></div>
      <div class="header-right">
        <router-link to="/portal" class="home-btn" title="返回总览">&#8962; 总览</router-link>
        <div class="user-info"><span>&#128100;</span><span>管理员--刘伟恒</span></div>
        <div class="avatar">刘</div>
        <button class="btn-logout">退出</button>
        <div class="top-tools">&#128197; &#127769; &#9881; &#9786;</div>
      </div>
    </header>

    <!-- ===== Body: Sidebar + Main ===== -->
    <div class="body">
      <!-- 左侧图标栏 -->
      <aside class="sidebar">
        <router-link to="/portal/tpm" class="sidebar-icon" title="TPM管理系统">&#9776;</router-link>
        <router-link to="/portal/facility" class="sidebar-icon" title="厂务管理数位化">&#127968;</router-link>
        <router-link to="/portal/quality" class="sidebar-icon" title="品质分析系统">&#9881;</router-link>
        <router-link to="/portal/spare" class="sidebar-icon" title="备品备件系统">&#128295;</router-link>
        <router-link to="/portal/motor" class="sidebar-icon" title="电机监控系统">&#128202;</router-link>
        <router-link to="/portal/energy" class="sidebar-icon" title="能源管理系统">&#128203;</router-link>
        <div class="sidebar-bottom"><div class="menu-btn">&#128722;</div></div>
      </aside>

      <!-- 主内容区 -->
      <main class="main-content">
        <div class="page-title-row">
          <h2 class="page-title">欢迎进入{{ data.name }}</h2>
        </div>

        <div class="dashboard-grid">
          <!-- 指标概览（大数字面板） -->
          <div class="panel big-num-panel">
            <div class="big-num-item" v-for="s in data.stats" :key="s.label">
              <div class="big-num-value">{{ s.value ?? '--' }}</div>
              <div class="big-num-label">{{ s.label }}</div>
            </div>
          </div>

          <!-- 数据列表面板 -->
          <div class="panel span-2">
            <div class="panel-header">
              <span class="panel-title">数据列表</span>
              <div class="panel-toolbar"><span class="arrow-btn">&#8250;</span></div>
            </div>
            <table class="data-table">
              <thead>
                <tr>
                  <th v-for="c in data.columns" :key="c">{{ c }}</th>
                </tr>
              </thead>
              <tbody>
                <tr v-if="!data.records || data.records.length === 0">
                  <td :colspan="(data.columns || []).length || 1" class="empty">暂无数据</td>
                </tr>
                <tr v-else v-for="(row, i) in data.records" :key="i">
                  <td v-for="c in data.columns" :key="c">{{ row[c] ?? '--' }}</td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- 趋势图占位面板（暂无数据） -->
          <div class="panel">
            <div class="panel-header">
              <span class="panel-title">趋势分析</span>
            </div>
            <div class="chart-placeholder">暂无数据</div>
          </div>

          <!-- 分布图占位面板（暂无数据） -->
          <div class="panel">
            <div class="panel-header">
              <span class="panel-title">分布占比</span>
            </div>
            <div class="chart-placeholder">暂无数据</div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import { getModule } from '@/api/portal'

export default {
  name: 'SubModulePage',
  data() {
    return {
      data: { name: '', desc: '', stats: [], columns: [], records: [] }
    }
  },
  created() {
    this.fetch()
  },
  watch: {
    // 组件在不同子路由间被复用，切换时需重新拉取
    '$route'() {
      this.fetch()
    }
  },
  methods: {
    async fetch() {
      const key = this.$route.meta.moduleKey
      if (!key) return
      try {
        const res = await getModule(key)
        this.data = res.data.data
      } catch (e) {
        console.error('加载模块数据失败', e)
      }
    }
  }
}
</script>

<style scoped>
/* ===== 全局暗色大屏主题（与产品原型一致） ===== */
* { margin: 0; padding: 0; box-sizing: border-box; }
.sub-dashboard {
  width: 100vw;
  min-height: 100vh;
  background: #061220;
  color: #e0e8f0;
  font-family: 'Microsoft YaHei', 'PingFang SC', sans-serif;
  overflow-x: hidden;
}
.sub-dashboard::before {
  content: '';
  position: fixed;
  inset: 0;
  background: radial-gradient(ellipse at 50% 0%, rgba(79,195,247,.04) 0%, transparent 60%);
  pointer-events: none;
  z-index: 0;
}

/* ===== Header ===== */
.header {
  height: 56px;
  background: linear-gradient(90deg, #0a1a30, #0f2240, #0a1a30);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  border-bottom: 1px solid rgba(80,160,220,.18);
  position: sticky;
  top: 0;
  z-index: 100;
}
.header-left { display: flex; align-items: center; gap: 18px; }
.logo { font-size: 17px; font-weight: bold; color: #ffd54f; letter-spacing: 1px; text-shadow: 0 0 12px rgba(255,213,79,.2); }
.logo-sub { font-size: 11px; color: #78909c; margin-left: 4px; }
.nav-links { display: flex; gap: 12px; font-size: 12px; }
.nav-links a { color: #90a4ae; text-decoration: none; transition: .2s; padding: 2px 6px; border-radius: 3px; }
.nav-links a:hover, .nav-links a.router-link-active { color: #4fc3f7; background: rgba(79,195,247,.08); }
.header-center h1 { font-size: 19px; font-weight: 600; letter-spacing: 3px; color: #fff; text-shadow: 0 0 16px rgba(79,195,247,.15); }
.header-right { display: flex; align-items: center; gap: 14px; font-size: 13px; color: #90a4ae; }
.user-info { display: flex; align-items: center; gap: 6px; }
.avatar { width: 28px; height: 28px; border-radius: 50%; background: linear-gradient(135deg, #37474f, #455a64); display: flex; align-items: center; justify-content: center; font-size: 11px; color: #b0bec5; border: 1px solid #546e7a; }
.btn-logout { background: rgba(66,133,244,.22); border: 1px solid rgba(66,133,244,.38); color: #90caf9; padding: 5px 16px; border-radius: 4px; cursor: pointer; font-size: 12px; transition: .2s; }
.btn-logout:hover { background: rgba(66,133,244,.35); }
.top-tools { display: flex; gap: 8px; font-size: 15px; color: #78909c; }
.home-btn { display: inline-flex; align-items: center; gap: 4px; background: rgba(0,188,212,.18); border: 1px solid rgba(0,188,212,.35); color: #80deea; padding: 5px 14px; border-radius: 4px; cursor: pointer; font-size: 12px; text-decoration: none; transition: .2s; }
.home-btn:hover { background: rgba(0,188,212,.3); }

/* ===== Body ===== */
.body { display: flex; position: relative; z-index: 1; }
.sidebar {
  width: 50px;
  min-height: calc(100vh - 56px);
  background: linear-gradient(180deg, #081626, #0c1e32);
  border-right: 1px solid rgba(80,160,220,.1);
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px 0;
  gap: 4px;
}
.sidebar-icon {
  width: 38px; height: 38px;
  display: flex; align-items: center; justify-content: center;
  border-radius: 6px; cursor: pointer; transition: .2s;
  color: #546e7a; font-size: 18px; text-decoration: none;
}
.sidebar-icon:hover, .sidebar-icon.router-link-active { background: rgba(79,195,247,.12); color: #4fc3f7; }
.sidebar-bottom { margin-top: auto; }
.menu-btn { width: 40px; height: 40px; border-radius: 50%; background: linear-gradient(135deg, #00acc1, #0097a7); display: flex; align-items: center; justify-content: center; color: #fff; font-size: 18px; box-shadow: 0 3px 14px rgba(0,188,212,.38); }

/* ===== Main Content ===== */
.main-content { flex: 1; padding: 16px 20px; }
.page-title-row { text-align: center; margin-bottom: 14px; }
.page-title { font-size: 25px; font-weight: 700; letter-spacing: 5px; color: #fff; text-shadow: 0 0 24px rgba(79,195,247,.25); }

/* ===== Grid Layout ===== */
.dashboard-grid { display: grid; grid-template-columns: 1fr 1.4fr 1fr; gap: 14px; max-width: 1680px; margin: 0 auto; }
.span-2 { grid-column: span 2; }

/* ===== Panel Base ===== */
.panel {
  background: linear-gradient(145deg, rgba(10,26,48,.88), rgba(14,36,62,.82));
  border: 1px solid rgba(79,195,247,.1);
  border-radius: 10px;
  padding: 14px 16px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0,0,0,.15);
}
.panel::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px; background: linear-gradient(90deg, transparent, rgba(79,195,247,.45), transparent); }
.panel-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px; }
.panel-title { font-size: 14px; font-weight: 600; color: #80deea; letter-spacing: 1px; text-shadow: 0 0 8px rgba(128,222,234,.15); }
.panel-toolbar { display: flex; gap: 6px; font-size: 12px; color: #607d8b; }
.arrow-btn { cursor: pointer; color: #4fc3f7; font-size: 16px; }

/* ===== Big Number Panel ===== */
.big-num-panel { display: flex; align-items: center; justify-content: center; gap: 50px; padding: 24px; flex-wrap: wrap; }
.big-num-item { text-align: center; }
.big-num-value { font-size: 44px; font-weight: 700; color: #ffd54f; text-shadow: 0 0 28px rgba(255,213,79,.35); line-height: 1; }
.big-num-label { font-size: 13px; color: #90a4ae; margin-top: 6px; letter-spacing: 1px; }

/* ===== Data Table ===== */
.data-table { width: 100%; border-collapse: collapse; font-size: 13px; }
.data-table th, .data-table td { padding: 9px 12px; border-bottom: 1px solid rgba(79,195,247,.1); text-align: left; }
.data-table th { color: #80deea; background: rgba(79,195,247,.06); font-weight: 600; }
.data-table td { color: #c5d3e0; }
.data-table tbody tr:hover { background: rgba(79,195,247,.05); }
.data-table .empty { text-align: center; color: #607d8b; padding: 32px 0; }

/* ===== Chart Placeholder ===== */
.chart-placeholder {
  width: 100%; height: 180px;
  display: flex; align-items: center; justify-content: center;
  color: #607d8b; font-size: 13px;
  background: radial-gradient(ellipse at center, rgba(79,195,247,.03) 0%, transparent 70%);
  border-radius: 8px;
}

/* Scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(79,195,247,.18); border-radius: 3px; }
</style>
