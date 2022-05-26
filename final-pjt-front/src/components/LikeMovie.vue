<template>
  <div>
      <div class="likecard d-flex flex-column align-items-center justify-content-between" style="width:200px; height:375px;">
          <img @click="goDetail" class="likeimg" :src='`https://image.tmdb.org/t/p/w500/${movie.poster_path}`' alt="#">
          <h6 class="mx-2 liketitle align-items-center text-center">{{ movie.title }}</h6>
          <button @click="deletebutton" class="mx-3 btn-close"></button>
      </div>
  </div>
</template>

<script>
import router from '@/router'
import { mapActions } from 'vuex'

export default {
    name:'LikeMovie',
    props :{
        movie:{
            type:Object,
        }
    },
    methods:{
        ...mapActions(['like','loadReview','movieDetail']),
        deletebutton: function () {
            this.like(this.movie.pk)
            router.go()
        },
        goDetail: function () {
            this.loadReview(this.movie.pk)
            this.movieDetail(this.movie.pk)
        }
    }
}
</script>

<style>
.likecard {
    border: solid 1px;
    border-radius: 10px;
    /* -webkit-box-shadow: -9px -16px 36px 0px rgba(99,110,168,1);
    -moz-box-shadow: -9px -16px 36px 0px rgba(99,110,168,1);
    box-shadow: -9px -16px 36px 0px rgba(99,110,168,1); */
}
.liketitle{
    display: inherit;
    overflow:hidden; 
    text-overflow:ellipsis;
}
.likeimg{
    width:200px;
    height: 300px;
    object-fit: cover; 
    border-radius: 10px 10px 0 0;
}
</style>