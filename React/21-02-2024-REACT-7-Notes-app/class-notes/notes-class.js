let notes=JSON.parse(localStorage.getItem("notes"))||["Welcome to Notes!", "This is a demo note", "For support contact"]

// ["Welcome to Notes!", "This is a demo note", "For support contact", "new"]

function createNote(value, index){
    let noteElement=document.createElement("textarea");
    noteElement.value=value
    noteElement.onchange=(e)=>{
        if (e.target.value==""){
            notes.push(e.target.value)
        } else {
            notes[index]=e.target.value
        }
        localStorage.setItem("notes", JSON.stringify(notes))
    }
    document.getElementById("main").appendChild(noteElement);
}

function showNotes(){
    notes.map((val,i)=>{
        createNote(val, i)
    })
}

function addNewNote(){
    createNote("")
}

showNotes()

