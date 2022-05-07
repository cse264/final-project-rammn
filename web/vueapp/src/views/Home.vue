<template>
  <div>
    <CRow class="justify-content-center">
      <CCol :xs="8">
        <div class="d-grid gap-2">
          <CButton type="submit" color="primary" shape="rounded-pill" size="lg" @click="search">
            <CRow class="align-items-center">
              <CCol xs="3">
                <div align="left">
                  <CImage :src="die" height="100"/>
                </div>
              </CCol>
              <CCol xs="6">
                <div align="center">
                  <strong>Roll the dice to find something fun!</strong>
                </div>
              </CCol>
              <CCol xs="3">
                <div align="right">
                  <CImage :src="die" height="100"/>
                </div>
              </CCol>
            </CRow>
          </CButton>
        </div>
      </CCol>
    </CRow>
    <br/>
    <br/>
    <CRow :xs="{ cols: 1, gutter: 4 }" :md="{ cols: 3}">
      <CCol xs v-for="item in results" :key="item.name">
        <CCard class="h-100">
          <CCardImage orientation="top" :src="item.image"/>
          <CCardBody>
            <CCardTitle>{{ item.title }}</CCardTitle>
            <CCardText>{{ item.description }}</CCardText>
          </CCardBody>
          <CCardFooter>
            <a :href="item.link" target="_blank">View Reddit Post</a>
          </CCardFooter>
        </CCard>
      </CCol>
    </CRow>
  </div>
</template>

<script>
import die from '@/assets/images/die-white.png'
export default {
  name: 'Home',
  setup() {
    return {
      die,
    }
  },
  data() {
    var results = []
    var searches = 1
    return {
      results,
      searches,
    }
  },
  methods: {
    async search() {
      this.results = await fetch("/reddit/" + this.searches).then(response => response.json()).then(data => data);
      this.searches = this.searches + 1;
    },
  },
}
</script>
