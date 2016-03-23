var PythonShell = require('python-shell');
var fs = require('fs');

// Create a log file
fs.writeFileSync('logfile.csv','time,message\n');
console.log('made new logfile.csv\n');

// Run out python script
var pyshell = new PythonShell('test.py');

pyshell.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
  var newMessage = JSON.parse(message);
  writeMessage(newMessage.middle_name);
});

function writeMessage(message){
    fs.appendFile('logfile.csv',`${message.trim()}\n`);
    console.log('logged message to file\n');
}

// end the input stream and allow the process to exit
// pyshell.end(function (err) {
//   if (err) throw err;
//   console.log('finished');
// });