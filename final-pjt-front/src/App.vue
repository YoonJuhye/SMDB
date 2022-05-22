<template>
  <div id="app">
    <nav class="sticky-top d-flex justify-content-between p-3">
      <h3 style="color: #3FC1C9;">SMDB</h3>
      <div class="d-flex align-items-center">
        <router-link to="/" class="text-decoration-none mx-2">HOME</router-link>

        <router-link v-if="login" to="/logout" class="text-decoration-none mx-2">로그아웃</router-link>
        <div v-else>
          <router-link to="/signup" class="text-decoration-none mx-2">회원가입</router-link>
          <router-link to="/login" class="text-decoration-none mx-2">로그인</router-link>
        </div>
      </div>
    </nav>
    
    <router-view id="view"/>
    
    <footer class="d-flex align-items-center">
      <h2 class="mx-3" style="color: #3FC1C9;">Ssafy Movie DB</h2>
    </footer>
  </div>
</template>

<script>
export default {
  data: function  () {
    return {
      login: false,
    }
  },
  created:function () {
    const token = localStorage.getItem('token')
    if (token) {
      this.login = true
    } else{
      this.login = false
    }
  },
  updated: function () {
    const token = localStorage.getItem('token')
    if (token) {
      this.login = true
    } else{
      this.login = false
    }
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

  min-height: 100%;
  position: relative;
  padding-bottom: 170px;

}

nav {
  background: #364F6B;
  padding: 30px;
  
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
#view {
  margin-top:20px;
  padding-bottom: 60px;
  min-height: 1200px;
}

footer {
  background: #364F6B;
  height: 100px;
  position: absolute;
  bottom: 0;
  width: 100%;
}
</style>
