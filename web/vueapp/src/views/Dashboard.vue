<template>
  <div>
    <CRow>
      <CCol :xs="4">
        <CWidgetStatsF color="primary" :padding="false" title="Users" value="1234">
          <template #icon>
            <CIcon icon="cil-user" size="xl" />
          </template>
        </CWidgetStatsF>
      </CCol>
      <CCol :xs="4">
        <CWidgetStatsF color="secondary" :padding="false" title="Searches" value="1234">
          <template #icon>
            <CIcon icon="cil-magnifying-glass" size="xl" />
          </template>
        </CWidgetStatsF>
      </CCol>
      <CCol :xs="4">
        <CWidgetStatsF color="info" :padding="false" title="idk" value="1234">
          <template #icon>
            <CIcon icon="cil-moon" size="xl" />
          </template>
        </CWidgetStatsF>
      </CCol>
    </CRow>
    <br />
    <CRow>
      <CCol :md="6">
        <CCard class="mb-4">
          <CCardHeader>Recent Users</CCardHeader>
          <CCardBody>
            <CTable align="middle" class="mb-0 border" hover responsive>
              <CTableHead color="light">
                <CTableRow>
                  <CTableHeaderCell>Name</CTableHeaderCell>
                  <CTableHeaderCell>Username</CTableHeaderCell>
                  <CTableHeaderCell>Last Access</CTableHeaderCell>
                </CTableRow>
              </CTableHead>
              <CTableBody>
                <CTableRow v-for="item in recentUsers" :key="item.name">
                  <CTableDataCell>
                    <div>{{ item.user }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item.search }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item.time }}</div>
                  </CTableDataCell>
                </CTableRow>
                <CTableRow> </CTableRow>
              </CTableBody>
            </CTable>
          </CCardBody>
        </CCard>
      </CCol>
      <CCol :md="6">
        <CCard class="mb-4">
          <CCardHeader>Most Searches</CCardHeader>
          <CCardBody>
            <CTable align="middle" class="mb-0 border" hover responsive>
              <CTableHead color="light">
                <CTableRow>
                  <CTableHeaderCell>User</CTableHeaderCell>
                  <CTableHeaderCell>Search</CTableHeaderCell>
                  <CTableHeaderCell>Time</CTableHeaderCell>
                </CTableRow>
              </CTableHead>
              <CTableBody>
                <CTableRow v-for="item in topUsers" :key="item.name">
                  <CTableDataCell>
                    <div>{{ item.user }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item.search }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item.time }}</div>
                  </CTableDataCell>
                </CTableRow>
                <CTableRow> </CTableRow>
              </CTableBody>
            </CTable>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
    <CRow>
      <CCol :md="12">
        <CCard class="mb-4">
          <CCardHeader>Recent Searches</CCardHeader>
          <CCardBody>
            <CTable align="middle" class="mb-0 border" hover responsive>
              <CTableHead color="light">
                <CTableRow>
                  <CTableHeaderCell>User</CTableHeaderCell>
                  <CTableHeaderCell>Search</CTableHeaderCell>
                  <CTableHeaderCell>Time</CTableHeaderCell>
                </CTableRow>
              </CTableHead>
              <CTableBody>
                <CTableRow v-for="item in recentSearches" :key="item.name">
                  <CTableDataCell>
                    <div>{{ item.user }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item.search }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item.time }}</div>
                  </CTableDataCell>
                </CTableRow>
                <CTableRow> </CTableRow>
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
  name: 'Dashboard',
  setup() {
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

    const recentUsers = [
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

    const topUsers = [
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
      recentSearches,
      recentUsers,
      topUsers,
    }
  },
}
</script>
