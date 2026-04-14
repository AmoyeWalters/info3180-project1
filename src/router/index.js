import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
    path: '/movies',
    name: 'Movies',
    component: () => import('../views/MoviesView.vue')
    },
    {
      path: '/movies/create',
      name: 'AddMovie',
      component: () => import('../views/AddMovieFormView.vue')
    }
  ]
})

export default router
