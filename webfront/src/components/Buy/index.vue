<template>
    <div class="main-body"> 
        <el-row :gutter="20">
            <el-col :span="5">
                <Drawer @person="handle_person" @decorate="handle_decorate" @material="handle_meterial"></Drawer>
            </el-col>
            <el-col :span="17">
                <Shop :category_id="category_id" :person_id="person_id"></Shop>
            </el-col>
            <el-col :span="2">
                <Center></Center>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import Drawer from './components/drawer.vue'
import Shop from './components/shop.vue'
import Center from './components/center.vue'
export default {
    name: 'Buy',
    components: {
        Drawer,
        Shop,
        Center
    },
    data(){
        return{
            person_id: [],
            category_id: []
        }
    },
    methods: {
        handle_person(val){
            if (val < 0){
                val = -val
                let index = this.person_id.indexOf(val)
                this.person_id.splice(index, 1)
            }
            else{
                this.person_id.push(val)
            }
        },
        handle_decorate(val){
            if (val < 0){
                val = -val
                let index = this.category_id.indexOf(val)
                this.category_id.splice(index, 1)
            }
            else{
                this.category_id.push(val)
            }
        },
        handle_meterial(val){
            if (val < 0){
                val = -val
                let index = this.category_id.indexOf(val)
                this.category_id.splice(index, 1)
            }
            else{
                this.category_id.push(val)
            }
        }
    }
}
</script>

<style scoped>
.main-body{
    width: 100%;
    min-height: 90vh;
    background-color: #131e3a;
    box-sizing: border-box;
    padding: 60px
}
</style>