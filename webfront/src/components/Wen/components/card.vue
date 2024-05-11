<template>
    <div class="main-card">
        <div class="title" @click="showmore">
            <div class="title-box">{{ title }}</div>
            <div class="more">更多</div>
        </div>
        <div class="news-card" v-for="(item, idx) in news" :key="idx" @click="handle_click(idx)">
            <div class="title-container">
                <div class="news-title">[ {{item.sub_title}} ] {{ item.title }}</div>
            </div>
            <div class="time">{{ item.news_time }}</div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'card',
    props: {
        'title': {
            type: String,
            required: true
        },
        'news': {
            type: Array,
            required: true
        }
    },
    data(){
        return{

        }
    },
    methods: {
        handle_click(idx){
            if (this.news[idx].category == 2){
                window.location.href = this.news[idx].content
            }
            else{
                this.$emit('detail_news', this.news[idx].id)
            }
        },
        showmore(){
            this.$emit('showmore', 0)
        }
    },
    mounted(){
    }
}
</script>

<style scoped>
.main-card{
    color: #fff;
    box-sizing: border-box;
    padding: 30px;
    height: 85vh;
    overflow-y: auto;
    overflow-x: hidden;
}
.main-card::-webkit-scrollbar {
  width: 6px; /* 滚动条的宽度 */
}

.main-card::-webkit-scrollbar-track {
  background: transparent; /* 滚动条轨道的颜色 */
}

.main-card::-webkit-scrollbar-thumb {
  background-color: #3d3d3d; /* 滚动条本身的颜色 */
  border-radius: 4px; /* 滚动条圆角 */
}

.main-card::-webkit-scrollbar-thumb:hover {
  background: #555; /* 滚动条鼠标悬停时的颜色 */
}
.title{
    width: 100%;
    height: 10vh;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}
.title-box{
    color: #fff;
    font-size: 4vh;
    font-family: DongfangDakai;
}
.more{
    font-size: 1.8vh;
    color: #fff;
    cursor: pointer;
}
.news-card{
    cursor: pointer;
    width: 100%;
    height: 12vh;
    border-bottom: 1px dashed #fff;
    font-size: 2vh;
}
.title-container{
    width: 100%;
    height: 7vh;
    display: flex;
    flex-direction: row;
    align-items: center;
}
.news-title{
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    text-align: left;
    transition: all .3s;
}
.news-title:hover{
    transform: scale(1.05);
}
.time{
    width: 100%;
    height: 5vh;
    text-align: left;
}
</style>