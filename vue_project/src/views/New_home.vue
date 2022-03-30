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
        <a style="text-decoration: none" href="#" class="cd-btn">开始执行</a>
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
    </div> <!-- .cd-secondary-nav -->
    <main class="cd-main-content">
      <section id="cd-placeholder-1" class="cd-section cd-container">
        <h2>1.选择设备</h2>
        <Device></Device>

      </section> <!-- #cd-placeholder-1 -->

      <section id="cd-placeholder-2" class="cd-section cd-container">
        <h2>2.选择环境</h2>
        <Env></Env>

      </section> <!-- #cd-placeholder-2 -->

      <section id="cd-placeholder-3" class="cd-section cd-container">
        <h2>3.选择脚本</h2>
        <Case></Case>

      </section> <!-- #cd-placeholder-3 -->

      <section id="cd-placeholder-4" class="cd-section cd-container">
        <h2>4.选择数据</h2>
        <Date></Date>

      </section> <!-- #cd-placeholder-4 -->

      <section id="cd-placeholder-5" class="cd-section cd-container">
        <h2>5.选择apk包</h2>
        <Apk></Apk>

      </section> <!-- #cd-placeholder-5 -->
    </main> <!-- .cd-main-content -->


  </div>
</template>

<script>
import Device from "../components/Device.vue";
import Task from "../components/Task.vue";
import Env from "../components/Env";
import Case from "../components/Case";
import Date from "../components/Date";
import Apk from "../components/Apk";


export default {
  data() {
    return {
      task_if_value: false
    }
  },

  methods: {
    help_shown() {
      alert('有问题请联系xxx')
    },
    task_btn() {
      this.task_if_value = !this.task_if_value
    }

  },
  components: {Apk, Date, Case, Env, Task, Device},

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