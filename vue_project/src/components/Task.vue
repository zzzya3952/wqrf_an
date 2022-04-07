<template>
  <div class="task_div" id="task_id">
    <button style="float: right" @click="clos_test_div" class="btn btn-outline-dark">关闭</button>
    <h5>当前平台所有任务</h5>
    <table class="table table-striped ">
      <thead class="table-dark">
      <tr>
        <th>任务描述</th>
        <th>启动时间</th>
        <th>当前状态</th>
        <th>操作</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="task in tasks">
        <td>{{ task.des }}</td>
        <td>{{ task.stime }}</td>
        <td>{{ task.state }}</td>
        <td>
          <a href="">终止</a> &#12288;
          <a href="">查看报告</a>
        </td>
      </tr>
      </tbody>

    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      tasks: []
    }
  },
  mounted: function () {
    axios.get('http://localhost:8000/get_tasks/').then(res => {
      this.tasks = res.data.tasks
    })
  },
  methods: {
    clos_test_div() {
      document.getElementById('task_id').style.display = 'none';
    }
  }
}
</script>

<style>
.task_div {
  background-color: white;
  width: 60%;
  height: 70%;
  position: absolute;
  left: 20%;
  top: 10%;
  z-index: 999;
  padding: 10px;
  border-radius: 5px;
  overflow-y: auto;

}
</style>