<script>
  import "../app.css";
  import NavBar from "../components/NavBar.svelte";
  import { page } from "$app/stores";

  let items = [
    { label: "Summer 2 - 24", icon: "☀️", href: "/summer2-24" },
    { label: "Summer 1 - 24", icon: "☀️", href: "/summer1-24" },
    { label: "Spring - 24", icon: "🌳", href: "/" },
    { label: "Fall - 23", icon: "🍂", href: "/fall23" },
    { label: "About", icon: "👋", href: "/about" },
  ];
  let activeItem = items[0]; // Default to the first item as active

  // try to assign the active item from the URL and the items list
  const activeItemFromUrl = items.find((item) => item.href === $page.route.id);
  if (activeItemFromUrl) {
    activeItem = activeItemFromUrl;
  }
</script>

<slot />
<NavBar {items} bind:activeItem />
