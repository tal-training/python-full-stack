function createDiv(data){
     let d=document.createElement("div");
     d.style.backgroundColor=data.color;
     d.style.height=data.height;
     d.style.width=data.width;
     d.id=data.id;
     data.parent.appendChild(d);     
     document.getElementById(data.id).innerHTML+=document.getElementById(data.id).parentElement.id
}


let d=document.createElement("div");
d.style.backgroundColor="lightblue";
d.style.height="200px";
d.style.width="200px";
d.id="blueDiv";

let y=document.createElement("div");
y.style.backgroundColor="yellow";
y.style.height="100px";
y.style.width="100px";
y.id="yellowDiv";

d.appendChild(y);
document.body.appendChild(d);

document.getElementById("blueDiv").innerHTML+=document.getElementById("blueDiv").parentElement;

document.getElementById("yellowDiv").innerHTML=document.getElementById("yellowDiv").parentElement;

createDiv({
     color:"green",
     height:"50px",
     width:"50px",
     id:"greenDiv",
     parent:document.getElementById("yellowDiv")
})
