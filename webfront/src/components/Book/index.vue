<template>
    <div class="book-body">
        <el-row :gutter="20">
            <el-col :span="14">
                <div class="show-box">
                    <div class="pointer">
                        <div class="icon">
                            <i class="el-icon-arrow-left"></i>
                        </div>
                    </div>
                    <div class="book-box">
                        <div class="book-content">
                            <img :src="book_content.img[0]" style="width: 100%; height: 100%;">
                        </div>
                        <div class="book-content">
                            <img :src="book_content.img[1]" style="width: 100%; height: 100%;">
                        </div>
                    </div>
                    <div class="pointer">
                        <div class="icon">
                            <i class="el-icon-arrow-right"></i>
                        </div>
                    </div>
                </div>
            </el-col>
            <el-col :span="10">
                <div class="content-box">
                    <div class="title">{{ book_content.title }}</div>
                    <div class="text" v-for="(item, idx) in book_content.describe" :key="idx" :class="text_class[idx]">
                        {{ item }}
                    </div>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
export default{
    name: 'Book',
    data(){
        return{
            book_index: 0,
            book_content: {
                img: ['', '']
            },
            text_class: []
        }
    },
    created(){
        let category = this.$route.query.id
        let params = {
            'id': category
        }
        this.$http({
            url: 'api/get_history_info',
            method: 'GET',
            params: params
        }).then(res=>{
            this.book_content = res.data.data
            for (let i=0; i<this.book_content.describe.length; i++){
                if (this.book_content.flag.indexOf(i) != -1){
                    this.text_class.push('text-active')
                }
                else{
                    this.text_class.push('text-ori')
                }
            }
        }).catch(e=>{this.$message.error(e)})
    }
}
</script>

<style scoped>
.book-body{
    width: 100%;
    height: 90vh;
    background-color: #131e3a;
    background-image: url('../../assets/main_bg_yin.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    box-sizing: border-box;
    padding: 40px;
}
.show-box{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    margin-top: 12vh;
}
.pointer{
    width: 5vh;
    height: 5vh;
    border-radius: 50%;
    background-color: #868a94;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    cursor: pointer;
}
.icon{
    color: #fff;
    font-weight: bold;
    font-size: 4vh;
}
.book-box{
    width: 80%;
    height: 50vh;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}
.book-content{
    width: 47%;
    height: 100%;
}
.content-box{
    margin-top: 8vh;
}
.title{
    font-family: DongfangDakai;
    font-size: 6vh;
    color: #fff;
    margin-bottom: 10px;
}
.text{
    font-size: 2vh;
    text-indent: 2em;
    text-align: left;
    line-height: 4.2vh;
}
.text-ori{
    color: #fff;
}
.text-active{
    color: #d09935;
}
</style>