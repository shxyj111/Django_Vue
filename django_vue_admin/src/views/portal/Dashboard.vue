<template>
  <div class="dashboard" :style="dashboardStyle">
    <!-- 顶部 Header -->
    <header class="header">
      <div class="logo-box">
        <img src="/imgs/KSF.png" alt="康师傅饮品事业" />
      </div>
      <h1 class="page-title">廊坊顶津智能管理系统</h1>
      <div class="header-btns">
        <button class="header-btn">
          <svg viewBox="0 0 24 24">
            <circle cx="16" cy="6" r="2.5"/>
            <circle cx="6" cy="12" r="2.5"/>
            <circle cx="16" cy="18" r="2.5"/>
            <line x1="13.5" y1="7.5" x2="8.5" y2="10.5"/>
            <line x1="13.5" y1="16.5" x2="8.5" y2="13.5"/>
          </svg>
          链路图
        </button>
        <button class="header-btn">
          <svg viewBox="0 0 24 24">
            <rect x="3" y="5" width="18" height="12" rx="2"/>
            <line x1="9" y1="20" x2="15" y2="20"/>
            <line x1="12" y1="17" x2="12" y2="20"/>
          </svg>
          动态屏
        </button>
      </div>
    </header>

    <!-- 主舞台区域（工厂俯瞰图 + 悬浮卡片） -->
    <div class="main-stage">
      <!-- 工厂占位背景 -->
      <div class="factory-bg">
        <div class="factory-placeholder">
          <div class="factory-building">
            <div class="building-block" style="width:60px;height:70px"><div class="building-roof"></div></div>
            <div class="building-block" style="width:90px;height:100px"><div class="building-roof"></div></div>
            <div class="building-block" style="width:45px;height:55px"><div class="building-roof"></div></div>
            <div class="building-block" style="width:110px;height:120px"><div class="building-roof"></div></div>
            <div class="building-block" style="width:65px;height:75px"><div class="building-roof"></div></div>
          </div>
          <div class="factory-label">K S F   F A C T O R Y</div>
        </div>
        <div class="factory-ground-hint"></div>
      </div>

      <!-- 六个子系统卡片（绝对定位，点击跳转子页面） -->
      <!-- 卡片位置与原型 HTML 一致 -->
      <router-link v-for="m in modules" :key="m.key"
                   :to="`/portal/${m.key}`"
                   :class="['sys-card', m.cardClass]"
                   :title="'进入' + m.name"
      >
        <div class="card-title">{{ m.name }}</div>
        <div class="card-icon">
          <img :src="m.icon" :alt="m.name">
        </div>
      </router-link>

      <!-- 左下角菜单按钮 -->
      <div class="bottom-action" title="返回首页">
        <router-link to="/portal" style="color:#fff;display:block;width:100%;height:100%;">
          <svg viewBox="0 0 24 24"><path d="M4 8h4V4H4v4zm6 12h4v-4h-4v4zm-6 0h4v-4H4v4zm0-6h4v-4H4v4zm6 0h4v-4h-4v4zm6-10v4h4V4h-4zm-6 4h4V4h-4v4zm6 6h4v-4h-4v4zm0 6h4v-4h-4v4z"/></svg>
        </router-link>
      </div>
    </div>

    <!-- 底部水印 -->
    <div class="footer-mark">Copyright &copy; 2026 Kangshifu Beverage All Rights Reserved</div>
  </div>
</template>

<script>
// 大屏主页面：卡片数据为静态配置，无需调用 API
export default {
  name: 'DashboardPage',
  computed: {
    // 背景图用行内样式，避免 css-loader 解析路径失败
    dashboardStyle() {
      return {
        backgroundImage: "url('/imgs/KSF-Overview.png')"
      }
    }
  },
  data() {
    return {
      // 六个子系统的卡片配置：名称、图标、定位类名
      modules: [
        { key: 'spare',  name: '备品备件系统', icon: '/imgs/1.png', cardClass: 'card-spare-parts' },
        { key: 'facility',name: '厂务管理数位化', icon: '/imgs/2.png', cardClass: 'card-factory-dig' },
        { key: 'tpm',    name: 'TPM管理系统',   icon: '/imgs/3.png', cardClass: 'card-tpm' },
        { key: 'energy', name: '能源管理系统',   icon: '/imgs/4.png', cardClass: 'card-energy' },
        { key: 'motor',  name: '电机监控系统',   icon: '/imgs/5.png', cardClass: 'card-motor' },
        { key: 'quality',name: '品质分析系统',   icon: '/imgs/6.png', cardClass: 'card-quality' },
      ]
    }
  }
}
</script>

<style scoped>
/* ===== 全局大屏样式 ===== */
* { margin: 0; padding: 0; box-sizing: border-box; }

.dashboard {
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  font-family: 'Microsoft YaHei', 'PingFang SC', sans-serif;
  background-size: cover;
  position: relative;
}

/* ===== Header ===== */
.header {
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 68px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px;
  z-index: 100;
  background: linear-gradient(180deg, rgba(0,0,0,.25) 0%, transparent 100%);
}

.logo-box {
  background: #fff;
  border: 1px solid #fff;
  border-radius: 10px;
  padding: 8px 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 12px rgba(0,0,0,.15), 0 0 0 1px rgba(0,0,0,.05);
}
.logo-box img { max-height: 36px; width: auto; display: block; }

.page-title {
  font-size: 34px;
  font-weight: 700;
  color: #ffffff;
  text-shadow: 0 2px 16px rgba(0,0,0,.4), 0 0 40px rgba(46,125,74,.15);
  letter-spacing: 6px;
}

.header-btns {
  display: flex;
  gap: 12px;
}
.header-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  min-width: 68px;
  min-height: 56px;
  background: rgba(16,40,30,.75);
  border: 1px solid rgba(90,220,150,.35);
  border-radius: 12px;
  color: #9effc8;
  font-size: 12px;
  padding: 6px 10px;
  cursor: pointer;
  transition: all .25s;
  backdrop-filter: blur(4px);
  box-shadow: 0 0 10px rgba(90,220,150,.08);
}
.header-btn:hover {
  background: rgba(30,80,55,.65);
  color: #cfffdf;
  border-color: rgba(120,255,170,.55);
  box-shadow: 0 0 18px rgba(90,220,150,.18);
  transform: translateY(-1px);
}
.header-btn svg { width: 18px; height: 18px; fill: none; stroke: currentColor; stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round; }

/* ===== Main Stage ===== */
.main-stage {
  position: absolute;
  top: 76px;
  left: 16px;
  right: 16px;
  bottom: 36px;
  border-radius: 16px;
  overflow: hidden;
}

.factory-bg {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background:
    linear-gradient(170deg, rgba(56,142,60,.06) 0%, rgba(27,94,32,.1) 30%, rgba(20,60,28,.12) 60%, rgba(15,45,22,.14) 100%);
}
.factory-placeholder {
  width: 85%;
  max-width: 1200px;
  height: 72%;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  opacity: .18;
  filter: blur(.3px);
}
.factory-building {
  display: flex;
  gap: 6px;
  margin-bottom: 16px;
  align-items: flex-end;
}
.building-block {
  background: linear-gradient(180deg, #a8cfb5 0%, #82ab96 50%, #6a9484 100%);
  border-radius: 3px 3px 0 0;
  position: relative;
  overflow: hidden;
  box-shadow: inset 0 -8px 16px rgba(0,0,0,.08);
}
.building-roof {
  position: absolute;
  top: 0; left: -2px; right: -2px;
  height: 12px;
  background: linear-gradient(90deg, #c8e2d4, #e0ede5, #c8e2d4);
  border-radius: 3px 3px 0 0;
  box-shadow: 0 1px 3px rgba(0,0,0,.1);
}
.factory-label {
  color: #9cc8a8;
  font-size: 14px;
  letter-spacing: 6px;
  text-transform: uppercase;
  opacity: .7;
}

.factory-ground-hint {
  position: absolute;
  bottom: 8%;
  left: 5%; right: 5%;
  height: 3px;
  background: linear-gradient(90deg, transparent, rgba(120,160,140,.15) 20%, rgba(120,160,140,.15) 80%, transparent);
  border-radius: 2px;
}

/* ===== System Cards ===== */
.sys-card {
  position: absolute;
  background: rgba(8,24,18,.55);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  border: 1px solid rgba(120,220,180,.45);
  border-radius: 20px;
  padding: 10px 12px;
  width: 176px;
  cursor: pointer;
  transition: all .35s cubic-bezier(.25,.8,.25,1);
  display: flex;
  flex-direction: column;
  gap: 6px;
  text-decoration: none;
  color: inherit;
  box-shadow: 0 0 14px rgba(120,220,180,.12);
}
.sys-card:hover {
  transform: translateY(-6px) scale(1.04);
  border-color: rgba(140,255,220,.65);
  box-shadow: 0 0 24px rgba(120,220,180,.25);
  background: rgba(8,24,18,.7);
}

.card-title {
  align-self: center;
  margin-top: -18px;
  padding: 6px 18px;
  background: linear-gradient(90deg, #0a4d3e, #14806a);
  border: 1px solid rgba(120,255,210,.35);
  border-radius: 8px;
  color: #fff;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: .5px;
  white-space: nowrap;
  text-shadow: none;
  box-shadow: 0 2px 8px rgba(0,0,0,.25);
}

.card-icon {
  width: 100%;
  aspect-ratio: 16/10;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  position: relative;
  background: rgba(0,0,0,.15);
  border: 1px solid rgba(120,220,180,.25);
  box-shadow: inset 0 0 0 1px rgba(0,0,0,.1);
}
.card-icon img { width: 50%; height: 50%; object-fit: contain; display: block; }

/* 卡片绝对定位（与原型一致） */
.card-spare-parts { top: 8%;   left: 26%; }
.card-factory-dig { top: 8%;   right: 26%; }
.card-tpm        { top: 40%;  left: 3%; }
.card-energy     { top: 42%;  right: 3%; }
.card-motor      { bottom: 8%; left: 26%; }
.card-quality    { bottom: 6%; right: 26%; }

/* ===== Bottom Action ===== */
.bottom-action {
  position: absolute;
  bottom: 22px;
  left: 22px;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: linear-gradient(135deg, #00bcd4, #0097a7);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 4px 20px rgba(0,188,212,.45), 0 0 0 3px rgba(0,188,212,.15);
  transition: all .3s;
  z-index: 50;
}
.bottom-action:hover {
  transform: scale(1.15) rotate(5deg);
  box-shadow: 0 8px 32px rgba(0,188,212,.6), 0 0 0 5px rgba(0,188,212,.2);
}
.bottom-action svg { width: 24px; height: 24px; fill: #fff; }

/* ===== Footer watermark ===== */
.footer-mark {
  position: absolute;
  bottom: 8px;
  right: 18px;
  font-size: 10.5px;
  color: rgba(255,255,255,.14);
  z-index: 5;
  letter-spacing: 1px;
}
</style>
