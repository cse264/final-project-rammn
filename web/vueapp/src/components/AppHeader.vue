<template>
  <CHeader position="sticky" class="mb-4">
    <CContainer fluid>
      <CNavbarBrand href="#">
        <CImage :src="logo" height="50"/>
      </CNavbarBrand>
      <CHeaderNav class="d-none d-md-flex me-auto">
        <CNavItem v-show="loggedin">
          <CNavLink href="#/profile">Profile</CNavLink>
        </CNavItem>
        <CNavItem v-show="admin">
          <CNavLink href="#/dashboard">Dashboard</CNavLink>
        </CNavItem>
      </CHeaderNav>
      <CHeaderNav>
        <CNavItem>
          <CButton v-show="button" color="primary" shape="rounded-pill" @click="login">
            <CRow class="align-items-center">
              <div align="center">
                <strong>Login</strong>
              </div>
            </CRow>
          </CButton>
          <div v-show="loggedin" align="right">
            <CNavLink href="#/profile">Logged in as {{ username }}</CNavLink>
          </div>
        </CNavItem>
      </CHeaderNav>
    </CContainer>
    <CHeaderDivider />
    <CContainer fluid>
      <AppBreadcrumb />
    </CContainer>
  </CHeader>
</template>

<script>
import AppBreadcrumb from './AppBreadcrumb'
import logo from '@/assets/images/logo.png'
export default {
  name: 'AppHeader',
  components: {
    AppBreadcrumb,
  },
  setup() {
    return {
      logo,
    }
  },
  data() {
    var loggedin = false;
    var button = true;
    var admin = true;
    var username = "u/lehigh-jac222";
    return {
      loggedin,
      button,
      username,
      admin,
    }
  },
  methods: {
    async login() {
      console.log("logged in");
      this.loggedin = true;
      this.button = false;
      var link = await fetch('/auth').then(response => response.json()).then(data => data);
      window.location.href = link;
    },
  }
}
</script>
