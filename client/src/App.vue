<template>
  <div id="app">
    <div class="container" style="width:600px">
      <div style="margin: 20px">
        <h4>Resize Images</h4>
      </div>

      <upload-images></upload-images>
    </div>
  </div>
</template>

<script>
import UploadImages from "./components/Resize";

export default {
  name: "App",
  components: {
    UploadImages
  }
};
</script>