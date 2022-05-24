<template>
  <div>
    <movie-search-form class="my-3" />
    <movie-list class="my-5" />
    <movie-sort-list class="my-5" />
  </div>
</template>

<script>
import MovieSearchForm from '../components/MovieSearchForm.vue'
import MovieSortList from '../components/MovieSortList.vue'
import MovieList from '../components/MovieList.vue'

import { mapActions } from 'vuex'

export default {
  name: 'HomeView',
  components: {
    MovieSearchForm, MovieSortList, MovieList
  },
  methods:{
    ...mapActions(['fetchCurrentUser'])
  },
  created: function(){
    this.fetchCurrentUser()
  }
}
</script>
