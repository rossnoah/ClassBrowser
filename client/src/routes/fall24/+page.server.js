// this is a svelete kit project, this file is a server side route

import classes from "../../../data/fall24.json";
//get the class data from the database

//console.log(db);

export const prerender = true; // Pre-generate the page at build time

export async function load() {
  return { classes };
}
