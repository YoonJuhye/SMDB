import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignupView from '../views/SignupView'
import LoginView from '../views/LoginView'
import LogoutView from '../views/LogoutView'
import SearchView from '../views/SearchView'
import MovieDetail from '../views/MovieDetail'
import MyPageView from '../views/MyPageView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/movie/',
    name: 'Detail',
    component: MovieDetail
  },
  {
    path: '/mypage/',
    name: 'MyPage',
    component: MyPageView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
