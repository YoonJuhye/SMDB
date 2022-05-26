<template>
  <div class="my-5 reviewblock">
        <h1 class="mx-4">Review <span class="badge bg-secondary">{{ this.$store.state.reviews.rank }}점</span></h1>
      <div class="cloumn my-3 justify-content-around">

        <form class="form-control" id="reviewform">
          <h2 class="my-3">리뷰 작성</h2>
          <h4>제목</h4>
          <input class="my-3 form-control" v-model="newReview.title" type="text"><br>
          <h4>평가점수</h4>
          <input class="my-3 form-control" v-model="newReview.rank" type="number" min="0" max="10">
          <h4>내용</h4>
          <textarea @keyup.enter="createForm(newReview)" v-model="newReview.content" class="form-control" cols="30" rows="10"></textarea><br>
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
    border-radius: 10px;

}
.reviewblock {
    border: solid 1px;
    box-shadow: 5px 5px 5px 5px rgba(172, 172, 172, 0.384);
    border-radius: 20px;
    padding: 30px;
}
</style>