<script>
  import { navigateTo } from "../router";  // ✅ Importazione da router.ts
</script>

  
  <!-- Hero Section -->
  <section class="bg-gray-900 text-white text-center py-20">
    <h1 class="text-4xl font-bold">Benvenuto nel mio Portfolio</h1>
    <p class="text-lg mt-2">Sviluppatore Web | Full Stack Developer | Appassionato di Tecnologia</p>
    <button on:click={() => navigateTo("/Projects")} 
      class="mt-6 bg-blue-500 hover:bg-blue-600 text-white font-bold py-3 px-6 rounded-lg shadow-lg transition">
      Guarda i miei progetti
    </button>
  </section>
  
  <!-- Sezione Chi Sono -->
  <section class="max-w-4xl mx-auto my-12 text-center px-6">
    <h2 class="text-3xl font-bold text-gray-800">Chi Sono</h2>
    <p class="mt-4 text-gray-600">
      Sono uno sviluppatore full-stack con esperienza nella creazione di applicazioni web moderne e scalabili. 
      Amo scrivere codice pulito e creare esperienze utente coinvolgenti.
    </p>
    <button on:click={() => navigateTo("/About")} 
      class="mt-6 bg-gray-700 hover:bg-gray-800 text-white font-bold py-2 px-6 rounded-lg shadow-lg transition">
      Scopri di più
    </button>
  </section>
  
  <!-- Sezione Progetti Recenti -->
  <section class="bg-gray-100 py-12">
    <div class="max-w-5xl mx-auto text-center">
      <h2 class="text-3xl font-bold text-gray-800">Progetti Recenti</h2>
      <p class="text-gray-600 mt-2">Ecco alcuni degli ultimi lavori realizzati.</p>
  
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-6 px-6">
        <!-- Progetto 1 -->
        <div class="bg-white p-4 rounded-lg shadow-md">
          <h3 class="text-xl font-semibold">Portfolio Web</h3>
          <p class="text-gray-600">Un sito personale per mostrare i miei lavori.</p>
          <button on:click={() => navigateTo("/Projects")}
            class="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
            Vedi Progetti
          </button>
        </div>
  
        <!-- Progetto 2 -->
        <div class="bg-white p-4 rounded-lg shadow-md">
          <h3 class="text-xl font-semibold">E-commerce</h3>
          <p class="text-gray-600">Un negozio online per vendita di prodotti digitali.</p>
          <button on:click={() => navigateTo("/Projects")}
            class="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
            Vedi Progetti
          </button>
        </div>
      </div>
    </div>
  </section>
  
  <!-- Sezione Contatti e Social -->
  <section class="text-center py-12">
    <h2 class="text-3xl font-bold text-gray-800">Contattami</h2>
    <p class="text-gray-600 mt-2">Seguimi sui social o inviami un messaggio!</p>
    
    <div class="flex justify-center gap-6 mt-6">
      <a href="https://github.com/" target="_blank" class="text-gray-600 hover:text-gray-800 text-2xl">
        🔗 GitHub
      </a>
      <a href="https://linkedin.com/" target="_blank" class="text-gray-600 hover:text-gray-800 text-2xl">
        🔗 LinkedIn
      </a>
      <a href="mailto:example@email.com" class="text-gray-600 hover:text-gray-800 text-2xl">
        ✉️ Email
      </a>
    </div>
  
    <button on:click={() => navigateTo("/Contact")}
      class="mt-6 bg-gray-700 hover:bg-gray-800 text-white font-bold py-2 px-6 rounded-lg shadow-lg transition">
      Scrivimi
    </button>
  </section>
  
