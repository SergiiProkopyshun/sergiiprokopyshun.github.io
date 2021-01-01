const product = {
	action: true,
	name: "Клавaіатура дротова Logitech G209 Prodigy USB",
	raviews: 204,
	price: 1399,
	photo: "images/z1-2.jpg",
};

const product_2 = {
	action: false,
	name: "Клавіаутура без дротова Cougar Vantar",
	raviews: 6,
	price: 1286,
	photo: "images/z1-4.jpg",
};

//Пункт №2
let poits_1 = product.raviews * 0.5;
let poits_2 = product_2.raviews * 0.5;

//Пункт №3
if( product.action ) { poits_1 += 100 }
if( product_2.action ) { poits_2 += 100 }

//Пункт №1
if( product.price > product_2.price ){
	const res = product.price - product_2.price;
	poits_2 += res;
} else{
	const res = product_2.price - product.price;
	poits_1 += res;
}

console.log(poits_1, poits_2);

const products = document.getElementById("products");

let action_1 = ``;

if( product.action == true ) { action_1 = `<div class="action">Акція</div>` }

let action_2 = ``;

if( product_2.action == true ) { action_2 = `<div class="action">Акція</div>` }

const card = 
`
<div>
	<h2 align="center">${poits_1}</h2>
	 <div class="card">
			<div class="header">
				${action_1}
			</div>
			
			<div class="card_image">
				<img src="${product.photo}" alt="">
			</div>
			
			<div class="card_info">
				<div class="name">
					${product.name}
				</div>
				
				<div class="reviews">
					${product.raviews} відгуки
				</div>
				
				<div class="price red">
					${product.price}&#8372;
				</div>
			</div>
		</div>
	</div>
`


const card_2 = 
`
<div>
	<h1 align="center">${poits_2}</h1>
	 <div class="card">
			<div class="header">
				${action_2}
			</div>
			
			<div class="card_image">
				<img src="${product_2.photo}" alt="">
			</div>
			
			<div class="card_info">
				<div class="name">
					${product_2.name}
				</div>
				
				<div class="reviews">
					${product_2.raviews} відгуки
				</div>
				
				<div class="price">
					${product_2.price}&#8372;
				</div>
			</div>
		</div>
	</div>
`



products.innerHTML = card + card_2;
console.log(product);