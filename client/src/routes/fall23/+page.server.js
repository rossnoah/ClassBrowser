// this is a svelete kit project, this file is a server side route

import classes from "../../../data/fall23.json";
//get the class data from the database

//console.log(db);

export async function load() {
  return { classes };
}
