
const API_URL="https://api.agify.io/?name=robert"

function getCat(){
    let name=document.getElementById("name").value;
    axios.get(`https://api.agify.io/?name=${name}`).then((response)=>{
        if (response.data.age>70){
            document.getElementById("main").innerHTML="you are old";    
        } else {
            document.getElementById("main").innerHTML="you are young";    
        }
    }
    )
}

function getUniversities(){
    let country=document.getElementById("country").value;
    axios.get(`http://universities.hipolabs.com/search?country=${country}`).then((response)=>{
        document.getElementById("main").innerHTML=response.data.map(item=>`<div>${item.name}</div>`)
    }
    )
}

document.getElementById("uniButton").addEventListener("click", ()=>getUniversities());

document.getElementById("country").value="israel";

document.getElementById("country").style.backgroundColor="gray";


