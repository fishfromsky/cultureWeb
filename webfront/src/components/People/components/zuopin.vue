<template>
    <div class="zuopin-body">
        <el-row :gutter="20">
            <el-col :span="6">
                <Search :category_list="category_list"></Search>
            </el-col>
            <el-col :span="18">
                <Dataset :dataset="item_data"></Dataset>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import Search from './search.vue';
import Dataset from './dataset.vue'
export default{
    name: 'zuopin',
    props: {
        person_id: {
            type: Number,
            required: true
        }
    },
    components: {
        Search,
        Dataset
    },
    data(){
        return{
            category_list: [],
            item_data: []
        }
    },
    created(){
        let params = {
            'id': this.person_id
        }
        this.$http({
            url: 'api/get_workman_zuopin',
            method: 'GET',
            params: params
        }).then(res=>{
            let work_list = res.data.data
            this.item_data = res.data.data
            for (let i=0; i<work_list.length; i++){
                let index = this.category_list.indexOf(work_list[i].category)
                if (index == -1){
                    this.category_list.push(work_list[i].category)
                }
            }
        }).catch(e=>{this.$message.error(e)})
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