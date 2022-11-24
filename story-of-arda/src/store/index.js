import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    raceList: [],
  },
  getters: {
    raceList: state => state.raceList
  },
  mutations: {
    SET_RACE: (state, raceList) => state.raceList = raceList
  },
  actions: {
    // 한 종족 캐릭터들 리스트 받기
    fetchRace({ commit }, raceName) {
      axios({
        url: `http://127.0.0.1:8000/race/${raceName}`,
        method: 'get',
      })
        .then((res) => { commit("SET_RACE", res.data) })
        .catch((err) => console.log(`get race error = ${err}`))
    }
  },
})
