const GAME_API="http://127.0.0.1:5000/api/guess"

function createDiv(data){
     i=document.createElement("input");
     i.style.width=data.width;
     i.setAttribute("type", "text");
     i.setAttribute("placeholder", data.placeholder);
     i.id=data.id;
     main.appendChild(i);
}

function setup(){
     // createDiv({"width":"20em", "placeholder":"guess a number", "id":"guess"})
     // createDiv({"width":"2em", "placeholder":"low", "id":"low"})
     // createDiv({"width":"2em", "placeholder":"high", "id":"high"})
     document.getElementById("guess").addEventListener("change", (e)=>{
          axios.post("http://127.0.0.1:5000/api/guess", {"number":e.target.value}).then((response)=>{
               document.getElementById("main").innerHTML+=response.data.result;
          })
     })
     document.getElementById("high").addEventListener("input", (e)=>{
          axios.post("http://127.0.0.1:5000/api/guess/range", {"low":low.value, "high":high.value}).then((response)=>{
               document.getElementById("main").innerHTML+=response.data.result;
          })
     })
}

setup();
