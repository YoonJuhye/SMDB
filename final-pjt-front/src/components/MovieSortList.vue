<template>
  <div>
      <h3 class="d-flex">Movie Sort List</h3>
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
    name:'MovieSortList',
    components:{
        MovieListItem
    }
}
</script>

<style>

</style>