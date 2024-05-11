<template>
    <div class="news_show_body">
        <div class="back" @click="backpage"></div>
        <div class="title">
            <div class="logo logo-left-bg"></div>
            <div class="text">活动信息</div>
            <div class="logo logo-right-bg"></div>
        </div>
        <div class="nav">
            <div class="nav-item" v-for="(item, idx) in nav_list" :key="idx" @click="selectItem(idx)">
                <div class="nav-logo" :class="[selected == idx? 'nav-logo-left-active': 'nav-logo-left']"></div>
                <div class="nav-text" :class="[selected == idx? 'nav-text-active': 'nav-text-no-active']">{{ item }}</div>
                <div class="nav-logo" :class="[selected == idx? 'nav-logo-right-active': 'nav-logo-right']"></div>
            </div>
        </div>
        <Show :content="news_content"></Show>
    </div>
</template>

<script>
import Show from './components/show.vue'
export default{
    name: 'news_show',
    components: {
        Show
    },
    data(){
        return{
            nav_list: ['比赛', '展览', '活动', '培训'],
            selected: 0,
            news_content: []
        }
    },
    methods: {
        selectItem(val){
            if (val != this.selected){
                this.selected = val
                this.get_news_content(val)
            }
        },
        get_news_content(val){
            let data = {
                'id': val
            }
            let that = this
            this.$http({
                url: 'api/get_show_news',
                params: data,
                method: 'GET'
            }).then(res=>{
                that.news_content = res.data.data
            }).catch(e=>{this.$message.error(e)})
        },
        backpage(){
            this.$emit('backpage', 0)
        }
    },
    created(){
        this.get_news_content(this.selected)
    }
}
</script>

<style scoped>
.title{
    margin-top: 40px;
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
}
.logo{
    width: 5vh;
    height: 5vh;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
}
.text{
    font-family: DongfangDakai;
    font-size: 5vh;
    color: #fff;
}
.logo-left-bg{
    background-image: url('../../assets/wen/left.png');
    margin-right: 20px;
}
.logo-right-bg{
    background-image: url('../../assets//wen/right.png');
    margin-left: 20px;
}
.nav{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
}
.nav-item{
    cursor: pointer;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    min-width: 15%;
}
.nav-logo{
    width: 4vh;
    height: 4vh;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    transition: all .3s;
}
.nav-text-no-active{
    color: #fff;
}
.nav-text{
    font-size: 2.7vh;
    transition: all .3s;
}
.nav-text-active{
    color: #c89b49;
}
.nav-logo-left{
    background-image: url('../../assets/wen/nav_left.png');
}
.nav-logo-right{
    background-image: url('../../assets/wen/nav_right.png');
}
.nav-logo-left-active{
    background-image: url('../../assets/wen/nav_left_active.png');
}
.nav-logo-right-active{
    background-image: url('../../assets/wen/nav_right_active.png');
}
.back{
    width: 5vh;
    height: 5vh;
    background-image: url('../../assets/back.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    position: absolute;
    top: 13vh;
    left: 4%;
    cursor: pointer;
}
</style>