function sayHi(){
	alert("Приветик")
}


function showGreeting(name){
	const test = document.getElementById("test");
	test.innerText = `Привит ${name}!`;
}

showGreeting("Петро")


