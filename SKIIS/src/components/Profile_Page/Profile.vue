<script setup>
import Add_window from './Add_window.vue'
</script>

<template>
    <div class="profile-container">
        <div class="personal-details">
            <div class="picture">
                <img class="profile-pic" src="./../../assets/Profile/profile_pic.jpg"/> 
            </div>
            <div class="details">
                <p>Name: {{ name }}</p>
                <p>Email: {{ email }}</p>
                <button class="edit">Edit Profile</button>
            </div>
        </div>
        <div class="public-stats">
            <div class="activity">
                <button class="commision" id="but1">Requests</button>
                <button class="commision" id="but2">Accepted</button>
            </div>
            <button class="add" @click="open_add_window">Add +</button>
            <div class="about">
                <div class="box"> </div>
                <div class="box"> </div>
                <button id="goback" @click="emit_goback_event">Back</button>
            </div>
        </div>
    </div>
    <Add_window v-if="trig_add" @custom-add-event="handleAddEvent"></Add_window>
</template>

<style scoped>
    #goback{
        background-color: rgb(58, 58, 58);
        color: white;
        font-size: 180%;
        font-weight: bold;
        border-radius: 100px;
        padding: 5px;
        border: solid;
        border-color: black;
        transition: 300ms;
        height: 7%;
        width: 10%;
        cursor: pointer;
        position: fixed;
        bottom: 5%;
        right: 7%;
        z-index: 999; 
    }
    #goback:hover{
        border-color: white;
        background-color: white;
        color: black;
    }
    .about{
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        height: 100%;
    }
    .box{
        background-color: rgb(74, 74, 74);
        height: 40%;
        width: 40%;
    }
    .add{
        height: 7%;
        margin: 5% 5% 5% 70% ;
        width: 15%;
        font-size: 1.5rem;
        font-weight: bold;
        color: white;
        background-color: blue;
        border-radius: 50px;
        transition: 300ms;
        cursor: pointer;
    }
    .add:hover{
        border: solid;
        border-color: black;
        color: black;
    }
    .commision{
        height: 50%;
        width: 20%;
        margin: 10% 0%;
        font-size: 2rem;
        font-weight: bold;
        border-radius: 25px;
        cursor: pointer;
        transition: 300ms;
        border: solid;
        color: rgb(0, 0, 0);
    }
    #but1{
        background-color: purple;
    }
    #but2{
        background-color: rgb(34, 254, 0);
    }
    .commision:hover{
        background-color: black;
        color: white;
    }
    .activity{
        height: 25%;
        width: 100%;
        display: flex;
        justify-content: space-evenly;
    }

    .profile-container{
        position: fixed;
        top: 0;
        left: 0;
        height: 100%; /*Full-screen height */
        width: 100%; /*Full-screen height */
        display: flex;
        flex-direction: row;
    }
    .personal-details{
        background-color: rgb(36, 36, 36);
        width: 40%;
    }
    .public-stats{
        background-color: rgb(20, 20, 20);
        width: 60%;
    }
    .picture{
        justify-content: center;
        display: flex;
        height: 40%;
    }
    .profile-pic{
        height: 70%;
        border-radius: 50%;
        margin: 10%;
    }
    .details{
        font-size: 1.5rem;
        color: white;
        font-weight: bolder;
        margin: 0% 10%;
    }
    .edit{
        background-color: rgb(58, 58, 58);
        color: white;
        font-size: 70%;
        font-weight: bold;
        border-radius: 25px;
        width: 30%;
        padding: 5px;
        border: solid;
        border-color: black;
        transition: 300ms;
        cursor: pointer;
    }
    .edit:hover{
        border-color: white;
        background-color: white;
        color: black;
    }
</style>

<script>
    export default {
        props: ['name','email'],
        data() {
            return {
                isBlurred: false,
                trig_add: null
            };
        },
        methods: {
            open_add_window(){
                this.trig_add = true;
            },
            handleAddEvent(data){
                this.trig_add = null;
            },
            emit_goback_event(){
                this.$emit('custom-goback-event', 'goback'); 
            }
                       
        }
    }
</script>