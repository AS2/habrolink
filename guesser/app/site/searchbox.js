// getting all required elements
const searchInput = document.querySelector(".searchInput");
const input = searchInput.querySelector("input");
const resultBox = searchInput.querySelector(".resultBox");
const icon = searchInput.querySelector(".icon");
let linkTag = searchInput.querySelector("a");
let webLink;

// if user press any key and release
input.onkeyup = (e)=>{
	let userData = e.target.value; //user enetered data
	let emptyArray = [];
	if(userData){
		emptyArray = suggestions.filter((data)=>{
			//filtering array value and user characters to lowercase and return only those words which are start with user enetered chars
			return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase()); 
		});
		emptyArray = emptyArray.slice(0, 10)
		emptyArray = emptyArray.map((data)=>{
			// passing return data inside li tag
			return data = '<li>'+ data +'</li>';
		});
		searchInput.classList.add("active"); //show autocomplete box
		showSuggestions(emptyArray);
		let allList = resultBox.querySelectorAll("li");
		for (let i = 0; i < allList.length; i++) {
			//adding onclick attribute in all li tag
			allList[i].setAttribute("onclick", "select(this)");
		}
	}else{
		searchInput.classList.remove("active"); //hide autocomplete box
	}
}

function showSuggestions(list){
	let listData;
	if(!list.length){
		userValue = input.value;
		listData = '<li>'+ userValue +'</li>';
	}else{
		listData = list.join('');
	}
	resultBox.innerHTML = listData;
}

function select(element) {
	input.value = element.innerHTML;
	searchInput.classList.remove("active"); //hide autocomplete box
	guess()
}