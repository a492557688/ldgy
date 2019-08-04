<template>
    <div>
 <el-carousel :interval="5000" arrow="always" height="550px" >
    <el-carousel-item v-for="st in img_list" v-bind:key="st">
     <el-image :src=static_url+st  ></el-image>
    </el-carousel-item>

  </el-carousel>
<el-button @click="drawer = true" type="primary" style="margin-left: 16px;">
  一键托管房屋
</el-button>




<el-drawer
  title="提交托管表单"
  :visible.sync="drawer"
  size="50%">
  <!--  表单 -->
    <el-form ref="form" :model="form" label-width="80px">
  <el-form-item label="姓名">
    <el-input v-model="form.name"></el-input>
  </el-form-item>
  <el-form-item label="电话">
         <el-input v-model="form.phone"></el-input>
  </el-form-item>
    <el-form-item label="房源地址">
     <el-cascader :options="quyu_list" clearable></el-cascader>
  </el-form-item>
  <el-form-item label="请输入街道">
         <el-input v-model="form.jiedao"></el-input>
  </el-form-item>

  <el-form-item label="预约时间">
    <el-col :span="11">
      <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
    </el-col>
    <el-col class="line" :span="2">-</el-col>
    <el-col :span="11">
      <el-time-picker placeholder="选择时间" v-model="form.date2" style="width: 100%;"></el-time-picker>
    </el-col>
  </el-form-item>

<el-form-item label="备注" placeholder="备注" >
    <el-input type="textarea" v-model="form.beizhu"></el-input>
  </el-form-item>


  <el-form-item>
    <el-button type="primary" @click="onsubmit">立即创建</el-button>
    <el-button>取消</el-button>
  </el-form-item>
</el-form>
        </el-drawer>
<!--    表单结束-->








        </div>
</template>

<script>
    export default {
        name: "banner",
        data(){
        return  {
            quyu_list:[],
             form: {
          name: '',
          phone: '',
          jiedao: '',
          date2: '',
          date1: false,
          beizhu: ''
        },

            static_url:this.$settings.static_img,
             drawer: false,
        innerDrawer: false,
            img_list:["CgoKZ1yPOamARigVAAG2AmFNtMo344.jpg","fwtg_banner.jpg",]
            }},
        methods: {
            onsubmit:function () {
                  this.$axios({
                    url:this.$settings.Host+"/process/submit_fwtg/",
                    method: 'POST',
                  // headers: { 'headers': {
           // 'Content-Type': 'application/x-www-form-urlencoded'
       // }},  // 携带请求头
                    data:this.form,

                  }).then(res =>{console.log(res)})
            }},



            created(){
              this.$axios.get(this.$settings.Host+"/filter/area/").then(res =>{this.quyu_list=res.data;});

        },



    }
</script>

<style scoped>

</style>