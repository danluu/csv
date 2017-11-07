var fs = require('fs'),
	path = require('path'),
	csv = require('csv');

fs.readFile(process.argv[2], {encoding: 'utf-8'}, function(err,data){
	if (!err) {
		csv.parse(data, function(err, data) {
			csv.stringify(data, function(err, data) {
				console.log(data);
			});
		});
	} else {
		console.log(err);
	}
});
