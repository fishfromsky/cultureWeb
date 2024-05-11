<template>
    <div class="register-form">
      <el-form ref="registerForm" :model="registerForm" @submit.native.prevent="onRegister" :rules="rules">
        <el-form-item label="用户名" prop="name">
          <el-input v-model="registerForm.name" autocomplete="username" placeholder="请输入您的用户名"></el-input>
        </el-form-item>
        <el-form-item label="手机号" prop="mobile">
          <el-input v-model="registerForm.mobile" placeholder="请输入您的联系手机号码"></el-input>
        </el-form-item>
        <el-form-item label="邮箱地址" prop="email">
          <el-input v-model="registerForm.email" placeholder="请输入您的邮箱地址"></el-input>
        </el-form-item>
        <el-form-item label="所在省市">
          <el-cascader v-model="registerForm.district" :options="optionsnative_place" placeholder="请输入您所在省市"/>
        </el-form-item>
        <el-form-item label="具体地址">
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
                  this.registerForm.email = ''
                  this.registerForm.mobile = ''
                  this.registerForm.district = ''
                  this.registerForm.address = ''
                  this.registerForm.password = ''
                  this.registerForm.confirmPassword = ''
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
  .register-form {
    max-width: 100%;
    margin-left: 10%;
  }
  </style>