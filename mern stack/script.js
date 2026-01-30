// console.log("Hello, World!");
// const age=58;
// if (age>=18){
//     console.log("You are an adult you can vote.");
//     if(age>+50){
//         console.log("You are eligible for senior citizen benefits.");
//     }
// }
// else{
//     console.log("You are a minor.");
// }

// const gradee=90;
// if(gradee>=90){
//     console.log("You got an A+ grade.");
// }else if (gradee>=80){
//     console.log("You got an A grade.");
// }else if (gradee>=70){
//     console.log("You got a B+ grade.");
// }else if (gradee>=60){
//     console.log("You got a B grade.");
// }else{
//     console.log("You need to work harder.");
// }
// console.log("End of the program.");
// const ag="25";
// ag>=18 ? console.log("You are an adult.") : console.log("You are a minor.");

// // looping statemets
// for(let i=0;i<=5;i++){    //for loop
//     console.log("rohan",i);
// }
// count=0;
// while(count<5){
//     console.log("count value is:",count);
//     count++;
//     if(count===3){
//         break;
//     }
// }
// named function
// function sum(a,b){
//     sum=(a+b);
//     return sum;
// }
// console.log(sum(5,10));

// // ananymous function
// // const greet = function(){
// //     console.log("Hello from anonymous function");
// // }
// // greet();

// // // arrow function in Es6
// // const greet1=()=>{
// //     console.log("Hello from arrow function");
// // }
// // greet1();

// // arrow function cocepts
// // const squ=(n)=> n*n;
// // console.log(squ(5));

// // const calulate=(a,d,operation)=>{
// //     return operation(a,d);
// // }
// // console.log(calulate(10,5,(x,y)=>x+y)); // addition
// // console.log(calulate(10,5,(x,y)=>x-y)); // subtraction

// // console.log("one")
// // console.log("two")
// // console.log("three")
// // //content related to synchorinazition
// // setTimeout(function(){
// //     console.log("four")
// // },3000);

// // function getCandies(){
// //     setTimeout(function(){
// //         console.log("Here are your candies!")
// //     },5000);
// // }
// // getCandies();
// // // call back function example
// // function gree(name,callback){
// //     console.log("hello",name);
// //     callback();
// // }
// // function saybye(){
// //     console.log("bye!");
// // }
// // gree("hari",saybye);
// // promise example with synchorinization
// const ticket=new Promise(function(res,rej){
//     const seatAvailable=true;
//     if(seatAvailable){
//         res("Ticket booked successfully!");
//     }else{
//         rej("Ticket booking failed. No seats available.");
//     }
// })
// ticket.then((data)=>{
//     console.log("on success:",data );
// }).catch((data)=>{
//     console.log("on failure:",data);
// });

// // async await example
// function getCandies(){
//     return new Promise((res,rej) =>{
//          setTimeout(()=>{
//             res("Here are your candies!");
//         },3000);
//     });
// }
// console.log(getCandies());
//accesing the html elements by dom
console.log(document.body);
const bodyBackground=document.body;
bodyBackground.style.backgroundColor="lightblue";

// accesing by id name
const box4=document.getElementById("box-4");
box4.style.backgroundColor="red";
box4.style.color="white";

//accesing by tag name
const h1=document.getElementsByTagName("h1");
 console.log(h1);

 
