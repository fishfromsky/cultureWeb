<template>
    <div class="introduce-body">
        <el-row>
            <el-col :span="13">
                <div class="avatar-box">
                    <div class="img-box" @click="showInfo">
                        <img :src="show_people.img" style="width: 100%; height: 100%;">
                    </div>
                    <div class="title">
                        <div class="title-logo logo-up"></div>
                        <div class="title-text">{{ show_people.title }}</div>
                        <div class="title-logo logo-down"></div>
                    </div>
                    <div class="title">
                        <div class="title-logo logo-up"></div>
                        <div class="title-text">{{ show_people.name }}</div>
                        <div class="title-logo logo-down"></div>
                    </div>
                </div>
            </el-col>
            <el-col :span="11">
                <div class="name-list">
                    <div class="border" v-for="(item, idx) in people_list" :key="idx" :class="class_name[idx]">
                        <div class="border-text-box" :class="text_class_name[idx]" @click="selectPeople(idx)">
                            <div>{{ item.title }}&nbsp;&bull;&nbsp;{{ item.name }}</div>
                        </div>
                    </div>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
export default{
    name: 'introduce-body',
    data(){
        return {
            total_people: [],
            people_list: [],
            class_name: ['border-bg1', 'border-bg2', 'border-bg3', 'border-bg4', 'border-bg5'],
            text_class_name: ['border-text-pos1', 'border-text-pos2', 'border-text-pos3', 'border-text-pos4', 'border-text-pos5'],
            selected: 0,
            show_people: {}
        }
    },
    methods: {
        selectPeople(idx){
            this.selected = this.people_list[idx].id
            this.people_list = []
            for (let i=0; i<this.total_people.length; i++){
                if (this.total_people[i].id != this.selected){
                    this.people_list.push(this.total_people[i])
                }
                else{
                    this.show_people = this.total_people[i]
                    this.selected = this.total_people[i].id
                }
            }
        },
        showInfo(){
            this.$emit('showinfo', this.show_people.id)
        }
    },
    created(){
        let that = this
        this.$http.get('api/get_all_workman').then(res=>{
            let people = res.data.data
            that.total_people = people
            for (let i=0; i<people.length; i++){
                if (i != 0){
                    that.people_list.push(people[i])
                }
                else{
                    that.show_people = people[i]
                    that.selected = people[i].id
                }
            }
        }).catch(e=>{this.$message.error(e)})
    }
}
</script>

<style scoped>
.avatar-box{
    width: 100%;
    height: 80vh;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
}
.img-box{
    width: 70vh;
    height: 70vh;
    cursor: pointer;
    transition: all .3s ease-out;
}
.img-box:hover{
    transform: scale(1.03);
}
.title{
    min-width: 10%;
    height: 70vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.title-logo{
    width: 5vh;
    height: 5vh;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
}
.logo-up{
    background-image: url('../../assets/people/up.png');
}
.logo-down{
    background-image: url('../../assets/people/down.png');
}
.title-text{
    color: #fff;
    font-family: DongfangDakai;
    font-size: 4vh;
    writing-mode: vertical-lr;
}
.name-list{
    width: 100%;
    height: 90vh;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}
.border{
    width: 15%;
    height: 100%;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 135% 117%;
}
.border-bg1{
    background-image: url('../../assets/people/border1.png');
}
.border-bg2{
    background-image: url('../../assets/people/border2.png');
}
.border-bg3{
    background-image: url('../../assets/people/border3.png');
}
.border-bg4{
    background-image: url('../../assets/people/border4.png');
}
.border-bg5{
    background-image: url('../../assets/people/border5.png');
}
.border-text-box{
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    writing-mode: vertical-lr;
    font-size: 3vh;
    font-family: DongfangDakai;
    color: #fff;
    cursor: pointer;
    transition: all .3s;
}
.border-text-box:hover{
    color: #c89b49;
}
.border-text-pos1{
    margin-top: 29vh;
}
.border-text-pos2{
    margin-top: 21vh;
}
.border-text-pos3{
    margin-top: 34.5vh;
}
.border-text-pos4{
    margin-top: 18vh;
}
.border-text-pos5{
    margin-top: 12vh;
}
</style>