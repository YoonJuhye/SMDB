<template>
  <div>
      <div class="my-3 likecard d-flex align-items-center justify-content-between">
          <img style="width:70px; border-radius: 10px;" :src='`https://image.tmdb.org/t/p/w500/${movie.poster_path}`' alt="#">
          <h3 class="mx-5">{{ movie.title }}</h3>
          <button @click="deletebutton" class="mx-3">좋아요 취소</button>
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
        ...mapActions(['like']),
        deletebutton: function () {
            this.like(this.movie.pk)
            router.go()
        }
    }
}
</script>

<style>
.likecard {
    border: solid 1px;
    border-radius: 10px;
    width: 500px;
}
</style>