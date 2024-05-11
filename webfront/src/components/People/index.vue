<template>
    <div class="people-body">
        <Main v-if="selected == 0" @showinfo="handle_info"></Main>
        <Info v-if="selected == 1" @goBack="go_back" :infoid="people_id"></Info>
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
.people-body{
    width: 100%;
    min-height: 90vh;
    background-color: #131e3a;
    box-sizing: border-box;
}

</style>