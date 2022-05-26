<template>
    <div @click="clicktable" class="d-flex justify-content-around">
      <h5 class="text-center overtext">{{ review.movie.title }}</h5>
      <h5 class="text-center overtext">{{ review.title }}<small class="mx-2">({{ review.comments.length }})</small></h5>
      
      <h5 class="text-center overtext">{{ review.created_at | moment('YYYY년 MM월 DD일 HH시 mm분')}}</h5>
    </div>
 
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
.overtext {
  width: 500px;
  display: inline;
  overflow: hidden;
}
</style>