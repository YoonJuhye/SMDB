<template>
  <div>
      <my-profile />
      <div>
          <h1>내가 좋아하는 영화</h1>
          <like-movie v-for="movie in this.$store.state.accounts.profile.like_movies" :key="movie.pk" :movie="movie" />
      </div>
        <div>
            <h1>내가 쓴 글</h1>
            
        </div>
        <review-list-item v-if="review" :review="review" />
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">영화제목</th>
                    <th scope="col">제목</th>
                    <th scope="col">작성시간</th>
                </tr>
            </thead>
            <tbody>
                <my-article @select-table="busSave" v-for="review in this.$store.state.movies.myarticle" :key="review.pk" :review="review"/>
            </tbody>
        </table>
  </div>
</template>

<script>
import MyProfile from '../components/MyProfile.vue'
import LikeMovie from '../components/LikeMovie.vue'
import MyArticle from '../components/MyArticle.vue'
import ReviewListItem from '@/components/Review/ReviewListItem.vue'

import { mapActions } from 'vuex'

export default {
    name:'MyPageView',
    data () {
        return {
            review:'',
        }
    },
    components:{
        MyProfile, LikeMovie,MyArticle,
        ReviewListItem,
    },
    methods: {
    ...mapActions(['fetchProfile','my_Review']),
    busSave : function(review) {
        console.log(review)
        if (this.review.id == review.id) {
            this.review = 0
        } else{
            this.review = review
        }

    }
    },
    created() {
        const myname = this.$store.state.accounts.currentUser.username
        const myPk =this.$store.state.accounts.currentUser.pk
        this.fetchProfile(myname)
        this.my_Review(myPk)
    
    }
}
</script>

<style>

</style>