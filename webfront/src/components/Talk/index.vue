<template>
    <div class="main-body">
        <el-row>
            <el-col :span="15">
                <div class="comment-box">
                    <div class="nav-list">
                        <div class="nav-item-list">
                            <div v-for="(item, idx) in nav_item" :class="{'nav-item-active': select_item==idx}" class="nav-item" @click="change_tab(idx)">{{ item }}</div>
                        </div>
                        <div class="search">
                            <div class="input-icon-container">
                                <i class="el-icon-search"></i>
                                <input type="text" v-model="search_content" placeholder="请输入您想搜索的内容" @keyup.enter="search">
                            </div>
                        </div>
                    </div>
                    <div class="comment-list">
                        <card v-for="(item, idx) in comment" :user_id="userID" :content="item" :key="idx"></card>
                    </div>
                </div>
            </el-col>
            <el-col :span="9">
                <personal :user_id="userID" :username="username"></personal>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import card from './components/card'
import personal from './components/personal'
import Cookies from 'js-cookie'
export default{
    name: 'Talk',
    components: {
        card,
        personal
    },
    data(){
        return{
            nav_item: ['推荐', '收藏', '关注', '热门', '赞过'],
            comment: [],
            select_item: 0,
            search_content: ''
        }
    },
    methods: {
        search(){
            let user_data = {
                'user_id': this.userID,
                'content': this.search_content
            }
            let that = this
            this.$http.post('api/get_search_content', user_data).then(res=>{
                that.comment = res.data.data
            }).catch(e=>{
                this.$message.error(e)
            })
        },
        get_all_comments(){
            let user_data = {
                'id': this.userID
            }
            let that = this
            this.$http({
                url: 'api/get_comments',
                method: 'GET',
                params: user_data
            }).then(res=>{
                that.comment = res.data.data
            }).catch(e=>{
                this.$message.error(e)
            })
        },
        get_my_shoucang(){
            let user_data = {
                'user_id': this.userID
            }
            let that = this
            this.$http({
                url: 'api/get_person_shoucang',
                method: 'GET',
                params: user_data
            }).then(res=>{
                that.comment = res.data.data
            }).catch(e=>{
                this.$message.error(e)
            })
        },
        get_my_guanzhu(){
            let user_data = {
                'user_id': this.userID
            }
            let that = this
            this.$http({
                url: 'api/get_person_guanzhu',
                method: 'GET',
                params: user_data
            }).then(res=>{
                that.comment = res.data.data
            }).catch(e=>{
                this.$message.error(e)
            })
        },
        get_hot_comment(){
            let user_data = {
                'user_id': this.userID
            }
            let that = this
            this.$http({
                url: 'api/get_hot_comment',
                method: 'GET',
                params: user_data
            }).then(res=>{
                that.comment = res.data.data
            }).catch(e=>{
                this.$message.error(e)
            })
        },
        get_my_liking(){
            let user_data = {
                'user_id': this.userID
            }
            let that = this
            this.$http({
                url: 'api/get_person_liking',
                method: 'GET',
                params: user_data
            }).then(res=>{
                that.comment = res.data.data
            }).catch(e=>{
                this.$message.error(e)
            })
        },
        ini_data(){
            let user_id = Cookies.get('user_id')
            this.userID = user_id
            this.username = Cookies.get('name')
            if (user_id == null){
                this.$router.push({path: '/login'})
            }
            else{
                this.get_all_comments()
            }
        },
        change_tab(idx){
            if (idx != this.select_item){
                this.select_item = idx
                if (idx == 0){
                    this.get_all_comments()
                }
                else if (idx == 1){
                    this.get_my_shoucang()
                }
                else if (idx == 2){
                    this.get_my_guanzhu()
                }
                else if (idx == 3){
                    this.get_hot_comment()
                }
                else if (idx == 4){
                    this.get_my_liking()
                }
            }
        }
    },
    created(){
        this.ini_data()
    }
}
</script>

<style scoped>
.main-body{
    width: 100%;
    height: 90vh;
    background-color: #131e3a;
    box-sizing: border-box;
    padding: 50px;
}
.comment-box{
    width: 100%;
    min-height: 20vh;
}
.nav-list{
    width: 100%;
    height: 5vh;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
.nav-item-list{
    width: 40%;
    height: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
}
.nav-item{
    color: #fff;
    font-size: 2vh;
    cursor: pointer;
    box-sizing: border-box;
    padding-bottom: 6px;
    transition: all .3s
}
.nav-item-active{
    border-bottom: 2px solid #fff;
}
.search{
    width: 50%;
    height: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
}
.input-icon-container {
    width: 100%;
    display: flex;
    align-items: center;
    background-color: #0c1429;
    color: #fff;
    border: 1px solid #fff;
    border-radius: 3vh;
    padding: 5px 10px;
    font-size: 1.5vh;
}

.input-icon-container input {
  border: none;
  outline: none;
  background-color: transparent;
  margin-left: 10px; 
  color: #fff;
  font-size: 2vh;
}

.icon {
  font-style: normal; 
}
.comment-list{
    width: 100%;
    height: 70vh;
    overflow-x: hidden;
    overflow-y: auto;
}
</style>