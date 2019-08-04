<template>
<el-row>
    <el-row>
      <el-col :span="8"><div class="grid-content bg-purple">{{zwf}}</div></el-col>
  <el-col :span="8"><div class="grid-content bg-purple-light">
       <el-button type="warning" plain @click="update_jpf(1)" >今日特惠</el-button>
       <el-button type="warning" plain  @click="update_jpf(2)">最新房源</el-button>
       <el-button type="warning" plain @click="update_jpf(3)">热门小区</el-button>
       <el-button type="warning" plain @click="update_jpf(4)">人气房源</el-button>
       <router-link to="/jinritehui">
            <a>更多房源</a>
       </router-link>
  </div></el-col>
  <el-col :span="8"><div class="grid-content bg-purple">{{zwf}}</div></el-col>
    </el-row>

     <el-row>
         <el-col :span="8"><div class="grid-content bg-purple">{{zwf}}</div></el-col>
        <el-col :span="8"><div class="grid-content bg-purple-light">
            <!--图片-->
                <div class="demo-image__placeholder">
          <div class="block">
<!--            <el-image :src="jpfy[0].first_img"></el-image>-->
          </div>
          <div class="block">
            <span class="demonstration"></span>
               <el-row>
            <el-card :body-style="{ padding: '0px', width:'500px',height: '400px' }" class="el-card">
              <el-image :src="this.$settings.Host+'/media/'+jpfy[0].first_img" class="image"  style="width: 500px; height: 400px"></el-image>
              <div style="padding: 14px;">
                <span>{{jpfy[0].xiaoqu.xiaozheng.name}}{{jpfy[0].xiaoqu.name }}</span>
                <el-tag type="danger" v-for="e1 in jpfy[0].expenses" v-bind:key="e1">{{e1}}</el-tag>
                <div class="bottom clearfix">
                  <time class="time">{{ currentDate }}</time>
                </div>
              </div>
            </el-card>
        </el-row>



<!--            <el-image :src="this.$settings.Host+'/media/'+jpfy[0].first_img"></el-image>-->
          </div>
        </div>
        </div></el-col>
  <el-col :span="8"><div class="grid-content bg-purple">{{zwf}}</div></el-col>
     <!--图片结束-->

     </el-row>


</el-row>

</template>

<script>
    export default {
        name: "jingpinfangyuan",
        methods: {
            update_jpf: function (num) {
                if (num===1){
                     this.thif_func="jrth";
                }
                else if(num===2){
                  this.thif_func="zxfy";
                }
                 else if(num===3){
                  this.thif_func="rmxq";
                }
                else{

                     this.thif_func="rqfy";
                }
                 this.$axios.get(this.$settings.Host+"/home/jpfy/?type="+this.thif_func).then(res =>{
                        this.jpfy=res.data

                    })

                }
        },
        data(){
        return  {
            zwf:".",
            jpfy:[],
            thif_func:"",

            }
        },
        created(){
      this.$axios.get(this.$settings.Host+"/home/jpfy/?type="+"jrth").then(res =>{
        this.jpfy=res.data;

      })
    }
    }

</script>

<style scoped>
     .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }

  .clearfix:after {
      clear: both
  }
  .el-card {
      width: 500px;
      height: 500px;
  }
    font{
        font-size: 29px;
    }
.el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
     background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
     background-color: #d3dce6;
  }
</style>