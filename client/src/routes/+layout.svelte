<script>
  import "../app.css";
  import NavBar from "../components/NavBar.svelte";
  import { page } from "$app/stores";

  let items = [
    { label: "Spring - 25", icon: "🌳", href: "/" },
    { label: "Winter 24-25", icon: "❄️", href: "/interim24-25" },
    { label: "Fall - 24", icon: "🍂", href: "/fall24" },
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
