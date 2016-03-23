var PythonShell = require('python-shell');
var CronJob = require('cron').CronJob;
var fs = require('fs');


/**
 * ----------------
 * SETUP CRON JOB
 *
 * Run a task every
 * 30 seconds.
 * ----------------
 */
var testCron = new CronJob('0,30 * * * * *',function(){
    checkFolder();
}, null, true, 'Europe/London');
testCron.start();

/**
 * ----------------
 * CHECK FOLDER
 *
 * Test if our logs
 * folder exists.
 * If not, create
 * it. Then run our
 * Python script.
 * ----------------
 */
function checkFolder(){
    if (fs.existsSync('logs')) {
        process.stdout.write('Found existing logs directory.\n');
    } else {
        fs.mkdir('logs',function(err){
            if (err){
                process.stdout.write(err);
            } else {
                process.stdout.write('Created new logs directory.\n');
            }
        });
    }
    runPython();
}

    // fs.writeFileSync('./logs/logfile.csv','time,first_name,middle_name,last_name\n');
    // process.stdout.write('made new logfile.csv\n');

function runPython(){
    // Run our python script
    var pyshell = new PythonShell('test.py');

    pyshell.on('message', function (message) {
      // received a message sent from the Python script (a simple "print" statement)
      var rawMessage = JSON.parse(message);

      var time = Date.now();
      time = time.toString();

      var outputMessage = `${time},${rawMessage.first_name},${rawMessage.middle_name},${rawMessage.last_name}`;

      writeMessage(outputMessage);

    });

    // end the input stream and allow the process to exit
    pyshell.end(function (err) {
      if (err) throw err;
      process.stdout.write('Python task terminated\n');
    });

}

function writeMessage(message){
    fs.stat('./logs/logfile.csv', function(err,stat) {
        if (err == null) {
            process.stdout.write('Found existing logfile.csv\n');
        } else {
            fs.writeFileSync('./logs/logfile.csv','time,first_name,middle_name,last_name\n');
            process.stdout.write('Created new logfile.csv\n');        
        }
    });

    fs.appendFile('./logs/logfile.csv',`${message.trim()}\n`,function(err) {
        if (err) {
            process.stdout.write(err);
        } else {
            process.stdout.write('Logged message to file\n===================\n');
        }
    });
}