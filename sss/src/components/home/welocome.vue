<template>
<!--&lt;!&ndash;    <div>&ndash;&gt;-->
<!--&lt;!&ndash;    <div height="500px">&ndash;&gt;-->
<!--&lt;!&ndash; <el-row >&ndash;&gt;-->
<!--&lt;!&ndash;        <el-col :span="8"><div class="grid-content bg-purple"></div></el-col>&ndash;&gt;-->
<!--&lt;!&ndash;            <el-col :span="8"><div class="grid-content bg-purple">&ndash;&gt;-->
<!--&lt;!&ndash;                <span>欢迎来到青客网,您是第</span>&ndash;&gt;-->
<!--&lt;!&ndash;                <span>{{geshu}}</span>&ndash;&gt;-->
<!--&lt;!&ndash;                <span>位灵动服务的客户!</span>&ndash;&gt;-->
<!--&lt;!&ndash;            </div></el-col>&ndash;&gt;-->
<!--&lt;!&ndash;         <el-col :span="8"><div class="grid-content bg-purple"></div></el-col>&ndash;&gt;-->
<!--&lt;!&ndash;     </el-row >&ndash;&gt;-->
<!--&lt;!&ndash; </div>&ndash;&gt;-->
<!--&lt;!&ndash;  </div>&ndash;&gt;-->
<!--    <el-row :gutter="3">-->
<!--  <el-col :span="1"><div class="grid-content ">{{zhanweifu}}</div></el-col>-->
<!--        -->
<!--&lt;!&ndash;            <div class="grid-content bg-purple">&ndash;&gt;-->

<!--&lt;!&ndash;                  <div class="grid-content bg-purple"></div>&ndash;&gt;-->
<!--                <span>欢迎来到青客网,您是第</span>-->
<!--                <span>{{geshu}}</span>-->
<!--                <span>位灵动服务的客户!</span></div>-->
<!--        -->

<!--  <el-col :span="1"><div class="grid-content bg-purple">{{zhanweifu}}</div></el-col>-->
<!--</el-row>-->
    <el-row :gutter="3">
  <el-col :span="8"><div class="grid-content">}{{ zhanweifu }}</div></el-col>
  <el-col :span="8"><div class="grid-content ">
       <span>欢迎来到灵动网,您是第</span>
      <span>{{geshu}}</span>
      <span>位灵动服务的客户!</span>
  </div></el-col>
  <el-col :span="8"><div class="grid-content ">{{ zhanweifu }}</div></el-col>
</el-row>



</template>

<script>
       export default {
        name: "welocome",

        data() {
        return  {
          geshu:"0",
            zhanweifu:"."
            }
        },
   }
</script>

<style scoped>
    span{
        font-size: 28px;
    }
    .el-row {
        height: 50px;
        margin-bottom: 20px;
      }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>