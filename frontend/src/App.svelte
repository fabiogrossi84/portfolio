<script lang="ts">
  import { onMount } from "svelte";
  import Home from "./routes/Home.svelte";
  import Projects from "./routes/Projects.svelte";
  import About from "./routes/About.svelte";
  import Contact from "./routes/Contact.svelte";
  import { navigateTo, currentPage } from "./router"; // ✅ Importiamo router.ts

// ✅ Usiamo le Rune per gestire il routing
//@state currentPage = "/";

//function navigateTo(page) {
//  window.history.pushState({}, "", page);
//  currentPage = page;
// }



  onMount(() => {
    currentPage.set(window.location.pathname);
  });
</script>

<!-- Navbar con la navigazione tra le pagine -->
<nav class="p-4 bg-gray-900 text-white flex gap-4">
  <button on:click={() => navigateTo("/")} class="hover:text-gray-300">Home</button>
  <button on:click={() => navigateTo("/Projects")} class="hover:text-gray-300">Progetti</button>
  <button on:click={() => navigateTo("/About")} class="hover:text-gray-300">Chi Sono</button>
  <button on:click={() => navigateTo("/Contact")} class="hover:text-gray-300">Contatti</button>
</nav>

<!-- Gestione del contenuto delle pagine -->
{#if $currentPage === "/"}
  <Home />
{:else if $currentPage === "/Projects"}
  <Projects />
{:else if $currentPage === "/About"}
  <About />
{:else if $currentPage === "/Contact"}
  <Contact />
{:else}
  <h1 class="text-center text-red-500">Pagina non trovata</h1>
{/if}
