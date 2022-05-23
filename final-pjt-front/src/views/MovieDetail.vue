<template>
  <div>
      <h1>Details</h1>
      <p>{{ this.$store.state.movies.movieDetail }}</p>
      <hr>
      <div class="d-flex">
        <img v-if="movie.poster_path" class="card-img col-5" style="width:300px;" :src='`https://image.tmdb.org/t/p/w500/${movie.poster_path}`'>
        <div class="card-body col-5">
          <h3 class="card-title">{{ movie.title }}</h3>
          <p>{{ movie.overview }}</p>

        </div>
      </div>
  </div>
</template>

<script>
export default {
  name:'MovieDetail',
  data () {
    return{
      movie:[],
    }
  },
  created : function () {
    this.movie = this.$store.state.movies.movieDetail
    console.log(this.movie)
  },

  }

</script>

<style>

</style>