<template>
    <div class="news-body">
        <div class="title">{{ news.title }}</div>
        <div class="source">
            <div class="source-text">来源:&nbsp {{ news.source }}</div>
            <div class="source-text">时间:&nbsp; {{ news.news_time }}</div>
        </div>
        <div class="divider">
            <div class="dot"></div>
            <div class="line"></div>
            <div class="right-item">
            </div>
        </div>
        <div class="img-box">
            <img :src="news.img" style="width: 100%; height: 100%;">
        </div>
        <div class="content">{{ news.content }}</div>
    </div>
</template>

<script>
export default{
    name: 'news_detail',
    data(){
        return{
            news: {}
        }
    },
    methods: {
        get_news_by_id(id){
            let that = this
            let data = {}
            data.id = id
            this.$http({
                url: 'api/get_specific_news',
                params: data,
                method: 'GET'
            }).then(res=>{
                that.news = res.data.news
            }).catch(err=>{this.$message.error(err)})
        }
    },
    created(){
        let id = this.$route.query.id
        this.get_news_by_id(id)
    }
}
</script>

<style scoped>
.news-body{
    width: 100%;
    min-height: 90vh;
    background-color: #131e3a;
    box-sizing: border-box;
    padding: 40px
}
.source{
    margin-top: 20px;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}
.source-text{
    color: #fff;
    font-size: 2.2vh;
}
.title{
    width: 100%;
    font-size: 5vh;
    color: #fff;
    text-align: center;
    font-family: DongfangDakai;
}
.content{
    margin-top: 4vh;
    color: #fff;
    font-size: 2vh;
    line-height: 3vh;
    text-align: left;
}
.divider{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
}
.dot{
    width: 1vh;
    height: 1vh;
    background-color: #fff;
    border-radius: 50%;
}
.line{
    width: 100%;
    height: 0.1vh;
    background-color: #fff;
}
.right-item{
    width: 3.5vh;
    height: 3.5vh;
    background-image: url('../../../assets/wen/nav_right.png');
    background-position: -1vh center;
    background-size: 100% 100%;
    background-repeat: no-repeat;
}
.img-box{
    width: 80%;
    margin-left: 10%;
    height: 70vh;
    margin-top: 20px
}
</style>