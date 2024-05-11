<template>
    <div class="personal">
        <div class="avatar-info">
            <div class="data">
                <div class="my-info">
                    <div class="avatar"></div>
                    <div class="name-box">
                        <div class="username title">
                            <div>{{ username }}</div>
                        </div>
                        <div class="username sign">
                            <div>{{ sign }}</div>
                        </div>
                    </div>
                </div>
                <div class="my-data">
                    <div v-for="(item, idx) in data" class="data-box">
                        <div>{{ item.data }}</div>
                        <div>{{ item.name }}</div>
                    </div>
                </div>
            </div>
            <div class="notion">
                <div class="logo bell"></div>
                <div class="logo message"></div>
            </div>
        </div>
        <div class="create">
            <div class="title-box">
                <div class="title">创客中心</div>
                <div class="draft">草稿箱 ( {{ draft }} )</div>
            </div>
            <div class="gallery">
                <div v-for="(item, idx) in create_data" class="activity">
                    <div class="img"></div>
                    <div class="activity-name">{{ item.name }}</div>
                </div>
            </div>
        </div>
        <div class="publish">
            <div class="publish-title">我的发布</div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'personal',
    props:{
        'username': {
            type: String,
            required: true
        },
        'user_id': {
            type: String,
            required: true
        }
    },
    data(){
        return{
            sign: '兢兢业业的打工人',
            data: [
                {name: '关注', data: 32}, {name: '粉丝', data: 32}, {name: '获赞', data: 32}
            ],
            draft: 0,
            create_data: [
                {name: '图文'}, {name: '视频'}, {name: '话题'}, {name: '活动'}
            ]
        }
    },
    methods:{
        ini_data(){
            let that = this
            let post_data = {'user_id': this.user_id}
            this.$http({
                url: 'api/get_person_info',
                method: 'GET',
                params: post_data
            }).then(res=>{
                let data = res.data.data
                that.data[0].data = data.guanzhu
                that.data[1].data = data.fensi
                that.data[2].data = data.dianzan
            }).catch(e=>{this.$message.error(e)})
        }
    },
    mounted(){
        this.ini_data()
    }
}
</script>

<style scoped>
.personal{
    width: 100%;
    min-height: 40vh;
    box-sizing: border-box;
    padding-left: 60px;
}
.avatar-info{
    width: 100%;
    height: 20vh;
    display: flex;
    flex-direction: row;
    border-bottom: 2px solid #fff;
}
.data{
    width: 70%;
    height: 100%;
}
.my-info{
    width: 100%;
    height: 50%;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
}
.my-data{
    width: 90%;
    height: 50%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}
.data-box{
    box-sizing: border-box;
    padding-left: 20px;
    padding-right: 20px;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: #fff;
    font-size: 2vh;
}
.avatar{
    width: 8vh;
    height: 8vh;
    background-image: url('../../../assets/avatar.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
}
.name-box{
    width: 80%;
    height: 100%;
    text-align: left;
    box-sizing: border-box;
    padding-left: 20px;
}
.username{
    width: 100%;
    height: 50%;
    display: flex;
    flex-direction: row;
    align-items: center;
}
.title{
    font-size: 2.5vh;
    color: #fff;
}
.sign{
    font-size: 1.5vh;
    color: #aaa;
}
.notion{
    width: 30%;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
}
.logo{
    width: 3vh;
    height: 3vh;
}
.bell{
    background-image: url('../../../assets/bell.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
}
.message{
    background-image: url('../../../assets/message.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    margin-left: 20px;
}
.create{
    width: 100%;
    height: 20vh;
    border-bottom: 2px solid #fff;
    margin-top: 10px;
}
.title-box{
    width: 100%;
    height: 5vh;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}
.title{
    color: #fff;
}
.draft{
    color: #aaa;
    font-size: 1.5vh;
}
.gallery{
    margin-top: 20px;
    width: 100%;
    height: 10vh;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
}
.activity{
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.img{
    width: 6vh;
    height: 6vh;
    border-radius: 50%;
    background-color: #bbb;
}
.activity-name{
    margin-top: 10px;
    font-size: 2vh;
    color: #fff;
}
.publish{
    margin-top: 20px;
    width: 100%;
    height: 20vh;
}
.publish-title{
    font-size: 2.5vh;
    color: #fff;
    text-align: left;
}
</style>