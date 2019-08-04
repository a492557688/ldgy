<template>
    <div class="bottom">
        <el-card class="box-card">
             <el-row>
          <el-col :span="8"><div class="grid-content bg-purple"  v-text="zwf"></div></el-col>
          <el-col :span="8"><div class="grid-content bg-purple-light">
                     <span></span>
                        <el-col :span="8">
                       <el-row>
                           扫描下载灵动APP
                       </el-row>
                        <el-row>
                           立即签约好品质房源
                       </el-row>
                    </el-col>
               <el-col :span="8">
                  <span ><el-image :src="img_url1" style="width:70px"></el-image></span>
                 </el-col>
          </div></el-col>
          <el-col :span="8"><div class="grid-content bg-purple" v-text="zwf"></div></el-col>
        </el-row>
        </el-card>
        <el-image :src="img_url2" style="width:130px" class="app_home"></el-image>
    </div>
</template>

<script>
    export default {
        name: "bottom",
            data(){
        return  {
            zwf:".",
            gg:" 扫描下载自如APP\r\n"+"\r\n立即签约好品质房源",
            img_url1:this.$settings.static_img+"/app_2q.jpg",
            img_url2:this.$settings.static_img+"/app_home.png",

            }
        },
     created(){
        //   this.$axios.get(this.$settings.static_img+"app_2q.jpg").then(res =>{
        // this.img_list=res.data

      // })
    }
    }
</script>

<style scoped>
    .app_home{
       float: right;;position: relative;
        bottom: 130px;
        right: 550px;
    }


 .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }


  .box-card {
      padding: 0;
      border: 0;
    width: 100%;
      height: 100px;
  }
 .el-card__body {
      padding: 0;
  }



</style>