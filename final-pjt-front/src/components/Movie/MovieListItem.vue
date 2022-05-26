<template>
    <div @click="moviebutton" class="card movielistitems border-light mx-3" style="width:200px; height:340px;">
        <img class="card-header card-img-top" style="width:200px; height:250px; padding:0;"  :src='`https://image.tmdb.org/t/p/w500/${movie.poster_path}`' alt="#">
        <div class="card-body">
            <p class="card-title" style="width:180px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"> {{ movie.title }} </p>
            <div class="card-text"><small class="text-muted">{{ movie.release_date }}</small></div>
        </div>
  </div>
</template>

<script>
import router from '@/router'
import { mapActions } from 'vuex'

export default {
    name:'MovieListItem',
    props:{
        movie:{
            type:Object,
        }
    },
    methods:{
        ...mapActions(['movieDetail','loadReview']),
        moviebutton: function () {
            if (this.$store.state.accounts.currentUser) {
                this.loadReview(this.movie.id)
                this.movieDetail(this.movie.id)
            } else {
            alert('로그인을 해주세요!')
            router.push({ name:'login' })
            }
        }
        }
    }


</script>

<style>
.movielistitems {
    box-shadow: 3px 3px 10px grey;
}
</style>