<script>
  const skills = [
    { name: "JavaScript", icon: "🟨" },
    { name: "Svelte", icon: "🟠" },
    { name: "TailwindCSS", icon: "🔵" },
    { name: "FastAPI", icon: "🟢" },
    { name: "Django", icon: "⚫" }
  ];

  const experiences = [
    { year: "2023 - Presente", role: "Sviluppatore Full Stack", company: "Freelance" },
    { year: "2021 - 2023", role: "Web Developer", company: "Azienda XYZ" },
    { year: "2019 - 2021", role: "Junior Developer", company: "Startup ABC" }
  ];
</script>

<section class="max-w-4xl mx-auto my-12 px-6 text-center">
  <h1 class="text-4xl font-bold text-gray-800">Chi Sono</h1>
  <p class="mt-4 text-gray-600">
    Sono uno sviluppatore full-stack con esperienza nella creazione di applicazioni web moderne e scalabili.
    Amo scrivere codice pulito e creare esperienze utente coinvolgenti.
  </p>
</section>

<section class="max-w-4xl mx-auto my-12 px-6">
  <h2 class="text-3xl font-bold text-gray-800 text-center">Competenze</h2>
  <div class="flex flex-wrap justify-center gap-4 mt-4">
    {#each skills as skill}
      <span class="bg-gray-200 text-gray-800 px-4 py-2 rounded-lg shadow flex items-center">
        {skill.icon} {skill.name}
      </span>
    {/each}
  </div>
</section>

<section class="max-w-4xl mx-auto my-12 px-6">
  <h2 class="text-3xl font-bold text-gray-800 text-center">Esperienza Lavorativa</h2>
  <div class="mt-6 space-y-4">
    {#each experiences as exp}
      <div class="p-4 bg-white shadow rounded-lg border border-gray-200">
        <h3 class="text-xl font-semibold">{exp.role} - {exp.company}</h3>
        <p class="text-gray-600">{exp.year}</p>
      </div>
    {/each}
  </div>
</section>