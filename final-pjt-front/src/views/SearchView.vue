<template>
  <div class="container">

      <div class="d-flex ms-4" style="padding-top:30px;">
        <input v-model="keyword" @keyup.enter="research(keyword)" class="col-10" type="text" id="searchInput" placeholder="영화를 검색하세요." aria-label="영화를 검색하세요." aria-describedby="searchButton">
        <button @click="research(keyword)" class="col-2 btn btn-outline-secondary fw-bold" type="button" id="searchButton">Search</button>
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
import SearchList from '../components/Movie/SearchList.vue'

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