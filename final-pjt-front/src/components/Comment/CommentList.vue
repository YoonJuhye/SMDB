<template>
  <div v-if="this.$store.state.reviews">
      <div v-for="comment in this.$store.state.reviews.reviews[0].comments" :key="comment.id">
          <p>{{ comment }}</p>
      </div>
  </div>
  <h3 v-else> 댓글이 없어요~ </h3>
</template>

<script>
export default {
    name:'CommentList'
}
</script>

<style>

</style>