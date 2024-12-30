<script setup>
import Login_Window from './components/Login_Page/Login_Window.vue'
import Feed_Page from './components/Home_Page/Feed_Page.vue'
import Video_Meet from './components/Virtual_Session/Video_Meet.vue'
import Profile from './components/Profile_Page/Profile.vue'
import Add_window from './components/Profile_Page/Add_window.vue'
</script>

<template>
  <Login_Window v-if="trig_login" @custom-login-event="handleLoginEvent"> </Login_Window>
  <Feed_Page v-if="trig_feed" @custom-video-event="handleVideoEvent" @custom-logout-event="handleLogoutEvent" @custom-profile-event="handleProfileEvent"></Feed_Page>
  <Profile v-if="trig_goback" @custom-goback-event="handleGoBackEvent" name="RIP" email="ripskillan312004@gmail.com"></Profile>
  <Video_Meet v-if="trig_video" @custom-leave-event="handleLeaveEvent"></Video_Meet>
</template>

<style scoped>
  
</style>

<script>
  export default {
    data() {
      return {
        trig_login: true,
        trig_video: null,
        trig_feed: null,
        trig_goback:null
      };
    },
    methods: {
      handleLoginEvent(data) {
        this.trig_feed = true;
        this.trig_login = null;
        console.log(data)
      },
      handleVideoEvent(data) {
        this.trig_video = true;
        this.trig_feed = null;
        console.log(data)
      },
      handleLogoutEvent(data){
        this.trig_login=true;
        this.trig_feed = null;
        console.log(data)
      },
      handleGoBackEvent(data){
        this.trig_feed = true;
        this.trig_goback = null;
        console.log(data)
      },
      handleProfileEvent(data){
        this.trig_goback = true;
        this.trig_feed = null;
        console.log(data);
      },
      handleLeaveEvent(data){
        this.trig_feed = true;
        this.trig_video = null;
        console.log(data);
      }
    }
  };
</script>
