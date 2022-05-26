import axios from 'axios'
import drf from '@/api/drf'
import router from "@/router"

export default {
    state:{
        searchKeyword: '',
        searchMovies : null,
        movies:[],
        movieDetail:[],
        sorted:[],
        movie_pk:'',
        likes : '',
        isLike: '',
        myarticle :[],
    },
    getters:{
        movies: state => state.movies,
        sorted: state => state.sorted,
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
        },
        SET_SORT: (state,genre) => state.sorted = genre,
        SET_MOVIEPK: (state, pk) => state.movie_pk = pk,
        SET_LIKES : (state, data) => state.likes = data.length,
        SET_MYARTICLE: (state,data) => state.myarticle = data
    },
    actions:{
        search({ commit,getters }, keyword) {
            commit('SET_SEARCHKEYWORD', keyword)
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
        fetchMovies({ commit, getters,dispatch }) {
            axios({
              url: drf.movies.movies(),
              method: 'get',
              headers: getters.authHeader,
            })
              .then(res => commit('SET_MOVIES', res.data))
              .catch(err => {
                  console.error(err.response)
                  if (err.response.status==401) {
                    dispatch("removeToken",'');
                  }
                })
        },
        movieDetail({commit, getters}, movie_pk){
            axios({
              url: drf.movies.movie_detail(movie_pk),
              method: 'get',
              headers: getters.authHeader,
            })
            .then(res => {
                commit('SET_MOVIEPK', movie_pk)
                commit('SET_DETAIL', res.data)
                commit('SET_LIKES', res.data.like_users)
                router.push({ name:'Detail' })
            })
            .catch(err => console.error(err.response))
            
        },
        sort({ commit,getters }, genre){
            axios({
                url: drf.movies.sort(genre),
                method: 'get',
                headers: getters.authHeader,
              })
            .then(res => {
                commit('SET_SORT', res.data)
            })
            .catch(err => console.error(err.response))
        },
        like({ commit, getters }, movie_pk){
            axios({
                url: drf.movies.like(movie_pk),
                method: 'post',
                headers: getters.authHeader,
              })
            .then(res => {
                console.log(res)
                commit('SET_DETAIL', res.data)
                commit('SET_LIKES',res.data.like_users)
            })
            .catch(err => console.error(err.response))
        },
        my_Review({ commit,getters }, myPK){
            axios({
                url: drf.movies.loadmyrivew(myPK),
                method: 'get',
                headers: getters.authHeader,
              })
            .then(res => {
                commit('SET_MYARTICLE', res.data)
                

            })
            .catch(err => console.error(err.response))
        },
    }
}