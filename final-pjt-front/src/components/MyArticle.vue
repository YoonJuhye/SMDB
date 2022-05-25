<template>
    <tr @click="clicktable">
      <th>{{ review.movie.title }}</th>
      <th>{{ review.title }}</th>
      <th>{{ review.created_at | moment('YYYY년 MM월 DD일 HH시 mm분')}}</th>
    </tr>
 
</template>

<script>

export default {
  name:'MyArticle',
  props:{
    review:{
      type:Object,
    }
  },
  methods : {
    clicktable: function () {
      this.$emit('select-table', this.review)
    },
  }
}
</script>

<style>

</style>