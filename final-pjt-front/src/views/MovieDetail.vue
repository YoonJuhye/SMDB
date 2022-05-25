<template>
  <div class="all-detail my-5">
      <div class="d-flex detailblock">
        <img v-if="movie.poster_path" class="card-img col-5" style="width:300px; border-radius: 20px;" :src='`https://image.tmdb.org/t/p/w500/${movie.poster_path}`'>
        <div class="card-body col-5 my-1">
          <div class="my-3">

            <h2 class="card-title mx-2">{{ movie.title }} ({{ movie.release_date | moment('YYYY')}})</h2>
            <dir style="padding:5px;">
              <small class="mx-2" v-for="genre in movie.genre_ids" :key="genre.pk">{{ genre.name }}</small>
            </dir>
            
            <div class="my-4 mx-3 ">
            </div>
            <div class="d-flex mx-3" style="margin:20px;">
              <h5 class="vote_ave text-center">{{ movie.vote_average }}</h5>
            </div>
          </div>
           <p class="my-1 mx-3 overview slimscroll">{{ movie.overview }}</p>
           <div class="d-flex mx-2 my-3">
            <button class="likebutton" v-if="isLike==false" @click="iLike"><font-awesome-icon class="fa-2x" style="color:rgb(111, 112, 111);" icon="fa-solid fa-thumbs-up"></font-awesome-icon></button>
            <button class="likebutton" v-if="isLike==true" @click="likecansle"><font-awesome-icon class="fa-2x" style="color:#7ab1f8;" icon="fa-solid fa-thumbs-up" /></button>
            <h5 class="my-3 mx-3">{{ this.$store.state.movies.likes }} 명이 이 영화를 좋아합니다.</h5>
           </div>
           
        </div>
      </div>
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

.all-detail {
  padding: 0 50px 0 50px;
}

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
.overview {
  height: 250px;
  border-radius: 10px;
  padding-block: 30px;
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
.detailblock {
  border-radius: 20px;
  background-color: #e3f2fd;
  box-shadow: 5px 5px 5px 5px rgba(172, 172, 172, 0.384);
}

.likebutton{
  background-color: #e3f2fd;
  border: none;
}
</style>