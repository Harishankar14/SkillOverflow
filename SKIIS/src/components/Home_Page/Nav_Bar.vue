<script setup>
</script>

<template>
  <div>
    <div class="search-bar">
      <input type="text" v-model="searchQuery" @input="searchPost" placeholder="Search Posts.."class="search-input"/>
    </div>
    <div class="filters">
      <button @click="filterPosts('Coding')" class="filters-button coding-btn">Coding</button>
      <button @click="filterPosts('Design')" class="filters-button design-btn">Design</button>
      <button @click="filterPosts('Video Editing')" class="filters-button video-btn">Video Editing</button>
      <button @click="filterPosts('Language')" class="filters-button language-btn">Language</button>
      <button @click="fetchPosts" class="filters-button all-btn">All</button>
    </div>

    <!-- Displaying Posts -->
    <div v-for="post in posts" :key="post.id" class="post-card">
      <h2>{{ post.title }}</h2>
      <p>{{ post.description }}</p>
      <small>Category: {{ post.category }}</small>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      posts: [], // To store posts
    };
  },
  methods: {
    searchPost() {
      let url = "http://127.0.0.1:5000/api/posts?search=" + this.searchQuery;
      axios.get(url)
        .then(response => {
          this.posts = response.data;
        })
        .catch(error => console.error(error));
    },
    fetchPosts() {
      // Fetch all posts
      axios.get("http://127.0.0.1:5000/api/posts")
        .then(response => {
          this.posts = response.data;
        })
        .catch(error => console.error(error));
    },
    filterPosts(category) {
      // Fetch posts filtered by category
      axios.get(`http://127.0.0.1:5000/api/posts?category=${category}`)
        .then(response => {
          this.posts = response.data;
        })
        .catch(error => console.error(error));
    },
  },
  mounted() {
    
    this.fetchPosts();
  },
};
</script>

<style scoped>
    
    .search-bar{
      width: 100%;
      margin: 10px 0;
      display: flex;
      justify-content: center;
    }
    .filters {
        background-color: rgb(1, 1, 1);
        width: 100%;
        height: 7%;
        display: flex;
        justify-content: space-evenly;
        align-items: center;
    }

    .filters-button {
        background-color: rgb(58, 58, 58);
        color: white;
        font-size: 1.2rem;
        font-weight: 500;
        border-radius: 30px;
        width: 12%;
        padding: 10px 20px;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        cursor: pointer;
        text-transform: uppercase;
    }

    .filters-button:hover {
        border-color: white;
        background-color: #f4f4f4;
        color: black;
        box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
        transform: translateY(-2px);
    }

    .filters-button:active {
        transform: translateY(0);
    }

    
    .coding-btn {
        background-color: #3b5998;
    }

    .design-btn {
        background-color: #e44d26;
    }

    .video-btn {
        background-color: #d453ed;
    }

    .language-btn {
        background-color: #4caf50;
    }

    .all-btn {
        background-color: #f1c40f;
    }

    .filters-button:hover.coding-btn {
        background-color: #334d8c;
    }

    .filters-button:hover.design-btn {
        background-color: #cc3e1f;
    }

    .filters-button:hover.video-btn {
        background-color: #c04dce;
    }

    .filters-button:hover.language-btn {
        background-color: #45a049;
    }

    .filters-button:hover.all-btn {
        background-color: #f39c12;
    }
    .post-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }

    .post-card:hover {
        transform: translateY(-5px); 
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }

    .post-card h2 {
        font-size: 1.8rem;
        color: #333;
        margin-bottom: 10px;
    }

    .post-card p {
        font-size: 1.1rem;
        color: #555;
        margin-bottom: 10px;
    }

    .post-card small {
        font-size: 0.9rem;
        color: #888;
        display: block;
        margin-top: 10px;
    }

    .post-card p {
        border-top: 2px solid #f4f4f4;
        padding-top: 15px;
    }
</style>
