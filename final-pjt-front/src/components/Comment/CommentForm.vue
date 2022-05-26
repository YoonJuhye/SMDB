<template>
  <div class="d-flex" style="padding-inline:10px;">
      <input @keyup.enter="createCommentbutton()" class="form" type="text" v-model="comment.content">
      <button class="button" @click="createCommentbutton()">작성</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
    name:'CommentForm',
    props: {
        reviewid:{
            type:Number,
        }
    },
    methods:{
        ...mapActions(['createComment']),
        createCommentbutton: function () {
            this.comment.review = this.reviewid
            this.createComment(this.comment)
            
        }
    },
    data () {
        return {
            comment:{
                content:'',
                review:'',
            }
        }
    },

}
</script>

<style>
.form {
    
    border-radius: 10px;
    border: solid 1px;
    margin-right: 10px;
}
.button {
    padding-inline: 30px;
    border: none;
    border-radius: 10px;
    background-color: #292961;
    color: white;
}
</style>