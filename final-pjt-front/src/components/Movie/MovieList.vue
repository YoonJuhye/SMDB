<template>
  <div class="all-popular">
      <h3 class="popular-title d-flex mx-3 my-3">인기 영화</h3>
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
@import url(//fonts.googleapis.com/earlyaccess/notosanskr.css);


.all-popular {
  padding: 0 50px 0 50px;
}

.popular-title {
  font-family: "Noto Sans KR", sans-serif;
  font-weight: 700;
}

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
    /* background-color: #B0B0B0; */
    background-image: linear-gradient(180deg, #6212a3 0%, #708ad4 99%);
    box-shadow: inset 2px 2px 5px 0 rgba(#fff, 0.5);
    border-radius: 10px;
    background-clip: padding-box;
    border: 2px solid transparent;
}

.slimscroll::-webkit-scrollbar-track {
    /* background-color: white; */
    background-color: #e4e4e4;
    border-radius: 10px;
    box-shadow: inset 0px 0px 3px white;
}
</style>