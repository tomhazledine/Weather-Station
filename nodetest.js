var PythonShell = require('python-shell');
var pyshell = new PythonShell('test.py');

// var testMessage = {
// 	'message': 'A test message'
// }

// sends a message to the Python script via stdin
// pyshell.send('hello');

pyshell.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
  var newMessage = JSON.parse(message);
  console.log(newMessage.first_name);

});

// end the input stream and allow the process to exit
// pyshell.end(function (err) {
//   if (err) throw err;
//   console.log('finished');
// });