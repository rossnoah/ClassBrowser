<title>ClassBrowser</title>
<script>
  import { text } from 'svelte/internal';

    export let data;
    let rawClasses = data.classes;

    // console.log(numClasses);

    // console.log(classes[0][0]);

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
<div class="  dark:text-slate-100">

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







<div class="m-4 font-medium text-center justify-items-center ">
<p class="font-black text-6xl">ClassBrowser</p>
<p>Currently Showing Fall 2023 Classes</p>
<p></p>


</div>

<div class="flex justify-center mt-8 ">
  <p class="bg-red-200 dark:bg-red-400 border-2 border-red-300 dark:border-red-500 dark:text-slate-900 inline-block p-2 max-w-screen rounded-lg text-center m-2 ">Please be aware that the information on this page may be inacurate and incomplete.
    <br>Data last updated 4/7/2023</p>
</div>



<div class="m-2 flex flex-wrap justify-center items-center text-sm">
  <!-- Add a row of checkboxes coresponding to the booleans above. -->
<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800 dark:text-slate-500 font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Values</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => v=!v} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800 dark:text-slate-500 font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Writing</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => w=!w} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800 dark:text-slate-500 font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Social Science</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => s=!s} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800 dark:text-slate-500 font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Humanities</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => h=!h} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800 dark:text-slate-500 font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Global 1</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => gm1=!gm1} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800 dark:text-slate-500 font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Global 2</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => gm2=!gm2} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800 dark:text-slate-500 font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Global 1 or 2</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => gm=!gm} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800 dark:text-slate-500 font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Language</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => l=!l} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800 dark:text-slate-500 font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Natural Science</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => ns=!ns} on:click={() => filter()}>
</label>

<label class="inline-flex items-center bg-slate-400 dark:bg-slate-800 dark:text-slate-500 font-bold px-4 py-2 rounded-full m-1 cursor-pointer shadow-lg">
  <span class="mr-2 select-none">Quantitative</span>
  <input type="checkbox" class="form-checkbox h-4 w-4" on:click={() => q=!q} on:click={() => filter()}>
</label>

</div>

<br>





<div class="flex justify-center">
  <div class="bg-slate-100 rounded-lg flex w-1/3 shadow-lg dark:bg-slate-300 ">
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
<div class="bg-slate-200 p-2 m-6 flex rounded-lg shadow-md dark:bg-slate-600 dark:text-slate-200">
    <p class="font-bold">{classes[i][0]} {classes[i][1]}&nbsp;</p>
    <p class="font-medium">- {classes[i][2]}&nbsp</p>
    <p class="font-medium">- {classes[i][3]}&nbsp</p>
    <p class="font-medium">- {classes[i][4]}</p>
    <div class="flex content-end">
      {#if (classes[i][6]==1||classes[i][7]==1||classes[i][8]==1||classes[i][9]==1||classes[i][10]==1||classes[i][11]==1||classes[i][12]==1||classes[i][13]==1||classes[i][14]==1)}
        <p class="font-medium">&nbsp-</p>
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


</div>
