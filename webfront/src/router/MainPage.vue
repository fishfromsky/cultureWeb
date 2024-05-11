<template>
    <div class="main">
        <NavBar></NavBar>
        <router-view></router-view>
    </div>
</template>

<script>
import NavBar from '@/components/NavBar'
import vueDanmaku from 'vue-danmaku'
import VueEmoji from 'emoji-vue'
import Cookies from 'js-cookie'
import Talk from '@/components/Talk'
export default{
    name: 'MainPage',
    components: {
        vueDanmaku,
        VueEmoji,
        NavBar
    },
    data(){
        return{
            comments: ['哇！好好看', '太了不起了', '好像买一个', '样式太精美了！'],
            myText: ''
        }
    },
    methods: {
        onInput (event) {
            this.myText = event.data
        },
        addComment(){
            let token_key = Cookies.get('token')
            if (token_key){
                this.comments.push(this.myText)
                this.myText = ''
            }
            else{
                this.$router.push('/login')
            }
        }
    },
    mounted(){
    }
}
</script>

<style scoped lang="less">
.main{
    min-width: 1150px;
    overflow-x: scroll;
    height: 100vh;
    overflow-x: auto;
}
.danmu{
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 500px;
    height: 200px;
    border: #fff 1px solid;
    padding: 20px;
}
.danmu-inline{
    width: 100%;
    height: 100%;
    display: block;
}
.emoji-box{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    position: fixed;
    top: 63%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: #fff
}
</style>