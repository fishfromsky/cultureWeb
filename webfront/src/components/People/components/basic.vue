<template>
    <div class="basic-body">
        <div class="title">
            <div class="logo logo-left" style="margin-right: 10px;"></div>
            <div class="title-text">{{ infoBody.name }}:&nbsp;{{ infoBody.title }}</div>
            <div class="logo logo-right" style="margin-left: 10px;"></div>
        </div>
        <div class="avatar-box">
            <el-row>
                <el-col :span="9">
                    <div class="img-box">
                        <div class="img">
                            <img :src="infoBody.koutu" style="width: 100%; height: 100%;">
                        </div>
                    </div>
                </el-col>
                <el-col :span="15">
                    <div class="content-box">
                        <div class="avatar-title">
                            <div class="flower"></div>
                            <div class="line"></div>
                            <div class="point"></div>
                            <div class="avatar-text">基本信息</div>
                        </div>
                        <div class="nation">
                            <div class="original-text">民族:&nbsp;{{ infoBody.ethic }}</div>
                            <div class="original-text">出生日期:&nbsp;{{ infoBody.birthday }}</div>
                        </div>
                        <div class="introduce-box">
                            {{ infoBody.introduction }}
                        </div>
                        <div class="avatar-title">
                            <div class="flower"></div>
                            <div class="line"></div>
                            <div class="point"></div>
                            <div class="avatar-text">所获荣誉</div>
                        </div>
                        <div class="introduce-box">
                            {{ infoBody.honor }}
                        </div>
                   </div>
                </el-col>
            </el-row>
        </div>
        <div class="avatar-title">
            <div class="flower"></div>
            <div class="line" style="width: 90%;"></div>
            <div class="point"></div>
        </div>
        <div class="shop-title">
            <div class="logo logo-left"></div>
            <div class="logo-text">{{ infoBody.name }}银饰店</div>
            <div class="logo logo-right"></div>
        </div>
        <el-row>
            <el-col :span="12">
                <div class="shop-img-box">
                    <div class="shop-img">
                        <img :src="shopInfo.img" style="width: 100%; height: 100%;">
                    </div>
                </div>
            </el-col>
            <el-col :span="12">
                <div class="shop-text">
                    <div class="shop-text-box">
                        <div class="shop-text-style">法人代表:&nbsp;{{ infoBody.name }}</div>
                        <div class="shop-text-style">成立日期:&nbsp;{{ shopInfo.found_time }}</div>
                        <div class="shop-text-style">经营范围:&nbsp;{{ shopInfo.range }}</div>
                        <div class="shop-text-style">店铺地址:&nbsp;{{ shopInfo.address }}</div>
                        <div class="shop-text-style">联系电话:&nbsp;{{ shopInfo.contact }}</div>
                    </div>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
export default{
    name: 'basic',
    props: {
        infoBody: {
            type: Object,
            required: true,
            default: null
        }
    },
    data(){
        return{
            shopInfo: {}
        }
    },
    watch:{
        infoBody(val){
            let that = this
            let params = {
                'id': val.id
            }
            this.$http({
                url: 'api/get_shop_info',
                params: params,
                method: 'GET'
            }).then(res=>{
                that.shopInfo = res.data.data
            }).catch(res=>{this.$message.error(res)})
        }
    },
}
</script>

<style scoped>
.title{
    margin-top: 8vh;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}
.title-text{
    font-size: 5vh;
    color: #fff;
    font-family: DongfangDakai;
}
.logo{
    width: 5vh;
    height: 5vh;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
}
.logo-left{
    background-image: url('../../../assets/wen/left.png');
}
.logo-right{
    background-image: url('../../../assets/wen/right.png');
}
.avatar-box{
    width: 100%;
    min-height: 40vh;
}
.img-box{
    width: 100%;
    height: 70vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.img{
    width: 50vh;
    height: 50vh;
}
.content-box{
    margin-top: 5vh;
    width: 100%;
    box-sizing: border-box;
    padding-right: 90px;
}
.avatar-title{
    margin-top: 10px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}
.flower{
    width: 5vh;
    height: 5vh;
    background-image: url('../../../assets/people/flower.png');
    background-position: center -1vh;
    background-repeat: no-repeat;
    background-size: 100% 100%;
}
.line{
    width: 77%;
    height: 0.1vh;
    background-color: #fff;
}
.point{
    width: 1.5vh;
    height: 1.5vh;
    background-color: #fff;
    border-radius: 50%;
}
.avatar-text{
    font-size: 2vh;
    color: #fff;
    margin-left: 10px;
}
.nation{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between
}
.original-text{
    margin-top: 10px;
    color: #fff;
    font-size: 2vh;
}
.introduce-box{
    margin-top: 10px;
    text-align: left;
    width: 100%;
    min-height: 10vh;
    color: #fff;
    font-size: 2vh;
}
.shop-title{
    width: 100%;
    color: #fff;
    font-size: 3vh;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    margin-left: 10%;
}
.logo-text{
    color: #fff;
    font-family: DongfangDakai;
    font-size: 5vh;
}
.shop-img-box{
    width: 100%;
    height: 60vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.shop-img{
    width: 70%;
    height: 40vh;
}
.shop-text{
    color: #fff;
    font-size: 2vh;
    width: 100%;
    height: 60vh;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
}
.shop-text-box{
    width: 100%;
    height: 40vh;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: flex-start;
}
.shop-text-style{
    color: #fff;
    font-size: 2.5vh;
}
</style>