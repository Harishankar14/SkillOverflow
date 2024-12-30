import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

import { initializeApp } from "firebase/app";

import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDgdfPEqj_QyTOS6GBnVVN_xVs1lF9i2W0",
  authDomain: "newproject-c87a5.firebaseapp.com",
  databaseURL: "https://newproject-c87a5-default-rtdb.firebaseio.com",
  projectId: "newproject-c87a5",
  storageBucket: "newproject-c87a5.firebasestorage.app",
  messagingSenderId: "475212235011",
  appId: "1:475212235011:web:c048bd106ee5b573c02936",
  measurementId: "G-QNQZ4M27VT"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
createApp(App).mount('#app')