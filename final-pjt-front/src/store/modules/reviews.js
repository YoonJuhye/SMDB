
import axios from 'axios'
import drf from '@/api/drf'
import router from "@/router"


export default {
    state:{
        reviews:[],
        comments:[],
        rank:0,
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
        },
        SET_RANK(state, rank){
            state.rank =rank
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
                let average = 0
                if (res.data.length > 0) {
                    for (const review of res.data) {
                    average = average + review.rank
                }
                commit('SET_RANK',(average/res.data.length).toFixed(1))
                } else {
                    commit('SET_RANK',(0).toFixed(1))
                }
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
                console.log(res.data)
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
        deleteComment({ getters },data){
            console.log(data)
            axios({
                url: drf.reviews.comment_update_or_delete(data),
                method: 'DELETE',
                headers: getters.authHeader,
            })
            .then( res => {
                console.log(res)
                router.go()
            })
            .catch(err => console.error(err.response))
        },
        updateComment({ getters },data){
            console.log(data)
            axios({
                url: drf.reviews.comment_update_or_delete(data),
                method: 'PUT',
                data:data,
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