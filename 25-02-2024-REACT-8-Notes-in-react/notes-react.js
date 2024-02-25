const root = ReactDOM.createRoot(document.getElementById("root"))

let notes = ["note1", "note2", "note3", ""]

if (localStorage.getItem("notes")){
    notes=JSON.parse(localStorage.getItem("notes")) // Can you do getItem only once?
} else {
    localStorage.setItem("notes", JSON.stringify(notes))
}

root.render(<Notes notes={notes}/>)

function Note(p){
    const [text, setText]=React.useState(p.text)
    const index=React.useRef(p.index)
    function save(){
        let tempArray=JSON.parse(localStorage.getItem("notes"))
        tempArray[index.current]=text
        localStorage.setItem("notes", JSON.stringify(tempArray))
    }
    return (
            <textarea onKeyPress={(e)=>{
                if (e.key=="Enter"){
                    save()    
                }
            }} onChange={(e)=>setText(e.target.value)}>{text}</textarea>
    )
}

function Notes(p){
    const [myNotes, setMyNotes]=React.useState(p.notes)
    return (
        <div className="notes">
            {myNotes.map((value,index)=><Note text={value} index={index}/>)}
            <button onClick={()=>{
                setMyNotes([...myNotes, ""])
            }}>Add</button>
        </div>
    )
}

