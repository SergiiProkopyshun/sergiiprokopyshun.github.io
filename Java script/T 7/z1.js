const pass = 1122;

let trys = 3;

for( i = 0; i < 3; i++ ){

 const new_try = Number ( prompt(`Введіть пароль. Не менше 4-х символів! ${trys}`));

   trys--;

	if( pass === new_try){
		console.log("Вірно")
		break;
	} else {	
			console.log("Невірно")
	}	

	 if( trys === 1){
		alert("Пароль 1***2")
	} 
}