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
      <div class="card-header">Imagens</div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item"
            v-for="(file, index) in fileInfos"
            :key="index"
          >
          <p><a :href="file.url">{{ index }}</a></p>
          <img :src="'data:image/jpeg;base64,'+file" :alt="file" height="200px">
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
        this.progressInfos[i].percentage = Math.round(100)
      }
      axios.post(path, formData)
        .then((response) => {
          let prevMessage = this.message ? this.message + "\n" : "";
          this.message = prevMessage + response.data.message;

          return axios.get(path)
        })
        .then((files) => {
          this.fileInfos = files.data
          console.log(this.fileInfos)
        })
        .catch((error) => {
          console.log(error)
        });
    },
    mounted() {
        axios.get(path)
          .then((response) => {
            this.fileInfos = response.data
        });
    }
  }
};
</script>
