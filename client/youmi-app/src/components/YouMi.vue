<template>
  <div>
    <canvas ref="video" width="1280" height="720" style="border: 1px solid black;"></canvas>
  </div>
</template>

<script>
import io from "socket.io-client";
export default {
  name: "YouMi",
  data() {
    return {
      socket: {},
      ctx: {},
      tempCtx: {},
      canvas: {},
      tempCanvas: {}
    }
  },
  created() {
    this.socket = io("http://127.0.0.1:4242");

  },
  mounted() {
    this.canvas = this.$refs.video;
    this.tempCanvas = this.$refs.video;
    this.ctx = this.$refs.video.getContext("2d");
    this.tempCtx = this.$refs.video.getContext("2d");
    this.socket.on("video", (data) => {
      // 获取视频帧 将base64转为图片img
      let data_json = JSON.parse(data); 
      let img_date_url = data_json['img_url']; 
      //新建img实例
      let img = new Image(); 
      //设置img的链接为base64格式
      img.src = img_date_url; 
      //等待图片加载完成后，绘制图片到缓存区（因绘制时间较长，使用缓存区防止闪屏）
      img.onload = () => {
        this.tempCtx.drawImage(img, 0, 0);
      }
      // 将缓存 canvas 复制到旧的 canvas（复制速度远快于绘制速度，不会闪屏）
      this.ctx.drawImage(this.tempCanvas, 0, 0); 
      //向后端发送请求，准备获取下一个视频帧
      this.socket.emit('video', '1');

    });
    this.socket.emit('video', '1');
  }
}
</script>

<style scoped>
</style>