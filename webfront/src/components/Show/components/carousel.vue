<template>
    <div class="carousal-body">
        <div class="switch-item">
            <div class="danmu-text" style="margin-right: 10px;">弹幕</div>
            <el-switch style="margin-right: 40px;" v-model="danmu" active-color="#fff" inactive-color="#0c1429"></el-switch>
        </div>
        <el-carousel indicator-position="none" arrow="always" :autoplay="false" @change="handle_change">
            <el-carousel-item v-for="(item, idx) in card" :key="idx">
                <img :src="item.src" style="width: 100%; height: 100%"/>
                <div class="wen2" :style="{display: mydisplay}">
                    <img :src="item.vice_src[1]" style="width: 100%; height: 100%;">
                </div>
                <div class="wen1" :style="{display: mydisplay}">
                    <img :src="item.vice_src[0]" style="width: 100%; height: 100%">
                </div>
                <div class="click-circle" @click="wave_click"></div>
            </el-carousel-item>
            <div class="danmu">
                <vueDanmaku v-if="danmu" class="danmu-inline" :danmus="comments" :channels="3" :loop="true" :top="20" :speeds="120"></vueDanmaku>
            </div>
        </el-carousel>
        <div class="button-list">
            <div class="button">
                <div>下载</div>
            </div>
            <div class="button">
                <div>收藏</div>
            </div>
            <div class="button">
                <div @click="make_comment">评论</div>
            </div>
        </div>
        <el-dialog title="添加评论" :visible.sync="commentDialog" width="20%">
            <div class="emoji-box">
                <VueEmoji ref="emoji" height="50" :value="myText" @input="onInput" />
                <el-button @click="addComment">发送</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
import vueDanmaku from 'vue-danmaku'
import Cookies from 'js-cookie'
import VueEmoji from 'emoji-vue'
export default{
    name: 'carousal',
    components: {
        vueDanmaku,
        VueEmoji
    },
    props: {
        card: {
            type: Array,
            required: true
        }
    },
    watch:{
        card(val){
            if (val.length != 0){
                let wen_id = val[0].id
                this.card_id = wen_id
                this.get_comment(wen_id)
            }
        }
    },
    data(){
        return{
            mydisplay: 'none',
            danmu: false,
            comments: [],
            commentDialog: false,
            myText: '',
            card_id: 1
        }
    },
    methods: {
        get_comment(wen_id){
            let that = this
            this.comments = []
            let params = {
                'id': wen_id
            }
            this.$http({
                url: 'api/get_wen_comment',
                method: 'GET',
                params: params
            }).then(res=>{
                let comment_list = res.data.data
                for (let i=0; i<comment_list.length; i++){
                    let comment = comment_list[i].username+': '+comment_list[i].comment
                    that.comments.push(comment)
                }
            }).catch(e=>{this.$message.error(e)})
        },
        wave_click(){
            this.mydisplay = 'block'
        },
        handle_change(val){
            let card_id = this.card[val].id
            this.card_id = card_id
            this.$emit('carouselChange', card_id)
            this.get_comment(card_id)
        },
        make_comment(){
            let user_id = Cookies.get('user_id')
            this.userID = user_id
            this.username = Cookies.get('name')
            if (user_id == null){
                this.$router.push({path: '/login'})
            }
            else{
                this.commentDialog = true
            }
        },
        onInput (event) {
            this.myText = event.data
        },
        addComment(){
            if (this.myText == ''){
                this.$message.error('请输入评论内容')
            }
            else{
                let user_id = Cookies.get('user_id')
                let username = Cookies.get('name')
                let card_id = this.card_id
                let data = {
                    'user_id': parseInt(user_id),
                    'comment': this.myText,
                    'card_id': card_id
                }
                this.$http.post('api/add_wen_comment', data).then(res=>{
                    this.$message.success('评论添加成功')
                }).catch(e=>{this.$message.error(e)})
                let comment = username+': '+this.myText
                this.comments.push(comment)
                this.myText = ''
                this.commentDialog = false
            }
        }
    }
}
</script>

<style scoped>
.danmu{
    width: 100%;
    height: 50%;
    position: absolute;
    top: 0;
    left: 0;
    z-index: 2000;
}
.danmu-inline{
    width: 100%;
    height: 100%;
    display: block;
}
.switch-item /deep/ .el-switch{
    border: 1px solid #fff;
    border-radius: 15px;
}
.switch-item /deep/ .el-switch__core::after{
    background-color: #0c1429;
}
.danmu-text{
    color: #fff;
}
.switch-item{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
}
.carousal-body{
    color: #fff;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.carousal-body /deep/ .el-carousel__container{
    width: 90%;
    margin-top: 5vh;
    height: 45vh;
    margin-left: 5%;
}
.carousal-body /deep/ .el-carousel__arrow{
   font-size: 5vh;
}
.wen1{
    position: absolute;
    left: 10%;
    bottom: 0;
    height: 18vh;
    width: 30%;
    margin-bottom: 2vh;
    overflow: hidden;
    transition: all .5s ease-out;
}
.wen2{
    position: absolute;
    top: 0;
    left: 10%;
    width: 30%;
    height: 18vh;
    margin-top: 2vh;
    transition: all .5s ease-out
}
.click-circle{
    cursor: pointer;
    width: 25%;
    height: 15vh;
    border: 3px solid #d09935;
    position: absolute;
    bottom: 2vh;
    right: 7%;
    border-radius: 50%;
    animation: rippleAnimation 1s ease-out infinite;
}
@keyframes rippleAnimation {
    0%  { 
        transform: scale(0.7);   
        opacity: 0; 
    }
    50% { 
        opacity: 1; 
    }
    100% {
        transform: scale(1);  
        opacity: 0;  
    }
}
.button-list{
    width: 90%;
    margin-left: 5%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    margin-top: 10px
}
.button{
    width: 16%;
    height: 3vh;
    border: 1px solid #fff;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    font-size: 1.8vh;
    border-radius: 2vh;
    transition: all .3s;
    cursor: pointer;
}
.button:hover{
    background-color: #fff;
    color: #0c1429;
}
.emoji-box{
    width: 100%;
    height: 10vh;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}
</style>