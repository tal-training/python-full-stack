const GAME_API="http://127.0.0.1:5000/api/guess"

function setup(){
     i=document.createElement("input");
     i.style.width="20em";
     i.setAttribute("type", "text");
     i.setAttribute("placeholder", "Guess a number between 1 and 10");
     i.id="guess"
     main.appendChild(i);
     document.getElementById("guess").addEventListener("change", ()=>{
          axios.get(`http://127.0.0.1:5000/api/guess?number=${document.getElementById("guess").value}`).then((response)=>{
               document.getElementById("main").innerHTML+=response.data.result;
          })
     })
}

setup();
