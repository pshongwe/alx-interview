#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charactersArray = JSON.parse(body).characters;
    const characterNames = charactersArray.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseError, __, characterRequest) => {
          if (promiseError) {
            reject(promiseError);
          }
          resolve(JSON.parse(characterRequest).name);
        });
      }));

    Promise.all(characterNames)
      .then(names => console.log(names.join('\n')))
      .catch(allErrors => console.log(allErrors));
  });
}
