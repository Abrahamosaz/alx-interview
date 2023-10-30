#!/usr/bin/node
/*
print all characters of the star movies base on the id
*/
const request = require("request");
const BASE_URL = "https://swapi-api.alx-tools.com/api/";

function ch_star_movie(id) {
  const url = BASE_URL + `films/${id}/`;
  request(url, (err, res, body) => {
    if (res.statusCode === 200) {
      const { characters } = JSON.parse(body);
      for (const sub_url of characters) {
        request(sub_url, (err, res, body) => {
          if (res.statusCode === 200) {
            const { name } = JSON.parse(body);
            console.log(name);
          }
        });
      }
    }
  });
}

ch_star_movie(process.argv[2]);
