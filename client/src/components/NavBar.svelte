<script>
  export let items = [];
  export let activeItem = "";
  export let onNavigate; // Optional prop for a callback function when navigation occurs
  import { goto } from "$app/navigation";
</script>

<br /><br />
<nav
  class="fixed inset-x-0 bottom-0 bg-slate-100 dark:bg-slate-800 border-t border-slate-300 dark:border-slate-700"
>
  <div class="flex justify-around">
    {#each items as item}
      <button
        on:click={() => {
          activeItem = item;
        }}
        class="text-slate-600 dark:text-slate-400 hover:bg-slate-300 dark:hover:bg-slate-700 focus:outline-none focus:bg-slate-300 dark:focus:bg-slate-700 p-1 w-full transition-colors duration-150 ease-in-out"
        class:class-active={item === activeItem}
        on:click|preventDefault={() => {
          goto(item.href);
        }}
      >
        {#if item.icon}
          <span class="icon block text-lg">{item.icon}</span>
        {/if}
        <span class="label text-xs">{item.label}</span>
      </button>
    {/each}
  </div>
</nav>

<style>
  .class-active {
    color: #0f172a; /* Active item color - using a hard-coded slate color here for the example */
    background-color: #e2e8f0; /* Light mode active background color */
  }

  /* You can also add dark mode styles directly with CSS if needed */
  @media (prefers-color-scheme: dark) {
    .class-active {
      color: #94a3b8; /* Dark mode active color */
      background-color: #0f172a; /* Dark mode active background color */
    }
  }
</style>
