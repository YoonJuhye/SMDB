<template>
  <div class="container">
      <h1>로그인</h1>

      <account-error v-if="authError"></account-error>

      <form @submit.prevent="login(credentials)">
        <div class="my-3">
            <label class="d-flex" for="username">아이디 </label>
            <input class="form-control" v-model="credentials.username" type="text" id="username" required>
        </div>

        <div class="my-3">
            <label class="d-flex" for="password">비밀번호</label>
            <input class="form-control" v-model="credentials.password" type="password" id="password" required>
        </div>
        <button class="d-flex btn btn-info fw-bold" style="color:white;">로그인</button>
      </form>
  </div>
</template>

<script>
import { mapActions,mapGetters } from 'vuex'
import AccountError from '../components/AccountError.vue'
export default {
    name:'LoginView',
    components:{
      AccountError,
    },
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
    computed: {
      ...mapGetters(['authError'])
    },
}
</script>

<style>
</style>