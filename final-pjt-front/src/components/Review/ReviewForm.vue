<template>
  <div class="my-5 reviewblock">
        <h1 class="mx-4">Review <span class="badge bg-secondary">{{ this.$store.state.reviews.rank }}점</span></h1>

    
      <div class="d-flex my-3 justify-content-around">
        <review-list class="col-7" />
        <form class="col-2 form-control my-5 mx-5" id="reviewform">
          <h2 class="my-3">리뷰 작성</h2>
          <h4>제목</h4>
          <input class="my-3 form-control" v-model="newReview.title" type="text"><br>
          <h4>평가점수</h4>
          <input class="my-3 form-control" v-model="newReview.rank" type="number" min="0" max="10">
          <h4>내용</h4>
          <textarea v-model="newReview.content" class="form-control" name="" id="" cols="30" rows="10"></textarea><br>
          <button @click="createForm(newReview)" class="form-control">제출하기</button>
        </form>
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
            average:'',
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
        createForm(newReview) {
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
}
.reviewblock {
    border: solid 1px;
    box-shadow: 5px 5px 5px 5px rgba(172, 172, 172, 0.384);
    border-radius: 20px;
}
</style>