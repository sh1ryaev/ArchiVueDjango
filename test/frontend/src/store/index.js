import {createStore} from 'vuex'

export default createStore({
    state: {
        token:'',
        isAuth: false,
        searchWord:'',
        post:'',
    },
    mutations:{
        initStore(state){
            if(localStorage.getItem('token')){
                state.token=localStorage.getItem(('token'))
                state.isAuth=true
            }
            else {
                state.token=''
                state.isAuth=false
            }
        },
        setToken(state, token){
            state.token=token
            state.isAuth=true
        },
        removeToken(state){
            state.token=''
            state.isAuth=false
        },
        setSearchWord(state, word){
          state.searchWord=word
        },
        setPost(state, post){
          state.post=post
        }
    },
    actions:{

    },
    modules:{

    }
})