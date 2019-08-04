<template>
    <div class="feature">
    <el-row>
  <el-col :span="4"><div class="grid-content bg-purple">{{zgu }}</div></el-col>
  <el-col :span="4"><div class="grid-content bg-purple-light">{{ zgu}}</div></el-col>
  <el-col :span="8"><div class="grid-content bg-purple">

     <el-carousel :interval="4000" type="card" height="200px">
    <el-carousel-item v-for="huxing_img in fangjianhuxing_list" :key="huxing_img">
            <img :src="huxing_img.xuanchuan_img" alt="..."  style="width: 319px; height: 198px">
    </el-carousel-item>
    </el-carousel>

  </div></el-col>

  <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
  <el-col :span="4"><div class="grid-content bg-purple-light"></div></el-col>
</el-row>











</div>
</template>

<script>
    export default {
        name: "fangjianhuxing.vue",
        data() {
        return  {
          zgu:".",
            fangjianhuxing_list:[],
            }
        },
        created(){
      this.$axios.get(this.$settings.Host+"/home/room_type/").then(res =>{
        this.fangjianhuxing_list=res.data;
      })
    }
    }

</script>


<style scoped>
    .feature {
    width: 100%;
    height: 220px;
    overflow: hidden;
    background-color: rgba(32, 206, 187, 0.3);
    filter: progid:DXImageTransform.Microsoft.gradient(startColorstr=#4c20cebb,endColorstr=#4c20cebb);
}


  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>