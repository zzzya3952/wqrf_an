<template>
    <div class="list-group list-group-checkable">
        <div v-for="(d,index) in device_list">
            <input @click="cd(d.name,d.id)" class="list-group-item-check" type="radio" :id="'device_'+d.id" name="listGroupCheckableRadios" >
            <label class="list-group-item py-3" :style="{borderColor:getColor(d.state)}" :for="'device_'+d.id">
                {{d.id}} . {{d.name}}
                <span class="small opacity-50">
                    系统版本：{{d.pla}} &#12288; 当前状态：{{d.state}} &#12288; UDID：{{d.udid}}
                </span>
            </label>
        </div>
        <div class="btn-group">
            <button @click="fix()" type="button" class="btn btn-sm btn-outline-dark">重新授权</button>
            <button onclick="alert('请手动检查设备数据线,开发者模式开关等情况！')" type="button" class="btn btn-sm btn-outline-dark">重新链接</button>
            <button onclick="window.open('/admin/myapp/db_devices/')" type="button" class="btn btn-sm btn-outline-dark">管理设备</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      device_list: []
    }
  },

  mounted: function () {
    axios({url: "http://localhost:8000/get_devices/"}).then(res => {
      this.device_list = res.data.data
    })
  },

  methods: {
    getColor(state) {
      if (state == '空闲中') {
        return 'green'
      } else {
        return 'red'
      }
    },

    fix() {
      if (confirm('当adb devices发现手机未授权，且不弹出授权窗口情况下，才可以使用此功能\n注意！此功能会导致adb重启，使所有设备重连，所以请确保无其他设备正在执行任务！') == false) {
        axios.get('/fix_devices/').then(res => {
          alert('重新授权成功');
          this.device_list = res.data.data
        })
      }
    }
  }
}
</script>

<style scoped>
label {
  border: 2px solid black;
  border-radius: 5px;
}
</style>