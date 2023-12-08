let suggestions = [];

var getJSON = function(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
      var status = xhr.status;
      if (status === 200) {
        callback(null, xhr.response);
      } else {
        callback(status, xhr.response);
      }
    };
    xhr.send();
};

function load_people() {
	getJSON("nicknames.json", function(status, data) {
		if (status == null)
			suggestions = data;
	});
}

function guessSuccessed(data)
{
	const newTable = document.createElement("table");
	let linesAmount = 0
	for (let column = 0; column < data.length; column += 1)
		linesAmount = Math.max(linesAmount, data[column].length)
	
	for (let line = 0; line < linesAmount; line += 1)
	{
		const newLine = document.createElement("tr");
		for (let column = 0; column < data.length; column += 1)
		{
			let newCell;
			if (line == 0)
			{
				newCell = document.createElement("th");
				if (line < data[column].length)
					newCell.innerHTML = data[column][line];
			}
			else
			{
				newCell = document.createElement("td");
				if (line < data[column].length)
					newCell.innerHTML = data[column][line][0] + " (" + data[column][line][1] + "%)";
			}
			newLine.appendChild(newCell);
		}
		newTable.appendChild(newLine)
	}
	document.getElementById("result").innerHTML = "";
	document.getElementById("result").appendChild(newTable);
}

function guessFailed()
{
	document.getElementById("result").innerHTML = "<div class=\"sub_title\">Please provide correct name!</div>"
}

function guess() {
	let searchingFor = document.querySelector(".searchInput").querySelector("input").value;
	if (searchingFor == null)
		guessFailed();
	else
		getJSON("guess?user=" + searchingFor, function(status, data) {
			if (status == null)
				guessSuccessed(data)
			else
				guessFailed()
		})
}