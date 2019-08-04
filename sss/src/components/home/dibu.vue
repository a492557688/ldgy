<template>
<dl class="babotForm">

</dl>
</template>

<script>
    export default {
        name: "dibu",
        data(){
            return{
              currentDate: new Date(),
                reg:"https://www.qk365.com/images/sss.png"
            }
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
</style>