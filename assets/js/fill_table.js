"use strict";
async function fetchJSON() {
  const response = await fetch("/schedule.json");
  const schedules = await response.json();
  return schedules;
}
fetchJSON().then(schedules => {
  console.log(schedules);

  if (current_schedule < 0) {
    current_schedule = 0;
  }
  else if (current_schedule >= schedules.length) {
    current_schedule = schedules.length-1;
  }

  if (schedules.length>0) {
    document.getElementById("schedule-number").innerHTML = "" + (current_schedule+1) + "/" + schedules.length;
  }
  else {
    document.getElementById("schedule-number").innerHTML = "" + current_schedule + "/" + schedules.length;
  }
  

  var schedule = schedules[current_schedule][0];
  let sun = new Array, mon = new Array, tue = new Array, wed = new Array, thu = new Array;

  for (var i=0; i < schedule.length; i++) {
    schedule[i].event_id = i;
    if (schedule[i]["days"].includes("U")) {
      sun.push(schedule[i]);
    }
    if (schedule[i]["days"].includes("M")) {
      mon.push(schedule[i]);
    }
    if (schedule[i]["days"].includes("T")) {
      tue.push(schedule[i]);
    }
    if (schedule[i]["days"].includes("W")) {
      wed.push(schedule[i]);
    }
    if (schedule[i]["days"].includes("R")) {
      thu.push(schedule[i]);
    }
    //if (schedule[i]["status"] == "Wait List") schedule[i].id = -1;
  }

  function getStringToTimestamp(time) {
    //accepts hh:mm format - convert hh:mm to timestamp
    var timeArray = (time+"").split(':');
    var timeStamp = parseInt(timeArray[0])*60 + parseInt(timeArray[1]);
    return timeStamp;
  }

  function getNumberToTimestamp(time) {
    //accepts hh.mm/60 format - convert hh.mm/60 to timestamp
    var timeStamp = Math.trunc(time)*60 + Math.round((time%1)*60);
    return timeStamp;
  }

  function getNumberToStringTime(time) {
    //accepts hh.mm/60 format - convert hh.mm/60 to hh:mm
    var hour = "" + Math.trunc(time);
    var min = "" + Math.round((time%1)*60);
    while (min.length<2) min = "0"+min;
    return hour + ":" + min;
  }

  var slotHeight = document.getElementsByClassName('cd-schedule__top-info')[0].offsetHeight;
  var timelineItems = document.getElementsByClassName('cd-schedule__timeline')[0].getElementsByTagName('li');
  var timelineStart = getStringToTimestamp(timelineItems[0].textContent);
  var timelineUnitDuration = getStringToTimestamp(timelineItems[1].textContent)-timelineStart;

  let weekdays = [sun,mon,tue,wed,thu];
  let weekdays_names = ["sun","mon","tue","wed","thu"];

  var old_events = document.getElementsByClassName("cd-schedule__event");
  for (var i = 0; i < old_events.length; i++) old_events[i].remove();
    
  for (var j = 0; j < weekdays.length; j++) {
    for (var i = 0; i < weekdays[j].length; i++) {
      var start = getNumberToTimestamp(weekdays[j][i]["start_date"]),
          duration = getNumberToTimestamp(weekdays[j][i]["end_date"]) - start;

      var courseTop = slotHeight*(start - timelineStart)/timelineUnitDuration,
          courseHeight = slotHeight*duration/timelineUnitDuration;

      //create a course element
      var name = document.createElement("em");
      name.className = "cd-schedule__name";
      var names = weekdays[j][i]["name"].split(" - ");
      name.innerHTML = names[1];
      var text = document.createElement("a");
      text.dataset.start = getNumberToStringTime(weekdays[j][i]["start_date"]);
      text.dataset.end = getNumberToStringTime(weekdays[j][i]["end_date"]);
      text.dataset.event = "event-"+weekdays[j][i]["event_id"];
      text.dataset.prof = weekdays[j][i]["instructor"];
      text.appendChild(name);
      var tag = document.createElement("li");
      tag.className = "cd-schedule__event";
      tag.appendChild(text);

      //position a course element
      tag.setAttribute('style', 'top: '+(courseTop-1)+'px; height: '+(courseHeight +1)+'px');

      //add a course element into html file
      var parent = document.getElementById("ul-"+weekdays_names[j]);
      parent.appendChild(tag);
    }
  }
});