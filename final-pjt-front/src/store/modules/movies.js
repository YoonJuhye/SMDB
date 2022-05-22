// import router from '@/router'
// import axios from 'axios'
// import drf from '@/api/drf'

import router from "@/router"


export default {
    state:{
        searchKeyword: '',
        searchMovie : null,

    },
    getters:{

    },
    mutations:{
        SET_SEARCHKEYWORD: (state,keyword) => state.searchKeyword = keyword,
    },
    actions:{
        search({ commit }, keyword) {
            commit('SET_SEARCHKEYWORD', keyword)
            router.push({ name:'search' })
        },
        research({ commit }, keyword) {
            commit('SET_SEARCHKEYWORD', keyword)
        }
    }
}