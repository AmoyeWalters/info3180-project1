<template>
  <header>
    <nav class="navbar navbar-dark bg-primary fixed-top shadow-sm px-4">

      <RouterLink to="/" class="navbar-brand fw-bold">
        VueJS with Flask
      </RouterLink>

      <ul class="navbar-nav flex-row gap-4 mb-0">

        <li class="nav-item">
          <RouterLink to="/" class="nav-link text-white">Home</RouterLink>
        </li>

        <li class="nav-item">
          <RouterLink to="/about" class="nav-link text-white">About</RouterLink>
        </li>

        <li class="nav-item">
          <RouterLink to="/movies" class="nav-link text-white">
            New Movies
          </RouterLink>
        </li>

        <li class="nav-item">
          <RouterLink to="/movies/create" class="nav-link text-white">
            Add Movie
          </RouterLink>
        </li>

      </ul>

    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from "vue-router";
</script>

<style scoped>

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-link {
  transition: 0.3s;
}

.nav-link:hover {
  color: #ffd369 !important;
}

.router-link-active {
  font-weight: bold;
  border-bottom: 2px solid #ffd369;
}

.navbar-brand {
  letter-spacing: 1px;
}
</style>