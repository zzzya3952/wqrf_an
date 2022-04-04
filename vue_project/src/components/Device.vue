<template>
  <div class="list-group list-group-checkable">
    <div v-for="(d,index) in device_list">
      <input @click="cd(d.name,d.id)" class="list-group-item-check" type="radio" :id="'device_'+d.id"
             name="listGroupCheckableRadios">
      <label class="list-group-item py-3" :style="{borderColor:getColor(d.state)}" :for="'device_'+d.id">
        {{ d.id }} . {{ d.name }}
        <span class="small opacity-50">
                    系统版本：{{ d.pla }} &#12288; 当前状态：{{ d.state }} &#12288; UDID：{{ d.udid }}
                </span>
      </label>
    </div>
    <div class="btn-group">
      <button @click="fix()" type="button" class="btn btn-sm btn-outline-dark">重新授权</button>
      <button onclick="alert('请手动检查设备数据线,开发者模式开关等情况！')" type="button" class="btn btn-sm btn-outline-dark">重新链接</button>
      <button onclick="window.open('/admin/myapp/db_devices/')" type="button" class="btn btn-sm btn-outline-dark">管理设备
      </button>
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
    cd(d_name, d_id) {
      this.$emit('upd', {now_deviceName: d_name, now_deviceId: d_id})
    },
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

.bd-placeholder-img {
  font-size: 1.125rem;
  text-anchor: middle;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none
}

@media (min-width: 768px) {
  .bd-placeholder-img-lg {
    font-size: 3.5rem
  }
}

.b-example-divider {
  height: 3rem;
  background-color: rgba(0, 0, 0, .1);
  border: solid rgba(0, 0, 0, .15);
  border-width: 1px 0;
  box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15)
}

.bi {
  vertical-align: -.125em;
  fill: currentColor
}

.opacity-50 {
  opacity: .5
}

.opacity-75 {
  opacity: .75
}

.list-group {
  width: auto;
  max-width: 460px;
  margin: 4rem auto
}

.form-check-input:checked + .form-checked-content {
  opacity: .5
}

.form-check-input-placeholder {
  pointer-events: none;
  border-style: dashed
}

[contenteditable]:focus {
  outline: 0
}

.list-group-checkable {
  display: grid;
  gap: .5rem;
  border: 0
}

.list-group-checkable .list-group-item {
  cursor: pointer;
  border-radius: .5rem
}

.list-group-item-check {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none
}

.list-group-item-check:hover + .list-group-item {
  background-color: var(--bs-light)
}

.list-group-item-check:checked + .list-group-item {
  color: #fff;
  background-color: var(--bs-blue)
}

.list-group-item-check[disabled] + .list-group-item, .list-group-item-check:disabled + .list-group-item {
  pointer-events: none;
  filter: none;
  opacity: .5
}

</style>