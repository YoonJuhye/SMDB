<template>
  <div>
    <movie-search-form class="" />
    <movie-list class="my-5" />
    <movie-sort-list class="my-5" />
  </div>
</template>

<script>
import MovieSearchForm from '../components/Movie/MovieSearchForm.vue'
import MovieSortList from '../components/Movie/MovieSortList.vue'
import MovieList from '../components/Movie/MovieList.vue'

import { mapActions } from 'vuex'

export default {
  name: 'HomeView',
  components: {
    MovieSearchForm, MovieSortList, MovieList
  },
  methods:{
    ...mapActions(['fetchCurrentUser'])
  },
}
</script>
