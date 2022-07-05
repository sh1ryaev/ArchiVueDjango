<template>
      <MDBRow center class="d-flex align-items-center" style="height: 650px">

    <MDBCol col="4">
          <div class="sign-in" >
    <h1>Регистрация</h1>
        <form>
          <MDBInput
              class="mb-3"
              type="email"
              label="Введите email"
              v-model="email"
              invalidFeedback="Укажите email"
              validFeedback="Отлично!"
              required
          />
          <MDBInput
              class="mb-3"
              type="text"
              label="Введите имя пользователя"
              v-model="username"
              invalidFeedback="Введите имя пользователя"
              validFeedback="Отлично!"
              required
          />
           <MDBInput
              class="mb-3"
              type="text"
              label="Введите имя"
              v-model="first_name"
              invalidFeedback="Введите имя"
              validFeedback="Отлично!"
              required
          />
          <MDBInput
              class="mb-3"
              type="text"
              label="Введите фамилию"
              v-model="last_name"
              invalidFeedback="Введите фамилию"
              validFeedback="Отлично!"
              required
          />
           <MDBInput
              class="mb-3"
              type="password"
              label="Введите пароль"
              v-model="password"
              invalidFeedback="Введите пароль"
              validFeedback="Отлично!"
              required
          />
          <MDBInput
              class="mb-3"
              type="password"
              label="Повторите пароль"
              v-model="re_password"
              invalidFeedback="Повторите пароль"
              validFeedback="Отлично!"
              required
          />
      <MDBBtn v-on:click="submitForm" color="primary"> Войти </MDBBtn>
    </form>
            <div v-if="status==='Created'">
              <p>Сообщение с подтверждением отправлено на почту {{email}}</p>
            </div>
  </div>
    </MDBCol>

  </MDBRow>
</template>

<script>
import { MDBInput, MDBBtn, MDBRow, MDBCol } from 'mdb-vue-ui-kit';
import axios from "axios"
export default {
  name: "SignUp",
  components:{
    MDBInput,
    MDBBtn,
    MDBCol,
    MDBRow,
  },
  data(){
    return{
      username:'',
      password:'',
      re_password:'',
      first_name:'',
      last_name:'',
      email:'',
      status:'',
    }
  },
  mounted() {
    this.status=''
  },
  methods: {
    submitForm(){
      axios.post('/api/v1/users/', {
            username:this.username,
        password:this.password,
        re_password:this.re_password,
        first_name:this.first_name,
        last_name:this.last_name,
        email:this.email,
  })
  .then(function (response) {
    console.log(response)
    console.log(response.statusText)
    this.status=response.statusText
  })
  .catch(function (error) {
    console.log(error);
  });
    }
  }
}
</script>

<style scoped>

</style>