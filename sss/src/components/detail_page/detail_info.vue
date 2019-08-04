<template>
    <div class="info">
        <el-carousel :interval="4000" type="card" height="400px">
            <el-carousel-item v-for="img_obj in house_info.hourseimg_list" :key="img_obj">
                <el-image :src="host+img_obj.img_file" style="width: 400px; height: 300px"></el-image>

            </el-carousel-item>
        </el-carousel>
        <el-row :gutter="20">
            <el-col :span="6">
                <div class="grid-content bg-purple">.</div>
            </el-col>
            <el-col :span="10">
                <div class="grid-content bg-purple">
                    <h1>{{house_info.title}}</h1>
                    <el-tag type="danger" v-for="e1 in house_info.expenses" v-bind:key="e1">{{e1}}</el-tag>
                    <div class="info">
                        <div>原 价:{{ house_info.yuanjia }}房间编号:{{ house_info.room_id }}</div>

                        <div>面 积 :{{ house_info.size }} 地 铁:{{ house_info.zhoubian.name }}</div>
                        <div>公 交:{{ house_info.transportation.name }} 朝向:{{ house_info.get_orientation_display }}</div>
                        <div>楼层:{{ house_info.level }} 小区名称 :{{ house_info.xiaoqu }}</div>
                        <div>所在区域 :{{ house_info.area }} 所在小镇 :{{ house_info.town }}</div>

                    </div>
                    <h1> 房屋配置：具体配置以现场实际情况为准</h1>
                    <ul v-for="allocation in house_info.allocation" v-bind:key="allocation">
                        <li>{{allocation}}</li>
                    </ul>

                    <div>
                        <el-card class="box-card">
                            <div slot="header" class="clearfix">
                                <el-button type="warning" round>基本信息</el-button>
                                <el-button type="warning" round>周边配套</el-button>
                                <el-button type="warning" round>扫码关注</el-button>
                                <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
                            </div>
                             <el-table
    :data="tableData"
    stripe
    style="width: 100%">
    <el-table-column
      prop="or_id"
      label="房间"
      width="180">
    </el-table-column>
    <el-table-column
      prop="price"
      label="租金"
      width="180">
    </el-table-column>
    <el-table-column
      prop="get_state_display"
      label="状态">
    </el-table-column>
<el-table-column
      prop="expiration_Date"
      label="	可租日期">
    </el-table-column>
<el-table-column
      prop="have_windows"
      label="窗户">
    </el-table-column>
      <el-table-column
      prop="have_yangtai"
      label="阳台">
    </el-table-column>
<el-table-column
      prop="have_selfwc"
      label="独立卫生间">
    </el-table-column>
  </el-table>
                            <div class="text item" v-html="house_info.protocol">
                            </div>
                        </el-card>

                    </div>
                </div>
            </el-col>
            <el-col :span="8">
                  <el-col :span="8"><div class="grid-content bg-purple">
                      <h1>活动价：{{ house_info.xianjia}}</h1>
                      <h1>转租换房用户不享受此优惠</h1>
                      <h1>预约看法电话:{{ phone }}</h1>
                      <h1>活动价：{{ house_info.xianjia}}</h1>

                  </div></el-col>
              <el-col :span="16"><div class="grid-content bg-purple-light"></div></el-col>

                <div class="grid-content bg-purple">.</div>
            </el-col>
        </el-row>

    </div>


</template>

<script>
    export default {
        name: "detail_info",
        data() {
            return {
                // zhanwefu:"   .    ",
                house_id: "",
                house_info: [],
                phone: "",

                test: "http://127.0.0.1:8000/media/housing/CgoKaFzuT_OAc-D-AACGM6HPvso003.jpg",
                host: this.$settings.Host + "/media/",
                tableData:""
            }
        },
        created() {
            this.house_id = this.$route.params.id;
            this.$axios.get(this.$settings.Host + "/detail/house_info/?id=" + this.house_id).then(res => {
                this.house_info = res.data[0];
                this.tableData=this.house_info.other_Room_details1;
                this.phone=this.$settings.phone
            })
        }
    }
</script>

<style scoped>

</style>