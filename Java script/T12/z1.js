const users = [
	"Андрусишин Олег",
	"Балицький Олексій",
	"Барановський Ігор",
	"Бей Тетяна",
	"Білас Всеволод",
	"Білоус Андрій",
	"Бордун Галина",
	"Буба Євген",
	"Вантух Володимир",
	"Васьків Роман",
	"Вервега Тарас",
	"Візняк Юрій",
	"Гагалюк Богдан",
	"Ганущин Олександр",
	"Гичка Михайло",
	"Гірняк Володимир",
	"Голуб Юрій",
	"Грабінський Ігор",
	"Грицик Ольга",
	"Гудима Юрій",
	"Дворянин Парасковія",
	"Дейнека Анатолій",
	"Демчина Роман",
	"Дзюдзь Михайло"
];

const users_table = document.getElementById("users_table");
const message = document.getElementById("message");

const name= prompt("Введіть ім'я користувача яким потрібно відправити лист -");

let all_users = ``;
let users_num = 0;

for( i = 0; i < users.length ; i++ ){
	
	let gray = ``;
	if( i % 2 > 0 ){
		gray= "gray"
	}	
	
	let checked = ``;
	if( users[i].includes(name) ){ checked = "checked"; users_num++ }
	
	all_users +=
	`
	<tr class="${gray}">
			 <td class="num">${i + 1}</td>
			 <td>${users[i]}</td>
			 <td>
			 <input type="checkbox" class="letter" ${checked}>
			 </td>
		</tr>
		`;
}	

message.innerText = `Знайдено користувачів з ім'ям ${name} - ${users_num}`;

users_table.innerHTML = all_users;