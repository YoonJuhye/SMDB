<template>
  <div class="container">
      <h1>Search List</h1>
      <div class="my-3">
        <input @keyup.enter="research(keyword)" v-model="keyword" type="text">
        <button @click="research(keyword)">Search</button>
        </div>
        
        <div v-if="this.$store.state.movies.searchMovies">
          <search-list v-for="movie in this.$store.state.movies.searchMovies"
           :key="movie.id" :movie="movie" />
        </div>
        <h2 class="my-5" v-else>'{{ this.$store.state.movies.searchKeyword }}' 검색어와 일치하는 영화가 없습니다.</h2>
      
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import SearchList from '../components/SearchList.vue'

export default {
    name:'SearchView',
    components:{
      SearchList
    },
    data: function () {
      return {
        keyword:'',
        searchMovies: null,
      }
    },
    methods: {
      ...mapActions(['research'])
    },

}
</script>

<style>

</style>