import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Axios from 'axios'
import ElementUI from 'element-ui';
import bootstrap3 from 'bootstrap3';
import 'element-ui/lib/theme-chalk/index.css';
Vue.config.productionTip = false;
Vue.prototype.$axios = Axios;
Vue.prototype.Elementui = Axios;

import settings from './settings'
Vue.prototype.$settings = settings;
// Axios.defaults.withCredentials = true;
Vue.use(ElementUI);
Vue.use(bootstrap3);
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
