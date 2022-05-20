<template>
  <div class="container" style="height:2000px;">
    <movie-search-form class="my-3" />
    <movie-list class="my-3" />
    <movie-sort-list class="my-3" />
  </div>
</template>

<script>
import MovieSearchForm from '../components/MovieSearchForm.vue'
import MovieSortList from '../components/MovieSortList.vue'
import MovieList from '../components/MovieList.vue'
export default {
  name: 'HomeView',
  components: {
    MovieSearchForm, MovieSortList, MovieList
  }
}
</script>
