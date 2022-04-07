<template>
  <div>
    <label class="radio-inline">
      <input @click="chose_apk_method(false)" type="radio" name="aabbcc" value="不安装" checked>
      不安装
    </label>
    &#12288;
    <label class="radio-inline">
      <input @click="chose_apk_method(true)" type="radio" name="aabbcc" value="覆盖安装">
      覆盖安装
    </label>
    &#12288;
    <label class="radio-inline">
      <input @click="chose_apk_method(true)" type="radio" name="aabbcc" value="卸载安装">
      卸载安装
    </label>

    <form target="iframe_name" v-if="show_up_apk" style="float: right" action="http://localhost:8000/up_apk/"
          method="post" enctype="multipart/form-data">
      <input id="up_apk_name" name="up_apk_name" type="file" class="btn btn-outline-primary btn-sm"
             style="border-radius: 5px 0 0 5px">
      <button @click="up_apk_btn" type="submit" class="btn btn-primary" style="border-radius: 0 5px 5px 0">上传apk
      </button>
    </form>
    <br><br>
    <iframe id="iframe_id" name="iframe_name" style="width: 100%;height: 60px"></iframe>

  </div>
</template>

<script>
export default {
  data() {
    return {
      show_up_apk: false
    }
  },
  mounted: function () {
    this.$emit('upa', {now_apk_method: $('input[name="aabbcc"]:checked').val(), now_apk_name: ""})
  }
  ,
  methods: {
    chose_apk_method(ft) {
      // 根据选择的是哪个方式来决定form上传显示还是隐藏。靠控制show_up_apk的值为真还是假来实现
      this.show_up_apk = ft;
      this.$emit('upa', {now_apk_method: $('input[name="aabbcc"]:checked').val(), now_apk_name: ""})
    },
    up_apk_btn() {
      var now_apk_name = document.getElementById('up_apk_name').value;
      var l = now_apk_name.split('\\');
      console.log(l)
      var res = l[l.length - 1]
      this.$emit('upa', {now_apk_method: $('input[name="aabbcc"]:checked').val(), now_apk_name: res})
    }
  }
}
</script>

<style scoped>

</style>