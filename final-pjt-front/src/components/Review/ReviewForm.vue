<template>
  <div class="my-5 reviewblock">
        <h1 class="mx-4">Review <span class="badge bg-secondary">{{ this.$store.state.reviews.rank }}점</span></h1>
      <div class="cloumn my-3 justify-content-around">

        <form class="form-control" id="reviewform">
          <h2 class="my-3">리뷰 작성</h2>
          <h5>제목</h5>
          <input class="my-3 form-control" v-model="newReview.title" type="text">
          <h5>평점</h5>
          <input class="my-3 form-control" v-model="newReview.rank" type="number" min="0" max="10">
          <h5>내용</h5>
          <textarea v-model="newReview.content" class="form-control" cols="30" rows="5"></textarea><br>
          <button @click="createForm(newReview)" class="form-control">제출하기</button>
        </form>

        <review-list />
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
            if (this.$store.state.reviews.reviews){
            for (const review of this.$store.state.reviews.reviews) {
                if (review.user.username == this.$store.state.accounts.currentUser.username) {

                    alert('이 영화에 이미 리뷰를 작성하셨습니다!')
                    return
                }
            }
            this.createReview(newReview)
            } else {
                this.createReview(newReview)
            }
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
    border-radius: 0px;

}
.reviewblock {
    /* border: solid 1px; */
    /* box-shadow: 5px 5px 5px 5px rgba(172, 172, 172, 0.384); */
    border-radius: 0px;
    padding: 30px;
}
</style>