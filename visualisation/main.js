const { spawn } = require('child_process');
const temperatures = [];

const main = spawn('python', ['main.py']);

main.stdout.on('data', function(data) {

    temperatures.push(parseFloat(data));
    console.log(temperatures);

});