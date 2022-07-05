<template>
 <MasonryWall :items="posts" :ssr-columns="1" :column-width="300" :gap="10">
    <template #default="{ item }">

        <MDBCard class="mb-1 p-1 mx-auto" >
          <div class="d-flex align-items-center">
            <a class="hvr-forward" href="/profile">
              <img class=" m-1" v-bind:src="'http://127.0.0.1:8000'+item.user_photo" alt="..." style="width: 30px;height: 30px; border-radius: 50%;">
            <span class="text-muted" style="font-size: 12px">{{item.username}}</span>
            </a>
              <a class="hvr-backward" role="button" @click="changeCat(item.cat_id)" style="font-size: 12px;position: absolute;right:1%"> {{item.category}}</a>
          </div>
      <div v-if="item.photos.length>1" v-bind:id="'slide'+item.id" class="carousel slide" data-bs-ride="carousel" >
          <div class="carousel-indicators">
    <button type="button" v-bind:data-bs-target="'#slide'+item.id" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button v-for="n in item.photos.length-1" :key="'key'+n" type="button" v-bind:data-bs-target="'#slide'+item.id" v-bind:data-bs-slide-to="n" aria-label="Slide 2"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img v-bind:src="item.photos[0]" class="d-block w-100" alt="..." style="width: 100%; object-fit: cover;">
    </div>
    <div v-for="n in item.photos.length-1" :key="'slide'+n" class="carousel-item">
      <img v-bind:src="item.photos[n]" class="d-block w-100" alt="..." style="width: 100%; object-fit: cover;">
    </div>
  </div>
  <button class="carousel-control-prev" type="button"  v-bind:data-bs-target="'#slide'+item.id" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Предыдущий</span>
  </button>
  <button class="carousel-control-next" type="button" v-bind:data-bs-target="'#slide'+item.id"  data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Следующий</span>
  </button>
</div>
<div v-else>
  <a @click="exampleModal=true"><img class="d-block w-100" v-bind:src="item.photos[0]" alt="..." style="width: 100%;  object-fit: cover;"></a>
</div>
    <MDBCardBody>
      <MDBCardTitle><strong>{{item.title}}</strong></MDBCardTitle>
      <div >
      <transition name="bounce" mode="out-in">
          <div v-if="item.is_liked >0">
           <MDBBtn v-on:click.once=" delLikePost(item.id)" color="danger" rounded>
              <font-awesome-icon icon="fa-solid fa-heart" size="xl"/>
             <span style="font-size: 16px"><strong>{{" "+item.like_count}}</strong> </span>

          </MDBBtn>
      </div>
      <div v-else>
           <MDBBtn v-on:click.once="doLikePost(item.id)" color="" rounded >
             <font-awesome-icon icon="fa-solid fa-heart" size="xl"/>
             <span style="font-size: 16px"><strong>{{" "+item.like_count}}</strong> </span>
          </MDBBtn>
      </div>
      </transition>
      <div class="justify-content-center">
        <small style="font-size: 12px" class="text-muted mt-3">Опубликовано {{item.created_at}}</small>
      </div>
      </div>
    </MDBCardBody>
  </MDBCard>
    </template>
  </MasonryWall>
</template>

<script>
import MasonryWall from "@yeger/vue-masonry-wall";
import { MDBCard, MDBCardBody, MDBCardTitle, MDBBtn,} from "mdb-vue-ui-kit";
import axios from "axios";
export default {
  name: "MasonryCard",
   data(){
    return{
     items: [
        { content: 'First', height: 150 },
        { content: 'Second', height: 300 },
        { content: 'Third', height: 150 },
        { content: 'Fourth', height: 450 },
                 { content: 'First', height: 150 },
        { content: 'Second', height: 300 },
        { content: 'Third', height: 150 },
        { content: 'Fourth', height: 450 },
                 { content: 'First', height: 150 },
        { content: 'Second', height: 300 },
        { content: 'Third', height: 150 },
        { content: 'Fourth', height: 450 },
      ],
      posts:[],
              exampleModal:false,
        like_posts:[],
        photos:[],
        categories:[],
        categories1:[],
        user_photo:[],
      type:'all',
      upHere : false

    }
   },
  components:{
    MasonryWall,
    MDBCard, MDBCardBody, MDBCardTitle, MDBBtn,
  },
  mounted() {
        this.getCategories();

     this.categories1 = this.chCategories;
      this.get_Photos();
      this.get_Posts();
  },
  methods:{
        changeCat(id){
      this.categories1=[]
      this.categories1[0]=id
      this.get_Posts()
    },
    getUserPhoto(pk){
      axios.get('/user-photo/'+pk+'/').then(response=>{this.user_photo = response.data})
      .catch(error =>{
        console.log(error)
      })
    },
    getLikePosts(){
          axios.get('/user-like/'+localStorage.getItem('user_id')+'/').then(response => {
            let ans = []
            for( var i = 0; i < response.data.length; i++ )
            {
              ans[i] = response.data[i].id_post
            }
            this.like_posts = ans
          });
        },
    getCategories(){
            axios.get('/get-categories/').then(response => this.categories = response.data);
        },
        get_Posts() {
          let str = ''
          console.log(str)
          axios.get('/posts?cat_id='+str+'&search='+this.$store.state.searchWord).then(response => {
            let posts = response.data;
              axios.get('/user-like/'+localStorage.getItem('user_id')+'/').then(async response => {
                console.log(posts)
                let ans = []
                let res = []
                for (var j = 0; j < response.data.length; j++) {
                  ans[j] = response.data[j].id_post
                }
                var iter = 0
                for (var i = 0; i < posts.length; i++) {
                  let is_liked = 0
                  if(this.$store.state.isAuth)
                  {
                    is_liked = ans.indexOf(posts[i].id) + 1
                  }
                  const d = new Date(posts[i].created_at);
                  var cat_name = this.categories.find(item => {
                    return item.id == posts[i].category_id
                  }).name
                  var photo = this.photos.filter(item => item.id_post === posts[i].id)
                  var photos = []
                  for (var k = 0; k < photo.length; k++) {
                    photos.push(photo[k].item)
                  }
                  const photo_user = await axios.get('/user-photo/'+posts[i].id_user+'/');
                  var options = {hour:'numeric', minute:'numeric', year: 'numeric', month: 'long', day: 'numeric' };
                  let created_at = d.toLocaleDateString('ru-RU', options)
                  var post = {
                      id: posts[i].id,
                      id_user: posts[i].id_user,
                      title: posts[i].title,
                      description: posts[i].description,
                      created_at: created_at,
                      like_count: posts[i].like_count,
                      is_liked: is_liked,
                      category: cat_name,
                      photos: photos,
                      username: photo_user.data.username,
                      user_photo: photo_user.data.photo,
                      date:posts[i].created_at,
                      cat_id:posts[i].category_id
                    }
                  if (this.type === 'mypost' && posts[i].id_user == localStorage.getItem('user_id')) {
                    res[iter] = post
                    iter += 1
                  } else if (this.type === 'likedpost' && is_liked > 0) {
                    res[iter] = post
                    iter += 1
                  } else if (this.type === 'all') {
                    res[i] = post
                  }
                }
                this.like_posts = ans
                if(this.filter==1)
                {
                  res.sort(function (a, b) {
                  return b.like_count - a.like_count})
                }
                else if(this.filter==2)
                {
                  res.sort(function (a, b) {
                  return a.like_count - b.like_count})
                }
                else if(this.filter==3)
                {
                  res.sort(function (a, b) {
                  return new Date(b.date) - new Date(a.date)})
                }
                else if(this.filter==4)
                {
                  res.sort(function (a, b) {
                  return new Date(a.date) - new Date(b.date)})
                }

                this.posts = res

              });
          });
        },
        get_Photos(){
          axios.get('/posts_photos/').then(response => {
            var photos = response.data
            var res = []
            for(var i=0;i<photos.length;i++)
            {
              var item = "http://127.0.0.1:8000"+photos[i].cover
              var pair = {id_post:photos[i].id_post, item:item}
              res.push(pair)
            }
            this.photos=res;
          });
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
        get_Items(id) {
          var items = []
          var iter = 0
          axios.get('/posts_photos/')
              .then(response => {
                    var photos = response.data;
                    for (var i = 0; i < photos.length; i++) {
                      if (photos[i].id_post == id) {
                        items[iter] = "http://127.0.0.1:8000" + photos[i].cover
                        iter += 1
                      }
                    }
                    return items
                  }
              );
        }
  },
}

</script>

<style scoped>
.hidden{
  display: none;
   transition: 3s linear;
}
.trigger:hover + .hidden{
  color: orange;
  display: inline;
   transition: 3s linear;
}
.bounce-enter-active {
  animation: bounce-in .4s;
}
.bounce-leave-active {
  animation: bounce-in .4s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}
</style>