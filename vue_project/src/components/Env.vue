<template>
  <div>
    <input type="text" placeholder="请在此输入环境关键字" class="form-control">
    <br>
    <span style="font-size: xx-small;color:gray">当前切换环境用脚本为：</span>{{ env_script }}
    <br><br>

    <form action="/upload_env_cass/" method="post" enctype="multipart/form-data">
      <input type="file" class="btn btn-outline-secondary btn-sm" style="border-radius:5px 0 0 5px">
      <button type="submit" class="btn btn-outline-secondary" style="border-radius:0 5px 5px 0">上传</button>
    </form>


  </div>

</template>

<script>
import axios from "axios";


export default {
  data() {
    return {
      env_script: 'biubiubiu',
    }
  },
  mounted: function () {
    axios.get('/get_env_script').then(res => {
      this.env_script = res.data
    })
  }
}
</script>

<style scoped>

</style>