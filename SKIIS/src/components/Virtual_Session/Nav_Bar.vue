<template>
    <div class="nav-bar">
        <button id="back-but" @click="emit_leave_event">Back</button>
    </div>
</template>

<style>
    .nav-bar{
        width: 100%;
        height: 10%;
        position: fixed;
        background-color: aqua;
        display: flex;
        align-items: center;

    }
    #back-but{
        margin-left: 5%;
        background-color: rgb(58, 58, 58);
        color: white;
        font-size: 150%;
        font-weight: bold;
        border-radius: 25px;
        width: 10%;
        height: 50%;
        padding: 5px;
        border: solid;
        border-color: black;
        transition: 300ms;
        cursor: pointer;
    }
    #back-but:hover{
        border-color: white;
        background-color: white;
        color: black;
    }
</style>

<script>
    export default{
        methods:{
            emit_leave_event(){
                this.$emit('custom-leave-event', 'leave');
            }
        }
    }
</script>