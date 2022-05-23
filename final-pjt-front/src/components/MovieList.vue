<template>
  <div class="container">
      <h3 class="d-flex mx-3 my-3">인기 영화</h3>
      <div class="slimscroll" id='popular'>
        <movie-list-item style="display: inline-block;" v-for="movie in movies" :key="movie.pk" :movie="movie" />
      </div>
      
  </div>
</template>

<script>
import MovieListItem from './MovieListItem.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
    name:'MovieList',
    components:{
        MovieListItem
    },
    computed: {
      ...mapGetters(['movies'])
    },
    methods: {
      ...mapActions(['fetchMovies'])
    },
    created() {
      this.fetchMovies()
    },
}
</script>

<style>
#popular {
  overflow-x: scroll;
  overflow-y: hidden;
  white-space: nowrap;
}
.slimscroll {
    overflow: auto;
}

.slimscroll::-webkit-scrollbar {
    width: 60px;
    height: 10px;
}

.slimscroll::-webkit-scrollbar-thumb {
    background-color: #B0B0B0;
    border-radius: 10px;
    background-clip: padding-box;
    border: 2px solid transparent;
}

.slimscroll::-webkit-scrollbar-track {
    background-color: white;
    border-radius: 10px;
    box-shadow: inset 0px 0px 3px white;
}
</style>