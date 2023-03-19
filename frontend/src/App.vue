<script>

</script>

<template>
  <header class="bg-light mb-4">
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container">
        <a class="navbar-brand" href="#">SpaceFermers</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <RouterLink to="/" class="nav-link">Полётный план</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink to="/consumption" class="nav-link">Расход</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>

  <div class="container">
    <RouterView />
  </div>
</template>

<style></style>
