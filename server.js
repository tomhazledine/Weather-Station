var express = require('express');
var app = express();

var data = [ { time: 1459069681778,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459069741772,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459069801777,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459069861774,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070101663,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070151522,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070161521,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070171524,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070181528,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070191532,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070201537,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070211540,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070221566,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070292020,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070302014,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070321974,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070331971,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070421731,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070431727,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070451057,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070491857,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070501856,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070511861,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070521865,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070531868,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070541869,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070551875,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070561876,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070571879,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070581879,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070591886,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070601889,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070611889,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070621895,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070631901,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070641906,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070651908,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070661909,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070671911,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070681915,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070691918,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070701922,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070711921,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070721926,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070731743,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070741741,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070751746,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070761748,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 },
  { time: 1459070771753,
    temp: 23.7,
    humidity: 53.9,
    pressure: 1019.2 } ];

app.use(function(req,res,next){
    console.log(req.method + ' request for ' + req.url);
    next();
});

app.get('/',function(req,res){
    res.json(data);
});

app.listen(3000);
console.log('Weather sever running on port 3000');