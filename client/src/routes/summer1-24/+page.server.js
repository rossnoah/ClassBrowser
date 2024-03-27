// this is a svelete kit project, this file is a server side route

import classes from "../../../data/summer1-24.json";
//get the class data from the database

//console.log(db);

export async function load() {
  return { classes };
}
