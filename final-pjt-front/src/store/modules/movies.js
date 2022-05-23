import axios from 'axios'
import drf from '@/api/drf'
import router from "@/router"


export default {
    state:{
        searchKeyword: '',
        searchMovies : null,
        movies:[],
        movieDetail:[],


    },
    getters:{
        movies: state => state.movies,
    },
    mutations:{
        SET_SEARCHKEYWORD: (state,keyword) => state.searchKeyword = keyword,
        SET_MOVIES: (state, movies) => state.movies = movies,
        SET_DETAIL: (state, movie) => state.movieDetail = movie,
        SET_SEARCH(state, movies) {
            if (movies.length == 0){
                state.searchMovies = null
            } else {
                console.log(movies)
                state.searchMovies = movies
            }
            
        }
    },
    actions:{
        search({ commit,getters }, keyword) {
            commit('SET_SEARCHKEYWORD', keyword)
            console.log(keyword)
            axios({
                url: drf.movies.search(keyword),
                method: 'get',
                headers: getters.authHeader,
            })
            .then(res => {
                commit('SET_SEARCH', res.data)
                router.push({ name:'search' })
            })
            .catch(err => console.error(err.response))
        },
        research({ commit,getters }, keyword) {
            commit('SET_SEARCHKEYWORD', keyword)
            console.log(keyword)
            axios({
                url: drf.movies.search(keyword),
                method: 'get',
                headers: getters.authHeader,
            })
            .then(res => {
                commit('SET_SEARCH', res.data)
            })
            .catch(err => console.error(err.response))
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