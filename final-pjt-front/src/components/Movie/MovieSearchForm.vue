<template>
  <div style="height:300px;" id="searchForm">
    <div id="maintext">
      <h1 class="welcome">Welcome.</h1>
      <h1 class="smdb">Ssafy Movie DB.</h1>
    </div>
    
    <div class="col-12 d-flex justify-content-center" style="padding-top:30px;">
        <input v-model="keyword" class="col-10" type="text" id="searchInput" placeholder="영화, 배우, 제작진을 검색하세요." aria-label="영화, 배우, 제작진을 검색하세요." aria-describedby="searchButton">
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
    background: linear-gradient(to right, #6441A5 40%, 
                #2a0845 100%);
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
#maintext {
  padding-left: 70px;
  padding-top: 60px;
}
.welcome {
    font-size: 3em;
    font-weight: 700;
    line-height: 1;
}
.smdb {
    font-size: 2em;
    font-weight: 600;
    margin: 0;
}
</style>