import Vue from 'vue'
import VueRouter from 'vue-router'

import ArdaMap from '@/components/ArdaMap.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/arda',
    name: 'arda',
    component: ArdaMap
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
