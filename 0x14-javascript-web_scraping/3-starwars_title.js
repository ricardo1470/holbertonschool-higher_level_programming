#!/usr/bin/node
const request = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/' + parseInt(process.argv[2]);
request(url, function (error, response, body) {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});