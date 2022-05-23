<template>
  <div class="container">
      <h1 class="my-5">회원가입</h1>
      <account-error v-if="authError"></account-error>

      <form @submit.prevent="signup(credentials)">
        <div class="my-5">
          <label class="d-flex fs-5" for="username">아이디</label>
          <input v-model="credentials.username" class="form-control" type="text" id="username" required/>
        </div>
        
        <div class="my-5">
          <label class="d-flex fs-5" for="password1">비밀번호
            <span class="mx-3 fs-6 fw-light">*숫자, 알파벳, 특수문자가 포함 된 8자리 이상이어야 합니다.</span>
          </label>
          <input v-model="credentials.password1" class="form-control" type="password" id="password1" required/>
        </div>
        
        <div class="my-5">
          <label class="d-flex" for="password2">비밀번호 확인</label>
          <input v-model="credentials.password2" class="form-control" type="password" id="password2" required/>
        </div>

        <div class="d-flex my-4">
          <button class="btn btn-info fw-bold" style="color:white;">회원가입</button>
          <button class="btn mx-3" style="color:#0dcaf0">취소</button>
        </div>
      </form>
  </div>
</template>

<script>
import { mapActions,mapGetters } from 'vuex'
import AccountError from '../components/AccountError.vue'


export default {
    name:'SignupView',
    components:{
      AccountError,
    },
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
        computed: {
      ...mapGetters(['authError'])
    },

}
</script>

<style>
</style>