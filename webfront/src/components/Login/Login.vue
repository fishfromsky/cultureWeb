<template>
  <div class="login-form">
    <div class="bg"></div>
    <div class="form-box">
      <div class="title">登&nbsp&nbsp&nbsp录</div>
      <el-form ref="loginForm" :model="loginForm" label-position="top" @submit.native.prevent="onLogin" style="margin-top: 40px;">
        <el-form-item>
          <el-input v-model="loginForm.username" autocomplete="username" placeholder="用户名"></el-input>
        </el-form-item>
        <el-form-item>
          <el-input type="password" v-model="loginForm.password" autocomplete="current-password" placeholder="密码"></el-input>
        </el-form-item>
        <div class="password-item">
          <el-checkbox v-model="checked">记住密码</el-checkbox>
          <div class="forget">忘记密码</div>
        </div>
        <el-form-item>
          <el-button type="primary" @click="onLogin">立即登录</el-button>
        </el-form-item>
        <div class="register">
          <span style="font-size: 2vh;">没有账号？</span>
          <span style="font-size: 2.5vh; margin-left: 5px; cursor: pointer;" @click="showRegisterDialog">立即注册</span>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script>
import RegisterForm from './RegisterForm.vue';
import Cookies from 'js-cookie'

export default {
  components: {
    RegisterForm,
  },
  data() {
    return {
      loginForm: {
        username: '',
        password: '',
      },
    };
  },
  methods: {
    onLogin() {
      // 登录逻辑
      this.$http.post('api/login', this.loginForm).then(res=>{
        let data = res.data.code
        if (data == 1){
          this.$message.error('该用户名尚未注册')
        }
        else if (data == 2){
          this.$message.error('密码错误')
        }
        else{
          let data = res.data.data
          Cookies.set('token', data.token)
          Cookies.set('name', data.username)
          Cookies.set('user_id', data.id)
          this.$message.success('登录成功')
          this.$router.push('/')
        }
      }).catch(e=>{
        this.$message.error(e)
      })
    },
    showRegisterDialog(){
      this.$router.push({path: '/register', replace: true})
    }
  },
};
</script>

<style scoped>

.login-form{
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
.login-form /deep/ .el-input__inner{
  background-color: transparent;
  color: #fff;
  height: 6vh;
  border-radius: 3vh;
  border: 1px solid #fff;
  font-size: 2vh;
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

.password-item{
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}
.password-item /deep/ .el-checkbox__input.is-checked .el-checkbox__inner, .el-checkbox__input.is-indeterminate .el-checkbox__inner {
    background-color: #000;
    border-color: #fff;
}
.password-item /deep/ .el-checkbox{
  color: #fff;
}
.password-item /deep/ .el-checkbox__label{
  font-size: 2vh;
}
.password .el-checkbox__inner{
  width: 2vh;
  height: 2vh
}
.password-item /deep/ .el-checkbox__input.is-checked+.el-checkbox__label {
    color: #000;
}
.forget{
  font-size: 2vh;
  color: #fff;
  cursor: pointer;
}
.login-form /deep/ .el-button--primary{
  margin-top: 40px;
  background-color: #fff;
  color: #000;
  border-color: #fff;
  height: 5.5vh;
  width: 100%;
  border-radius: 3vh;
  font-size: 2.5vh;
}
.login-form /deep/ .el-button--primary:focus, .el-button--primary:hover{
  background-color: #ccc;
}
.register{
  width: 100%;
  text-align: center;
  color: #fff;
}
</style>
