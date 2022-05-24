
import axios from 'axios'
import drf from '@/api/drf'
import router from "@/router"


export default {
    state:{
        reviews:[],
        comments:[],
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
        },
        SET_COMMENTS(state,comments){
            if (comments.length == 0) {
                state.comments = null
                console.log(state.comments)
            } else {
                state.comments = comments
                console.log(state.comments)
            }
        }
    },
    actions:{
        loadReview({ commit,getters }, movie_pk){
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
            })
            .catch(err => console.error(err.response))
        },
        deleteReview({ getters }, review){
            axios({
                url: drf.reviews.update_delete_rivew(review),
                method: 'DELETE',
                headers: getters.authHeader,
            })
            .then(() => {
                router.go()
                
            })
            .catch(err => console.error(err.response))
        },
        updateReview({ getters }, data){
            axios({
                url: drf.reviews.update_delete_rivew(data),
                method: 'PUT',
                data : data,
                headers: getters.authHeader,
            })
            .then( res => {
                console.log(res.data.movie)
                router.go()
            })
            .catch(err => console.error(err.response))
        },
        createComment({ getters }, data){
            console.log(data)
            axios({
                url: drf.reviews.create_comment(data),
                method: 'post',
                data : data,
                headers: getters.authHeader,
            })
            .then( res => {
                console.log(res)
                router.go()
            })
            .catch(err => console.error(err.response))
        },
    }
}