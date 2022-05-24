<template>
  <div>
      <div>
        <h1>Review</h1>
        <h3>사용자 평점</h3>
      </div>
    
      <div class="d-flex justify-content-between my-3">
        <review-list class="col-7" />
        <form class="col-3 form-control my-5" id="reviewform">
          <h2 class="my-3">리뷰 작성</h2>
          <h4>제목</h4>
          <input class="my-3 form-control" v-model="newReview.title" type="text"><br>
          <h4>내용</h4>
          <textarea v-model="newReview.content" class="form-control" name="" id="" cols="30" rows="10"></textarea><br>
          <button @click="create(newReview)" class="form-control">제출하기</button>
        </form>
        <div class="col1">
        </div>
      </div>
    
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import ReviewList from './ReviewList.vue'

export default {
    name:'ReviewForm',
    data () {
        return {
            movie_pk:'',
            newReview:{
                title : '',
                content: '',
                movie: '',
                rank : 0,
            }
        }
    },
    components:{
        ReviewList
    },
    methods:{
        ...mapActions(['createReview']),
        create(newReview) {
            this.createReview(newReview)
        }
    },
    created () {
        this.movie_pk = this.$store.state.movies.movie_pk
        this.newReview.movie = this.$store.state.movies.movie_pk
    },
    
}
</script>

<style>
#reviewform {
    width: 400px;
    border-radius: 10px;
    height: 100%;
    margin-right: 50px;
}
</style>