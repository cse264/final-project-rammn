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
                    <div>{{ item.user }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item.search }}</div>
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
              <CCardImage :src="photo"/>
            </CCol>
            <CCol :md="8">
              <CCardBody>
                <CCardTitle>{{ username }}</CCardTitle>
                <CCardText>User: </CCardText>
                <CCardText>Name: </CCardText>
                <CCardText>Account Age: </CCardText>
                <CCardText>Etc: </CCardText>
              </CCardBody>
            </CCol>
          </CRow>
          <CRow>
            <CCol :md="12">
              <CCardFooter>
                <a :href="profile" target="_blank">View Reddit Profile</a>
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
                    <div>{{ item.search }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item.time }}</div>
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
  setup() {
    const profile = "https://reddit.com";
    const photo = "asdf";
    const username = "test123";
    const interests = [
      {
        user: 'Yiorgos Avraamu',
        search: 'redditpost link',
        activity: '1/1/2022',
      },
      {
        user: 'Yiorgos Avraamu',
        search: 'redditpost link',
        activity: '1/1/2022',
      },
      {
        user: 'Yiorgos Avraamu',
        search: 'redditpost link',
        activity: '1/1/2022',
      },
      {
        user: 'Yiorgos Avraamu',
        search: 'redditpost link',
        activity: '1/1/2022',
      },
      {
        user: 'Yiorgos Avraamu',
        search: 'redditpost link',
        activity: '1/1/2022',
      },
      {
        user: 'Yiorgos Avraamu',
        search: 'redditpost link',
        activity: '1/1/2022',
      },
      {
        user: 'Yiorgos Avraamu',
        search: 'redditpost link',
        activity: '1/1/2022',
      },
    ]

    const recentSearches = [
      {
        user: 'Yiorgos Avraamu',
        search: 'redditpost link',
        activity: '1/1/2022',
      },
      {
        user: 'Yiorgos Avraamu',
        search: 'redditpost link',
        activity: '1/1/2022',
      },
      {
        user: 'Yiorgos Avraamu',
        search: 'redditpost link',
        activity: '1/1/2022',
      },
      {
        user: 'Yiorgos Avraamu',
        search: 'redditpost link',
        activity: '1/1/2022',
      },
      {
        user: 'Yiorgos Avraamu',
        search: 'redditpost link',
        activity: '1/1/2022',
      },
      {
        user: 'Yiorgos Avraamu',
        search: 'redditpost link',
        activity: '1/1/2022',
      },
      {
        user: 'Yiorgos Avraamu',
        search: 'redditpost link',
        activity: '1/1/2022',
      },
    ]

    return {
      interests,
      recentSearches,
      profile,
      photo,
      username,
    }
  },
}
</script>
