<template>
  <div>
      <h1>Sign Up</h1>

      <form @submit.prevent="signup(credentials)">
        <div>
          <label for="username">ID : </label>
        <input type="text" id="username" required/>
        </div>
        
        <div>
          <label for="password1">비밀번호 : </label>
          <input type="password" id="password" required/>
        </div>
        
        <div>
          <label for="password2">비밀번호 확인 : </label>
          <input type="password" id="password2" required/>
        </div>

        <div>
          <button>회원가입</button>
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