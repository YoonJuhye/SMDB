<template>
  <div class="container" style="width: 800px;">
      <h1>회원가입</h1>

      <form @submit.prevent="signup(credentials)">
        <div class="my-3">
          <label class="d-flex" for="username">아이디</label>
          <input class="form-control" type="text" id="username" required/>
        </div>
        
        <div class="my-3">
          <label class="d-flex" for="password1">비밀번호</label>
          <input class="form-control" type="password" id="password" required/>
        </div>
        
        <div class="my-3">
          <label class="d-flex" for="password2">비밀번호 확인</label>
          <input class="form-control" type="password" id="password2" required/>
        </div>

        <div class="d-flex my-4">
          <button class="btn btn-info fw-bold" style="color:white;">회원가입</button>
          <button class="btn mx-3" style="color:#0dcaf0">취소</button>
        </div>
      </form>
  </div>
</template>

<script>
import { mapActions, } from 'vuex'

export default {
    name:'SignupView',
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },

    methods: {
      ...mapActions(['signup'])
    },

}
</script>

<style>

</style>