<script setup>
    import Nav_Bar from './Nav_Bar.vue'
    import Content_Container from './Content_Container.vue';
</script>

<template>
    <div class="feedmain">
        <Nav_Bar @custom-logout-event="emit_logot_event"/>
        <div class="content">
            <Content_Container title="I Wanna Learn React" desc="I'm a 2nd year student interested in learning react"></Content_Container>
            <Content_Container title="Teach me Blender" desc="I love building stuff but can't model for the life of me, so i wanna try learning 3D modelling in blender and build 3D printed models's of my own"></Content_Container>
            <Content_Container title="I wanna learn Japanese" desc="Could anybody help learn Japanese, I'm a huge otaku but I can't learn it quick enough since I don't have anyone to practice with."></Content_Container>
            <Content_Container title="Help me Master Vue" desc="I'm undergrad student and I know basics of web dev (html,css,js) quite well. But I tried learning view and it was Hell. I can't bring myself to understand how it truly works"></Content_Container>  
            <Content_Container></Content_Container>
            <Content_Container></Content_Container>  
        </div>
        <div class="nav-menu">
            <button class="dumb-expan" @click="emit_profile_event">Profile</button>
            <button class="dumb-expan">Settings</button>
        </div>
        <button class="video_meet" @click="emit_video_event">Video Meet</button>       
    </div>
</template>

<style scoped>
    .dumb-expan{background-color: rgb(58, 58, 58);
        color: white;
        font-size: 150%;
        font-weight: bold;
        border-radius: 25px;
        width: 80%;
        padding: 5px;
        border: solid;
        border-color: black;
        transition: 300ms;
        cursor: pointer;
        margin-top: 10%;
        margin-left: 10%;
    }
    .dumb-expan:hover{
        border-color: white;
        background-color: white;
        color: black;
    }
    .nav-menu{
        position: fixed;
        width: 20%;
        height: 100%;
        background-color: rgb(15, 15, 15);bottom: 10%;
        border: solid;
        border-radius: 30px;
        right: -17%;
        bottom: 0%;
        transition: 1s;
    }
    .nav-menu:hover{
        right: 0%;
    }
    .video_meet{
        background-color: rgb(58, 58, 58);
        color: white;
        font-size: 180%;
        font-weight: bold;
        border-radius: 100px;
        padding: 5px;
        border: solid;
        border-color: black;
        transition: 300ms;
        height: 10%;
        width: 10%;
        cursor: pointer;
        position: fixed;
        bottom: 10%;
        right: 7%;
        z-index: 999; /* Ensure it's above other elements */
    }
    .video_meet:hover{
        border-color: white;
        background-color: white;
        color: black;
    }
    .feedmain{
        background-color: black;
        position: fixed;
        top: 0;
        left: 0;
        height: 100%; /*Full-screen height */
        width: 100%;
    }
    .content{
        padding: 2% 10% 0%;
        height: 100%;
        display: flex;
        flex-wrap: wrap;
        overflow-y: scroll;
    }
</style>

<script>
    export default{
        methods: {
            emit_video_event() {
                this.$emit('custom-video-event', 'video');
            },
            emit_logot_event(){
                this.$emit('custom-logout-event', 'logout');
            },
            emit_profile_event(){
                this.$emit('custom-profile-event', 'profile');
            }
        }
    }
</script>