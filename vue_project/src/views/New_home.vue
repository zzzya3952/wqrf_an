<template>
  <div>
    <Task v-if="task_if_value"></Task>

    <header class="cd-header">
      <div id="cd-logo"><a style="text-decoration: none" href="#"><img src="/static/CSS_menu/img/logo.png"
                                                                       style="width: 100px" alt="Logo"></a></div>
      <nav class="cd-primary-nav">
        <ul>
          <!-- inser more links here -->
          <li><a style="text-decoration: none" href="http://localhost:8080/#/admin/" target="_blank">管理后台</a></li>
          <li><a style="text-decoration: none" href="#0" @click="help_shown">帮助</a></li>
          <li><a style="text-decoration: none" href="#0">下载本地调试包</a></li>
          <li><a style="text-decoration: none" href="#0" @click="task_btn">查看任务列表</a></li>
        </ul>
      </nav> <!-- cd-primary-nav -->
    </header>
    <section id="cd-intro">
      <div id="cd-intro-tagline">
        <h1><strong> Automatic platform</strong></h1>
        <a style="cursor:pointer;text-decoration: none" data-bs-toggle="modal" data-bs-target="#myModal_play"
           class="cd-btn">开始执行</a>
      </div> <!-- #cd-intro-tagline -->
    </section> <!-- #cd-intro -->
    <div class="cd-secondary-nav">
      <a style="text-decoration: none" href="#0" class="cd-secondary-nav-trigger">Menu<span></span></a>
      <!-- button visible on small devices -->
      <nav>
        <ul>
          <li>
            <a style="text-decoration: none" href="#cd-placeholder-1">
              <b>选择设备</b>
              <span></span><!-- icon -->
            </a>
          </li>
          <li>
            <a style="text-decoration: none" href="#cd-placeholder-2">
              <b>选择环境</b>
              <span></span><!-- icon -->
            </a>
          </li>
          <li>
            <a style="text-decoration: none" href="#cd-placeholder-3">
              <b>选择脚本</b>
              <span></span><!-- icon -->
            </a>
          </li>
          <li>
            <a style="text-decoration: none" href="#cd-placeholder-4">
              <b>选择数据</b>
              <span></span><!-- icon -->
            </a>
          </li>
          <li>
            <a style="text-decoration: none" href="#cd-placeholder-5">
              <b>选择apk包</b>
              <span></span><!-- icon -->
            </a>
          </li>
        </ul>
      </nav>

      <div style="text-align: center;margin-top: 3px">
                <span
                    style="color: white;background-color: #101621;font-size: xx-small;padding: 10px;border-radius: 0 0 10px 10px">
                    【已选设备-{{
                    now_deviceName
                  }}】 【已选环境-{{ now_env }}】 【已选用例-{{ now_cases_count }}个】 【已选数据-{{
                    now_data_name
                  }}】 【安装方式-{{ now_apk_method }}】
                </span>
      </div>


    </div> <!-- .cd-secondary-nav -->
    <main class="cd-main-content">
      <section id="cd-placeholder-1" class="cd-section cd-container">
        <h2>1. 选择设备</h2>
        <Device @upd="upd"></Device>
      </section> <!-- #cd-placeholder-1 -->

      <section id="cd-placeholder-2" class="cd-section cd-container">
        <h2>2. 选择环境</h2>
        <Env @upe="upe"></Env>
      </section> <!-- #cd-placeholder-2 -->

      <section id="cd-placeholder-3" class="cd-section cd-container">
        <h2>3.选择脚本</h2>
        <Case @upc="upc"></Case>
      </section> <!-- #cd-placeholder-3 -->

      <section id="cd-placeholder-4" class="cd-section cd-container">
        <h2>4. 选择数据</h2>
        <Data @upda="upda"></Data>
      </section> <!-- #cd-placeholder-4 -->

      <section id="cd-placeholder-5" class="cd-section cd-container">
        <h2>5. 选择apk包</h2>
        <Apk @upa="upa"></Apk>
      </section> <!-- #cd-placeholder-5 -->
    </main> <!-- .cd-main-content -->
    <div class="card" style="box-shadow: 4px -4px 10px darkgray">
      <div class="card-body">
        <h4>平台最近30天的功能使用情况：</h4>
        <div id="myChart" style="width: 100%;height: 400px"></div>
      </div>
    </div>

    <!-- 模态框 -->
    <div class="modal fade" id="myModal_play">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">

          <!-- 模态框头部 -->
          <div class="modal-header">
            <h4 class="modal-title">请描述下这次任务：</h4>
          </div>

          <!-- 模态框内容 -->
          <div class="modal-body">
            <div class="input-group mb-3">
              <input id="task_des" type="text" class="form-control" placeholder="在此写描述">
              <button @click="play" class="btn btn-success" data-bs-dismiss="modal">启动任务</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Device from "../components/Device.vue";
import Task from "../components/Task.vue";
import Env from "../components/Env.vue";
import Case from "../components/Case.vue";
import Data from "../components/Data.vue";
import Apk from "../components/Apk.vue";
// vue文件中引入echarts工具
let echarts = require('echarts/lib/echarts')
require('echarts/lib/chart/line')
// 以下的组件按需引入
require('echarts/lib/component/tooltip')   // tooltip组件
require('echarts/lib/component/title')   //  title组件
require('echarts/lib/component/legend')  // legend组件
import {GridComponent} from 'echarts/components';
import axios from "axios";

echarts.use([GridComponent]);

export default {
  data() {
    return {
      task_if_value: false,
      now_deviceName: '',
      now_deviceId: '',
      now_env: '',
      env_script: '',
      now_cases_count: 0,
      now_case_ids: [],
      now_data_name: '',
      now_data_id: '',
      // option将要设置以下字段感觉就足够使用了
      option: {
        legend: {data: []},//展示的折线图标题
        xAxis: {
          type: 'category',   // 还有其他的type，可以去官网喵两眼哦
          data: [],   // x轴数据
          name: '日期',   // x轴名称
          // x轴名称样式
          nameTextStyle: {
            fontWeight: 400,//字体出席
            fontSize: 15,//字体大小
            color: 'green'//字体颜色
          },
          axisTick: {
            show: true,//是否显示刻度
            alignWithLabel: true,//对齐文字
            interval: '0',
            length: 5,//标度标尺的长度
            inside: false //刻度尺 标记 朝内 朝外
          },
          axisLabel: {
            interval: 0, //刻度显示间隔 0代表 全部显示 1代表这个 隔一个显示一个
            rotate: 0 //对刻度进行角度旋转 竖着显示
          }
        },//x轴的配置显示
        yAxis: {
          type: 'value',
          name: '使用次数',   // y轴名称
          // y轴名称样式
          nameTextStyle: {
            fontWeight: 400,
            fontSize: 15
          }
        },//y轴的配置显示
        label: {},
        tooltip: {trigger: 'item'},//点击折点 展示的样式
        series: []//y轴展示的数据
      }

    }
  },

  mounted: function () {
    axios('http://localhost:8000/get_tjs/').then(res => {
      console.log(res.data);
      // 填充数据
      this.option.legend.data = res.data.legend_data;
      this.option.xAxis.data = res.data.xAxis_data;
      this.option.series = res.data.series;

      let myChart = echarts.init(document.getElementById('myChart'));
      myChart.setOption(this.option)
    })
  },

  methods: {
    help_shown() {
      alert('有问题请联系xxx')
    },
    task_btn() {
      this.task_if_value = !this.task_if_value
    }
    ,
    upd(e) {
      this.now_deviceName = e.now_deviceName;
      this.now_deviceId = e.now_deviceId
    }
    ,
    upe(e) {
      this.now_env = e.now_env;
      this.env_script = e.env_script
    },

    upc(e) {
      this.now_cases_count = e.now_cases_count;
      this.now_case_ids = e.now_case_ids
    },

    upda(e) {
      this.now_data_name = e.now_data_name;
      this.now_data_id = e.now_data_id
    },

    play() {
      axios({
        method: 'post',
        url: 'http://localhost:8080/play',
        headers: {
          "Cotent-type": "application/x-ww=form-urlencoded"
        },
        data: {
          task_des: document.getElementById('').value,
          now_devicesId: this.now_deviceId,
          now_env: this.now_env,
          env_script: this.env_script,
          now_case_ids: this.now_case_ids,
          now_data_id: this.now_data_id,

        }
      }).then(res => {
        alert('任务已经开始，详情可在任务列表看板中查看和控制')
      })
    },

  },

  components: {
    Apk, Data, Case, Env, Task, Device
  },


}

</script>

<style>
h1 {
  border: 1px solid black;
  width: 600px;
  padding: 10px;
  border-radius: 50px;
  margin-left: -webkit-calc(50% - 250px);
}
</style>