const email = "test@gmail.com";

const pass = "test";

const name = "Ivan Petro";

const new_email = prompt("Введіть почту");


if( email == new_email ){
	const pass2 = prompt("Введіть password");
		
	if( pass == pass2 ){
		alert(`Вітаю ${name}`);

	} else{
		alert(`Користувача з таким password не інсує`);
	}
	
	
} else{
    alert(`Користувача з таким email інсує`);
}



	

