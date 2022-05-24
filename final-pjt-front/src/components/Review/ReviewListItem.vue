<template>
  <div class="card">
    <div v-if="isModal==false">
      <h3 id="reviewtitle">{{ review.title }}</h3>
      <p>{{ review.rank }}점</p>
      <p id="reviewContent">{{ review.content }}</p>
      <p>{{ review.created_at }}</p>
      <p>{{ review.updated_at }}</p>
      <p type=""></p>
      <div>
        <button @click="isModal=true">UPDATE</button>
        <button @click="deleteReview(review)">DELETE</button>
      </div>
    </div>
      
      
      <div class="black-bg" v-if="isModal==true" id="updateReview">
        <div class="white-bg">
          <label>제목</label>
          <input class="form-control my-2" type="text" v-model="upReview.title">
          <label>내용</label>
          <input class="form-control my-2" type="text" v-model="upReview.content">
          <button @click="updateButton(upReview)">수정하기</button>
        </div>

      </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name : 'ReviewListItem',
  data(){
    return {
      isModal: false,
      upReview:{
                title : '',
                content: '',
                movie: '',
                rank : 0,
            },
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
</style>