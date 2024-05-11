<template>
    <div class="people-body">
        <div class="back" @click="go_back"></div>
        <Main v-if="selected == 0" @showinfo="handle_info"></Main>
        <Info v-if="selected == 1" :infoid="people_id"></Info>
    </div>
</template>

<script>
import Main from './main.vue'
import Info from './info.vue'
export default {
    name: 'People',
    components: {
        Main,
        Info
    },
    data(){
        return{
            selected: 0,
            people_id: 0
        }
    },
    methods: {
        handle_info(val){
            this.people_id = val
            this.selected = 1
        },
        go_back(){
            this.selected = 0
        }
    },
    created(){
       
    }
}
</script>

<style scoped>
.back{
    width: 4vh;
    height: 4vh;
    position: absolute;
    top: 14vh;
    left: 4%;
    background-image: url('../../assets/back.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    cursor: pointer;
    z-index: 1000;
}
.people-body{
    width: 100%;
    min-height: 90vh;
    background-color: #131e3a;
    box-sizing: border-box;
}

</style>