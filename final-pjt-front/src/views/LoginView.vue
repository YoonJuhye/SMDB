<template>
  <div class="center">
      <h1>Login</h1>
      <account-error v-if="authError"></account-error>

      <form @submit.prevent="login(credentials)">
        <div class="txt-field">
            <input v-model="credentials.username" type="text" id="username" required>
            <span></span>
            <label for="username">ID</label>
        </div>

        <div class="txt-field">
            <input v-model="credentials.password" @keyup.enter="sumbit" type="password" id="password" required>
            <span></span>
            <label for="password">PW</label>
        </div>
        <input type="submit" value="Login">
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
      ...mapActions(['login','cleanError'])
    },
    computed: {
      ...mapGetters(['authError'])
    },
    created () {
      this.cleanError()
    }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap');

/* body {
  margin: 0;
  padding: 0;
  font-family: 'Poppins', sans-serif;
  font-weight: 700;
  background: linear-gradient(120deg, #2980b9, #8e44ad);
  height: 100vh;
} */

.center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%);
  width: 400px;
  height: 400px;
  background: white;
  border-radius: 10px;
  box-shadow: 5px 5px 10px grey;
}

.center h1 {
  font-family: 'Poppins', sans-serif;
  text-align: center;
  padding: 10px 0 10px 0;
  border-bottom: 1px solid silver;
}

.center form {
  padding: 0 40px;
  box-sizing: border-box;
}

form .txt-field {
  position: relative;
  border-bottom: 2px solid #adadad;
  margin: 30px 0;
}

.txt-field input {
  width: 100%;
  padding: 0 5px;
  height: 40px;
  font-size: 16px;
  border: none;
  background: none;
  outline: none;
}

.txt-field label {
  position: absolute;
  top: 50%;
  left: 5px;
  color: #adadad;
  transform: translateY(-50%);
  font-size: 16px;
  pointer-events: none;
  transition: .5s;
}

.txt-field span::before{
  content: '';
  position: absolute;
  top: 40px;
  left: 0;
  width: 0%;
  height: 2px;
  background: #2691d9;
  transition: .5s;
}

.txt-field input:focus ~ label,
.txt-field input:valid ~ label {
  top: -5px;
  color: #2691d9;
}

.txt-field input:focus ~ span::before,
.txt-field input:valid ~ span::before {
  width: 100%;
}

input[type="submit"] {
  width: 100%;
  height: 50px;
  border: 1px solid;
  background: #2691d9;
  border-radius: 25px;
  font-size: 18px;
  color: #e9f4fb;
  font-weight: 700;
  cursor: pointer;
  outline: none;
}

input[type="submit"]:hover {
  border-color: #2691d9;
  transition: .5s;
}
</style>