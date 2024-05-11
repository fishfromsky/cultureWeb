<template>
    <div class="show-body">
        <div class="card" v-for="(item, idx) in content" :key="idx">
            <div class="divider">
                <div class="dot"></div>
                <div class="line"></div>
                <div class="right-item">
                </div>
            </div>
            <el-row :gutter="20">
                <el-col :span="10">
                    <div class="img-box">
                        <div class="img">
                            <img :src="item.img" style="width: 100%; height: 100%;"> 
                        </div>
                    </div>
                </el-col>
                <el-col :span="14">
                    <div class="news-title">{{ item.title }}</div>
                    <div class="source">
                        <div>{{ item.news_time }}</div>
                        <div>来源:&nbsp;{{ item.source }}</div>
                    </div>
                    <div class="content">{{ item.sub_content }}</div>
                    <div class="more" @click="showmore(item.id)">
                        <div class="text-box">
                            <div class="more-text">查看更多</div>
                        </div>
                        <div class="go">
                            <div class="icon-go">
                                <i class="el-icon-arrow-right"></i>
                            </div>
                        </div>
                    </div>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
export default{
    name: 'show-body',
    props: {
        content: {
            type: Array,
            required: true,
            default: []
        }
    },
    data(){
        return{

        }
    },
    methods: {
        showmore(val){
            this.$router.push({path:'/news_detail',query: {id: val}, replace: true})
        }
    }
}
</script>

<style scoped>
.show-body{
    width: 100%;
    height: 66vh;
    overflow-y: auto;
    overflow-x: hidden;
}
.main-card::-webkit-scrollbar {
  width: 6px; /* 滚动条的宽度 */
}

.main-card::-webkit-scrollbar-track {
  background: transparent; /* 滚动条轨道的颜色 */
}

.main-card::-webkit-scrollbar-thumb {
  background-color: #3d3d3d; /* 滚动条本身的颜色 */
  border-radius: 4px; /* 滚动条圆角 */
}
.card{
    width: 100%;
    height: 33vh;
}
.divider{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}
.dot{
    width: 1vh;
    height: 1vh;
    background-color: #fff;
    border-radius: 50%;
}
.line{
    width: 90%;
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
    margin-top: 2vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.img{
    width: 65%;
    height: 25vh;
}
.news-title{
    color: #fff;
    font-size: 4vh;
    text-align: left;
}
.source{
    margin-top: 10px;
    width: 90%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    color: #fff;
    font-size: 2vh;
}
.content{
    width: 90%;
    margin-top: 20px;
    color: #fff;
    font-size: 2vh;
    text-align: left;
}
.more{
    margin-top: 15px;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    cursor: pointer;
}
.go{
    width: 2vh;
    height: 2vh;
    border-radius: 50%;
    background-color: #fff;
    margin-left: -1%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.icon-go{
    font-size: 1.5vh;
}
.text-box{
    width: 15%;
    height: 4vh;
    border: 1px solid #fff;
    border-radius: 2vh;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.more-text{
    font-size:2.5vh;
    color: #fff;
}
</style>