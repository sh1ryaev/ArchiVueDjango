import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
        path: '/sign-up',
        name: 'SignUp',
        component: () => import('../views/SignUp.vue')
    },
    {
        path: '/log-in',
        name: 'LogIn',
        component: () => import('../views/LogIn.vue')
    },
    {
        path: '/profile',
        name: 'UserProfile',
        component: () => import('../views/UserProfile.vue')
    },
    {
        path:'/masonry',
        name:'MasonryCard',
        component: () => import('../views/MasonryCard.vue')
    },
     {
        path:'/light',
        name:'LightBox',
        component: () => import('../views/LightBox.vue')
    },
         {
        path:'/post',
        name:'PostView',
        component: () => import('../views/PostView.vue')
    },
    {
        path: '/',
        name: 'HomePage',
        component: () => import('../views/HomePage.vue')
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router