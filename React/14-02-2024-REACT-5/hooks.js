// Component that counts how many times it is clicked

const root=ReactDOM.createRoot(document.getElementById("main"))
root.render(<CounterMax/>)

function CounterMax(){
    console.log("hi");
    const [num, setNum]=React.useState(0) // num=5
    const [max, setMax]=React.useState(10) // num=5
    function checkNum(){
        if (num<max){
            setNum(num+1)
        } else {
        }
    }
    return (
        <div className="container">
            <input placeholder="enter maximum clicks" onChange={(e)=>setMax(e.target.value)}></input>
            <div className="display">{num}</div>
            <button onClick={checkNum} >Click Me</button> 
        </div>
    )
}

function Counter(p){
    console.log("hi");
    const [num, setNum]=React.useState(0) // num=5
    const [message, setMessage]=React.useState("") // num=5
    function checkNum(){
        if (num<p.max){
            setNum(num+1)
        } else {
            setMessage("too many clicks")
        }
    }
    return (
        <div className="container">
            <div className="display">{num}</div>
            <div className="clickStat">{message}</div>
            <button onClick={checkNum} >Click Me</button> 
        </div>
    )
}



