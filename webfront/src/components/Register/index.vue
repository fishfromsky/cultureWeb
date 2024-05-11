<template>
    <div class="register-form">
        <div class="bg"></div>
        <div class="form-box">
            <div class="title">注册</div>
            <el-form ref="registerForm" :model="registerForm" @submit.native.prevent="onRegister" :rules="rules" style="margin-top: 40px;">
                <el-form-item prop="name">
                    <el-input v-model="registerForm.name" autocomplete="username" placeholder="请输入您的用户名"></el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input type="password" v-model="registerForm.password" placeholder="请输入密码"></el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input type="password" v-model="registerForm.confirmPassword" placeholder="请再次输入密码"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onRegister">提交注册</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
  </template>
  
  <script>
  import {codeToText, pcTextArr, pcaTextArr, provinceAndCityData, regionData} from 'element-china-area-data'
  export default {
    name: 'RegisterForm',
    data() {
      return {
        optionsnative_place: provinceAndCityData,
        registerForm: {
          name: '',
          mobile: '',
          email: '',
          district: '',
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
          password: [
            {required: true, message: '请输入密码', trigger: 'blur'}
          ]
        }
      };
    },
    methods: {
      onRegister() {
        if (this.registerForm.password != this.registerForm.confirmPassword){
          this.$message.error('两次输入密码不一致，请重新输入')
        }
        else{
          this.$refs.registerForm.validate((valid) => {
            if (valid) {
              let provincecode = this.registerForm.district[0]
              let citycode = this.registerForm.district[1]
              let province = codeToText[provincecode]
              let city = codeToText[citycode]
              this.registerForm['province'] = province
              this.registerForm['city'] = city
              this.$http.post('api/register', this.registerForm).then(res=>{
                let code = res.data.code
                if (code == 1){
                  this.$message.error('该用户名已经存在')
                }
                else{
                  this.$message.success('注册成功!')
                  this.$emit('registered', 'success')
                  this.registerForm.name = ''
                  this.registerForm.password = ''
                  this.registerForm.confirmPassword = ''
                  this.$router.push({path: '/login', replace: true})
                }
              }).catch(e=>{
                this.$message.error(e)
              })
            } else {
              this.$message.error('表单格式不正确')
              return false;
            }
          });
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .register-form{
  width: 100%;
  height: 100vh;
  background-image: url('../../assets/login-bg.jpg');
  background-position: center center;
  background-repeat: no-repeat;
  background-size: 100% 100%;
}
.bg{
  width: 100%;
  height: 100%;
  position: fixed;
  background-color: rgba(0, 0, 0, 0.3);
}
.register-form /deep/ .el-input__inner{
  background-color: transparent;
  color: #fff;
  height: 6vh;
  border-radius: 3vh;
  border: 1px solid #fff;
  font-size: 2vh;
}
input::placeholder{
    color: #000;
}
.form-box{
  width: 28%;
  min-height: 20vh;
  box-sizing: border-box;
  padding: 40px;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border-radius: 2vh;
  border: 1px solid #fff;
  background-color: rgba(255, 255, 255, 0.2);
}
.title{
  text-align: center;
  width: 100%;
  font-size: 4vh;
  color: #fff;
}
.register-form /deep/ .el-button--primary{
  margin-top: 40px;
  background-color: #fff;
  color: #000;
  border-color: #fff;
  height: 5.5vh;
  width: 100%;
  border-radius: 3vh;
  font-size: 2.5vh;
}
.register-form /deep/ .el-button--primary:focus, .el-button--primary:hover{
  background-color: #ccc;
}
</style>