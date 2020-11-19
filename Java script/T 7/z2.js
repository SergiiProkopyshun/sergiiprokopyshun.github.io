const nums = [ 2, 5, 8];

console.log(nums);
for( i=0; i < 5; i++){
	
const num = Number ( prompt (`Введіть число. №${i+1}`) );
	
	const index = nums.indexOf(num);


   if( index === -1 ){
  nums.push(num);
 }  else {
	 nums[index] = "*";
 }
 
}
console.log(nums);

if( nums.length <= 5 ){
	alert("Перемога")
} else {
		alert("Програв")
}		

	