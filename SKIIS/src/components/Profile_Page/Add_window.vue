<script setup>

</script>

<template>
    <div class="window">
        <label id="skill">What New Skills Do Ya Have???</label>
        <input id="skill-input" type="text" />
        <button id="add-skill" @click="emit_add_event">Add Skill</button>
    </div>
</template>

<style scoped>
    #add-skill{
        background-color: rgb(82, 81, 81);
        color: rgb(0, 0, 0);
        border-radius: 5px;
        height: 10%;
        width: 50%;
        font-weight: bold;
        font-size: 1.5rem;
        transition: 300ms;
        cursor: pointer;
        margin-top: 50%;
    }
    #add-skill:hover{
        background-color: black;
        color: white;
        border: solid;
    }
    .window{
        position: fixed;
        top: 0;
        left: 0;
        margin: 2% 32%;
        width: 36%;
        height: 90%;
        background-color: rgb(0, 0, 0);
        border-radius: 25px;
        padding: 10% 5%;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    #skill{
        font-size: 2rem;
        color: white;
    }
    #skill-input{
        margin-top: 10%;
        font-size: 1.5rem;
        position: fixed;
        height: 5%;
        width: 20%;
        border-radius: 10px;
    }
</style>

<script>
    export default{
        methods: {
            emit_add_event() {
                this.$emit('custom-add-event', 'add')
            },
            emit_goback_event(){
                this.$emit('custom-video-event', 'video');
            }
        }
    }
</script>