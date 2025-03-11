<script>
    let name = "";
    let email = "";
    let message = "";
  
    function submitForm() {
      if (!name || !email || !message) {
        alert("Compila tutti i campi prima di inviare.");
        return;
      }
  
      console.log("Nome:", name);
      console.log("Email:", email);
      console.log("Messaggio:", message);
  
      // Simulazione di invio (da sostituire con API backend)
      alert("Messaggio inviato con successo!");
  
      // Resettare il form dopo l'invio
      name = "";
      email = "";
      message = "";
    }
  </script>
  
  <h1 class="text-3xl font-bold text-center mt-6 text-gray-800">Contattami</h1>
  
  <form class="max-w-lg mx-auto bg-white p-6 rounded-lg shadow mt-4"
    on:submit|preventDefault={submitForm}>
  
    <!-- Nome -->
    <label for="name" class="block mb-2 font-semibold">Nome</label>
    <input id="name" type="text" bind:value={name} 
      class="w-full p-2 border border-gray-300 rounded mb-4 focus:ring-2 focus:ring-blue-400"
      placeholder="Il tuo nome" required />
  
    <!-- Email -->
    <label for="email" class="block mb-2 font-semibold">Email</label>
    <input id="email" type="email" bind:value={email} 
      class="w-full p-2 border border-gray-300 rounded mb-4 focus:ring-2 focus:ring-blue-400"
      placeholder="La tua email" required />
  
    <!-- Messaggio -->
    <label for="message" class="block mb-2 font-semibold">Messaggio</label>
    <textarea id="message" bind:value={message} 
      class="w-full p-2 border border-gray-300 rounded mb-4 h-32 focus:ring-2 focus:ring-blue-400"
      placeholder="Scrivi il tuo messaggio" required></textarea>
  
    <!-- Pulsante di invio -->
    <button type="submit"
      class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 w-full transition duration-200">
      Invia
    </button>
  </form>
  
  