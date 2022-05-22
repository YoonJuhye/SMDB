<template>
  <div class="container">
      <h3 class="d-flex">인기 영화</h3>
      <div class="d-flex">
        <movie-list-item />
        <movie-list-item />
        <movie-list-item />
        <movie-list-item />
      </div>
      
  </div>
</template>

<script>
import MovieListItem from './MovieListItem.vue'
export default {
    name:'MovieList',
    components:{
        MovieListItem
    }
}
</script>

<style>

</style>