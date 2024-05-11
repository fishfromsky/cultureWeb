<template>
    <div class="wen-body">
        <el-row :gutter="20">
            <el-col :span="12">
                <div class="main-content">
                    <div class="main-content-title">{{ main_title }}</div>
                    <div class="main-content-text">{{ main_content }}</div>
                </div>
                <ChildComponent :child_title="detail_list.title" :child_content="detail_list.content"></ChildComponent>
            </el-col>
            <el-col :span="12">
                <Carousel @carouselChange="handle_carousel" :card="detail_card"></Carousel>
            </el-col>
        </el-row>
        <bottomNavigator @changeWen="handle_change"></bottomNavigator>
    </div>
</template>

<script>
import ChildComponent from './wen_component.vue'
import Carousel from './carousel.vue'
import bottomNavigator from './bottom_navigate.vue'
export default{
    name: 'wen',
    components: {
        ChildComponent,
        Carousel,
        bottomNavigator
    },
    data(){
        return{
            getData: false,
            main_title: '',
            main_content: '',
            detail_card: [{title: '', vice_src: ['','']}],
            detail_list: {
                title: '', content: ''
            },
        }
    },
    methods: {
        handle_carousel(val){
            let that = this
            let params = {
                'card_id': val
            }
            this.$http({
                url: 'api/get_wen_title',
                method: 'GET',
                params: params
            }).then(res=>{
                that.detail_list.title = res.data.title
                that.detail_list.content = res.data.content
            }).catch(e=>{this.$message.error(e)})
        },
        get_detail(val){
            let params = {
               'id': val 
            }
            let that = this
            this.$http({
                url: 'api/get_wen_detail',
                params: params,
                method: 'GET'
            }).then(res=>{
                let return_list = res.data.data
                if (return_list.length == 0){
                    that.detail_list.title = ''
                    that.detail_list.content = ''
                    that.detail_card = []
                }
                else{
                    for (let i=0; i<return_list.length; i++){
                        let detail_item = return_list[i]
                        detail_item.vice_src = detail_item.vice_src.split(',')
                        return_list[i] = detail_item
                        if (i == 0){
                            that.detail_list.title = detail_item.title
                            that.detail_list.content = detail_item.content
                        }
                    }
                    that.detail_card = return_list
                }
            })
            .catch(e=>{this.$message.error(e)})
        },
        handle_change(val){
            let that = this
            let params = {
                'id': val
            }
            this.$http({
                url: 'api/get_show_content',
                params: params,
                method: 'GET'
            }).then(res=>{
                if (res.data.status == 1){
                    that.main_title = res.data.data.title
                    that.main_content = res.data.data.content
                }
                else{
                    that.main_title = ''
                    that.main_content = ''
                }
                that.get_detail(val)
            }).catch(e=>{this.$message.error(e)})
        }
    },
    created(){
        this.handle_change(0)
    }
}
</script>

<style scoped>
.wen-body{
    width: 100%;
    box-sizing: border-box;
    padding: 20px;
    color: #fff
}
.main-content{
    width: 100%;
}
.main-content-title{
    width: 100%;
    text-align: center;
    font-family: DongfangDakai;
    font-size: 5vh;
}
.main-content-text{
    width: 100%;
    font-size: 2vh;
    text-align: left;
    text-indent: 2em;
    margin-top: 30px;
}
</style>