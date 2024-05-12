<template>
    <div class="interview-body">
        <div class="img-box">
            <div class="img">
                <img :src="content.img" style="width: 100%; height: 100%;">
            </div>
            <div class="introduce-box">
                <div class="introduce-title">
                    <div class="logo logo-left-bg"></div>
                    <div class="title-text">{{ person_name }}口述史</div>
                    <div class="logo logo-right-bg"></div>
                </div>
                <div class="introduce-text">{{ content.introduce }}</div>
            </div>
        </div>
        <div class="interviewer-box">
            <div class="person-box">
                <div class="person-text">采访者:&nbsp;{{ content.interviewer }}</div>
                <div class="person-text" style="margin-left: 20px;">翻译校对:&nbsp;{{ content.translator }}</div>
            </div>
            <div class="person-box" style="margin-top: 20px;">
                <div class="person-text">采访时间:&nbsp;{{ content.time }}</div>
            </div>
        </div>
        <div class="content-box" v-for="(item, idx) in question" :idx="idx">
            <div class="question-box">Q:&nbsp;{{ item }}</div>
            <div class="question-box">A:&nbsp;{{ answer[idx] }}</div>
        </div>
    </div>
</template>

<script>
export default{
    props: {
        person_id: {
            type: Number,
            required: true
        },
        person_name: {
            type: String,
            required: true
        }
    },
    data(){
        return {
            content: {},
            question: [],
            answer: []
        }
    },
    watch: {
        person_id(val){
            
        }
    },
    created(){
        let params = {
            'id': this.person_id
        }
        this.$http({
            url: 'api/get_interview_content',
            params: params,
            method: 'GET'
        }).then(res=>{
            this.content = res.data.data
            this.question = res.data.data.question.split('|')
            this.answer = res.data.data.answer.split('|')
        }).catch(e=>{this.$message.error(e)})
    }
}
</script>

<style scoped>
.interview-body{
    width: 100%;
    min-height: 90vh;
    box-sizing: border-box;
    padding: 40px;
    padding-left: 10%;
}
.img-box{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    margin-top: 4vh;
}
.img{
    width: 40%;
    height: 30vh;
}
.introduce-box{
    width: 50%;
    min-height: 30vh;
}
.introduce-title{
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
}
.logo-left-bg{
    background-image: url('../../../assets/wen/left.png');
    margin-right: 20px;
}
.logo-right-bg{
    background-image: url('../../../assets/wen/right.png');
    margin-left: 20px;
}
.logo{
    width: 4vh;
    height: 4vh;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
}
.title-text{
    color: #fff;
    font-size: 4vh;
    font-family: DongfangDakai;
}
.introduce-text{
    margin-top: 30px;
    color: #fff;
    font-size: 2vh;
    text-align: left;
}
.interviewer-box{
    box-sizing: border-box;
    padding: 20px;
    width: 100%;
}
.person-box{
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
}
.person-text{
    color: #fff;
    font-family: DongfangDakai;
    font-size: 2vh;
}
.content-box{
    width: 100%;
    box-sizing: border-box;
    padding: 5px;
    padding-left: 20px;
    padding-right: 20px;
    font-size: 2vh;
    color: #fff;
}
.question-box{
    width: 100%;
    word-wrap: break-word;
    word-break: normal;
    text-align: left;
}
</style>