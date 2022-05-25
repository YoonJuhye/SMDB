<template>
  <div class="my-5">
      <hr>
      <div class="d-flex">
        <img v-if="movie.poster_path" class="card-img col-5" style="width:300px;" :src='`https://image.tmdb.org/t/p/w500/${movie.poster_path}`'>
        <div class="card-body col-5 my-1">
          <div class="my-3">

            <h2 class="card-title my-0 mx-2">{{ movie.title }}</h2>
            <div class="d-flex mx-3" style="margin:20px;">
              <h5 class="vote_ave text-center">{{ movie.vote_average }}</h5>
              <p class="date" style="padding-top:10px;">개봉일 : {{ movie.release_date }}</p>
            </div>

          </div>

          <div class="my-4 mx-3 ">
            <span class="mx-2" id="genre" v-for="genre in movie.genre_ids" :key="genre.pk">{{ genre.name }}</span>
          </div>
           <p class="my-1 mx-3 overview slimscroll">{{ movie.overview }}</p>
           <div class="mx-4 my-3">
            <h5>{{ this.$store.state.movies.likes }} 명이 이 영화를 좋아합니다.</h5>
            <button v-if="isLike==false" @click="iLike"> 좋아요 </button>
            <button v-if="isLike==true" @click="likecansle"> 좋아요취소 </button>
           </div>
           
        </div>
      </div>
       <hr>
    <review-form />
  </div>
 
</template>

<script>
import { mapActions } from 'vuex'
import ReviewForm from '../components/Review/ReviewForm.vue'

export default {
  name:'MovieDetail',
  components:{
    ReviewForm
  },
  data () {
    return{
      movie:[],
      isLike: false,
    }
  },
  methods:{
    ...mapActions(['loadReview','like']),
    iLike:function () {
      this.isLike = true
      this.like(this.movie.id)
    },
    likecansle:function (){
      this.isLike = false
      this.like(this.movie.id)
    }
  },
  created : function () {
    this.movie = this.$store.state.movies.movieDetail
    this.loadReview(this.movie.id)
    for (const likeuser of this.movie.like_users) {
      if (this.$store.state.accounts.currentUser.username == likeuser.username) {
        this.isLike = true
      }
    }
    
  },

  }

</script>

<style>
.vote_ave {
  background-color: #7ab1f8;
  border-radius: 10px;
  width: 60px;
  padding: 5px;
  align-self: center;
}
.date {
  margin-left:15px;

}
#genre {
  background-color: rgb(199, 247, 211);
  border-radius: 10px;
  padding: 7px;
}
.overview {
  border: solid 1px;
  height: 250px;
  border-radius: 10px;
  padding: 20px;
  overflow: scroll;
  overflow-x: hidden;
}

.slimscroll {
    overflow: auto;
}

.slimscroll::-webkit-scrollbar {
    width: 10px;
    height: 30px;
}

.slimscroll::-webkit-scrollbar-thumb {
    background-color: #B0B0B0;
    border-radius: 10px;
    background-clip: padding-box;
    border: 1px solid transparent;
}

.slimscroll::-webkit-scrollbar-track {
    background-color: white;
    border-radius: 10px;
    box-shadow: inset 0px 0px 3px white;
}
</style>