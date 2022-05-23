<template>
  <div style="padding-top:30px;">
    <div class="d-flex">
       <h3 class="d-flex">장르별 정렬</h3>
        <div class="mx-3">
          <button @click="sort('all')" id="selectbutton">전체</button>
          <button @click="sort(28)" id="selectbutton">액션</button>
          <button @click="sort(10749)" id="selectbutton">로맨스</button>
          <button @click="sort(16)" id="selectbutton">애니메이션</button>
          <button @click="sort(35)" id="selectbutton">코미디</button>
        </div>
    </div>
     
  </div>
</template>

<script>
import { mapActions } from 'vuex'
// import MovieListItem from './MovieListItem.vue'

export default {
    name:'MovieSortList',
    components:{
        
    },
    methods:{
      ...mapActions(['sort'])
    }
}
</script>

<style>
#selectbutton {
  background-color: #d1d1f0;
  overflow: auto;
  border-radius: 20px;
  border: none;
  width: 100px;
  margin-right: -20px;
  margin-top: 5px;
}
#selectbutton:active {
  box-shadow: 1px 1px 0 rgb(0,0,0,0.5);
  background-color: rgb(224, 128, 253);
  top:2px;
}
</style>