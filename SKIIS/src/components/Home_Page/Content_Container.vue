<script setup>

</script>

<!-- <template>
    <div class="container">
        <h1 class="message">{{ title }}</h1>
        <p class="description">{{ desc }}</p>
    </div>
</template> -->

<style scoped>
    .container{
        background-color: rgb(58, 58, 58);
        width: 35%;
        height: 30%;
        border-radius: 10px;
        margin: 5%;
        display: flex;
        flex-direction: column;
        padding: 2%;
    }
    .message{
        font-size: 2rem;
        align-self: center;
        font-weight: bold;
        height: 30%;
        color: rgb(255, 74, 237);
    }
    .description{
        font-size: 1.25rem;
        color: wheat;
        
    }
</style>
<script>
    export default {
    props: ['title','desc']
    }
</script>