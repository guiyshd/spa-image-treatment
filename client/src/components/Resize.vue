<template>
  <div>
    <div v-if="progressInfos">
      <div class="mb-2"
        v-for="(progressInfo, index) in progressInfos"
        :key="index"
      >
        <span>{{progressInfo.fileName}}</span>
        <div class="progress">
          <div class="progress-bar progress-bar-info"
            role="progressbar"
            :aria-valuenow="progressInfo.percentage"
            aria-valuemin="0"
            aria-valuemax="100"
            :style="{ width: progressInfo.percentage + '%' }"
          >
            {{progressInfo.percentage}}%
          </div>
        </div>
      </div>
    </div>

    <label class="btn btn-default">
      <input type="file" accept="image/*" multiple @change="selectFile" />
    </label>

    <button class="btn btn-success"
      :disabled="!selectedFiles"
      @click="addImage"
    >
      Upload
    </button>

    <div v-if="message" class="alert alert-light" role="alert">
      <ul>
        <li v-for="(ms, i) in message.split('\n')" :key="i">
          {{ ms }}
        </li>
      </ul>
    </div>

    <div class="card">
      <div class="card-header">List of Files</div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item"
          v-for="(file, index) in fileInfos"
          :key="index"
        >
          <p><a :href="file.url">{{ file.name }}</a></p>
          <img :src="file.url" :alt="file.name" height="80px">
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios"

const path = 'http://localhost:5000/files'

export default {
  name: "resize-images",
  data() {
    return {
      selectedFiles: undefined,
      progressInfos: [],
      message: "",

      fileInfos: [],
    };
  },
  methods: {
    selectFile() {
      this.progressInfos = []
      this.selectedFiles = event.target.files
    },
    addImage(){
      var formData = new FormData()
      for (let i = 0; i < this.selectedFiles.length; i++) {
        this.progressInfos[i] = { percentage: 0, fileName: this.selectedFiles[i].name };
        formData.append('uploads', this.selectedFiles[i])
        axios.post(path, formData)
          .then((response) => {
            this.progressInfos[i].percentage = Math.round(100)
            let prevMessage = this.message ? this.message + "\n" : "";
            this.message = prevMessage + response.data.message;

            return axios.get(path)
          })
          .then((files) => {
            this.fileInfos = files.data;
          })
          .catch(() => {
            this.progressInfos[i].percentage = 0;
            this.message = "Could not upload the file:" + this.selectedFiles[i].name;
          });
      }
    },
    mounted() {
        axios.get(path)
          .then((response) => {
            this.fileInfos = response.data;
        });
    }
  }
};
</script>
