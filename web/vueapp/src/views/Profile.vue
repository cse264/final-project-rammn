<template>
  <div>
    <CRow>
      <CCol :md="6">
        <CCard class="mb-4">
          <CCardHeader>Interests</CCardHeader>
          <CCardBody>
            <CTable align="middle" class="mb-0 border" hover responsive>
              <CTableHead color="light">
                <CTableRow>
                  <CTableHeaderCell>Interest</CTableHeaderCell>
                  <CTableHeaderCell>Details</CTableHeaderCell>
                </CTableRow>
              </CTableHead>
              <CTableBody>
                <CTableRow v-for="item in interests" :key="item.name">
                  <CTableDataCell>
                    <div>{{ item[0] }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item[1] }}</div>
                  </CTableDataCell>
                </CTableRow>
              </CTableBody>
            </CTable>
          </CCardBody>
        </CCard>
      </CCol>
      <CCol :xs="6">
        <CCard>
          <CRow>
            <CCol :md="4">
              <CCardImage :src="profile.pic"/>
            </CCol>
            <CCol :md="8">
              <CCardBody>
                <CCardTitle>{{ profile.display_name }}</CCardTitle>
                <CCardText>Username: {{ profile.username }}</CCardText>
                <CCardText>Karma: {{ profile.karma }}</CCardText>
                <CCardText>Account Age: {{ profile.account_age }}</CCardText>
                <CCardText>Bio: {{ profile.bio }}</CCardText>
              </CCardBody>
            </CCol>
          </CRow>
          <CRow>
            <CCol :md="12">
              <CCardFooter>
                <a :href="profile.link" target="_blank">View Reddit Profile</a>
              </CCardFooter>
            </CCol>
          </CRow>
        </CCard>
      </CCol>
    </CRow>
    <br/>
    <CRow>
      <CCol :md="12">
        <CCard class="mb-4">
          <CCardHeader>Recent Searches</CCardHeader>
          <CCardBody>
            <CTable align="middle" class="mb-0 border" hover responsive>
              <CTableHead color="light">
                <CTableRow>
                  <CTableHeaderCell>Search</CTableHeaderCell>
                  <CTableHeaderCell>Time</CTableHeaderCell>
                </CTableRow>
              </CTableHead>
              <CTableBody>
                <CTableRow v-for="item in recentSearches" :key="item.name">
                  <CTableDataCell>
                    <div>{{ item[1] }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item[2] }}</div>
                  </CTableDataCell>
                </CTableRow>
              </CTableBody>
            </CTable>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  </div>
</template>

<script>
export default {
  name: 'Profile',
  data() {
    return {
      interests: [],
      recentSearches: [],
      profile: {},
      timer: "",
    }
  },
  created() {
    this.fetchData();
    this.timer = setInterval(this.fetchData, 60000);
  },
  methods: {
    async fetchData() {
      this.profile = await fetch("/reddit/profile").then(response => response.json()).then(data => data);
      this.interests = await fetch("/reddit/interests").then(response => response.json()).then(data => data);
      this.recentSearches = await fetch("/users/history/" + this.profile.id).then(response => response.json()).then(data => data);
    },
    cancelAutoUpdate() {
      clearInterval(this.timer);
    },
  },
  beforeUnmount() {
    this.cancelAutoUpdate();
  },
}
</script>
