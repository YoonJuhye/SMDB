<template>
  <div class="all-sort" style="padding-top:30px;">
    <div class="d-flex">
       <h3 class="sort-title mx-3 d-flex">장르별 추천</h3>
        <div class="sort-tap mx-3">
          <button @click="sort('all')" class="selectbutton leftbutton">전체</button>
          <button @click="sort(28)" class="selectbutton">액션</button>
          <button @click="sort(10749)" class="selectbutton">로맨스</button>
          <button @click="sort(16)" class="selectbutton">애니메이션</button>
          <button @click="sort(27)" class="selectbutton">공포</button>
          <button @click="sort(35)" class="selectbutton rightbutton">코미디</button>
        </div>
    </div>
    <div class="slimscroll" id="sorted">
      <movie-list-item class="my-3" style="display: inline-block;" v-for="movie in sorted" :key="movie.pk" :movie="movie" />
    </div>
  </div>
</template>

<script>
import { mapActions,mapGetters } from 'vuex'
import MovieListItem from './MovieListItem.vue'

export default {
    name:'MovieSortList',
    components:{
        MovieListItem
    },
    methods:{
      ...mapActions(['sort']),
    },
    computed:{
      ...mapGetters(['sorted'])
    },
    created(){
      this.sort('all')
    }
    
}
</script>

<style>
@import url(//fonts.googleapis.com/earlyaccess/notosanskr.css);

.all-sort {
  padding: 0 50px 0 50px;
}


.sort-title {
  font-family: "Noto Sans KR", sans-serif;
  font-weight: 700;
}

.sort-tap {
  font-family: "Noto Sans KR", sans-serif;
}

.selectbutton {
  background-color: #d1d1f0;
  overflow: auto;
  border: none;
  width: 120px;
  margin-top: 5px;
}
.rightbutton {
  border-top-right-radius: 20px;
  border-bottom-right-radius: 20px;
}
.leftbutton {
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;
}

.selectbutton:active {
  box-shadow: 1px 1px 0 rgb(0,0,0,0.5);
  background-color: rgb(224, 128, 253);
  border-color: bisque;
  top:2px;
}


#sorted {
  overflow-x: scroll;
  overflow-y: hidden;
  white-space: nowrap;
}

.slimscroll {
    overflow: auto;
}

.slimscroll::-webkit-scrollbar {
    width: 600px;
    height: 100px;
}

.slimscroll::-webkit-scrollbar-thumb {
    background-color: #B0B0B0;
    border-radius: 10px;
    background-clip: padding-box;
    border: 2px solid transparent;
}

.slimscroll::-webkit-scrollbar-track {
    background-color: white;
    border-radius: 10px;
    box-shadow: inset 0px 0px 3px white;
}

</style>