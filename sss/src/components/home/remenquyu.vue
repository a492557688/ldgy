<template>
    <el-row>
    <el-row>
      <el-col :span="8"><div class="grid-content bg-purple">{{zwf}}</div></el-col>
  <el-col :span="9"><div class="grid-content bg-purple-light">
       <el-button type="warning" plain @click="update_rmqy(1)" >嘉定区</el-button>
       <el-button type="warning" plain  @click="update_rmqy(2)">松江区</el-button>
       <el-button type="warning" plain @click="update_rmqy(3)">闵行区</el-button>
       <el-button type="warning" plain @click="update_rmqy(4)">宝山区</el-button>
       <el-button type="warning" plain @click="update_rmqy(5)">浦东新区</el-button>
       <el-button type="warning" plain @click="update_rmqy(6)">奉贤区</el-button>
        <router-link to="/filter"><el-button type="text">更多房源</el-button> </router-link>
  </div></el-col>
  <el-col :span="8"><div class="grid-content bg-purple">{{zwf}}</div></el-col>
    </el-row>
     <el-row>
         <el-col :span="8"><div class="grid-content bg-purple">{{zwf}}</div></el-col>
  <el-col :span="8"><div class="grid-content bg-purple-light">
            <!--图片-->
                <div class="demo-image__placeholder">
<!--          <div class="block">-->
<!--            <el-image :src="this.$settings.Host+'/media/'+area_list[0].first_img"></el-image>-->
<!--          </div>-->
    <div class="block">
            <span class="demonstration"></span>
               <el-row>
            <el-card :body-style="{ padding: '0px', width:'500px',height: '400px' }" class="el-card">
              <el-image :src="this.$settings.Host+'/media/'+area_list[0].first_img" class="image"  style="width: 500px; height: 400px"></el-image>
              <div style="padding: 14px;">
                <span>{{area_list[0].xiaoqu.xiaozheng.name}}{{area_list[0].xiaoqu.name }}</span>
                  <div></div>
                <span>现价：{{area_list[0].xianjia}}</span>
                <el-tag type="danger" v-for="e1 in area_list[0].expenses" v-bind:key="e1">{{e1}}</el-tag>
                <div class="bottom clearfix">

                </div>
              </div>
            </el-card>
        </el-row>

          </div>




        </div>
        </div>
  </el-col>
  <el-col :span="7"><div class="grid-content bg-purple">{{zwf}}</div></el-col>
     <!--图片结束-->
     </el-row>
    </el-row>
</template>

<script>
    export default {
        name: "remenquyu",
        methods: {
            update_rmqy: function (num) {
                if (num===1){
                     this.this_area="嘉定";
                }
                else if(num===2){
                  this.this_area="松江";
                }
                 else if(num===3){
                  this.this_area="闵行";
                }
                 else if(num===4){
                  this.this_area="宝山";
                }
                 else if(num===5){
                  this.this_area="浦东";
                }
                else{
                     this.this_area="奉贤";
                }
                 this.$axios.get(this.$settings.Host+"/home/area_houre/?area="+this.this_area).then(res =>{
                        this.area_list=res.data
                    })
                }
                },
        data(){
        return  {
            zwf:".",
            area_list:[],
            this_area:"",
               currentDate: new Date()
            }
        },
     created(){
          this.$axios.get(this.$settings.Host+"/home/area_houre/?area=嘉定").then(res =>{
        this.area_list=res.data

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