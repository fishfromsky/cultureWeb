<template>
    <div class="zuopin-body">
        <el-row :gutter="20">
            <el-col :span="6">
                <Search></Search>
            </el-col>
            <el-col :span="18"></el-col>
        </el-row>
    </div>
</template>

<script>
import Search from './search.vue';
export default{
    name: 'zuopin',
    components: {
        Search
    },
    data(){
        return{

        }
    }
}
</script>

<style scoped>
.zuopin-body{
    width: 100%;
    height: 90vh;
    box-sizing: border-box;
    padding: 40px;
    padding-left: 10%;
}
</style>