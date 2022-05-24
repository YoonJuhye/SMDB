<template>
  <div>
      <h1>Review</h1>
      <div v-if="reviews">
          <review-list-item v-for="review in reviews" :key="review.pk" :review="review" />
      </div>
      <div v-else>
          <h2>리뷰가 없어요~</h2>
      </div>
    
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import ReviewListItem from './ReviewListItem.vue'

export default {
    name:'ReviewList',
    data () {
        return {
            reviews:[],
        }
    },
    components:{
        ReviewListItem
    },
    methods:{
        ...mapActions(['loadReview']),
    },
    created () {
        console.log(this.$store.state.movies.movie_pk)
        this.loadReview(this.$store.state.movies.movie_pk)
        this.reviews = this.$store.state.reviews.reviews
    }
}
</script>

<style>

</style>