<template>
    <div>
    <div class="shaixuank">
    <!--这里一块是筛选框-->
    <h1>行政区域：</h1>
    <div >
         <el-button>不限</el-button>
        <el-button v-for="quyu in quyu_list" v-bind:key="quyu" @click="get_filtet_by_quyu(quyu.name)">{{ quyu.name }}区</el-button>
    </div>
    <h1>地铁沿线：</h1>

     <div >
           <el-button>不限</el-button>
        <el-button v-for="ditie in dities" v-bind:key="ditie" @click="get_filtet_by_ditiexian(ditie)">地铁{{ ditie }}</el-button>
          <el-button>浦东线</el-button>
    </div>

    <h1>小区首字母：</h1>
           <el-button>不限</el-button>
            <el-button  v-for="zimu in zimus" v-bind:key="zimu">{{ zimu }}</el-button>
     <div>
    </div>




    </div>
    <div class="reg_model">
        <el-row :gutter="20">
  <el-col :span="4"><div class="grid-content bg-purple">.</div></el-col>
  <el-col :span="14"><div class="grid-content bg-purple">

<!--    <div v-for="img in img_list" v-bind:key="img">-->
      <div class="block" v-for="s in img_list" :key="s">
          <div @click="to_detail(s.id)"><h1 class="el-icon-map-location" size="100px">{{s.xiaoqu.name}}小区-{{s.town}}-{{s.ditie}}地铁线</h1></div>
          <div><el-image :src=host+s.first_img  style="width: 300px; height: 280px" :fit="fit" class="_img" ></el-image></div>



    </div>

  </div></el-col>
  <el-col :span="6"><div class="grid-content bg-purple">.</div></el-col>
</el-row>
</div>
    <div class="fengyeqi">
        <el-row :gutter="20">
  <el-col :span="4"><div class="grid-content bg-purple">.</div></el-col>
  <el-col :span="14"><div class="grid-content bg-purple">
    <el-pagination  @size-change="handleSizeChange"  @current-change="handleCurrentChange"
            background
    :page-size="1"
    :pager-count="7"
    layout="prev, pager, next"
    :total="zongshu">
        </el-pagination>
      </div></el-col>
  <el-col :span="6"><div class="grid-content bg-purple">.</div></el-col>
</el-row>
    </div>
    </div>


</template>

<script>
    export default {
        name: "filter_page",
        data() {
      return {
          dities: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], zimus: [], quyu_list: [], img_list:[],test:"/media/housing/jd_oldFkTR.jpg",
host:this.$settings.Host+"/media/",
          next_url:"",
          pager_count:1,
          zongshu:"",
          previous_url:"",
          this_url:""
      }
      },
      created(){
            this.$axios.get(this.$settings.Host+"/filter/area/").then(res =>{this.quyu_list=res.data;});

            for(var i = 65; i < 91; i++){
                this.zimus.push(String.fromCharCode(i));
            }
        },
          methods: {
            get_filtet_by_quyu: function (quyu) {
                this.$axios.get(this.$settings.Host+"/filter/area_house/?area="+quyu).then(res =>{
                    this.previous_url=res.data.previous;
                    this.next_url=res.data.next;
                    this.zongshu=parseInt(res.data.count);
                    this.img_list=res.data.results;
                    this.this_url=this.$settings.Host+"/filter/area_house/?area="+quyu;
                    this.pager_count=Math.round(this.zongshu/this.img_list.length);


                });

            },
            to_detail:function(id){
               this.$router.push({name:'detail', params:{id: id}})}  ,


            get_filtet_by_ditiexian: function (ditie) {
                this.$axios.get(this.$settings.Host+"/filter/ditie_house/?ditie="+ditie).then(res =>{
                   this.img_list=res.data.results;
                   this.previous_url=res.data.previous;
                    this.next_url=res.data.next;
                    this.zongshu=parseInt(res.data.count);
                    this.this_url=this.$settings.Host+"/filter/ditie_house/?ditie="+ditie;
                    this.pager_count=Math.round(this.zongshu/this.img_list.length);

                });
            },
            handleSizeChange:function (val) {
                 this.$axios.get(this.this_url+"&page="+val).then(res =>{
                    this.img_list=res.data.results;
                   this.previous_url=res.data.previous;
                    this.next_url=res.data.next;
                    this.zongshu=parseInt(res.data.count);
                   this.pager_count=Math.round(this.zongshu/this.img_list.length);

                });
            },
              handleCurrentChange:function (val) {
                 this.$axios.get(this.this_url+"&page="+val).then(res =>{
                    this.img_list=res.data.results;
                   this.previous_url=res.data.previous;
                    this.next_url=res.data.next;
                    this.zongshu=parseInt(res.data.count);
                  this.pager_count=Math.round(this.zongshu/this.img_list.length);

                });
              }
          }
    }

</script>

<style scoped>
.el-image{
        margin:50px ;
}
    #el-image{
        margin:50px ;
}
</style>