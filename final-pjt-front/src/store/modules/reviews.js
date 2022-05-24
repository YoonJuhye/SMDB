
import axios from 'axios'
import drf from '@/api/drf'
// import router from "@/router"


export default {
    state:{
        reviews:[],
    },
    getters:{
    },
    mutations:{
        SET_REVIEW(state, review){
            if (review.length == 0) {
                state.reviews = null
            } else {
                state.reviews = review
            }
        }
    },
    actions:{
        loadReview({ commit,getters }, movie_pk){
            console.log('로드리뷰')
            axios({
                url: drf.reviews.reviews(movie_pk),
                method: 'get',
                headers: getters.authHeader,
            })
            .then(res => {
                commit('SET_REVIEW',res.data)
            })
            .catch(err => console.error(err.response))
        },
        createReview({ getters }, data){
            axios({
                url: drf.reviews.reviews(data.movie),
                method: 'post',
                data : data,
                headers: getters.authHeader,
            })
            .then( res => {
                console.log(res.data.movie)
                this.loadReview(res.data.movie)
            })
            .catch(err => console.error(err.response))
        }
    }
}