<template>
  <div>
      <input type="text" v-model="comment.content">
      <button @click="createCommentbutton(comment)">작성</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
    name:'CommentForm',
    props: {
        reviewComment:{
            type:Number,
        }
    },
    methods:{
        ...mapActions(['createComment']),
        createCommentbutton: function (content) {
            this.comment.review = this.reviewComment
            this.createComment(content)
            
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

</style>