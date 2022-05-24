import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';

import accounts from './modules/accounts'
import movies from './modules/movies'
import reviews from  './modules/reviews'
import vueMoment from 'vue-moment'

Vue.use(Vuex)
Vue.use(vueMoment)

export default new Vuex.Store({
  modules: { accounts,movies,reviews },
  plugins: [createPersistedState({ paths: ['accounts','movies','reviews'] })]


})
