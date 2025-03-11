<script>
  let projects = [
    { title: "Portfolio Web", description: "Il mio sito personale", link: "#" },
    { title: "E-commerce", description: "Negozio online", link: "#" },
    { title: "Dashboard Admin", description: "Gestione utenti e statistiche", link: "#" }
  ];
</script>

<h1 class="text-4xl font-bold text-center mt-6 text-gray-800">Progetti</h1>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-6 px-6">
  {#each projects as project}
    <div class="bg-white p-4 rounded-lg shadow-lg border border-gray-200">
      <h2 class="text-xl font-semibold">{project.title}</h2>
      <p class="text-gray-700">{project.description}</p>
      <a href={project.link} class="text-blue-500 hover:underline">Dettagli</a>
    </div>
  {/each}
</div>