<template>
  <div>
      <h1>Details</h1>

      <hr>
      <div class="d-flex">
        <img v-if="movie.poster_path" class="card-img col-5" style="width:300px;" :src='`https://image.tmdb.org/t/p/w500/${movie.poster_path}`'>
        <div class="card-body col-5">
          <h3 class="card-title">{{ movie.title }}</h3>
          <p>{{ movie.release_date }}</p>
          <p>{{ movie.overview }}</p>
          <span class="mx-2" v-for="genre in movie.genre_ids" :key="genre.pk">{{ genre.name }}</span>
          <p></p>
        </div>
      </div>
       <hr>
    <review-list />
  </div>
 
</template>

<script>
import ReviewList from '../components/ReviewList.vue'

export default {
  name:'MovieDetail',
  components:{
    ReviewList
  },
  data () {
    return{
      movie:[],
    }
  },
  created : function () {
    this.movie = this.$store.state.movies.movieDetail
    
  },

  }

</script>

<style>

</style>