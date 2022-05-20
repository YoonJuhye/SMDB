<template>
  <div>
      <h1>Movie Sort List</h1>
      <movie-list-item />
  </div>
</template>

<script>
import MovieListItem from './MovieListItem.vue'

export default {
    name:'MovieSortList',
    components:{
        MovieListItem
    }
}
</script>

<style>

</style>