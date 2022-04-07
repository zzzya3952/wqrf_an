<template>
  <div>
    <table class="table" style="text-align: center">
      <thead class="table-light">
      <tr style="font-size: large;color: #067f40">
        <th>选中</th>
        <th>id</th>
        <th>数据变量名称</th>
        <th>
          <button class="btn btn-success" @click="add_datas">添加新数据</button>
        </th>
      </tr>
      </thead>

      <tbody>
      <tr v-for="(i,index) in datas">
        <td><input @click="tj_data(index)" type="radio" name="aaa" class="form-check-input"></td>
        <td>{{ i.id }}</td>
        <td>{{ i.name }}</td>
        <td>
          <button @click="set_datas(index)" class="btn btn-outline-success btn-sm" data-bs-toggle="modal"
                  data-bs-target="#myModal_2">设置
          </button> &nbsp;
          <button @click="del_datas(i.id)" class="btn btn-outline-danger btn-sm">删除</button>
        </td>
      </tr>
      </tbody>
    </table>


    <!-- 模态框 -->
    <div class="modal fade" id="myModal_2">
      <div class="modal-dialog modal-lg modal-dialog-centered">
        <div class="modal-content">

          <!-- 模态框头部 -->
          <div class="modal-header">
            <h4 class="modal-title">请修改数据变量: </h4>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>

          <!-- 模态框内容 -->
          <div class="modal-body">
            name:
            <input type="text" class="form-control" placeholder="数据变量名称" v-model="chose_data.name"> <br>
            value:
            <textarea class="form-control" rows="5" placeholder="数据变量的值" v-model="chose_data.value"></textarea>

          </div>

          <!-- 模态框底部 -->
          <div class="modal-footer">
            <button @click="save_datas" type="button" class="btn btn-success" data-bs-dismiss="modal">保存</button>
          </div>

        </div>
      </div>
    </div>


  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      datas: [],
      chose_data: {},
    }
  },
  mounted: function () {
    axios({
      url: "http://localhost:8000/get_datas/"
    }).then(res => {
      this.datas = res.data.datas
    })
  },
  methods: {
    add_datas() {
      axios({
        url: "http://localhost:8000/add_datas/"
      }).then(res => {
        this.datas = res.data.datas
      })
    },
    del_datas(id) {
      axios.get("http://localhost:8000/del_datas/", {
        params: {
          id: id
        }
      }).then(res => {
        this.datas = res.data.datas
      })
    },
    deepCopy(obj) {
      var a = JSON.stringify(obj);
      var newobj = JSON.parse(a);
      return newobj
    },
    set_datas(index) {
      this.chose_data = this.deepCopy(this.datas[index])
    },
    save_datas() {
      axios.get("http://localhost:8000/save_datas/", {
        params: {
          id: this.chose_data.id,
          new_name: this.chose_data.name,
          new_value: this.chose_data.value,
        }
      }).then(res => {
        this.datas = res.data.datas
      })
    },
    tj_data(index) {
      this.$emit('upda', {now_data_name: this.datas[index].name, now_data_id: this.datas[index].id})
    }
  }
}
</script>

<style scoped>

</style>