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
                    <div>{{ item.subreddit }}</div>
                  </CTableDataCell>
                  <CTableDataCell>
                    <div>{{ item.description }}</div>
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
                <CCardText>Username: u/lehigh-jac222</CCardText>
                <CCardText>Karma: 1</CCardText>
                <CCardText>Account Age: 11h</CCardText>
                <CCardText>Bio: test123</CCardText>
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
    const profile = "https://www.reddit.com/user/lehigh-jac222";
    const photo = "https://i.redd.it/snoovatar/avatars/b2c68f85-e46a-4fbc-b24f-f8cc4c3dff53.png";
    const username = "jac222";
    const interests = [
      {
        subreddit: 'r/News',
        description: 'The place for news articles about current events in the United States and the rest of the world. Discuss it all here.',
      },
      {
        subreddit: 'r/Pics',
        description: 'A place for pictures and photographs.',
      },
      {
        subreddit: 'r/Politics',
        description: '/r/Politics is for news and discussion about U.S. politics.',
      },
    ]

    const recentSearches = [
      {
        search: 'https://i.redd.it/zaqxjbuvwdx81.jpg',
        time: '2022-05-04 12:51:07',
      },
      {
        search: 'https://i.redd.it/0i9mv63c7la31.jpg',
        time: '2022-05-04 12:51:07',
      },
      {
        search: 'https://www.reddit.com/r/AskReddit/comments/uhze53/whats_stopping_you_from_having_sex/',
        time: '2022-05-04 12:51:07',
      },
      {
        search: 'https://i.redd.it/gzvw9bb7psw81.jpg',
        time: '2022-05-04 12:51:07',
      },
      {
        search: 'https://www.reddit.com/live/18hnzysb1elcs',
        time: '2022-05-04 12:51:07',
      },
      {
        search: 'https://v.redd.it/l0e20b6ktdx81',
        time: '2022-05-04 12:51:07',
      },
      {
        search: 'https://www.reddit.com/gallery/ui51zq',
        time: '2022-05-04 12:39:23',
      },
      {
        search: 'https://v.redd.it/s02clyst7fx81',
        time: '2022-05-04 12:39:23',
      },
      {
        search: 'https://www.reddit.com/r/AskReddit/comments/ui2a0b/what_is_your_goto_small_talk_topic_with_strangers/',
        time: '2022-05-04 12:39:23',
      },
      {
        search: 'https://itsgoingdown.org/anarchist-and-autonomous-formations-hit-the-streets-of-mexico-city-on-may-day/',
        time: '2022-05-04 12:39:23',
      },
    ]
    // fetch('/users/history').then(response => response.json()).then(data => data);
    // console.log(recentSearches);

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
