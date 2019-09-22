var express = require('express');
var bodyParser = require('body-parser');
var app = express();
var fs = require('fs');
var jsonQuery = require('json-query');
var moment = require('moment');
var conte;
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use('/css',express.static(__dirname+ '/css'));
app.set('view engine', 'ejs');


	//Date search function  
function search_date(datee){
	var result = jsonQuery('feedback[*date='+datee+']', {data: conte}).value;
	return result;
}
	//Location search function
function search_location(locat){
	var result = jsonQuery('feedback[*location='+locat+']', {data: conte}).value;
	return result;
}
	//Answer search function
function search_answer(answ){
	var result = jsonQuery('feedback[*answer='+answ+']', {data: conte}).value;
	return result;
}

app.get('/', function(req, res) {
	res.sendFile(__dirname +"/index.html");
});

app.get('/alldata', function(req, res) {
	res.sendFile(__dirname +"/index.html");
	var file_cont = fs.readFileSync('./jsonfile.json');
  	conte = JSON.parse(file_cont);
 	var data = JSON.stringify(conte, null,2);
 	res.render('alldata', {answer: conte});	
});

app.get('/add', function(req, res) {
	// http://localhost:3030/add?location=laws210&answer=ok     Add a record
	var d = new Date();
 	var date = moment().format('L'); 
 	var time = d.getHours()+":"+d.getMinutes()+":"+d.getSeconds();
	var location=req.query.location;
	var answer=req.query.answer;
	var file_cont = fs.readFileSync('./jsonfile.json');
  	conte = JSON.parse(file_cont);
 	conte.feedback.push({location:location, date:date, time:time,answer:answer});
 	var data = JSON.stringify(conte, null,2);
 	fs.writeFileSync('./jsonfile.json', data);
 	res.status(200);
 	res.end();
});

app.get('/resloc', function(req, res) {
 // http://localhost:3030/resloc?location=	search by location
 	var file_cont = fs.readFileSync('./jsonfile.json');
 	conte = JSON.parse(file_cont);
 	var search = req.query.location; 
 	var result = search_location(search); 
 	var jsonstr = JSON.stringify(result, null,2);
 	 
 	if (jsonstr.length>2) {
 		res.setHeader('Content-Type', 'text/html');
 		res.render('resloc', {answer: result});	
 	}else {
 		res.status(404).send("Nothing was found");
 	}
});

app.get('/resans', function(req, res) {
 // http://localhost:3030/resans?answer=   search by answer
 	var file_cont = fs.readFileSync('./jsonfile.json');
 	conte = JSON.parse(file_cont);
 	var search = req.query.answer; 
 	var result = search_answer(search); 
 	var jsonstr = JSON.stringify(result, null,2); 
 	
 	if (jsonstr.length>2) {
 		res.render('resans', {ans: result});	
 	}else {
 		res.status(404).send("Nothing was found");
 	}
});

app.get('/resdat', function(req, res) {
 // http://localhost:3030/resdat?datetime= search by date
 	var file_cont = fs.readFileSync('./jsonfile.json');
 	conte = JSON.parse(file_cont);
 	var search = req.query.date; 										
 	var result = search_date(search); 
 	var jsonstr = JSON.stringify(result, null,2); 
 	
 	if (jsonstr.length>2) {
 		res.render('resdat', {dateans: result});	
 	}else {
 		res.status(404).send("Nothing was found");
 	}
});

app.listen(3030, function() {
 	console.log('Server is runnung!');
 });
