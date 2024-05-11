<template>
    <div class="detail-body">
        <el-row :gutter="20">
            <el-col :span="8">
                <news_card @showmore="toDongtai" @detail_news="handle_news" :news="news" :title="'新闻动态'"></news_card>
            </el-col>
            <el-col :span="8">
                <news_card @showmore="toActivity" :news="activity" @detail_news="handle_news" :title="'活动信息'"></news_card>
            </el-col>
            <el-col :span="8">
                <news_card @showmore="toStudy" :news="study" :title="'研究成果'"></news_card>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import news_card from './components/card.vue'
export default {
    name: 'Wen',
    components: {
        news_card
    },
    data(){
        return{
            news: [],
            activity: [],
            study: []
        }
    },
    methods:{
        init_data(){
            let that = this
            this.$http.get('api/get_news').then(res=>{
                let data = res.data.data
                for (let i=0; i<data.length; i++){
                    if (data[i].category == 0){
                        that.news.push(data[i])
                    }
                    else if (data[i].category == 1){
                        that.activity.push(data[i])
                    }
                    else{
                        that.study.push(data[i])
                    }
                }
            }).catch(e=>{this.$message.error(e)})
        },
        handle_news(res){
            this.$router.push({path:'/news_detail',query: {id: res}, replace: true})
        },
        toDongtai(){
            console.log('新闻动态')
        },
        toActivity(){
            this.$emit('showdetail', 1)
        },
        toStudy(){
            console.log('研究')
        }
    },
    created(){
        this.init_data()
    }
}
</script>

<style scoped>
</style>