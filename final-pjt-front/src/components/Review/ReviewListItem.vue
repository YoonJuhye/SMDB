<template>
  <div class="card" id="reviewCard">
    <div class="d-flex justify-content-between mx-4 my-4" v-if="isModal==false">
      <div class="col-6">
        <h3 class="mx-3" id="reviewtitle">{{ review.title }}</h3>
        
        <p class="mx-3" id="reviewContent">{{ review.content }}</p>


        <details>
          <summary @click="commentClick">댓글</summary>
            <div>
              <comment-list :reviewComment="reviewComment" />
              <comment-form :reviewComment="reviewComment" />
            </div>
          </details>
      </div>
   
      <div class="col-5 d-flex justify-content-between">
        <div>
          <h3>작성자 : {{ review.user.username }}</h3>
          <p>평가점수 : {{ review.rank }}점</p>
        </div>

        <div>
          <div>
            <label>게시일</label>
            <p>{{ review.created_at }}</p>
          </div>
  
          <div>
            <label>수정일</label>
            <p>{{ review.updated_at }}</p>
          </div>

          <div class="d-flex">
            <div class="align-self-center" v-if="this.$store.state.accounts.currentUser.username == review.user.username">
              <button @click="isModal=true" id="updelbutton">UPDATE</button>
              <button @click="deleteReview(review)" id="updelbutton">DELETE</button>
            </div>
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
          <button @click="updateButton(upReview)">수정하기</button>
          <button @click="isModal=false">취소</button>
        </div>

      </div>
      
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
    }
  },
  props:{
    review:{
      type:Object,
    }
  },
  methods:{
    ...mapActions(['deleteReview','updateReview']),
    updateButton(upReview) {
      this.isModal=false
      this.updateReview(upReview)
    },
    commentClick() {
      this.reviewComment = this.review.id
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
}

#reviewContent {
  border: solid 1px rgb(106, 185, 250);
  border-radius: 10px;

  height: 150px;
  padding: 10px;
}
</style>