const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.json());

let currentCpuUsage = 0;

app.post('/update-cpu-usage', (req, res) => {
    
    currentCpuUsage = req.body.cpu_percent;
    console.log(`Received CPU Usage: ${currentCpuUsage}`);
    res.sendStatus(200);
  });

  app.post('/update-memory-usage', (req, res) => {
    
    currentCpuUsage = req.body.memory_used;
    console.log(`Received Memory used: ${currentCpuUsage}`);
    res.sendStatus(200);
  });

app.listen(port,() => console.log(`Server is running on port ${port}`))