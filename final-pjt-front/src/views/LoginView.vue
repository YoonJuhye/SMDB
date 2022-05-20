<template>
  <div>
      <h1>Login</h1>

      <form @submit.prevent="login(credentials)">
        <div>
            <label for="username">ID : </label>
            <input type="text" id="username" required>
        </div>

        <div>
            <label for="password">비밀번호 : </label>
            <input type="password" id="password" required>
        </div>
        <button>로그인</button>
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