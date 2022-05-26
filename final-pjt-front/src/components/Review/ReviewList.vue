<template>
  <div>
      <div v-if="this.$store.state.reviews.reviews">
          <review-list-item class="my-5" v-for="review in this.$store.state.reviews.reviews" :key="review.pk" :review="review" />
      </div>
      <div v-else>
          <h2 class="tung my-5">첫번째 리뷰의 주인공이 되어 보세요.</h2>
      </div>
    
  </div>
</template>

<script>
import ReviewListItem from './ReviewListItem.vue'

export default {
    name:'ReviewList',
    data () {
        return {
            reviews:[],
        }
    },
    components:{
        ReviewListItem,
    },
}
</script>

<style>

.tung {
    font-size: 20px;
    text-align: center;
    text-justify: center;
}
</style>