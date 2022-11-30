import Vue from 'vue'
import VueRouter from 'vue-router'

import ArdaMap from '@/components/ArdaMap.vue'
import RaceView from '@/views/RaceView.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '',
    name: 'arda',
    component: ArdaMap
  },
  {
    path: '/races',
    name: 'races',
    component: RaceView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
