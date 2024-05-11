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
                            <img :src="book_url1" style="width: 100%; height: 100%;">
                        </div>
                        <div class="book-content">
                            <img :src="book_url2" style="width: 100%; height: 100%;">
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
                    <div class="title">《岳西县志》</div>
                    <div class="text" style="margin-top: 20px;">第十五篇《金融》的第二章《货币》中提到了早期时把银作为货币进行交易。</div>
                    <div class="text" style="color: #d09935">"解放前，曾以少量黄金、大量白银当货币，自由买卖”</div>
                    <div class="text">第二十七篇《社会风土》的第三章《风土习俗》第二节生活》中有大量描写彝族人民佩戴银饰的文字。</div>
                    <div class="text" style="color: #d09935;">"耳缀银箔泡花”</div>
                    <div class="text" style="color: #d09935;">"妇女用铜、银铸制的领花、领牌、领珠缝于领口”</div>
                    <div class="text" style="color: #d09935;"> “手饰以金、银、铜、玉为料”</div>
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
            book_url1: 'http://127.0.0.1:8000/static/img/history/book1.png',
            book_url2: 'http://127.0.0.1:8000/static/img/history/book2.png'
        }
    }
}
</script>

<style scoped>
.book-body{
    width: 100%;
    height: 90vh;
    background-color: #131e3a;
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
    margin-top: 10vh;
}
.title{
    font-family: DongfangDakai;
    font-size: 6vh;
    color: #fff;
}
.text{
    font-size: 2vh;
    text-indent: 2em;
    text-align: left;
    color: #fff;
    line-height: 4.5vh;
}
</style>