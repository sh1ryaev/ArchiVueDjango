<template>
  <NavBar></NavBar>
  <div class="bg-light bg-gradient">
    <router-view/>
  </div>
  <FooterVue></FooterVue>
</template>


<script>
import axios from "axios"
import NavBar from "./views/NavBar"
import FooterVue from "./views/Footer"
export default {
  name: 'App',
  components: {
    NavBar,
    FooterVue,
  },
  data(){
    return{
      isLoading: false,
      fullPage: true,
      loader: 'bars'
    }
  },
  beforeCreate() {
    this.$store.commit('initStore')
    const token = this.$store.state.token
    if(token){
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else{
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  methods: {
      handleLogout() {
          localStorage.removeItem('token')
          this.$store.commit('removeToken')
      },
    },
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

</style>
