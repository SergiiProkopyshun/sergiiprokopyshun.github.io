const number = prompt("Введіть число.");

if( number < 0 && number%2 == 0 ){
	alert("Число є від'ємним і парним.")
}

else if( number < 0 && number%2 < 0 ){
	alert("Число є від'ємним парним.")
}

else if( number < 0 && number%2 > 0 ){
	alert("Число є від'ємним не парним.")
}

else if( number > 0 && number%2 == 0 ){
	alert("Число є додатнім і парнем.")
}

else if( number > 0 && number%2 <= 0 ){
	alert("Число є додатнім не париним.")
}

else if( number > 0 && number%2 > 0 ){
	alert("Число є додатнім не париним.")
}

else if( number == 0){
	alert("Введене число не є ні додатнім ні від'ємни і париним.")
}

else {
	alert("Число введено не вірно.")
}	



	





	

