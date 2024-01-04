#!/usr/bin/node


const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const completed = {};
    const tasks = JSON.parse(body);

    for (const task of tasks) {
      if (task.completed === true) {
        completed[task.userId] = (completed[task.userId] || 0) + 1;
      }
    }

    console.log(completed);
  } else {
    console.log('An error occurred. Status code:', response.statusCode);
  }
});
