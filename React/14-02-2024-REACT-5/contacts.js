const root=ReactDOM.createRoot(document.getElementById("main"))
root.render(<SaveContact/>)

function SaveContact(){
    return (
        <div className="contact">
            <input className="name" onChange={(e)=>localStorage.setItem("name", e.target.value)}></input>
            <input className="age" onChange={(e)=>localStorage.setItem("age", e.target.value)} ></input>
        </div>
    )
}
