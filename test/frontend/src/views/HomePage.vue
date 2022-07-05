<template>
      <MDBRow class=" w-100 p-0">
            <MDBCol col="1">
            </MDBCol>
            <MDBCol>
                <div class="pb-4 mb-4">
                <div class="d-flex bg-gradient bg-light position-fixed w-100" style="z-index: 11">
                              <MDBBtnGroup id="filter-target" class=" m-2" >

              <MDBBtn
                   title="Фильтр"
        v-on:click="dropdown = !dropdown"
        class="dropdown-toggle btn-sm ">
                <MDBIcon icon="filter"></MDBIcon>
              </MDBBtn>
      <MDBDropdown  v-model="dropdown" target="#filter-target">
        <MDBDropdownMenu aria-labelledby="dropdownMenuButton">
          <div class="d-flex align-items-center justify-content-center">
            <p class="m-1"><strong>Сортировать по:</strong></p>
          </div>
          <MDBDropdownItem @click="changeFilter(1)" href="#">Количество лайков(возр)</MDBDropdownItem>
          <MDBDropdownItem @click="changeFilter(2)" href="#">Количество лайков(уб)</MDBDropdownItem>
          <MDBDropdownItem @click="changeFilter(3)" href="#">Сначала новые</MDBDropdownItem>
          <MDBDropdownItem @click="changeFilter(4)" href="#">Сначала старые</MDBDropdownItem>
                    <div class="d-lg-none d-md-none align-items-center justify-content-center">
                      <div class="m-2   align-items-center justify-content-center text-nowrap"
                     v-for="category in categories" :key="category.id">
          <MDBCheckbox
    tag="span"
    :id="category.id"
    :btnCheck="true"
    labelClass="btn btn-info rounded-pill btn-sm "
    :label="category.name"
    @click="changeCtg(category.id)"
  />
      </div>
          </div>
        </MDBDropdownMenu>
      </MDBDropdown>
    </MDBBtnGroup>
                <div class="m-2  d-lg-block d-none align-items-center justify-content-center text-nowrap"
                     v-for="category in categories" :key="category.id">
          <MDBCheckbox
    tag="span"
    :id="category.id"
    :btnCheck="true"
    labelClass="btn btn-info rounded-pill btn-sm "
    :label="category.name"
    @click="changeCtg(category.id)"
  />
      </div>
                                 <MDBBtn v-if="this.$store.state.isAuth" @click="
      () => {
        modalContent = '@getbootstrap';
        varyingExampleModal = true;
      }" tag="a" title="Добавить пост"  class="btn-sm mt-2 float-end" color="light" href="#!" floating>
    <MDBIcon icon="plus"></MDBIcon>
  </MDBBtn>
              </div>
</div>

            </MDBCol>
            <MDBCol col="1"></MDBCol>
      </MDBRow>
    <MDBRow class="mb-3 w-100 p-0">
    <MDBCol col="1"></MDBCol>

          <MDBCol>



            <PostCard v-cloak type="all" :page="pageNum" :grid="grid" :chCategories="categories1" :filter="filter" :key="componentKey"></PostCard>
            <a class="btn btn-primary" @click="prevPage">Предыдушая</a>
            <a class="btn btn-primary" @click="nextPage">Следующая</a>
    </MDBCol>
      <MDBCol col="1">
          <div class="position-fixed">
               <!-- <MDBBtn @click="
      () => {
        modalContent = '@getbootstrap';
        filterModal = true;
      }" tag="a" color="dark" href="#!" floating>
    <MDBIcon icon="filter"></MDBIcon>
  </MDBBtn>-->
       <!--     <MDBBtnGroup id="filter-target">
              <MDBBtn
                   title="Фильтр"
        color=""
        v-on:click="dropdown = !dropdown"
        class="dropdown-toggle">
                <MDBIcon icon="filter"></MDBIcon>
              </MDBBtn>
      <MDBDropdown  v-model="dropdown" target="#filter-target">
        <MDBDropdownMenu aria-labelledby="dropdownMenuButton">
          <div class="d-flex align-items-center justify-content-center">
            <p class="m-1"><strong>Сортировать по:</strong></p>
          </div>
          <MDBDropdownItem @click="changeFilter(1)" href="#">Количество лайков(возр)</MDBDropdownItem>
          <MDBDropdownItem @click="changeFilter(2)" href="#">Количество лайков(уб)</MDBDropdownItem>
          <MDBDropdownItem @click="changeFilter(3)" href="#">Сначала новые</MDBDropdownItem>
          <MDBDropdownItem @click="changeFilter(4)" href="#">Сначала старые</MDBDropdownItem>
                    <div class="d-flex align-items-center justify-content-center">
            <p class="m-1"><strong>Категории:</strong></p>
          </div>
          <div class="m-2 d-flex align-items-center justify-content-center" v-for="category in categories" :key="category.id">

                <input class="form-check-input float-start" type="checkbox" v-bind:value="category.id" v-model="categories1" v-bind:id="category.id">
                <label v-bind:for="category.id" class="fs-6 small form-check-label float-start"><small>{{ category.name }}</small></label><br>

          <MDBCheckbox
    tag="span"
    :id="category.id"
    :btnCheck="true"
    labelClass="btn btn-info"
    :label="category.name"
    @click="changeCtg(category.id)"
  />
      </div>
        </MDBDropdownMenu>
      </MDBDropdown>
    </MDBBtnGroup>-->

  </div>
      </MDBCol>
  </MDBRow>

<!--Модальное окно-->
  <MDBModal
    id="varyingExampleModal"
    tabindex="-1"
    labelledby="varyingExampleModalLabel"
    v-model="varyingExampleModal"
  >
    <MDBModalHeader>
      <MDBModalTitle id="varyingExampleModalLabel"> Новый пост </MDBModalTitle>
    </MDBModalHeader>
    <MDBModalBody>
      <form>
        <div class="mb-3">
          <label for="title" class="col-form-label">Заголовок: </label>
          <input
            type="text"
            class="form-control"
            id="title"
            v-model="title"
          />
        </div>
        <div class="mb-3">
          <label for="message-text" class="col-form-label">Описание:</label>
          <textarea class="form-control" id="message-text" v-model="description"></textarea>
        </div>
        <div class="mb-3">
          <p class="col-form-label">Категория:</p>
          <div v-for="category in categories" :key="category.id">
              <input  v-model="ch_category" v-bind:value="category.id" class="form-check-input float-start m-1" type="radio" v-bind:id="'radio'+category.id">
              <label class="form-check-label float-start m-1" v-bind:for="'radio'+category.id">{{category.name}}</label>
          </div>
        </div>
        <div class="mb-3">
          <MDBFile
          v-model="files"
          multiple
          label="Выберите изображения:"
          v-on:change="handleFileUploads"
          />
        </div>
      </form>
      <div class="large-12 medium-12 small-12 cell">
  <div v-for="(file, key) in files" :key="key" class="file-listing">{{ file.name }} <span class="remove-file" v-on:click="removeFile( key )">{{key}}Remove</span></div>
</div>
<br>
    </MDBModalBody>
    <MDBModalFooter>

      <MDBBtn v-on:click="savePost" color="primary"> Сохранить пост </MDBBtn>
    </MDBModalFooter>
  </MDBModal>
</template>

<script>
  import { MDBCol,MDBCheckbox,MDBIcon, MDBRow, MDBBtn, MDBModal, MDBModalHeader, MDBModalTitle, MDBModalBody, MDBModalFooter,MDBFile, MDBBtnGroup,MDBDropdown,MDBDropdownMenu, MDBDropdownItem} from "mdb-vue-ui-kit";
  import axios from "axios";

  import PostCard from "@/views/PostCard";
  import { ref } from 'vue'
  export default {
    name: "HomePage",
    data(){
      return{
        posts:[],
        like_posts:[],
        photos:[],
        categories:[],
        categories1:[],
        varyingExampleModal:false,
        filterModal:false,
        files:'',
        title:'',
        description:'',
        ch_category:'',
        componentKey: 0,
        grid: false,
        filter:3,
        filterName:'',
        dropdown:false,
        pageNum:1,
      }
    },
    components: {
      MDBCol,
      MDBRow,
      MDBBtn,
      MDBModal,
      MDBModalHeader,
      MDBModalTitle,
      MDBModalBody,
      MDBModalFooter,
      MDBFile,
      MDBBtnGroup,
      MDBDropdown,MDBDropdownMenu, MDBDropdownItem,MDBIcon,MDBCheckbox,
      PostCard
    },
    mounted () {
      this.getCategories();

    },
      methods: {
      changeCtg(id){
        if(this.categories1.includes(id)===false){
          this.categories1.push(id)
        }
        else{
          const index = this.categories1.indexOf(id);
          if (index > -1) {this.categories1.splice(index, 1);}
        }
        this.componentKey += 1;
      },
      forceRerender() {

    },
        prevPage(){
                this.pageNum-=1
                this.componentKey += 1;
        },
        nextPage(){
                this.pageNum+=1
                this.componentKey += 1;
        },
        changeFilter(num){
          this.filter=num

          if(num===1)
          {
            this.filterName = 'Количество лайков(возр)'
          }
          else if(num===2)
          {
            this.filterName = 'Количество лайков(уб)'
          }
          else if(num===3)
          {
            this.filterName = 'Сначала новые'
          }
          else if(num===4)
          {
            this.filterName = 'Сначала старые'
          }
          this.componentKey+=1
        },
        changeGrid(){
          this.grid=true
          this.componentKey += 1;
        },
         changeGrid1(){
          this.grid=false
           this.componentKey += 1;
        },
              getCategories(){
            axios.get('/get-categories/').then(response => this.categories = response.data);
        },
        handleFileUploads(){
          this.files = this.$refs.files;
        },
        removeFile( key ){
          var a = []
          for( var i = 0; i < this.files.length; i++ ){
          let file = this.files[i];
          a[i]=file
          console.log(file)
        }
          a.splice( key, 1 );
          this.files=a
        },
        savePost(){
          var now = new Date();
                    axios
      .post('/posts/',{
        id_user:localStorage.getItem('user_id'),
        title:this.title,
        description:this.description,
        created_at:now,
        category_id:this.ch_category
  })
      .then(response=>{
        console.log(response)
        console.log(ref(["file"]).value)
        for( var i = 0; i < this.files.length; i++ ){
          let file = this.files[i];
          var formData = new FormData();
          formData.append("cover", file);
        formData.append("id_post", response.data.id);
        axios.post('/posts_photos/',formData,{headers:{
          'Content-Type': 'multipart/form-data'
        }})
      .then(response=>{
        console.log(response)

      })
      .catch(error =>{
        console.log(error)
      })
        }
      })
      .catch(error =>{
        console.log(error)
      })
        }
      }}
</script>

<style lang="scss">
[v-cloak] {
    display: none !important;
}
</style>