<template>
  <div id="app">
    <nav class="sticky-top d-flex justify-content-between p-3">
      <h3 style="color: #3FC1C9;">SMDB</h3>
      <div class="d-flex align-items-center">
        <router-link to="/" class="text-decoration-none mx-2">HOME</router-link>
        <router-link to="/signup" class="text-decoration-none mx-2">회원가입</router-link>
        <router-link to="/login" class="text-decoration-none mx-2">로그인</router-link>
      </div>
    </nav>
    <router-view style="margin-top:20px;" />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
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
</style>
