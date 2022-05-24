<template>
  <div class="card">
      <h3>{{ review.title }}</h3>
      <p>{{ review.content }}</p>
      <p>{{ review.created_at }}</p>
      <p>{{ review.updated_at }}</p>
  </div>
</template>

<script>
export default {
  name : 'ReviewListItem',
  props:{
    review:{
      type:Object,
    }
  }
}
</script>

<style>

</style>