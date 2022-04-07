<template>
  <div>
    <table class="table table-striped table-bordered" style="text-align: center">
      <thead>
      <tr>
        <th>选中</th>
        <th>用例名称</th>
        <th>重要等级</th>
        <th>Unittest</th>
        <th>
          <button @click="add_cases()" class="btn btn-outline-primary btn-sm">添加新脚本</button>
        </th>
      </tr>
      </thead>

      <tbody>
      <tr v-for="(i,index) in case_list">
        <td><input @click="tj_cases_count" type="checkbox" name="cccc" class="form-check-input" :value="i.id" checked>
        </td>
        <td>{{ i.name }}</td>
        <td>{{ i.level }}</td>
        <td>{{ i.ifut }}</td>
        <td>
          <button @click="set_cases(index)" data-bs-toggle="modal" data-bs-target="#myModal"
                  class="btn btn-outline-success btn-sm">设置
          </button>
          &nbsp;
          <button @click="del_cases(i.id)" class="btn btn-outline-danger btn-sm">删除</button>
        </td>
      </tr>

      </tbody>
    </table>

    <!-- 模态框 -->
    <div class="modal fade" id="myModal">
      <div class="modal-dialog modal-lg modal-dialog-centered">
        <div class="modal-content">

          <!-- 模态框头部 -->
          <div class="modal-header">
            <h4 class="modal-title">请修改用例: </h4>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>

          <!-- 模态框内容 -->
          <div class="modal-body">
            name:
            <input type="text" class="form-control" placeholder="用例名称" v-model="chose_case.name"> <br>
            level:
            <input type="text" class="form-control" placeholder="重要性" v-model="chose_case.level"> <br>
            unittest:
            <input type="checkbox" class="form-check-input" :checked="chose_case.ifut" @click="check_ifut()">
            <br><br>
            script: <span style="font-size: xx-small;color: gray">（当前脚本为：{{ chose_case.script }}）</span>
            <form id="form_cases" :action="'http://localhost:8000/upload_case/'+chose_case.id+'/'" method="post"
                  enctype="multipart/form-data">
              <input type="file" name="upload_case_script" class="btn btn-outline-secondary btn-sm">
            </form>
          </div>

          <!-- 模态框底部 -->
          <div class="modal-footer">
            <button @click="save_cases" type="button" class="btn btn-success" data-bs-dismiss="modal">保存</button>
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
      case_list: [],
      chose_case: {},
    }
  },
  mounted: function () {
    axios({
      url: 'http://localhost:8000/get_cases/'
    }).then(res => {
      this.case_list = res.data.cases;
      var now_case_ids = [];
      for (var i in this.case_list) {
        now_case_ids.push(this.case_list[i].id.toString())
      }
      this.$emit('upc', {now_cases_count: this.case_list.length, now_case_ids: now_case_ids})
    })
  },
  methods: {
    tj_cases_count() {
      var all_chose_case = $('input[name="cccc"]:checked');
      var now_case_ids = [];
      for (var i = 0; i < all_chose_case.length; i++) {
        now_case_ids.push(all_chose_case[i].value)
      }
      this.$emit('upc', {now_cases_count: all_chose_case.length, now_case_ids: now_case_ids})
    },
    add_cases() {
      axios({
        url: "http://localhost:8000/add_cases/"
      }).then(res => {
        this.case_list = res.data.cases
      })
    },
    del_cases(case_id) {
      axios.get("http://localhost:8000/del_cases/", {
        params: {
          case_id: case_id
        }
      }).then(res => {
        this.case_list = res.data.cases
      })
    },
    deepCopy(obj) {
      var a = JSON.stringify(obj);
      var newobj = JSON.parse(a);
      return newobj
    },
    set_cases(index) {
      this.chose_case = this.deepCopy(this.case_list[index])
    },
    save_cases() {
      axios.get('http://localhost:8000/save_cases/', {
        params: {
          case_id: this.chose_case.id,
          new_name: this.chose_case.name,
          new_level: this.chose_case.level,
          new_ifut: this.chose_case.ifut,
        }
      }).then(res => {
        document.getElementById('form_cases').submit();
      })
    },
    check_ifut() {
      this.chose_case.ifut = event.target.checked;
    }
  }
}
</script>

<style scoped>

</style>