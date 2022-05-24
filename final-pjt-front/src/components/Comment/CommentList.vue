<template>
    <div class="d-flex align-items-center">
        <div class="col-10 mx-2 my-2 d-flex justify-content-between" id="comments"> 
            <h5>{{ comment.content }}</h5>
            <p style="margin-bottom:0;">{{ comment.user.username }}</p>
        </div>

        <button v-if="comment.user.username==this.$store.state.accounts.currentUser.username" type="button" class="btn-close"></button>
    </div>
   
</template>

<script>

export default {
    name:'CommentList',
    props:{
        comment:{
            type:Object,
        }
    }
}
</script>

<style>
#comments {
    background-color: rgb(234, 218, 247);
    border-radius: 10px;
    align-items: center;
    padding-inline: 20px;

}
</style>