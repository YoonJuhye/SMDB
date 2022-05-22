<template>
  <div class="container">
      <h1>로그인</h1>

      <form @submit.prevent="login(credentials)">
        <div class="my-3">
            <label class="d-flex" for="username">아이디 </label>
            <input class="form-control" type="text" id="username" required>
        </div>

        <div class="my-3">
            <label class="d-flex" for="password">비밀번호</label>
            <input class="form-control" type="password" id="password" required>
        </div>
        <button class="d-flex btn btn-info fw-bold" style="color:white;">로그인</button>
      </form>
  </div>
</template>

<script>
import { mapActions, } from 'vuex'
export default {
    name:'LoginView',

    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
    methods: {
      ...mapActions(['login'])
    },
}
</script>

<style>
</style>