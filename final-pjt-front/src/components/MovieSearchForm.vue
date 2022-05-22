<template>
  <div class="d-flex align-items-center" style="height:300px;" id="searchForm">
    <div class="col-12 d-flex justify-content-center">
        <input @keyup.enter="search(keyword)" v-model="keyword" class="col-10" type="text" id="searchInput" placeholder="영화, 배우, 제작진을 검색하세요." aria-label="영화, 배우, 제작진을 검색하세요." aria-describedby="searchButton">
        <button @click="search(keyword)" class="col-1 btn btn-outline-secondary fw-bold" type="button" id="searchButton">Search</button>
    </div>
    
  </div>
</template>

<script>
import { mapActions } from 'vuex'


export default {
  name:'MovieSearchForm',
  data() {
    return {
      keyword:'',
    }
  },
  methods: {
      ...mapActions(['search'])
    },

}
</script>

<style>
#searchButton {
    background: linear-gradient(to right, rgba(30,213,169, 1) 30%, 
                rgba(1,180,228, 1) 100%);
    border-radius: 20px;
    border: none;
    color: white;
    
}
#searchInput {
    border-radius: 20px;
    border: none;
    margin-right: -30px;
    outline: none;
    padding: 10px 20px;
}
#searchForm {
    background-color: rgba(216, 214, 226, 0.301);
}
</style>