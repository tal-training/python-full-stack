
const root=ReactDOM.createRoot(document.getElementById("root"))
root.render(<LightBulb state={localStorage.getItem("state") || "Off"}/>)

// on click, save the state in local storage.
function LightBulb(p){
    const [state, setState]=React.useState(p.state || "Off")
    function setBulb(e){
        if (state=="On"){
            localStorage.setItem("state", state)
            setState("Off")
        } 
        if (state=="Off"){
            localStorage.setItem("state", state)
            setState("On")
        }
    }
    return (
        <button onClick={(e)=>setBulb(e)}>{state}</button>
    )
}

function LightBulbs(p){
    return (
        <div>
            <LightBulb state="On"/>
            <LightBulb />
        </div>
    )
}