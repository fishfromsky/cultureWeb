<template>
    <div class="info-body">
        <div class="title">个人信息修改和完善</div>
        <el-form ref="registerForm" style="width: 30%;" :model="registerForm" @submit.native.prevent="onRegister" :rules="rules">
            <el-form-item label="用户名" prop="name">
                <el-input v-model="registerForm.name" autocomplete="username" placeholder="请输入您的用户名"></el-input>
            </el-form-item>
            <el-form-item label="手机号" prop="mobile">
                <el-input v-model="registerForm.mobile" placeholder="请输入您的联系手机号码"></el-input>
            </el-form-item>
            <el-form-item label="邮箱地址" prop="email">
                <el-input v-model="registerForm.email" placeholder="请输入您的邮箱地址"></el-input>
            </el-form-item>
            <el-form-item label="所在省市" prop="district">
                <el-cascader v-model="registerForm.district" :options="optionsnative_place" placeholder="请输入您所在省市"/>
            </el-form-item>
            <el-form-item label="具体地址" prop="address">
                <el-input v-model="registerForm.address" placeholder="请输入具体地址"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input type="password" v-model="registerForm.password" placeholder="请输入密码"></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="password">
                <el-input type="password" v-model="registerForm.confirmPassword" placeholder="请再次输入密码"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onRegister">提交注册</el-button>
            </el-form-item>
      </el-form>
    </div>
</template>

<script>
import {
  provinceAndCityData,
  pcTextArr,
  regionData,
  pcaTextArr,
  codeToText,
} from "element-china-area-data"
import Cookies from 'js-cookie'
export default{
    name: 'info',
    data(){
        return{
            optionsnative_place: pcTextArr,
            registerForm: {
                id: '',
                name: '',
                mobile: '',
                email: '',
                district: [],
                address: '',
                password: '',
                confirmPassword: '',
            },
            rules: {
                name: [
                    { required: true, message: '请输入姓名', trigger: 'blur' }
                ],
                email: [
                    { required: true, message: '请输入邮箱地址', trigger: 'blur' },
                    { type: 'email', message: '请输入正确的邮箱格式', trigger: ['blur', 'change'] }
                ],
                mobile: [
                    { required: true, message: '请输入手机号', trigger: 'blur' },
                    { pattern: /^1[3|5|7|8|9]\d{9}$/, message: '请输入正确的号码格式', trigger: ['blur', 'change'] }
                ],
                district: [
                    {required: true, message: '请选择您所在省市'}
                ],
                address: [
                    {required: true, message: '请输入您所在具体地址'}
                ],
                password: [
                    {required: true, message: '请输入密码', trigger: 'blur'}
                ]
            }
        } 
    },
    methods: {
        onRegister(){
            this.$refs.registerForm.validate((valid) => {
            if (valid) {
                let params = this.registerForm
                params.province = this.registerForm.district[0]
                params.district = this.registerForm.district[1]
                this.$http.post('api/modify_user_info', params).then(res=>{
                    this.$message.success('修改成功')
                }).catch(e=>{this.$message.error(e)})
            }
            else{
                this.$message.error('表单格式不正确')
            }
        })
        }
    },
    created(){
        let user_id = Cookies.get('user_id')
        if (user_id == null){
            this.$router.push({path: '/login'})
        }
        else{
            let params = {
                'id': user_id
            }
            this.$http({
                url: 'api/get_user_info',
                params: params,
                method: 'GET'
            }).then(res=>{
                let data = res.data.data
                this.registerForm.id = user_id
                this.registerForm.name = data.username
                this.registerForm.mobile = data.phone_number
                this.registerForm.email = data.email
                this.registerForm.district = [data.province, data.district]
                this.registerForm.password = data.password
                this.registerForm.confirmPassword = data.password
            }).catch(e=>{this.$message.error(e)})
        }
    }
}
</script>

<style scoped>
.info-body{
    width: 100%;
    min-height: 90vh;
    background-color: #131e3a;
    box-sizing: border-box;
    padding: 40px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    color: #fff;
}
.title{
    font-size: 5vh;
}
.info-body /deep/ .el-input__inner{
    background-color: transparent
}
.register-item{
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
}
</style>