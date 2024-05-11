<template>
    <div class="card-body">
        <div class="header">
            <div class="user">
                <div class="avatar"></div>
                <div class="username">{{ content.username }}</div>
            </div>
            <div class="manage">
                <div class="guanzhu" @click="handle_guanzhu">
                    <div v-if="content.my_guanzhu">√ 已关注</div>
                    <div v-else>+ 关注</div>
                </div>
                <div class="shoucang" @click="handle_shoucang">
                    <div v-if="content.shoucang" class="save"></div>
                    <div v-else class="no_save"></div>
                </div>
            </div>
        </div>
        <div class="message">
            {{ content.content }}
        </div>
        <div class="bottom">
            <div class="dongtai">
                <div v-if="content.my_dianzan" class="logo dianzan" @click="handle_dianzan"></div>
                <div v-else class="logo no_dianzan" @click="handle_dianzan"></div>
                <div class="dongtai-text">{{ content.dianzan }}</div>
                <div class="logo comment-logo"></div>
                <div class="dongtai-text">{{ content.pinglun.length }}</div>
                <div class="logo share"></div>
            </div>
        </div>
    </div>
</template>

<script>
export default{
    name: 'card-body',
    props: {
        'content': {
            type: Object,
            required: true
        },
        'user_id': {
            type: String,
            required: true
        }
    },
    data(){
        return{

        }
    },
    methods:{
        handle_guanzhu(){
            let that = this
            let target_user_id = this.content.user
            let user_id = parseInt(this.user_id)
            let post_data = {'user_id': user_id, 'target_user_id': target_user_id} 
            if (this.content.my_guanzhu){
                this.$http.post('api/delete_guanzhu', post_data).then(res=>{
                    that.content.my_guanzhu = false
                }).catch(e=>{this.$message.error(e)})
            }
            else{
                this.$http.post('api/add_guanzhu', post_data).then(res=>{
                    that.content.my_guanzhu = true
                }).catch(e=>{this.$message.error(e)})
            }
        },
        handle_dianzan(){
            let that = this
            let comment_id = this.content.id
            let user_id = parseInt(this.user_id)
            let post_data = {'comment_id': comment_id, 'user_id': user_id}
            if (this.content.my_dianzan){
                this.$http.post('api/delete_dianzan', post_data).then(res=>{
                    that.content.my_dianzan = false
                    that.content.dianzan -= 1
                }).catch(e=>{this.$message.error(e)})
            }
            else{
                this.$http.post('api/add_dianzan', post_data).then(res=>{
                    that.content.my_dianzan = true
                    that.content.dianzan += 1
                }).catch(e=>{this.$message.error(e)})
            }
        },
        handle_shoucang(){
            let that = this
            let comment_id = this.content.id
            let user_id = parseInt(this.user_id)
            let post_data = {'comment_id': comment_id, 'user_id': user_id}
            if (this.content.shoucang){
                this.$http.post('api/delete_shoucang', post_data).then(res=>{
                    that.content.shoucang = false
                }).catch(e=>{this.$message.error(e)})
            }
            else{
                this.$http.post('api/add_shoucang', post_data).then(res=>{
                    that.content.shoucang = true
                }).catch(e=>{this.$message.error(e)})
            }
        }
    }
}
</script>

<style scoped>
.card-body{
    width: 100%;
    min-height: 20vh;
    box-sizing: border-box;
    padding: 10px;
    border: 1px solid #fff;
    margin-top: 20px;
}
.header{
    box-sizing: border-box;
    padding-top: 10px;
    width: 100%;
    height: 5vh;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
.user{
    width: 20%;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
}
.avatar{
    width: 5vh;
    height: 5vh;
    background-image: url('../../../assets/avatar.png');
    background-position: center center;
    background-size: 100% 100%;
    background-repeat: no-repeat;
    margin-left: 10px;
}
.username{
    color: #fff;
    margin-left: 5%;
    font-size: 2vh;
}
.manage{
    width: 30%;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
}
.guanzhu{
    width: 30%;
    height: 3.5vh;
    border-radius: 5vh;
    border: 1px solid #fff;
    color: #fff;
    cursor: pointer;
    transition: all .3s;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: 1.5vh;
}
.guanzhu:hover{
    background-color: #fff;
    color: #0c1429;
}
.shoucang{
    width: 3.5vh;
    height: 3.5vh;
    margin-left: 5%;
}
.save{
    width: 100%;
    height: 100%;
    background-image: url('../../../assets/save.png');
    background-position: center center;
    background-size: 100% 100%;
    background-repeat: no-repeat;
    cursor: pointer;
}
.no_save{
    width: 100%;
    height: 100%;
    background-image: url('../../../assets/no_save.png');
    background-position: center center;
    background-size: 100% 100%;
    background-repeat: no-repeat;
    cursor: pointer;
}
.message{
    width: 100%;
    min-height: 10vh;
    box-sizing: border-box;
    padding-top: 20px;
    padding-bottom: 10px;
    padding-left: 40px;
    padding-right: 40px;
    color: #fff;
    text-align: left;
    font-size: 1.5vh;
}
.bottom{
    width: 100%;
    height: 5vh;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}
.dongtai{
    width: 40%;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
}
.logo{
    width: 2.5vh;
    height: 2.5vh;
    cursor: pointer;
}
.no_dianzan{
    background-image: url('../../../assets/dianzan.png');
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position: center center;
    margin-left: 40px;
}
.dianzan{
    background-image: url('../../../assets/dianzan_block.png');
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position: center center;
    margin-left: 40px;
}
.dongtai-text{
    color: #fff;
    margin-left: 10px;
    font-size: 1.5vh;
}
.comment-logo{
    background-image: url('../../../assets/comment.png');
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position: center center;
    margin-left: 5%;
}
.share{
    background-image: url('../../../assets/share.png');
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position: center center;
    margin-left: 5%;
}
</style>
