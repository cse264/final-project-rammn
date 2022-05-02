<template>
  <CHeader position="sticky" class="mb-4">
    <CContainer fluid>
      <CNavbarBrand href="#">
        <CImage :src="logo" height="50"/>
      </CNavbarBrand>
      <CHeaderNav class="d-none d-md-flex me-auto">
        <CNavItem>
          <CNavLink href="#/search">Search</CNavLink>
        </CNavItem>
        <CNavItem>
          <CNavLink href="#/login">Login</CNavLink>
        </CNavItem>
        <CNavItem>
          <CNavLink href="#/profile">Profile</CNavLink>
        </CNavItem>
        <CNavItem>
          <CNavLink href="#/dashboard">Dashboard</CNavLink>
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
}
</script>
