<template>
    <div class="content-body">
        <div class="title-box">
            <div class="title">彝族银饰制作技艺</div>
        </div>
        <div class="content-box">
            {{ introduction }}
        </div>
        <div class="timeline-container">
            <el-timeline>
                <el-timeline-item v-for="(activity, index) in activities" :key="index" :hide-timestamp="true"  size="large" class="timeline-item-dot">
                    <div class="timeline-box">
                        <el-row :gutter="20">
                            <el-col :span="10">
                                <div class="timeline-title">
                                    <div class="main-title">{{activity.title}}</div>
                                    <div class="main-content">{{activity.content}}</div>
                                </div>
                            </el-col>
                            <el-col :span="14">
                                <div class="fig-title">{{activity.fig_title}}</div>
                                <div class="fig-container">
                                    <img :src="activity.fig_src" style="width: 110%; height: 110%"/>
                                    <div class="mask">
                                        <div class="bottom-line">
                                            <div class="fig-button">
                                                <div>下载</div>
                                            </div>
                                            <div class="fig-button">
                                                <div>收藏</div>
                                            </div>
                                            <div class="fig-button">
                                                <div>分享</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </el-col>
                        </el-row>
                    </div>
                </el-timeline-item>
            </el-timeline>
        </div>
    </div>
</template>

<script>
export default {
    name: 'detail',
    data(){
        return{
            introduction: '彝族银饰的制作技艺做工讲究，工艺复杂，每件银器的成形，都要经过熔、铸、锤、拉、敲、剪、焊、洗、宰、挖、挫、拧、雕、刻等多道工序。每个手工艺人可能会根据自己的经验和技术习惯进行微调和改进。这些工艺步骤需要耐心、技巧和细致的操作，以下时彝族银饰制作时较为常见的技艺种类。',
            activities: [
            ]
        }
    },
    methods: {
        get_ji_content(){
            let that = this
            this.$http.get('api/get_show_ji').then(res=>{
                that.activities = res.data.data
            }).catch(e=>{this.$message.error(e)})
        }
    },
    created(){
        this.get_ji_content()
    }
}
</script>

<style scoped>
.content-body{
    width: 100%;
    height: 80vh;
    color: #fff;
    overflow-y: auto;
    overflow-x: hidden;
}
.content-body::-webkit-scrollbar {
  width: 6px; /* 滚动条的宽度 */
}

.content-body::-webkit-scrollbar-track {
  background: transparent; /* 滚动条轨道的颜色 */
}

.content-body::-webkit-scrollbar-thumb {
  background-color: #3d3d3d; /* 滚动条本身的颜色 */
  border-radius: 4px; /* 滚动条圆角 */
}

.content-body::-webkit-scrollbar-thumb:hover {
  background: #555; /* 滚动条鼠标悬停时的颜色 */
}
.title-box{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
}
.title{
   font-family: DongfangDakai;
   font-size: 7vh;
}
.content-box{
    width: 90%;
    margin-left: 5%;
    min-height: 8vh;
    font-size: 2vh;
    text-align: left;
    margin-top: 30px;
    text-indent: 2em
}
.timeline-container{
    width: 100%;
    min-height: 50vh;
    padding: 20px;
    margin-top: 20px;
    box-sizing: border-box;
}
.timeline-box{
    width: 100%;
    min-height: 40vh;
    box-sizing: border-box;
}
.timeline-item-dot /deep/ .el-timeline-item__node--large{
    width: 58px;
    height: 50px;
    left: -27px;
}
.timeline-item-dot /deep/ .el-timeline-item__node{
    position: absolute;
    background-image: url('../../../assets/flower.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-color: transparent;
}
.timeline-title{
    width: 100%;
    min-height: 20vh;
    box-sizing: border-box;
    padding-left: 20px;
    padding-right: 20px;
    padding-bottom: 20px;
    color: #fff
}
.main-title{
    font-size: 5vh;
    font-family: cursive;
    font-weight: bolder;
    text-align: left;
}
.main-content{
    margin-top: 20px;
    font-size: 2vh;
    text-align: left;
}
.fig-title{
    font-size: 5vh;
    font-family: cursive;
    text-align: left;
    color: #fff;
    font-weight: bolder;
}
.fig-container{
    width: 100%;
    height: 30vh;
    margin-top: 20px;
    position: relative;
    display: block;
}
.mask{
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    right: 0;
    color: #fff
}
.bottom-line{
    position: absolute;
    width: 100%;
    bottom: 0;
    color: fff;
    box-sizing: border-box;
    padding-bottom: 20px;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
}
.fig-button{
    width: 13%;
    height: 3vh;
    border: 1px solid #fff;
    display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  border-radius: 2vh;
  margin-left: 20px;
  font-size: 1.5vh;
  cursor: pointer;
  transition: all .3s ease-out
}
.fig-button:hover{
    background: #fff;
    color: #0c1429
}
</style>