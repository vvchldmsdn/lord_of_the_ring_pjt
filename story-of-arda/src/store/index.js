import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
    fetchRace({ commit, getters }) {
      axios({
        url: "http://127.0.0.1:8000/"
      })
    }
  },
})
