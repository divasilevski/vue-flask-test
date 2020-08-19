<template lang="pug">
.about
  h1 Response
    p {{ response }}
  h1 Отправка файла
    div
      input#file(type="file", ref="file", v-on:change="handleFileUpload()")
      button(v-on:click="submitFile()") Submit
</template>

<script>
export default {
  data: () => ({
    response: "",
    file: "",
  }),
  mounted() {
    const url = "http://127.0.0.1:5000/ping";
    this.$http.get(url).then((response) => {
      this.response = response.data;
    });
  },
  methods: {
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    },
    submitFile() {
      let formData = new FormData();
      formData.append("file", this.file);
      const url = "http://127.0.0.1:5000/pong"
      this.$http
        .post(url, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then( response => {
          this.response = response.data;
        })
        .catch(function () {
          console.log("FAILURE!!");
        });
    },
  },
};
</script>

