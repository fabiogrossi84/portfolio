// ✅ Modulo TypeScript per la navigazione
import { writable } from "svelte/store";

export const currentPage = writable("/");

export function navigateTo(page: string): void {
  window.history.pushState({}, "", page);
  currentPage.set(page);
}

// ✅ Permetti la navigazione con i pulsanti del browser
window.onpopstate = () => {
  currentPage.set(window.location.pathname);
};
