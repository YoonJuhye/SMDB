<template>
  <div style="height:400px;" id="searchForm">
    <div id="maintext">
      <h1 class="welcome">Welcome.</h1>
      <h1 class="smdb">Ssafy Movie DB.</h1>
    </div>
    
    <div class="col-12 d-flex justify-content-center" style="padding-top:50px;">
        <input v-model="keyword" @keyup.enter="search(keyword)" class="col-10" type="text" id="searchInput" placeholder="영화를 검색하세요." aria-label="영화를 검색하세요." aria-describedby="searchButton">
        <button @click="searchRequest(keyword)" class="col-1 btn btn-outline-secondary fw-bold" type="button" id="searchButton">Search</button>
    </div>
    
  </div>
</template>

<script>
import router from '@/router'
import { mapActions } from 'vuex'


export default {
  name:'MovieSearchForm',
  data() {
    return {
      keyword:'',
    }
  },
  methods: {
      ...mapActions(['search']),
      searchRequest: function (keyword) {
        if (this.$store.state.accounts.currentUser) {
          this.search(keyword)
        } else {
          alert('로그인을 해주세요!')
          router.push({ name:'login' })
        }
      }
    },

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

#searchButton {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(to right, #6441A5 40%, 
                #2a0845 100%);
    border-radius: 20px;
    border: none;
    color: white;
    
}
#searchInput {
    font-family: 'Poppins', sans-serif;
    border-radius: 20px;
    border: solid 1px;
    margin-right: -30px;
    outline: none;
    padding: 10px 20px;
}

#searchForm {
    padding: 0 50px 0 50px;
    background-color: rgba(216, 214, 226, 0.301);
    background-image: url(../../assets/search-back.jpg);
    background-repeat: no-repeat;
    background-size: cover;
}
#maintext {
  color: white;
  font-family: 'Poppins', sans-serif;
  padding-left: 70px;
  padding-top: 100px;
  margin-left: 180;
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