<template>
  <div>
      <h1>Search List</h1>
      <div>
        <input @keyup.enter="research(keyword)" v-model="keyword" type="text">
        <button @click="research(keyword)">Search</button>

        <div v-if="this.$store.state.movies.searchMovie">
          <h1>영화</h1>
        </div>
        <h2 v-else>'{{ this.$store.state.movies.searchKeyword }}' 검색어와 일치하는 영화가 없습니다.</h2>
      </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name:'SearchView',
    data: function () {
      return {
        keyword:'',
      }
    },
    methods: {
      ...mapActions(['research'])
    },

}
</script>

<style>

</style>