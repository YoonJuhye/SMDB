<template>
  <div>
        <div class="box">
          <h1 class="mx-5 my-5">내가 좋아하는 영화</h1>
          <like-movie class="mx-5 my-5" v-for="movie in this.$store.state.accounts.profile.like_movies" :key="movie.pk" :movie="movie" />
        </div>
        <div class="box">
            <h1 class="mx-5 my-5">내가 쓴 글</h1>
            <review-list-item class="mx-5 my-5" v-if="review" :review="review" />
            <table class="table table-striped">
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
        
  </div>
</template>

<script>
import LikeMovie from '../components/LikeMovie.vue'
import MyArticle from '../components/MyArticle.vue'
import ReviewListItem from '@/components/Review/ReviewListItem.vue'

import { mapActions,mapGetters } from 'vuex'
import router from '@/router'

export default {
    name:'MyPageView',
    data () {
        return {
            review:'',
        }
    },
    components:{
        LikeMovie,MyArticle, ReviewListItem,
    },
    methods: {
    ...mapActions(['fetchProfile','my_Review']),
    ...mapGetters(['isLoggedIn']),
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
        if (this.$store.state.accounts.currentUser) {
        const myname = this.$store.state.accounts.currentUser.username
        const myPk =this.$store.state.accounts.currentUser.pk
        this.fetchProfile(myname)
        this.my_Review(myPk)
        } else {
            alert('로그인을 해주세요!')
            router.push({ name: 'login' })
        }
        
    
    }
}
</script>

<style>
.box {
    border : solid 1px;
    border-radius: 10px;
    margin-block: 40px;
    padding-inline: 50px;
}
</style>