let total = 0;

//Запитання
const otvet_1 = prompt("Як звати батька Івана Франка?"); //Запитання_1

if( otvet_1 == "Яків" || otvet_1 == "Яків"){
		total = total + 2; 
}

const otvet_2 = prompt("Коли народився батько Тараса Шевченка?"); //Запитання_2

if( otvet_2 == "1781" || otvet_2 == "1781р"){
		total = total + 2; 
}

const otvet_3 = prompt("В якому році народилась Ліна Костенко?"); //Запитання_3

if( otvet_3 == "1930р" || otvet_3 == "1930"){
		total = total + 2; 
}

const otvet_4 = prompt("Коли народилася Леся Українка?"); //Запитання_4

if( otvet_4 == "25 лютого" || otvet_4 == "1871"){
		total = total + 2; 
}

const otvet_5 = prompt("Коли народився Зеленський?"); //Запитання_5

if( otvet_5 == "25 січня" || otvet_5 == "1978"){
		total = total + 2; 
}

const otvet_6 = prompt("Коли народився Порошенко?"); //Запитання_6

if( otvet_6 == "26 вересня" || otvet_6 == "1965"){
		total = total + 2; 
}

const otvet_7 = confirm("Ти дивишся YouTube?"); //Запитання_7

if( otvet_7 == "Так" || otvet_7 == true){
		total = total + 2; 
}

const otvet_8 = confirm("Ти дальтонік?"); //Запитання_8

if( otvet_8 == "Ні" || otvet_8 == false){
		total = total + 2; 
}

const otvet_9 = prompt("Коли вийшлов Minecraft?"); //Запитання_9

if( otvet_9 == "2012р" || otvet_9 == "2012"){
		total = total + 2; 
}

const otvet_10 = prompt("Коли вийшла GTA 5?"); //Запитання_10

if( otvet_10 == "17 вересня" || otvet_10 == "2013"){
		total = total + 2; 
}




//Виводим результат
if( total < 6 ){
//Провал
alert (`Тест не складено. ${total}`)
} else if( total >= 6 && total <= 9 ){
//Задовільно
  alert (`Тест складено задовільно. ${total}`)	
} else if( total >=10 ){
//Відміно
  alert (`Тест складено відмінно. ${total}`)
}