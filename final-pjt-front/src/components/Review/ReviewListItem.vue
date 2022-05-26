<template>
  <div class="card" id="reviewCard">
    <div class="d-flex justify-content-around mx-3" v-if="isModal==false">

      <div class="card mx-2 col-2 profilecard" style="margin-block:30px;">
        <img v-if="Error==false" class="imgsize" :src="review.user.profile_img" @error="imgError">
        <img v-else class="imgsize" src="../../assets/people.png">

        <div class="d-flex justify-content-around">
          <h3>{{ review.user.username }} <span class="badge bg-secondary">{{ review.rank }}점</span></h3>
        </div>        
      </div>

      <div class="column col-6 my-5">
        <h3 id="reviewtitle">{{ review.title }}</h3>
        <p class="my-3" id="reviewContent">{{ review.content }}</p>
        
        <details class="mx-3 my-3">
            <summary>댓글 ({{ review.comments.length }})</summary>
              <div v-if="review.comments.length">
                <comment-list v-for="comment in review.comments" :key="comment.pk" :comment="comment" />
              </div>
              <h5 v-else class="my-3 ms-3">댓글을 작성해주세요.</h5>
              <comment-form :reviewid="review.id" />
          </details>
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
              <button @click="tryupdate" id="updelbutton">수정</button>
              <button @click="deleteReview(review)" id="delbutton">삭제</button>
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
          <input class="my-3 form-control" v-model="upReview.rank" type="number" min=0 max=10>
          <div class="d-flex justify-content-end">
              <button id="updelbutton" @click="updateButton(upReview)">수정하기</button>
            <button style="background-color:rgb(255, 175, 175);" id="updelbutton" @click="isModal=false">취소</button>
          </div>
        </div>
      </div>



  </div>
</template>

<script>
import router from '@/router'
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
      if (upReview.rank > 10 || upReview.rank < 0){
        alert('0~10점까지만 입력해주세요.')
        router.go()
      }else{
        this.isModal=false
        this.updateReview(upReview)
      }


      
    },
    tryupdate: function () {
      this.upReview=this.review
        this.isModal=true
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
  border-radius: 0px;
  /* border-left : thick solid #32a1ce; */
}
#updelbutton {
  background-color: #292961;
  color: white;
  border : none;
  border-radius: 10px;
}

#delbutton {
  background-color: rgb(255, 255, 255);
  color: #292961;
  border: solid 1px;
  border-color: #292961;
  border-radius: 10px;
}

#reviewContent {
  border: solid 1px #5f0080;
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