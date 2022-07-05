<template>
    <MDBRow class="pt-5">
      <MDBCol col="2"></MDBCol>
      <MDBCol>
         <div class="text-center">
    <MDBCard class="mb-3 w-100">
    <MDBRow>
      <MDBCol style="min-width: 250px">
        <MDBCardImg @click="showLightBox" class="mainImg" :src="mainPhoto" alt="..."/>
        <carousel class="m-4" :items-to-show="3" >
    <slide v-for="(slide,index) in photos" :key="index">
      <MDBCardImg class="p-1" @click="mainPhoto=slide;mainPhotoIndex=index" :src="slide" alt="..."/>
    </slide>

    <template #addons>
      <navigation />
      <pagination />
    </template>
  </carousel>

      </MDBCol>
      <MDBCol>
        <MDBCardBody>
          <MDBCardTitle>
                  <p class="mb-0" style="font-family: Montserrat;"><strong>{{posts.title}}</strong></p>
          </MDBCardTitle>
          <MDBCardText class=" mobile-text">
           {{posts.description}}
          </MDBCardText>
                            <div class="d-flex justify-content-between mt-5" style="position:relative; padding-bottom: 50px;height:100%">
               <a class="hvr-forward">
              <img class=" m-1" v-bind:src="'http://127.0.0.1:8000'+posts.user_photo" alt="..."
                   style="width: 40px;height: 40px; border-radius: 50%;">
            <span class="text-muted" style="font-size: 10px"><strong>{{posts.username}}</strong></span>
            </a>
                      <transition name="bounce" mode="out-in" style="position: absolute; right:3%;top:3%">
          <div v-if="posts.is_liked >0">
           <MDBBtn size="sm" v-on:click.once=" delLikePost(posts.id)" color="danger" rounded>
              <font-awesome-icon icon="fa-solid fa-heart" size=""/>
             <span style="font-size: 16px"><strong>{{" "+posts.like_count}}</strong> </span>

          </MDBBtn>
      </div>
      <div v-else>
           <MDBBtn size="sm" v-on:click.once="doLikePost(posts.id)" color="light" rounded >
             <font-awesome-icon icon="fa-solid fa-heart" size=""/>
             <span style="font-size: 16px"><strong>{{" "+posts.like_count}}</strong> </span>
          </MDBBtn>
      </div>
      </transition>
                              <MDBCardFooter class="text-muted" style="position:absolute;bottom:0;">
              <small class="text-muted">{{posts.created_at}}</small>
</MDBCardFooter>
        </div>

        </MDBCardBody>
      </MDBCol>
    </MDBRow>
  </MDBCard>
  </div>
                  <MDBRow>
                    <div><h2>Похожее</h2></div>
           <PostCard type="all" page="1" grid="recom" :chCategories="[posts.cat_id]" filter="3"></PostCard>
        </MDBRow>
      </MDBCol>
      <MDBCol col="2"></MDBCol>
    </MDBRow>
  <vue-easy-lightbox
      escDisabled
      moveDisabled
      :visible="visible"
      :imgs="imgs"
      :index="index"
      @hide="handleHide"
    ></vue-easy-lightbox>
</template>

<script>
import { MDBRow, MDBCol, MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImg, MDBCardFooter,MDBBtn } from "mdb-vue-ui-kit";
import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel';
import VueEasyLightbox from 'vue-easy-lightbox'
import PostCard from "@/views/PostCard";
import axios from "axios";
export default {
  name: "PostView",
  components:{
          MDBRow,
      MDBCol,
      MDBCard,
      MDBCardBody,
      MDBCardTitle,
      MDBCardText,
    MDBCardImg,
    MDBCardFooter,
    MDBBtn,
    Carousel,
    Slide,
    Pagination,
    Navigation,
    VueEasyLightbox,
    PostCard,
  },
   props: {
     item:Object
  },
  data(){
    return{
      photos:[],
      categories:[],

      posts:'',
      mainPhoto:'',
      mainPhotoIndex:0,
      id_post:'',
       imgs: '', // Img Url , string or Array of string
        visible: false,
        index: 0 // default: 0
    }
  },
  mounted() {
    this.id_post=localStorage.getItem('id_post')
    this.getCategories()
    this.get_Photos()
    this.get_Posts()

  },
  methods:{
    get_Posts() {
          axios.get('/posts/'+this.id_post+'/').then(response => {
            let posts = response.data;
            console.log(posts)
              axios.get('/user-like/'+localStorage.getItem('user_id')+'/').then(async response => {
                let ans = []
                for (var j = 0; j < response.data.length; j++) {
                  ans[j] = response.data[j].id_post
                }
                console.log('ans----------')
                                console.log(ans)
                  let is_liked = 0
                  if(this.$store.state.isAuth)
                  {
                    is_liked = ans.indexOf(posts[0].id)
                  }
                  var cat_name = this.categories.find(item => {
                    return item.id == posts[0].category_id
                  })
                console.log(cat_name)
                  //const photo_user = await axios.get('/user-photo/'+posts.id_user+'/');
                  var options = {hour:'numeric', minute:'numeric', year: 'numeric', month: 'long', day: 'numeric' };
                  const d = new Date(posts[0].created_at);
                  let created_at = d.toLocaleDateString('ru-RU', options)
                  const photo_user = await axios.get('/user-photo/'+posts[0].id_user+'/');
                  var res = {
                      id: posts[0].id,
                      id_user: posts[0].id_user,
                      title: posts[0].title,
                      description: posts[0].description,
                      created_at: created_at,
                      like_count: posts[0].like_count,
                      is_liked: is_liked,
                      category: cat_name,
                      username: photo_user.data.username,
                      user_photo: photo_user.data.photo,
                      date:posts[0].created_at,
                      cat_id:posts[0].category_id
                    }
                this.posts = res
                console.log(this.posts)
              });
          });

        },
    get_Photos(){
          axios.get('/posts-photo/'+this.id_post+'/').then(response => {
            var photos = response.data
            var res = []
            for(var i=0;i<photos.length;i++)
            {
              var item = "http://127.0.0.1:8000"+photos[i].cover
              //var pair = {id_post:photos[i].id_post, item:item}
              res.push(item)
            }
            this.photos=res;
            this.mainPhoto=res[0]
            console.log(this.photos)
          });
        },
        getCategories(){
            axios.get('/get-categories/').then(response => {this.categories = response.data;console.log(response)});
        },
    showLightBox(){
            this.imgs=this.photos;
            this.index=this.mainPhotoIndex
       this.visible = true

    },
     showMultiple() {

       this.show()
     },
     show() {
       this.visible = true
     },
     handleHide() {
       this.visible = false
     },
     doLikePost(id) {
          if(this.$store.state.isAuth)
          {
            axios.post('/user-like/',{id_user:localStorage.getItem('user_id'),id_post:id}).then(response=>{console.log(response);this.get_Posts()})
          }
      },
        delLikePost(id){
          if(this.$store.state.isAuth)
          {
            axios.post('/user-dellike/',{id_user:localStorage.getItem('user_id'),id_post:id}).then(response => {

            console.log(response)
            this.get_Posts()
          });
          }
        },

  },
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital@0;1&display=swap');
@media (min-width: 576px) {
  .mobile-text {
    font-size: 10px!important;
  }
}
.carousel__next{
 right: 5%!important;
}
.carousel__prev{
  left: 5%!important;
}
.carousel__prev, .carousel__next{
  background-color: white;
  opacity: 0.55;
  color: black;
}
</style>