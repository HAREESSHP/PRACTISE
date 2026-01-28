console.log("Hello, World!");
const age=58;
if (age>=18){
    console.log("You are an adult you can vote.");
    if(age>+50){
        console.log("You are eligible for senior citizen benefits.");
    }
}
else{
    console.log("You are a minor.");
}

const gradee=90;
if(gradee>=90){
    console.log("You got an A+ grade.");
}else if (gradee>=80){
    console.log("You got an A grade.");
}else if (gradee>=70){
    console.log("You got a B+ grade.");
}else if (gradee>=60){
    console.log("You got a B grade.");
}else{
    console.log("You need to work harder.");
}
console.log("End of the program.");
const ag="25";
ag>=18 ? console.log("You are an adult.") : console.log("You are a minor.");

// looping statemets
for(let i=0;i<=5;i++){    //for loop
    console.log("rohan",i);
}
count=0;
while(count<5){
    console.log("count value is:",count);
    count++;
    if(count===3){
        break;
    }
}

function sum(a,b){
    sum=(a+b);
    return sum;
}
console.log(sum(5,10));