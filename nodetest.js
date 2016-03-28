var PythonShell = require('python-shell');
var CronJob = require('cron').CronJob;
var fs = require('fs');

var logFilepath = './logs/logfile.csv';


var ftpClient = require('ftp-client'),
    config = {
        host: 'eatenbymonsters.com',
        port: 21,
        user: process.env.USER_ID,
        password: process.env.USER_KEY
    },
    options = {
        logging: 'basic'
    },
    ftp = new ftpClient(config, options);


/**
 * ----------------
 * MEASURE CRON JOB
 *
 * Trigger the task
 * to record all of
 * the measurements
 * every 30 seconds
 * ----------------
 */
var testCron = new CronJob('1 * * * * *',function(){
    process.stdout.write('\n Starting...\n');
    checkFolder();
    uploadFile();
    process.stdout.write('\n Finished. \n===================\n');
}, null, true, 'Europe/London');
testCron.start();


/**
 * ---------------
 * UPLOAD CRON JOB
 *
 * Copy the log of
 * measurements to
 * the live server
 * ---------------
 */
//var uploadCron = new CronJob('0 1 * * * *',function(){
//    uploadFile();
//}, null, true, 'Europe/London');
//uploadCron.start();

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
    var pyshell = new PythonShell('weather.py');

    pyshell.on('message', function (message) {
      // received a message sent from the Python script (a simple "print" statement)
      var rawMessage = JSON.parse(message);

      var time = Date.now();
      time = time.toString();

      var outputMessage = time + ',' + rawMessage.temp + ',' + rawMessage.humidity + ',' + rawMessage.pressure;

      writeMessage(outputMessage);

    });

    // end the input stream and allow the process to exit
    pyshell.end(function (err) {
      if (err) throw err;
      // process.stdout.write('Python task terminated\n');
    });

}

function writeMessage(message){
    fs.stat(logFilepath, function(err,stat) {
        if (err == null) {
            process.stdout.write('Found existing logfile.\n');
        } else {
            fs.writeFileSync(logFilepath,'time,temp,humidity,pressure\n');
            process.stdout.write('Created new logfile.\n');        
        }
    });

    fs.appendFile(logFilepath, message.trim() + '\n',function(err) {
        if (err) {
            process.stdout.write(err);
        } else {
            process.stdout.write('Logged results to file\n');
        }
    });
}

// function convertCsvIntoJson(){
//     var converter = new Converter({});

//     //end_parsed will be emitted once parsing finished 
//     converter.on("end_parsed", function (jsonArray) {
//        console.log(jsonArray); //here is your result jsonarray 
//     });

//     //read from file 
//     require("fs").createReadStream(logFilepath).pipe(converter);
// }

function uploadFile(){
    ftp.connect(function () {
     
        ftp.upload(['logs/**'], '/logs', {
            baseDir: 'logs',
            overwrite: 'older'
        }, function (result) {
            // console.log(result);
            process.stdout.write('Copied file to server.\n');
        });
     
    });
}
