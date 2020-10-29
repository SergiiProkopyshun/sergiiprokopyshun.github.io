const color = prompt("Який вибрати колір на світлофорі");

if( color == "Зелений" || color == "зелений" || color == "green" ){
	alert("Можна рухатись.")
}

if( color == "Жовтий" || color == "жовтий" || color == "yellow" ){
	alert("Приготуватися.")
}

if( color == "Червоний" || color == "червоний" || color == "red"){
	alert("Стояти.")
}		

//*alert(`Зараз ${color}`);