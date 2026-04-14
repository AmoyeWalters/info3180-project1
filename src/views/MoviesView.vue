<template>
  <div class="page-container">
    <h1>Movies</h1>

    <div v-if="movies.length === 0">
      <p>No movies added yet.</p>
    </div>

    <div class="movie-grid">
      <div v-for="movie in movies" :key="movie.id" class="movie-card">
        <img :src="'http://127.0.0.1:5000/uploads/' + movie.poster" />
        <h3>{{ movie.title }}</h3>
        <p>{{ movie.description }}</p>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

let movies = ref([]);

function getMovies() {
  fetch('/api/v1/movies')
    .then(res => res.json())
    .then(data => {
      movies.value = data.movies;
    });
}

onMounted(() => {
  getMovies();
});
</script>

<style scoped>
.page-container {
  max-width: 900px;
  margin: 40px auto;
  text-align: center;
}

.movie-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
}

.movie-card {
  background: white;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

img {
  width: 100%;
  border-radius: 8px;
}
</style>