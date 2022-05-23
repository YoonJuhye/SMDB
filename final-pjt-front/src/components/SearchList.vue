<template>
  <div class="my-5" id="search_card">
      <div class="d-flex">
      <img style="width:150px; border-radius: 10px;" :src='`https://image.tmdb.org/t/p/w500/${movie.poster_path}`'>
      <div class="mx-5 my-4">
          <h3>{{ movie.title }}</h3>
          <small style="color: #999;">{{ movie.release_date }}</small>
          <p class="my-5">{{ movie.overview }}</p>
      </div>
  </div>
  </div>
</template>

<script>
export default {
    name:'SearchList',
    props:{
        movie:{
            type:Object,
        }
    }

}
</script>

<style>
#search_card {
    border:2px solid rgba(95, 167, 201, 0.24);
    box-shadow: 2px 2px 3px;
    border-radius: 10px;
}
</style>