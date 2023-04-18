#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const tasks = JSON.parse(body);
  const tasksCompleted = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (tasksCompleted[task.userId]) {
        tasksCompleted[task.userId]++;
      } else {
        tasksCompleted[task.userId] = 1;
      }
    }
  });
  console.log(tasksCompleted);
});
