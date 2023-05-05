<title>ClassBrowser</title>
<script>
  import { text } from 'svelte/internal';
  import { onMount } from 'svelte';
  export let data;

  let isMobile = false;
  let rawClasses = data.classes;

  onMount(() => {
    isMobile = window.innerWidth < 640;

    // isMobile = true;//force sorting duplicates and displaying less info


    if(isMobile){
  rawClasses = rawClasses.filter(function (el, index, self) {
    return index === self.findIndex((t) => (
      t[0] === el[0] && t[1] === el[1]
    ))
  })
    filter();
}
  });



//filter out class where [0] length is less than 2
    rawClasses = rawClasses.filter(function (el) {
      return el[0].length > 1;
    })
  

    
    let search = "";

    let darkMode = false;







    function toggleDarkMode() {
      darkMode = !darkMode;
  const html = document.querySelector('html');
  html.classList.toggle('dark');
}




    let v = false;
    let w = false;
    let s = false;
    let h = false
    let gm1 = false;
    let gm2 = false;
    let l = false;
    let ns = false;
    let q = false;
    let gm = false;

    let classes;
    let numClasses;

    let minCCS = 0;

    let numRaw= rawClasses.length;

    function filterCCS(){



      classes=rawClasses;

    if(v){
      //filter out classes that don't have [5] == 1
      classes = classes.filter(function (el) {
        return el[6] == 1;
      })
    }

    if(w){
      //filter out classes that don't have [6] == 1
      classes = classes.filter(function (el) {
        return el[7] == 1;
      })
    }

    if(s){
      //filter out classes that don't have [7] == 1
      classes = classes.filter(function (el) {
        return el[8] == 1;
      })
    }

    if(h){
      //filter out classes that don't have [8] == 1
      classes = classes.filter(function (el) {
        return el[9] == 1;
      })
    }

    if(gm){
      //filter out classes that don't have [9] == 1 or [10] == 1
      classes = classes.filter(function (el) {
        return el[10] == 1 || el[11] == 1;
      })
    }

    if(gm1){
      //filter out classes that don't have [9] == 1
      classes = classes.filter(function (el) {
        return el[10] == 1;
      })
    }

    if(gm2){
      //filter out classes that don't have [10] == 1
      classes = classes.filter(function (el) {
        return el[11] == 1;
      })
    }

    if(l){
      //filter out classes that don't have [10] == 1
      classes = classes.filter(function (el) {
        return el[12] == 1;
      })
    }

    if(ns){
      //filter out classes that don't have [10] == 1
      classes = classes.filter(function (el) {
        return el[13] == 1;
      })
    }

    if(q){
      //filter out classes that don't have [10] == 1
      classes = classes.filter(function (el) {
        return el[14] == 1;
      })
    }


    
      
    

    

  }







  function filterSearch(term){
    //count the length of the search term without spaces
    let termLengthNoSpace = term.replace(" ","");

    if(termLengthNoSpace.length<2){
      return;
    }

    //while the search term has spaces at the end, remove them
    while(term[term.length-1]==" "){
      term = term.slice(0,-1);
    }

    //remove periods from the search term
    term = term.replace(".","");
    //remove commas from the search term
    term = term.replace(",","");
    //remove colons from the search term
    term = term.replace(":","");
    //remove semicolons from the search term
    term = term.replace(";","");
    //remove slashes from the search term
    term = term.replace("/","");


    //filter out classes that don't have [0] == search
    classes = classes.filter(function (el) {

      //split term into words
      let words = term.split(" ");
      let found = false;

      //if words.length is 2 and the first words is 2-4 letters and the second word is numbers
      if(words.length==2 && words[0].length>=2 && words[0].length<=4 && !isNaN(words[1])){
        //if the first word is in [0] and the second word is in [1]
        if(el[0].toLowerCase().includes(words[0].toLowerCase()) && el[1].toLowerCase().includes(words[1].toLowerCase())){
          found = true;
        }
        return found;
      }
      




      words.forEach(word => {
        if(el[0].toLowerCase().includes(word.toLowerCase())||el[3].toLowerCase().includes(word.toLowerCase())||el[1].toLowerCase().includes(word.toLowerCase())){
          found = true;
        }
      });


      




      return found;

      
    })
  }

  function filterCount(number){
    //filter out classes where the total of [6-14] is less than number
    classes = classes.filter(function (el) {
      return (el[6]+el[7]+el[8]+el[9]+el[10]+el[11]+el[12]+el[13]+el[14])>=number;
    })
  }

  function filter(){
    classes=rawClasses;
    filterCCS()
    if(minCCS>0){
      filterCount(minCCS);
    }
    filterSearch(search);

    numClasses = classes.length;

  }



  filter();

    

  </script>

<!-- DARKMODE CODE -->

<!-- {#if (!darkMode)}
<div class="flex justify-end mr-4 mt-4">
  <label class="flex items-center cursor-pointer">
    <div class="relative">
      <input type="checkbox" class="sr-only" id="dark-mode-toggle" on:click={toggleDarkMode}>
      <div class="block bg-gray-600 w-14 h-8 rounded-full"></div>
      <div class="dot absolute left-1 top-1 bg-white w-6 h-6 rounded-full transition"></div>
    </div>
    <div class="ml-3 text-gray-700 font-medium">Light Mode</div>
  </label>
</div>
{/if}

{#if (darkMode)}
<div class="flex justify-end mr-4 mt-4">
  <label class="flex items-center cursor-pointer">
    <div class="relative">
      <input type="checkbox" class="sr-only" id="dark-mode-toggle" on:click={toggleDarkMode}>
      <div class="block bg-gray-600 w-14 h-8 rounded-full"></div>
      <div class="dot absolute left-1 top-1 bg-white w-6 h-6 rounded-full transition translate-x-6"></div>
    </div>
    <div class="ml-3 text-gray-700 font-medium ">Dark Mode</div>
  </label>
</div>
{/if} -->




<div class="my-4 mx-2 font-medium text-center justify-items-center ">
<h1 class="font-black text-4xl md:text-6xl">ClassBrowser</h1>
<p>Currently Showing Fall 2023 Classes</p>
<p></p>
</div>

<div class="flex flex-col items-center justify-center">
  <p class="bg-red-200 dark:bg-red-400 border-2 border-red-300 dark:border-red-500 dark:text-slate-900 inline-block p-2 max-w-screen rounded-lg text-center m-2 ">Please be aware that the information on this page may be inacurate and incomplete.
    <br>Data last updated 5/5/2023</p>
</div>



<div class="m-2 flex flex-wrap justify-center items-center text-sm dark:text-slate-400">
  <!-- Add a row of checkboxes coresponding to the booleans above. -->
<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800  font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Values</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => v=!v} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800  font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Writing</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => w=!w} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800  font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Social Science</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => s=!s} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800  font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Humanities</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => h=!h} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800  font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Global 1</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => gm1=!gm1} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800  font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Global 2</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => gm2=!gm2} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800  font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Global 1 or 2</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => gm=!gm} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800  font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Language</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => l=!l} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800  font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Natural Science</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => ns=!ns} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800  font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Quantitative</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => q=!q} on:click={() => filter()}>
</label>

</div>

<br>





<div class="flex justify-center">
  <div class="bg-slate-100 rounded-lg flex w-5/6 md:w-1/2 lg:w-1/3  shadow-lg dark:bg-slate-300">
    <input class="border-none bg-transparent outline-none p-2 w-full placeholder-slate-500 dark:placeholder-slate-700 dark:text-slate-900" bind:value={search}  on:input={() => filter()} placeholder="Search for classes">
  </div>
</div>






{#if numClasses==0}
<p class="font-bold m-6">No Classes Found. Try reducing the filters or clearing the search bar</p>
{/if}

{#if numClasses>1}
<p class="font-bold m-6">{numClasses} Classes Found</p>
{/if}

{#if numClasses==1}
<p class="font-bold m-6">{numClasses} Class Found</p>
{/if}




{#each Array(numClasses).fill(0) as _, i}



<div class="bg-slate-200 p-2 m-2 md:m-6 flex flex-wrap items-center rounded-lg shadow-md dark:bg-slate-700 dark:text-slate-100">
  <p class="font-bold">{classes[i][0]} {classes[i][1]}&nbsp;</p>
  {#if !isMobile}
  <p class="font-medium">{classes[i][2]} - {classes[i][3]} - {classes[i][4]}&nbsp</p>

  {/if}
  {#if isMobile}
  <p class="font-medium">{classes[i][3]}&nbsp</p>

  {/if}


  <div class="flex content-end">
      {#if (classes[i][6]==1||classes[i][7]==1||classes[i][8]==1||classes[i][9]==1||classes[i][10]==1||classes[i][11]==1||classes[i][12]==1||classes[i][13]==1||classes[i][14]==1)}
        <p class="font-medium">-</p>
      {/if}


    {#if (classes[i][6])==1}
    <div class="font-bold">
        <p>&nbspV</p>
      </div>
    {/if}
    {#if (classes[i][7])==1}
    <div class="font-bold">
        <p>&nbspW</p>
      </div>
    {/if}
    {#if (classes[i][8])==1}
    <div class="font-bold">
      <p>&nbspSS</p>
    </div>
    {/if}
    {#if (classes[i][9])==1}
    <div class="font-bold">
      <p>&nbspH</p>
    </div>
    {/if}
    {#if (classes[i][10])==1}
    <div class="font-bold">
      <p>&nbspGM1</p>
    </div>
    {/if}
    {#if (classes[i][11])==1}
    <div class="font-bold">
      <p>&nbspGM2</p>
    </div>
    {/if}
    {#if (classes[i][12])==1}
    <div class="font-bold">
      <p>&nbspLANG</p>
    </div>
    {/if}
    {#if (classes[i][13])==1}
    <div class="font-bold">
      <p>&nbspNS</p>
    </div>
    {/if}
    {#if (classes[i][14])==1}
    <div class="font-bold">
      <p>&nbspQ</p>
    </div>
    {/if}
  </div>

  </div>
{/each}



<button class="fixed bottom-0 right-0 p-3 m-4 bg-slate-400 text-white dark:bg-slate-500 rounded-full shadow-lg"
  on:click={() => window.scrollTo({ top: 0, behavior: 'smooth' })}>
  <i class="fa fa-arrow-up"></i> <!-- Font Awesome icon -->
  <svg class="h-6 w-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" xmlns="http://www.w3.org/2000/svg"> <!-- Heroicons icon -->
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path>
  </svg>
</button>