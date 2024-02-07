
let nums = [1,2,3,3,3,4,5,6,7,10];
let colors=["blue", "green", "red", "yellow"]

function ShowArrayBigger5(p){
    return (
        p.array.filter(i=>i>5).map(i=><div>{i} </div>)
    )
}

function PricesPlusVAT(p){
    return (
        p.array.map(i=><div>{i*1.17}$</div>)
    )
}

function ShowColorsNoRed(p){
    return (
        p.colors.filter(i=>i!="red").map(i=><div>{i}</div>)
    )
}

const main=ReactDOM.createRoot(document.getElementById("main"));

main.render(<ShowColorsNoRed colors={colors}/>);