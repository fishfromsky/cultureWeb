<template>
    <div class="main-body">
        <news_detail v-if="show==false" @showdetail="handle_detail"></news_detail>
        <news_show v-if="show==true" @backpage="backpage"></news_show>
    </div>
</template>

<script>
import news_detail from './news_detail.vue'
import news_show from './news_show.vue'
export default {
    name: 'Wen',
    components: {
        news_detail,
        news_show
    },
    data(){
        return{
            news: [],
            activity: [],
            study: [],
            show: false
        }
    },
    methods:{
        handle_detail(val){
            this.show = true
        },
        backpage(){
            this.show = false
        },
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
        }
    },
    created(){
        this.init_data()
    }
}
</script>

<style scoped>
.main-body{
    width: 100%;
    height: 90vh;
    background-color: #131e3a;
    background-image: url('../../assets/main_bg_wen.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    box-sizing: border-box;
    padding: 20px;
}
</style>