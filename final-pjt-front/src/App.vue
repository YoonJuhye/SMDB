<template>
  <div id="app">
    <nav class="sticky-top d-flex justify-content-between p-2 align-items-center">
      <div>
        <a class="SMDB text-decoration-none" href="/">
          <img alt="ssafy logo" src="./assets/SMDB.png" style="height:70px;">
        </a>
      </div>
      
      <div class="d-flex align-items-center">
        <router-link to="/" class="text-decoration-none mx-2">HOME</router-link>
        <router-link to="/mypage/" class="text-decoration-none mx-2">마이페이지</router-link>
        <router-link v-if="login" to="/logout" class="text-decoration-none mx-2" style="color:#d1d1f0;">로그아웃</router-link>
        <div v-else>
          <router-link to="/signup" class="text-decoration-none mx-2">회원가입</router-link>
          <router-link to="/login" class="text-decoration-none mx-2">로그인</router-link>
        </div>
      </div>
    </nav>
    
    <router-view class="mx-5" id="view" :key="$route.fullPath" />
    
    <footer class="d-flex align-items-center justify-content-center">
      <div class="container">
          <div class="align-">
                <a href="https://github.com/haengsong/MovieProject" target="_blank" rel="noopener noreferrer">
                <img class="mt-3" alt="ssafy logo" src="./assets/git.png" style="height:30px;">
                </a>
            <p class="copyright mt-1">&copy; Copyright haengsong & juhye</p>
          </div>
      </div>
    </footer>
  </div>
</template>

<script>

export default {
  data: function  () {
    return {
      login: false,
      user: '',
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
@import url(//fonts.googleapis.com/earlyaccess/notosanskr.css);


#app {
  font-family: "Noto Sans KR", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;

  min-height: 100%;
  position: relative;
  padding-bottom: 170px;

}

nav {
  background: #292961;
  padding: 30px;
  
}

nav a {
  font-weight: bold;
  color: #d1d1f0;
}

nav a.router-link-exact-active {
  background-color: white;
  color: #292961;
  border-radius: 10px;
  padding: 10px;
  padding-top: 5px;
  padding-bottom: 5px;
}
#view {
  margin-top:20px;
  padding-bottom: 80px;
  height: 100%;
  position: relative;
}
html,body{
  height: 100%;
  margin: 0;
  padding: 0;
}
footer {
  padding: 0;
  text-align: center;
  background: #292961;
  height: 80px;
  position: absolute;
  bottom: 0;
  width: 100%;
  color: #d1d1f0;
}

.social, .copyright {
  margin: 1rem;
}

.social li {
  display: inline-block;
}

.SMDB {
  color: #d1d1f0;
  font-size: 25px;
  font-weight: 100;
  height: 100px;
}
</style>
