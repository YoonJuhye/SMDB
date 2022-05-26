<template>
  <div class="card" id="reviewCard">
    <div class="d-flex justify-content-around mx-3 my-4" v-if="isModal==false">

      <div class="card mx-2 col-2 profilecard" style="margin-top:30px;">
        <img v-if="Error==false" class="imgsize" :src="review.user.profile_img" @error="imgError">
        <img v-else class="imgsize" src="../../assets/people.png">

        <div class="d-flex justify-content-around">
          <h3>{{ review.user.username }} <span class="badge bg-secondary">{{ review.rank }}점</span></h3>
        </div>        
      </div>

      <div class="col-6 my-5">
        <h3 id="reviewtitle">{{ review.title }}</h3>
        <p class="my-3" id="reviewContent">{{ review.content }}</p>
      </div>


      <div class="col-2 d-flex profilecard">
        <div class="d-flex flex-column justify-content-between">
          <div>
            <div class="my-3">
              <label>게시일</label>
              <p>{{ review.created_at | moment('YYYY-MM-DD HH:mm')}}</p>
            </div>
    
            <div class="my-3">
              <label>수정일</label>
              <p>{{ review.updated_at | moment('YYYY-MM-DD HH:mm')}}</p>
            </div>
          </div>
            <div class="d-flex" v-if="this.$store.state.accounts.currentUser.username == review.user.username">
              <button style="background-color:rgba(190, 255, 255, 0.767);" @click="isModal=true" id="updelbutton">UPDATE</button>
              <button style="background-color:rgb(255, 175, 175);" @click="deleteReview(review)" id="updelbutton">DELETE</button>
            </div>
        </div>
      </div>

    </div>
       

      <div class="black-bg" v-if="isModal==true" id="updateReview">
        <div class="white-bg">
          <label>제목</label>
          <input class="form-control my-2" type="text" v-model="upReview.title">
          <label>내용</label>
          <input class="form-control my-2" type="text" v-model="upReview.content">
          <label>평가점수</label>
          <input class="my-3 form-control" v-model="upReview.rank" type="number" min="0" max="10">
          <div class="d-flex justify-content-end">
              <button style="background-color:rgba(190, 255, 255, 0.767);" id="updelbutton" @click="updateButton(upReview)">수정하기</button>
            <button style="background-color:rgb(255, 175, 175);" id="updelbutton" @click="isModal=false">취소</button>
          </div>
        </div>
      </div>


       <details class="mx-5 my-3" style="padding-inline:450px;">
          <summary @click="commentClick">댓글 ({{ review.comments.length }})</summary>
            <div v-if="review.comments.length">
              <comment-list v-for="comment in review.comments" :key="comment.pk" :comment="comment" />
            </div>
            <h4 v-else class="my-3">댓글이 없어요~</h4>
            <comment-form :reviewid="review.id" />
        </details>



  </div>
</template>

<script>
import { mapActions } from 'vuex'
import CommentForm from '../Comment/CommentForm.vue'
import CommentList from '../Comment/CommentList.vue'

export default {
  name : 'ReviewListItem',
  components:{
    CommentForm,CommentList
  },
  data(){
    return {
      isModal: false,
      upReview:{ 
                title : '',
                content: '',
                movie: '',
                rank : 0,
            },
      reviewComment:'',
      Error:false
    }
  },
  props:{
    review:{
      type:Object,
    }
  },
  methods:{
    ...mapActions(['deleteReview','updateReview','loadComment']),
    updateButton(upReview) {
      this.isModal=false
      this.updateReview(upReview)
    },
    commentClick() {

    },
    imgError: function(){
            this.Error = true
        }
  },
  created : function () {
    this.upReview = this.review
  }
}
</script>

<style>
#updateReview {
  padding: 30px;
}

#reviewCard{
  border-radius: 10px;
  border-left : thick solid #32a1ce;
}
#updelbutton {
  height: 30px;
  align-self: center;
  border: none;
  border-radius: 10px;
}

#reviewContent {
  border: solid 1px rgb(106, 185, 250);
  border-radius: 10px;

  height: 200px;
  padding: 10px;
}
.profilecard{
  align-self: center;
}
.imgsize{
  display:block;
	height:auto;
}
</style>