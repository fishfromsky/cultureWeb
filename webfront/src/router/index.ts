import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import MainPage from '@/views/MainPage.vue'
import Login from '@/components/Login/Login.vue'
import Talk from '@/components/Talk/index.vue'
import Buy from '@/components/Buy/index.vue'
import Game from '@/components/Game/index.vue'
import People from '@/components/People/index.vue'
import Show from '@/components/Show/index.vue'
import Wen from '@/components/Wen/index.vue'
import NewsDetain from '@/components/Wen/components/detail.vue'
import Decorate from '@/components/Decorate/index.vue'
import Material from '@/components/Material/index.vue'
import MaterialDetail from '@/components/Material/Detail.vue'
import Book from '@/components/Book/index.vue'
import Register from '@/components/Register/index.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'MainPage',
    component: MainPage,
    redirect: '/show',
    children: [
      {
        path: '/show',
        name: 'Show',
        component: Show
      },
      {
        path: '/decorate',
        name: 'decorate',
        component: Decorate
      },
      {
        path: '/material',
        name: 'material',
        component: Material,
      },
      {
        path: '/history',
        name: 'history',
        component: Book
      },
      {
        path: '/material/detail',
        name: 'material_detail',
        component: MaterialDetail
      },
      {
        path: '/people',
        name: 'People',
        component: People
      },
      {
        path: '/wen',
        name: 'Wen',
        component: Wen
      },
      {
        path: '/news_detail',
        name: 'newsDetail',
        component: NewsDetain
      },
      {
        path: '/buy',
        name: 'Buy',
        component: Buy
      },
      {
        path: '/game',
        name: 'Game',
        component: Game
      },
      {
        path: '/talk',
        name: 'Talk',
        component: Talk
      }
    ]
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  }
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
