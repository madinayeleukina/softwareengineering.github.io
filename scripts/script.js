var courses = require('../courses.json');
console.log(courses);

/*'use strict';
const fs = require('fs');

let rawdata = fs.readFileSync('courses.json');
let student = JSON.parse(rawdata);
console.log(student);

/*


/*
let weekdays = new Array(5);
for (let i=0; i<courses.length; i++) {
	if (courses[i]["days"].includes("M")) {
		weekdays[0].push(courses[i]);
	}
	if (courses[i]["days"].includes("T")) {
		weekdays[1].push(courses[i]);
	}
	if (courses[i]["days"].includes("W")) {
		weekdays[2].push(courses[i]);
	}
	if (courses[i]["days"].includes("R")) {
		weekdays[3].push(courses[i]);
	}
	if (courses[i]["days"].includes("S")) {
		weekdays[4].push(courses[i]);
	}
}
*/