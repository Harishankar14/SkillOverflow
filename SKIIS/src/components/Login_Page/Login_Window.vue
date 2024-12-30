
<script setup>

</script>


<template>
    <div v-if="!user" class="main-container">
        <h1 class="welcome-text">Join our community of skill exchangers today!</h1>
        <h2 class="msg">Sign in to SkillOverflow</h2>
        <button class="google-signin" @click="signInWithGoogle">
            <img alt="Google logo" src="@/assets/Login_Page/logo.png" class="google-icon" />
            <span>Sign in with Google</span>
        </button>
    </div>
    <div v-if="user" class="main-container">
        <h1 class="welcome-text">Welcome {{ user.displayName }}</h1>
        <h2 class="welcome-text"></h2>
        <button class="google-signin"  @click="signOut">
            <img alt="Google logo" src="@/assets/Login_Page/logo.png" class="google-icon" />
            <span>Logout</span>
        </button>
        <button class="continue" @click="emit_log_event">Continue</button>
    </div>
    
</template>
<script>
  import { getAuth, GoogleAuthProvider, signInWithPopup, signOut, onAuthStateChanged } from "firebase/auth";
  
  export default {
    
    data() {
      return {
        user: null,
      };
    },
    methods: {
        emit_log_event() {
            this.$emit('custom-login-event', 'login');
        }, 
        signInWithGoogle() {
        const auth = getAuth();
        const provider = new GoogleAuthProvider();
  
        signInWithPopup(auth, provider)
          .then((result) => {
            this.user = result.user;
            console.log("Google Sign-In successful:", this.user);
          })
          .catch((error) => {
            console.error("Error during Google Sign-In:", error);
          });
      },
      signOut() {
        const auth = getAuth();
        signOut(auth)
          .then(() => {
            this.user = null;
            console.log("User signed out successfully.");
          })
          .catch((error) => {
            console.error("Error signing out:", error);
          });
      },
    },
    mounted() {
      const auth = getAuth();
      onAuthStateChanged(auth, (user) => {
        if (user) {
          this.user = user;
        } else {
          this.user = null;
        }
      });
    },
  };
  </script>
<style scoped>
    .main-container {
        background-color: #000000; /*Pure black background */
        color: #fff; /* White text color for contrast */
        position: fixed;
        top: 0;
        left: 0;
        height: 100%; /*Full-screen height */
        width: 100%; /*Full-screen height */

    }

    /* Styling for the welcome text */
    .welcome-text {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        width: 70%;
        height: 7%;
        background-color: #000000;
        margin: auto;
        margin-top: 7%;
        
    }

    .msg{
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        width: 70%;
        height: 7%;
        background-color: #000000;
        margin: auto;
        margin-top: 10%;
    }

    /*Styling for the Google sign-in button */
    .google-signin {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 20%;
        background-color: #fff;
        color: #000000;
        border: none;
        border-radius: 30px;
        padding: 12px 24px;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        margin: auto;
        margin-top: 3%;
    }
    
    .google-signin:hover {
        background-color: #87004d;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .continue{
        background-color: #fff;
        color: #000000;
        border: none;
        border-radius: 30px;
        padding: 12px 24px;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        margin-left: 90%;
        margin-top: 18%;
    }
    .continue:hover{
        background-color: #000000;
        color: white;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }


    .google-icon {
        width: 20px;
        height: 20px;
        margin-right: 12px;
    }
</style>