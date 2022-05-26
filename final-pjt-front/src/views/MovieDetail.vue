<template>
  <div class="all-detail">
      <div class="d-flex detailblock text-white bg-dark">
        <div class="card-body col-5 my-1 ms-3 mt-3">
          <div>
            <p class="card-title detail-title mx-2">{{ movie.title }} ({{ movie.release_date | moment('YYYY')}})</p>
            <dir style="padding:5px;">
              <span class="mx-2 genrename" v-for="genre in movie.genre_ids" :key="genre.pk">#{{ genre.name }}</span>
            </dir>
            
            <div class="mx-3 ">
            </div>
            <div class="d-flex mx-3" style="">
              <h5 class="vote_ave text-center">{{ movie.vote_average }}</h5>
            </div>
          </div>
           <p v-if="movie.overview" class="my-1 mx-3 overview slimscroll">{{ movie.overview }}</p>
           <p v-else class="my-1 mx-3 overview slimscroll">줄거리 정보가 존재하지 않습니다.</p>
           <div class="d-flex mx-2">
            <button class="likebutton mb-1" v-if="isLike==false" @click="iLike"><font-awesome-icon class="fa-2x" style="color:white;" icon="fa-solid fa-thumbs-up"></font-awesome-icon></button>
            <button class="likebutton mb-1" v-if="isLike==true" @click="likecansle"><font-awesome-icon class="fa-2x" style="color:#007bff;" icon="fa-solid fa-thumbs-up" beat /></button>
            <h5 class="my-3">{{ this.$store.state.movies.likes }} 명이 이 영화를 좋아합니다.</h5>
           </div>
           
        </div>
        <img v-if="movie.poster_path" class="card-img col-5" style="width:370px;" :src='`https://image.tmdb.org/t/p/w500/${movie.poster_path}`'>
      </div>
    <review-form  />
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
  font-family: "Noto Sans KR", sans-serif;
  padding: 0 50px 0 50px;
}

.detail-title {
  font-family: "Noto Sans KR", sans-serif;
  font-weight: 700;
  font-size: 32px;
}

.genrename {
  /* background-color: rgb(255, 255, 255);
  border-radius: 20px;
  width: 60px; */
  font-size: 18px;
  color: white;
  padding: 5px;
  align-self: center;
}

.vote_ave {
  background-color: rgba(255, 255, 255, 0.879);
  color: black;
  border-radius: 20px;
  width: 60px;
  padding: 5px;
  align-self: center;
}
.date {
  margin-left:15px;

}
.overview {
  font-weight: 400;
  height: 280px;
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
  /* border-radius: 20px; */
  background-color: #dedede;
  border-width : solid 1px;
  border-color: #212223;
  color: #04040b;
  /* box-shadow: 5px 5px 5px 5px rgba(172, 172, 172, 0.384); */
}

.likebutton{
  background: none;
  border: none;
}
</style>