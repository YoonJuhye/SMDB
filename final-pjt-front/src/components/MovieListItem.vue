<template>
    <div @click="movieDetail(movie.id)" class="card mx-3" style="width:200px; height:340px;">
        <img class="card-header card-img-top" style="width:200px; height:250px; padding:0;"  :src='`https://image.tmdb.org/t/p/w500/${movie.poster_path}`'>

        <div class="card-body">
            <p class="card-title" style="width:200px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"> {{ movie.title }} </p>
            <div class="card-text"><small class="text-muted">{{ movie.release_date }}</small></div>
        </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name:'MovieListItem',
    props:{
        movie:{
            type:Object,
        }
    },
    methods:{
        ...mapActions(['movieDetail'])
    }

}
</script>

<style>
</style>