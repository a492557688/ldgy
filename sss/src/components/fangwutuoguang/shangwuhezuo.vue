<template>
    <div>
<el-card class="box-card">
  <div slot="header" class="clearfix">
    <h1>我们需要您有这样的资质</h1>
    <el-button style="float: right; padding: 3px 0" type="text">


    </el-button>
  </div>
  <div  class="text item" v-html="msg">

  </div>
</el-card>
<el-row>
  <el-col :span="8"><div class="grid-content bg-purple" v-text="zwf"></div></el-col>
  <el-col :span="8"><div class="grid-content bg-purple-light"><el-button @click="drawer = true" type="primary" style="margin-left: 16px;">
  一键托管房屋
</el-button></div></el-col>
  <el-col :span="8"><div class="grid-content bg-purple"></div></el-col>
</el-row>





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

        </div>
</template>

<script>
    export default {
        name: "shangwuhezuo",
        data(){
        return  {
            quyu_list:[],
            zwf:".",
            msg:"<div class=\"engineering_main01\">" +
                "\t\t\t<h3>我们需要您有这样的资质</h3><br><br>\n" +
                "\t\t\t<p>1、具备工作能力，有营业执照者为佳 </p><br>\n" +
                "\n" +
                "\t\t\t<p>2、有一定的团队规模，至少在3个班组以上，每个班组至少会四个工种，包含水、电、泥、木等</p><br>\n" +
                "\t\t\t\n" +
                "\t\t\t<p>3、接受清包纯人工的装修</p><br>\n" +
                "\t\t\t\n" +
                "\t\t\t<p>4、按我司规定完成相应的装修需求，包括电气线路的敷设及走向、装饰抹灰基层、建筑装饰给排\n" +
                "\t\t\t水设置走向、吊顶工程、墙地砖及片材铺设、卫生间和厨房的防水作业等</p><br>\n" +
                "\t\t\t\n" +
                "\t\t\t<p>5、施工地点分布在上海、北京、南京、杭州、武汉、苏州六大城市</p>\n" +
                "\t\t</div>",
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