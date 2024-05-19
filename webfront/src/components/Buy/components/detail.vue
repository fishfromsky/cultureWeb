<template>
    <div class="detail">
        <div class="back" @click="back"></div>
        <el-row style="margin-top: 2vh;">
            <el-col :span="10">
                <div class="detail-container">
                    <div class="detail-list">
                        <div class="small-img" v-for="(item, idx) in goods_info.child_list" :key="idx" :class="[idx == selected_goods? 'small-img-active': 'small-img-no-active']" @click="select_size(idx)">
                            <img :src="item" style="width: 100%; height: 100%;">
                        </div>
                    </div>
                    <div class="detail-img-box">
                        <img :src="goods_info.child_list[selected_goods]" style="width: 100%; height: 100%;">
                    </div>
                </div>
            </el-col>
            <el-col :span="14">
                <div class="content-box">
                    <div class="title-box">
                        <div class="title">{{ goods_info.name }}</div>
                    </div>
                    <div class="price-list">
                       <div class="price-text">
                        &yen {{ goods_info.prices[selected_goods] }}
                       </div>
                       <div class="pay-count">{{ pay_count }}人已付款</div>
                    </div>
                    <div class="address-list">
                        <div class="peisong">配送：</div>
                        <div class="address-text" style="margin-left: 20px;">西昌市</div>
                        <div class="address-text" style="margin-left: 20px;">至</div>
                        <div class="address-text" v-if="province != ''" style="margin-left: 20px;">{{ province }}&nbsp;{{ district }}</div>
                        <div class="address-btn" @click="add_info" v-else style="margin-left: 20px;">完善您的地址信息</div>
                    </div>
                    <div class="post">快递：{{ post }}元</div>
                    <div class="size-box">
                        <div class="address-text">尺寸：</div>
                        <div class="peisong" style="margin-left: 20px;">{{ goods_info.describe[selected_goods] }}</div>
                    </div>
                    <div class="size-select">
                        <div class="select-box" v-for="(item, idx) in goods_info.sizes" :key="idx" :class="[selected_goods == idx? 'selected-box': '']" @click="select_size(idx)">
                            <div style="font-size: 2vh;">{{ item }}</div>
                        </div>
                    </div>
                    <div class="comment">
                        <div class="comment-list">
                            <div class="price-text">评论&nbsp;({{ goods_info.comment.length }})</div>
                            <div class="peisong" style="cursor: pointer;" @click="show_dialog=true">更多<i class="el-icon-arrow-right"></i></div>
                        </div>
                        <div class="comment-card">
                            <div class="avatar"></div>
                            <div class="comment-detail">
                                <div class="peisong">
                                    {{ goods_info.comment[0].username }}
                                    &nbsp;
                                    尺寸分类：&nbsp;{{ goods_info.comment[0].size }}
                                </div>
                                <div class="comment-text">
                                    <div class="address-text">{{ goods_info.comment[0].comment }}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="btn-list">
                        <div class="left-btn">
                            <div class=btn-box>
                                <div class="btn-logo btn-kefu"></div>
                                <div class="address-text">客服</div>
                            </div>
                            <div class=btn-box>
                                <div class="btn-logo btn-save"></div>
                                <div class="address-text">收藏</div>
                            </div>
                            <div class=btn-box>
                                <div class="btn-logo btn-share"></div>
                                <div class="address-text">分享</div>
                            </div>
                        </div>
                        <div class="right-btn">
                            <div class="right-btn-item">立即购买</div>
                            <div class="right-btn-item">加入购物车</div>
                        </div>
                    </div>
                </div>
            </el-col>
        </el-row>
        <el-dialog
            title="购买评论"
            width="40%"
            :visible.sync="show_dialog">
            <div class="comment-dialog">
                <div class="comment-card" style="border: 1px #ccc solid; border-radius: 1vh" v-for="(item, idx) in goods_info.comment" :key="idx">
                    <div class="avatar"></div>
                        <div class="comment-detail">
                            <div class="peisong" style="color: #aaa;">
                                {{ item.username }}
                                &nbsp;
                                尺寸分类：&nbsp;{{ item.size }}
                            </div>
                            <div class="comment-text">
                                <div class="address-text" style="color: #000;">{{ item.comment }}</div>
                            </div>
                        </div>
                </div>
            </div>
            <span slot="footer" class="dialog-footer">
                <el-button @click="show_dialog = false">取 消</el-button>
                <el-button type="primary" @click="show_dialog = false">确 定</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
import Cookies from 'js-cookie'
export default{
    name: 'detail',
    props: {
        goods_id: {
            type: Number,
            required: true
        }
    },
    data(){
        return{
            goods_info: {
                child_list: [''],
                name: '',
                prices: [''],
                sizes: [''],
                describe: [''],
                comment: [
                    {username: '', size: '', comment: ''}
                ]
            },
            selected_goods: 0,
            pay_count: 0,
            address: '',
            province: '',
            district: '',
            post: '0.00',
            show_dialog: false
        }
    },
    methods: {
        back(){
            this.$emit('back', 0)
        },
        select_size(val){
            this.selected_goods = val
        },
        add_info(){
            this.$router.push({path: '/info', replace: true})
        }
    },
    created(){
        let user_id = Cookies.get('user_id')
        let that = this
        let params = {
            'id': this.goods_id
        }
        this.$http({
            url: 'api/get_goods_detail',
            method: 'GET',
            params: params
        }).then(res=>{
            that.goods_info = res.data.data
        }).catch(err=>{this.$message.error(err)})
        this.$http({
            url: 'api/get_pay_count',
            method: 'GET',
            params: params
        }).then(res=>{
            that.pay_count = res.data.count
        }).catch(err=>{this.$message.error(err)})
        let user_param = {
            'id': user_id
        }
        this.$http({
            url: 'api/get_address',
            method: 'GET',
            params: user_param
        }).then(res=>{
            that.province = res.data.province
            that.district = res.data.district
            that.address = res.data.address
            that.post = res.data.post
        }).catch(err=>{this.$message.error(err)})
    }
}
</script>

<style scoped>
.detail{
    color: #fff;
    box-sizing: border-box;
}
.back{
    width: 5vh;
    height: 5vh;
    background-image: url('../../../assets/back.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    position: absolute;
    left: 0%;
    top: -5vh;
    cursor: pointer;
}
.detail-container{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}
.detail-list{
    width:20%;
    height: 70vh;
    box-sizing: border-box;
    padding: 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    overflow-x: hidden;
    overflow-y: auto;
}
.detail-list::-webkit-scrollbar {
  width: 6px; /* 滚动条的宽度 */
}

.detail-list::-webkit-scrollbar-track {
  background: transparent; /* 滚动条轨道的颜色 */
}

.detail-list::-webkit-scrollbar-thumb {
  background-color: #fff; /* 滚动条本身的颜色 */
  border-radius: 4px; /* 滚动条圆角 */
}

.detail-list::-webkit-scrollbar-thumb:hover {
  background: #555; /* 滚动条鼠标悬停时的颜色 */
}
.detail-img-box{
    margin-left: 10px;
    width: 80%;
    height: 70vh;
    border: 1px solid #fff;
    border-radius: 2vh;
    box-sizing: border-box;
    padding: 10px;
}
.small-img{
    width: 100%;
    height: 12vh;
    border-radius: 2vh;
    cursor: pointer;
    transition: all .3s;
}
.small-img-no-active{
    border: 1px solid #fff;
}
.small-img-active{
    border: 1px solid #c89b49;
}
.title-box{
    width: 100%;
    text-align: left;
}
.title{
    font-size: 4vh;
}
.content-box{
    margin-left: 10%;
}
.price-list{
    text-align: left;
    margin-top: 20px;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center
}
.price-text{
    font-size: 3vh;
}
.pay-count{
    font-size: 1.5vh;
    color: #aaa;
    margin-left: 30%
}
.address-list{
    margin-top: 20px;
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
}
.peisong{
    font-size: 2vh;
    color: #aaa
}
.address-text{
    font-size: 2vh;
}
.address-btn{
    box-sizing: border-box;
    padding: 2px;
    border: 1px solid #fff;
    border-radius: 1vh;
    cursor: pointer;
    transition: all .3s;
}
.address-btn:hover{
    background-color: #fff;
    color: #131e3a;
}
.post{
    width: 100%;
    text-align: left;
    font-size: 2vh;
    margin-top: 10px;
}
.size-box{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    margin-top: 20px;
}
.size-select{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    margin-top: 10px
}
.select-box{
    width: 6vh;
    height: 6vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border: 1px solid #fff;
    border-radius: 1vh;
    cursor: pointer;
    margin-left: 20px;
    transition: all .3s;
}
.select-box:first-child{
    margin-left: 0;
}
.selected-box{
    background-color: #fff;
    color: #131e3a;
}
.comment-list{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    margin-top: 30px;
}
.comment-card{
    margin-top: 10px;
    width: 100%;
    min-height: 10vh;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    box-sizing: border-box;
    padding: 10px
}
.avatar{
    width: 6vh;
    height: 6vh;
    border-radius: 50%;
    background-image: url('../../../assets/avatar.png');
    background-repeat: no-repeat;
    background-position: center center;
    background-size: 100% 100%;
}
.comment-detail{
    text-align: left;
    margin-left: 20px
}
.comment-text{
    margin-top: 5px;
}
.comment-dialog{
    width: 100%;
    height: 30vh;
    overflow-x: hidden;
    overflow-y: auto;
}
.comment-dialog:-webkit-scrollbar {
  width: 6px; /* 滚动条的宽度 */
}

.comment-dialog::-webkit-scrollbar-track {
  background: transparent; /* 滚动条轨道的颜色 */
}

.comment-dialog::-webkit-scrollbar-thumb {
  background-color: #ccc; /* 滚动条本身的颜色 */
  border-radius: 4px; /* 滚动条圆角 */
}

.comment-dialog::-webkit-scrollbar-thumb:hover {
  background: #555; /* 滚动条鼠标悬停时的颜色 */
}
.comment-dialog /deep/ .el-button--primary{
    background-color: #131e3a;
}
.comment-dialog /deep/ .el-button--primary:hover{
    background-color: #1e2f5a;
}
.btn-list{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    margin-top: 20px;
}
.left-btn{
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
}
.btn-logo{
    width: 5vh;
    height: 5vh;
    background-repeat: no-repeat;
    background-position: center center;
}
.btn-kefu{
    background-image: url('../../../assets/kefu.png');
    background-size: 80% 80%;
}
.btn-save{
    background-image: url('../../../assets/no_save.png');
    background-size: 100% 100%;
}
.btn-share{
    background-image: url('../../../assets/fenxiang.png');
    background-size: 80% 80%;
}
.btn-box{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-left: 30px;
}
.btn-box:first-child{
    margin-left: 0;
}
.right-btn{
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
}
.right-btn-item{
    font-size: 3vh;
    box-sizing: border-box;
    padding: 5px;
    padding-left: 10px;
    padding-right: 10px;
    border: 1px solid #fff;
    border-radius: 3vh;
    cursor: pointer;
    transition: all .3s;
}
.right-btn-item:hover{
    background-color: #fff;
    color: #131e3a
}
.right-btn-item:first-child{
    margin-right: 20px;
}
</style>