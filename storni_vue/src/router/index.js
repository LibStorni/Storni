import { createRouter, createWebHistory } from 'vue-router'
import store     from '../store'
import Home      from '../views/Home.vue'
import Article   from '../views/Article.vue'
import Search    from '../views/Search.vue'
import Cart      from '../views/Cart.vue'
import SignUp    from '../views/SignUp.vue'
import LogIn     from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'
import Checkout  from '../views/Checkout.vue'
import Success   from '../views/Success.vue'



const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },

  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },

  {
    path: '/login',
    name: 'LogIn',
    component: LogIn
  },

  {
    path: '/myaccount',
    name: 'MyAccount',
    component: MyAccount,
    meta:{
       requireLogin:true
    }
  },

  {
    path: '/search',
    name: 'Search',
    component: Search
  },

  {
    path: '/cart',
    name: 'Cart',
    component: Cart,
    meta:{
       requireLogin:true
    }
  },

  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout,
    meta:{
       requireLogin:true
    }
  },

  {
    path: '/cart/Success',
    name: 'Success',
    component: Success
  },

  {
    path: '/:article_slug/',
    name :'Article',
    component: Article
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to,from,next)=>{
    if (to.matched.some(record => record.meta.requireLogin)&& !store.state.isAuthenticated){
      next({name:'LogIn', query: {to:to.path}});

    } else{
      next()
    }
})

export default router