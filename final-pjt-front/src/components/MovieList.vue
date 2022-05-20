<template>
  <div>
      <h1>현재 인기있는 영화</h1>
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