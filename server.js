var express = require('express');
var expressLayouts = require("express-ejs-layouts");
var bodyParser = require("body-parser");
var MongoClient = require('mongodb').MongoClient;
var fs = require('fs');
var bodyParser = require('body-parser');
var schedule = require('node-schedule');
var PythonShell = require('python-shell');
var exec = require('child_process').exec
var command = 'mongoimport -h ds155747.mlab.com:55747 -d heroku_50hc8zr3 -c gasolineras -u gusy -p das --file a.json'
test = require('assert');



var app = express();
app.use(expressLayouts);
app.use(bodyParser.json({
    type: 'application/json'
}))
app.set('view engine', 'ejs');
app.use(expressLayouts);
app.use(express.static('public'));


var jsonParser = bodyParser.json()

//Nº de puerto en el que estará escuchando el servidor
var serverPort = 3000;
var data2 = "";

//El script que recibe los precios correra cada 24h a las 9.00 de la mañana
var j = schedule.scheduleJob('* * 9:00 * * *', function() {
    PythonShell.run('parser_gasolineras.py', function() {

        MongoClient.connect("mongodb://gusy:das@ds155747.mlab.com:55747/heroku_50hc8zr3", function(err, db) {
            if (err) {
                return console.dir(err);
            }
            //Seleccion de la coleccion dentro de la base de datos
            var collection = db.collection('gasolineras');

            collection.removeMany();

            var a = read();

            exec(command, function(error, stdout, stderr) {
                console.log('Data added to the database')
            });

            db.close();
        });
    });

});


app.get('/a', function(req, res, next) {
    MongoClient.connect("mongodb://gusy:das@ds155747.mlab.com:55747/heroku_50hc8zr3", function(err, db) {
        if (err) {
            return console.dir(err);
        }
        console.log('Entrando');

        var collection = db.collection('gasolineras');

        collection.find().toArray(function(err, docs) {
            test.equal(null, err);
            var data = JSON.stringify(docs);
            res.json(docs);
        });
    });
});

app.get('/', function(req, res) {
  console.log("Renderizando index");
    res.render('index');
});

function read() {
    var fs = require('fs');
    data2 = fs.readFileSync('a.json', 'utf8');
    return data2;
}


//El servidor se pone a escuchar en el puerto asignado y escribe por consola
app.listen((process.env.PORT || serverPort), function() {
    PythonShell.run('parser_gasolineras.py', function() {

        MongoClient.connect("mongodb://gusy:das@ds155747.mlab.com:55747/heroku_50hc8zr3", function(err, db) {
            if (err) {
                return console.dir(err);
            }
            //Seleccion de la coleccion dentro de la base de datos
            var collection = db.collection('gasolineras');

            collection.removeMany();

            var a = read();

            exec(command, function(error, stdout, stderr) {
                console.log('Success')
            });

            db.close();
        });
    });

    console.log('GasolinApp Server listening on port ' + serverPort);
});
