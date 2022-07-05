<template>
    <MDBRow center class="d-flex align-items-center" style="height: 650px">

    <MDBCol col="4">
          <div class="login " >
    <h1>Войти</h1>
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
              type="password"
              label="Введите пароль"
              v-model="password"
              invalidFeedback="Укажите пароль"
              validFeedback="Отлично!"
              required
          />
      <MDBBtn v-on:click="submitForm" color="primary"> Войти </MDBBtn>
    </form>
  </div>
    </MDBCol>

  </MDBRow>

</template>

<script>
import axios from "axios"
import { MDBInput, MDBBtn, MDBRow, MDBCol } from 'mdb-vue-ui-kit';
export default {
  name: "LogIn",
  components:{
    MDBInput,
    MDBBtn,
    MDBCol,
    MDBRow,
  },
  data(){
    return{
      email:'',
      password:'',
      checkForm:null,
    }
  },
  mounted() {
    this.checkForm = e => {
          e.target.classList.add("was-validated");
        };
  },
  methods: {
    submitForm(){

    axios
      .post('/api/v1/jwt/create/', {email:this.email, password:this.password})
      .then(response=>{
        const token = response.data.access
        const refresh = response.data.refresh
        this.$store.commit('setToken', token)
        //axios.defaults.headers.common['Authorization'] = 'JWT '+token
        localStorage.setItem('token',token)
        localStorage.setItem('refresh',refresh)
                  axios.get('/api/v1/users/me/', {headers: {Authorization: `JWT ${localStorage.getItem('token')}`}})
              .then(response => {this.user = response.data;
                alert('Welcome '+response.data.username);
                const user_id = response.data.id;
                localStorage.setItem('user_id',user_id)
                window.location.assign('/')
              });
      })
      .catch(error =>{
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

</style>