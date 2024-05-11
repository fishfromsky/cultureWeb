<template>
    <div class="detail-body">
        <el-row :gutter="40">
            <el-col :span="13">
                <el-carousel height="60vh" class="carousel" indicator-position="outside">
                    <el-carousel-item v-for="item in card_item" :key="item">
                        <img :src="item" style="width: 100%; height: 100%;">
                    </el-carousel-item>
                </el-carousel>
            </el-col>
            <el-col :span="11">
                <div class="content-box">
                    <div class="title-box">{{ title }}</div>
                    <div class="content-detail">{{ content }}</div>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
export default{
    name: 'detail',
    data(){
        return{
            card_item: [],
            title: '',
            content: ''
        }
    },
    created(){
        let that = this
        let id = this.$route.query.id
        let params = {
            'id': id
        }
        this.$http({
            url: 'api/get_material_detail',
            method: 'GET',
            params: params
        }).then(res=>{
            let code = res.data.code
            if (code != 0){
                that.card_item = res.data.data.img
                that.title = res.data.data.title
                that.content = res.data.data.content
            }
        }).catch(e=>{this.$message.error(e)})
    }
}
</script>

<style scoped>
.detail-body{
    width: 100%;
    height: 90vh;
    background-color: #0c1429;
    box-sizing: border-box;
    padding: 40px;
    color: #fff;
}
.carousel{
    margin-top: 8vh;
}
.detail-body /deep/ .el-carousel__arrow{
    font-size: 40px;
}
.content-box{
    margin-top: 10vh;
    width: 100%;
    min-height: 60vh;
}
.title-box{
    width: 100%;
    text-align: center;
    font-family: DongfangDakai;
    font-size: 7vh;
}
.content-detail{
    margin-top: 20px;
    font-size: 2.3vh;
    text-align: left;
    line-height: 32px;
    text-indent: 2em;
}
</style>