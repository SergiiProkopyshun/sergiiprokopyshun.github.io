const users = [
	{
		name: "Олег",
		email: "olegivanov@.gmail.com"
	},
	{
		name: "Таня",
		email: "taniavit@.gmail.com"
	},
	{
		name: "Тарас",
		email: "tarik95@.gmail.com"
	},
	{
		name: "Оксана",
		email: "oksana2002@.gmail.com"
	}
];

function showError(text){
	
	const error_text = `<div class="alert alert-danger col-6">${text}</div>`
	
	const message = document.getElementById("message");
	
	message.innerHTML = error_text;
	
	setTimeout( function (){
		
		message.innerHTML = ``;
	}, 3000 )
}

function showSuccess(text){
	
	const error_text = `<div class="alert alert-success col-6">${text}</div>`
	
	const message = document.getElementById("message");
	
	message.innerHTML = error_text;
	
	setTimeout( function (){
		
		message.innerHTML = ``;
	}, 3000 )
}

showSuccess("Успішно");

function checkName(){
	
	const name= document.getElementById("name").value;

    console.log(email, name)

    const new_arr = users.filter( function(user){
		return user.name.toLowerCase() == name.toLowerCase()
	} )
	
	if( new_arr.length > 0){
		showError("Користувач з таким ім'ям вже існує");
		return false
	}else{
		return true
	}	
}

function checkEmail(){
	
	const email = document.getElementById('email').value;
	
	const new_arr = users.filter( function(user){
		return user.email.toLowerCase() == email.toLowerCase()
	})
	
	if( new_arr.length > 0 ){
		showError("Користувач з таким email вже існує")
	    return false
	}else{
		return true
	}	
}

function register(){
	const name = document.getElementById("name").value;
	const email = document.getElementById("email").value;
	const password = document.getElementById("password").value;
	
	if( name.length > 3 && email.length > 6 && password.length > 6 && checkEmail() && checkName() ){
	showSuccess("Користувач успішно зареєстрований");	
	}else{
		showError("Помилка в заповнені форми");
	}	
}	