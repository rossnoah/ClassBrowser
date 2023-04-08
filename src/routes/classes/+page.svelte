<script>
  import { text } from 'svelte/internal';

    export let data;
    let rawClasses = data.classes;
     console.log(rawClasses);

    // console.log(numClasses);

    // console.log(classes[0][0]);

//filter out class where [0] length is less than 2
    rawClasses = rawClasses.filter(function (el) {
      return el[0].length > 1;
    })
  

    
    let search = "";


    



    let v = false;
    let w = false;
    let s = false;
    let h = false
    let gm1 = false;
    let gm2 = false;
    let gm = false;

    let classes;
    let numClasses;


    let numRaw= rawClasses.length;

    function filter(){
      classes=rawClasses;

    if(v){
      //filter out classes that don't have [5] == 1
      classes = classes.filter(function (el) {
        return el[5] == 1;
      })
    }

    if(w){
      //filter out classes that don't have [6] == 1
      classes = classes.filter(function (el) {
        return el[6] == 1;
      })
    }

    if(s){
      //filter out classes that don't have [7] == 1
      classes = classes.filter(function (el) {
        return el[7] == 1;
      })
    }

    if(h){
      //filter out classes that don't have [8] == 1
      classes = classes.filter(function (el) {
        return el[8] == 1;
      })
    }

    if(gm){
      //filter out classes that don't have [9] == 1 or [10] == 1
      classes = classes.filter(function (el) {
        return el[9] == 1 || el[10] == 1;
      })
    }

    if(gm1){
      //filter out classes that don't have [9] == 1
      classes = classes.filter(function (el) {
        return el[9] == 1;
      })
    }

    if(gm2){
      //filter out classes that don't have [10] == 1
      classes = classes.filter(function (el) {
        return el[10] == 1;
      })
    }
    numClasses = classes.length;
  }
  filter();





  function filterSearch(term){
    classes=rawClasses;
    filter();
    if(term.length<2){
      return;
    }

    //filter out classes that don't have [0] == search
    classes = classes.filter(function (el) {
      return (el[0].toLowerCase().includes(term.toLowerCase())||el[2].toLowerCase().includes(term.toLowerCase()));
    })
    numClasses = classes.length;
  }

    

  </script>
<div class="m-4 font-medium">
<p >Welcome to LafUtils</p>
<p >Please be aware that the information on this page may be inacurate and incomplete.</p>
<p>Currently showing Fall 2023 Classes</p>
</div>


<div class="m-2">
<!-- Add a row of checkboxes coresponding to the booleans above. -->
<label class="font-bold bg-slate-400 p-2 rounded-lg m-2">
  Values 
<input type="checkbox" on:click={() => v=!v} on:click={() => filter()}>
</label>

<label class="font-bold bg-slate-400 p-2 rounded-lg m-2">
  Writing 
<input type="checkbox" on:click={() => w=!w} on:click={() => filter()}>
</label>

<label class="font-bold bg-slate-400 p-2 rounded-lg m-2">
  Social Science 
<input type="checkbox" on:click={() => s=!s} on:click={() => filter()}>
</label>

<label class="font-bold bg-slate-400 p-2 rounded-lg m-2">
  Humanities 
<input type="checkbox" on:click={() => h=!h} on:click={() => filter()}>
</label>

<label class="font-bold bg-slate-400 p-2 rounded-lg m-2">
  Global 1 
<input type="checkbox" on:click={() => gm1=!gm1} on:click={() => filter()}>
</label>

<label class="font-bold bg-slate-400 p-2 rounded-lg m-2">
  Global 2 
<input type="checkbox" on:click={() => gm2=!gm} on:click={() => filter()}>
</label>

<label class="font-bold bg-slate-400 p-2 rounded-lg m-2">
  Global 1 or 2 
<input type="checkbox" on:click={() => gm=!gm} on:click={() => filter()}>
</label>



<input class="p-2 rounded-lg m-2" bind:value={search}  on:input={() => filterSearch(search)} placeholder="Search for classes">

</div>








{#if numClasses==0}
<p class="font-bold">No Classes Found</p>
{/if}



{#each Array(numClasses).fill(0) as _, i}
<div class="bg-slate-200 p-2 m-4 flex rounded-md">
    <p class="font-bold">{classes[i][0]} {classes[i][1]}&nbsp;</p>
    <p class="font-medium">- {classes[i][2]}&nbsp</p>
    <p class="font-medium">- {classes[i][3]}</p>
    <div class="flex content-end">
    <p>CCS:</p>
    {#if (classes[i][5])==1}
    <div class="font-bold">
        <p>V</p>
      </div>
    {/if}
    {#if (classes[i][6])==1}
    <div class="font-bold">
        <p>W</p>
      </div>
    {/if}
    {#if (classes[i][7])==1}
    <div class="font-bold">
      <p>SS</p>
    </div>
    {/if}
    {#if (classes[i][8])==1}
    <div class="font-bold">
      <p>H</p>
    </div>
    {/if}
    {#if (classes[i][9])==1}
    <div class="font-bold">
      <p>GM1</p>
    </div>
    {/if}
    {#if (classes[i][10])==1}
    <div class="font-bold">
      <p>GM2</p>
    </div>
    {/if}
  </div>

  </div>
{/each}


