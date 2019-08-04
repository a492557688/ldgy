import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import qingsongzhaofang from './views/fangwuchuzu/qingsongzhaofang.vue'
import xiaoquzhaofang from './views/fangwuchuzu/xiaoquzhaofang.vue'
import jinritehui from './views/fangwuchuzu/jinritehui.vue'
import fangwutuoguan from './views/fangwutuoguan_hezuo/fangwutuoguan.vue'
import shangwuhezuo from './views/fangwutuoguan_hezuo/hezuo.vue'
import Detail from './views/detail_page.vue'

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/qingsongzhaofang/',
      name: 'qingsongzhaofang',
      component: qingsongzhaofang
    },
     {
      path: '/detail',
      name: 'detail',
      component: Detail
     },
         {
      path: '/filter',
      name: 'filter',
      component: qingsongzhaofang
     },

       {
      path: '/xiaoquzhaofang',
      name: 'xiaoquzhaofang',
      component: xiaoquzhaofang
     },
   {
      path: '/jinritehui',
      name: 'jinritehui',
      component: jinritehui
     },
       {
      path: '/fangwutuoguan',
      name: 'fangwutuoguan',
      component: fangwutuoguan
     },
   {
      path: '/shangwuhezuo',
      name: 'shangwuhezuo',
      component: shangwuhezuo
     },


  ]
})
