<template>
  <div class="container">
    <h1>Add Movie</h1>

    <form id="movieForm" class="form-card">

      <div class="form-group">
        <label>Movie Title</label>
        <input type="text" name="title" placeholder="Enter movie title" />
      </div>

      <div class="form-group">
        <label>Description</label>
        <textarea name="description" placeholder="Enter movie description"></textarea>
      </div>

      <div class="form-group">
        <label>Poster</label>
        <input type="file" name="poster" />
      </div>

      <button type="button" @click="saveMovie">Add Movie</button>

    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

let csrf_token = ref("");

function getCsrfToken() {
  fetch('/api/v1/csrf-token', {
    credentials: 'same-origin'
  })
    .then(res => res.json())
    .then(data => {
      csrf_token.value = data.csrf_token;
    });
}

function saveMovie() {
  let movieForm = document.getElementById('movieForm');
  let form_data = new FormData(movieForm);

  fetch("/api/v1/movies", {
    method: 'POST',
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
    },
    credentials: 'same-origin'
  })
  .then(res => res.json())
  .then(data => {
    if (data.errors) {
      console.log("ERROR:", data.errors);
    } else {
      movieForm.reset();
      window.location.href = "/movies";
    }
  })
  .catch(err => {
    console.log("FETCH ERROR:", err);
  });
}

onMounted(() => {
  getCsrfToken();
});
</script>

<style scoped>
.container {
  max-width: 500px;
  margin: 50px auto;
  text-align: center;
}

h1 {
  margin-bottom: 20px;
}

.form-card {
  background: #fff;
  padding: 25px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

.form-group {
  margin-bottom: 15px;
  text-align: left;
}

label {
  font-weight: bold;
  display: block;
  margin-bottom: 5px;
}

input, textarea {
  width: 100%;
  padding: 10px;
  border-radius: 6px;
  border: 1px solid #ccc;
}

textarea {
  min-height: 100px;
}

button {
  width: 100%;
  padding: 10px;
  background: #42b883;
  color: white;
  border: none;
  border-radius: 6px;
  font-weight: bold;
  cursor: pointer;
}

button:hover {
  background: #369870;
}
</style>