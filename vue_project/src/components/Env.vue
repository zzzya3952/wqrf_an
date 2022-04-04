<template>
  <div>
    <input type="text" placeholder="请在此输入环境关键字" class="form-control" v-model="now_env">
    <br>
    <span style="font-size: xx-small;color:gray">当前切换环境用脚本为：</span>{{ env_script }}
    <br><br>

    <form action="http://localhost:8000/upload_env_script/" method="post" enctype="multipart/form-data">
      <input name="upload_env_script" type="file" class="btn btn-outline-secondary btn-sm"
             style="border-radius:5px 0 0 5px">
      <button type="submit" class="btn btn-outline-secondary" style="border-radius:0 5px 5px 0">上传</button>
    </form>
  </div>

</template>

<script>
import axios from "axios";


export default {
  data() {
    return {
      env_script: '',
      now_env: '',
    }
  },
  mounted: function () {
    axios.get('http://localhost:8000/get_env_script/').then(res => {
      this.env_script = res.data
    })
  },
  watch: {
    now_env() {
      this.$emit('upe', {now_env: this.now_env})
    }
  }

}
</script>

<style scoped>

</style>