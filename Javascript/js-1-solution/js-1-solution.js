// 1

let name="tal";
let age=18;

document.getElementById("name").innerHTML=name;
document.getElementById("age").innerHTML=age;

// 2

if (age>20) {
    document.getElementById("age").innerHTML="age is too big";
} else {
    document.getElementById("age").innerHTML="age is too small";
}

// 3

let ages=[18, 21, 32, 45];
for (age of ages) {
    if (age > 20){
        document.getElementById("age").innerHTML+=" " +age+" is too big ";
    }
}

// 4

let names=["tal", "sal", "mal"];
for (name of names) {
    if (name == "tal"){
        document.getElementById("name").innerHTML+="ok";
    }
}

// 5

for (name of names) {
    document.getElementById("name").innerHTML+="<div>"+name+"</div>";
}

// 6

ages = [
    ["tal", 30],
    ["gal", 40],
    ["wal", 20]
]

for (age of ages) {
    document.getElementById("name").innerHTML+="<div>"+ages[0]+"</div>"+"<div>"+ages[1]+"</div>";
}

// 7 

function add(){
    document.getElementById('counter').innerHTML=parseInt(document.getElementById('counter').innerHTML)+1;
}

// 8

function add(){
    if (parseInt(document.getElementById('counter').innerHTML)<10){
        document.getElementById('counter').innerHTML=parseInt(document.getElementById('counter').innerHTML)+1;
    }
}




