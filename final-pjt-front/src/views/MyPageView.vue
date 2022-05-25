<template>
  <div class="all-mypage">
        <div class="box">
          <h1 class="mx-5 my-5 text-center underline">내가 좋아하는 영화</h1>
          <div class="d-flex slimscroll">
              <like-movie class="mx-5 my-5" v-for="movie in this.$store.state.accounts.profile.like_movies" :key="movie.pk" :movie="movie" />
          </div>
        </div>
        <hr>
        <div class="box">
            <h1 class="mx-5 my-5 text-center">내가 쓴 글</h1>
            <review-list-item class="mx-5 my-5" v-if="review" :review="review" />
            <div class="d-flex justify-content-around">
                <h3 class="text-center" style="width:500px;">영화</h3>
                <h3 class="text-center" style="width:500px;">제목</h3>
                <h3 class="text-center" style="width:500px;">작성시간</h3>
            </div> 
            <hr>
            <my-article class="my-3 articlebox" @select-table="busSave" v-for="review in this.$store.state.movies.myarticle" :key="review.pk" :review="review"/>
            
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
.underline{
    text-decoration: underline;
    text-underline-position: under;
    text-decoration-thickness : 1px
}
.all-mypage {
  padding: 0 50px 0 50px;
}

.box {
    border-inline: solid 1px;
    margin-block: 40px;
    padding-inline: 30px;
}

.slimscroll {
    overflow: auto;
}

.slimscroll::-webkit-scrollbar {
    width: 60px;
    height: 10px;
}

.slimscroll::-webkit-scrollbar-thumb {
    /* background-color: #B0B0B0; */
    background-image: linear-gradient(180deg, #6212a3 0%, #708ad4 99%);
    box-shadow: inset 2px 2px 5px 0 rgba(#fff, 0.5);
    border-radius: 10px;
    background-clip: padding-box;
    border: 2px solid transparent;
}

.slimscroll::-webkit-scrollbar-track {
    /* background-color: white; */
    background-color: #e4e4e4;
    border-radius: 10px;
    box-shadow: inset 0px 0px 3px white;
}
.articlebox {
    background-color: rgb(195, 247, 247);
    border-radius: 10px;
    padding: 10px 0px 10px 0px;
    color: rgb(0, 0, 0);
}
</style>