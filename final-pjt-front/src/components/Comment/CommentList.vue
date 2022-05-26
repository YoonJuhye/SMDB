<template>
    <div class="d-flex">
        <div v-if="isCommentModal==false" class="comment-lst col-10 mx-2 my-2 d-flex justify-content-between" id="comments"> 
            <h5 class="mx-3 my-3">{{ comment.content }}</h5>
            <p style="margin-bottom:0;">{{ comment.user.username }}</p>
        </div>
            
        
            
        <div v-if="isCommentModal==true" class="comment-lst col-11 mx-2 my-2" id="upCommentID">
            <div>
                <input type="text" class="form" id="updateForm" v-model="upComment.content">
            </div>
        </div>

        <div class="d-flex align-items-center" v-if="isCommentModal==false">
            <button class="updatebutton commentbutton" @click="updateCommentbutton" v-if="comment.user.username==this.$store.state.accounts.currentUser.username">수정</button>
            <button id="cancle" @click="deleteComment(comment)" v-if="comment.user.username==this.$store.state.accounts.currentUser.username" type="button" class="commentbutton">삭제</button>
        </div>
        <div class="d-flex align-items-center" v-if="isCommentModal==true" style="">
            <button @click="updateComment(upComment)" class="updatebutton commentbutton">수정</button>
            <button class="commentbutton" id="cancle" @click="isCommentModal=false">취소</button>
        </div>
        
    </div>
   
</template>

<script>
import { mapActions } from 'vuex'
export default {
    name:'CommentList',
    data () {
        return {
            isCommentModal: false,
            upComment:{
                content:'',
            }
        }
    },
    props:{
        comment:{
            type:Object,
        }
    },
    methods:{
        ...mapActions(['deleteComment','updateComment']),
        updateCommentbutton: function () {
            this.isCommentModal = true
            this.upComment = this.comment
        }
    }
}
</script>

<style>
#comments {
    background-color:#f8f8fa;

    border-radius: 10px;
    width: 505px;
    align-items: center;
    padding-inline: 20px;

}
#upCommentID {
    background-color: rgb(221, 234, 247);
    padding: 10px;
    border-radius: 10px;
}
#updateForm {
    border : none;
    background-color:rgb(221, 234, 247);
}

.updatebutton {
    background-color: #292961;
    color: white;
    border : none;
    border-radius: 10px;
}
#cancle {
    background-color: rgb(255, 255, 255);
    color: #292961;
    border: solid 1px;
    border-color: #292961;
    border-radius: 10px;
    /* border: none; */
}
.commentbutton{
    width: 60px;
    height: 30px;
}
.form {
    border-radius: 10px;
    border: solid 1px;
    width: 500px;
    margin-right: 10px;
}
</style>