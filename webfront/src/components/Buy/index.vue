<template>
    <div class="main-body">
        <el-row :gutter="20">
            <el-col v-if="selected == 0" :span="5">
                <Drawer @person="handle_person" @decorate="handle_decorate" @material="handle_meterial"></Drawer>
            </el-col>
            <el-col v-if="selected == 0" :span="17">
                <Shop @selectGoods="select_goods" :category_id="category_id" :person_id="person_id"></Shop>
            </el-col>
            <el-col v-if="selected == 1" :span="22">
                <Detail @back="handle_back" :goods_id="goods_id"></Detail>
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
import Detail from './components/detail.vue'
export default {
    name: 'Buy',
    components: {
        Drawer,
        Shop,
        Center,
        Detail
    },
    data(){
        return{
            person_id: [],
            category_id: [],
            selected: 0,
            goods_id: -1,
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
        handle_back(val){
            this.selected = val
        },
        select_goods(val){
            this.selected = 1;
            this.goods_id = val
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
    height: 90vh;
    background-color: #131e3a;
    background-image: url('../../assets/main_bg_si.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    box-sizing: border-box;
    padding: 60px
}
</style>