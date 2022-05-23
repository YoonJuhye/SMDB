// import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

import router from "@/router"


export default {
    state:{
        searchKeyword: '',
        searchMovie : null,
        movies:[],
        movieDetail:[],


    },
    getters:{
        movies: state => state.movies,
    },
    mutations:{
        SET_SEARCHKEYWORD: (state,keyword) => state.searchKeyword = keyword,
        SET_MOVIES: (state, movies) => state.movies = movies,
        SET_DETAIL: (state, movie) => state.movieDetail = movie
    },
    actions:{
        search({ commit }, keyword) {
            commit('SET_SEARCHKEYWORD', keyword)
            router.push({ name:'search' })
        },
        research({ commit }, keyword) {
            commit('SET_SEARCHKEYWORD', keyword)
        },
        fetchMovies({ commit, getters }) {
            axios({
              url: drf.movies.movies(),
              method: 'get',
              headers: getters.authHeader,
            })
              .then(res => commit('SET_MOVIES', res.data))
              .catch(err => console.error(err.response))
        },
        movieDetail({commit, getters}, movie_pk){
            console.log(movie_pk)
            axios({
              url: drf.movies.movie_detail(movie_pk),
              method: 'get',
              headers: getters.authHeader,
            })
            .then(res => {
                commit('SET_DETAIL', res.data)
                router.push({ name:'Detail' })
            })
            .catch(err => console.error(err.response))
        }
    }
}