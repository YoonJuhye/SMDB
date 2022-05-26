<template>
  <div @click="movieDetail(movie.id)" class="my-5" id="search_card">
      <div class="d-flex">
      <img v-if="movie.poster_path" style="width:200px;" :src='`https://image.tmdb.org/t/p/w500/${movie.poster_path}`' alt="#">
      <div class="mx-4 my-4">
          <h3>{{ movie.title }}</h3>
          <small style="color: #999;">{{ movie.release_date }}</small>
          <p class="my-5">{{ movie.overview }}</p>
      </div>
  </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
    name:'SearchList',
    props:{
        movie:{
            type:Object,
        }
    },
    methods:{
        ...mapActions(['movieDetail'])
    }

}
</script>

<style>
#search_card {
    font-family: "Noto Sans KR", sans-serif;
    background-color: #343a40;
    border-width : solid 1px;
    border-color: #212223;
    color: #ffffff;

    box-shadow: 10px 10px 7px -8px rgba(0,0,0,0.6);
}

h3 {
    font-family: "Noto Sans KR", sans-serif;
    font-weight: 700;
}
</style>