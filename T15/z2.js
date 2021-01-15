const user = {
	name: "Петро",
	lastName: "Иванов", 
	age: 17,
	email: "petrovich@gmail.com",
	city: "Львив"
};

function showUser(){
	const  user_data = document.getElementById("user_data");
	
	user_data.innerHTML = 
	`
	<tr>
	      <td>${user.name}</td>
		  <td>${user.lastName}</td>
		  <td>${user.age}</td>
		  <td>${user.email}</td>
		  <td>${user.city}</td>
	</tr>
	`;
}	

showUser()

function changeName(new_name){
	user.name = new_name;
	showUser()
}	

function changeLastName(new_lastName){
	user.lastName = new_lastName;
	showUser()
}

function changeAge(new_age){
	user.age = new_age;
	showUser()
}

function changeEmail(new_email){
	user.email = new_email;
	showUser()
}

function changeCity(new_city){
	user.city = new_city;
	showUser()
}

function changeUserData(new_name, new_lastName, new_age, new_email, new_city){
	user.name = new_name;
	user.lastName = new_lastName;
	user.age = new_age;
	user.email = new_email;
	user.city = new_city;
	
	showUser()
}	

changeUserData("Оля", "Микитюк", 20, "olgamukutiuk@gmail.com", "Полтава");