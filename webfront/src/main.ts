import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import '@/assets/fonts/font.css'

Vue.use(ElementUI)
Vue.config.productionTip = false
axios.defaults.baseURL = 'http://120.27.144.206:8000'
Vue.prototype.$http = axios

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
