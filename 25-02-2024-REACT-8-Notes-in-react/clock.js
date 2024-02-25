

function ReactClock(){
    const [date, setDate]=React.useState(Date())
    React.useEffect(()=>{
        setInterval(()=>setDate(Date), 1000)
    },[])
    return <div>{date}</div>
}

setInterval(() => {
    document.getElementById("clock").innerHTML=Date()
}, 1000);    


const root=ReactDOM.createRoot(document.getElementById("root"))
root.render(<ReactClock/>)

axios.get("http://127.0.0.1:5000/api/notes").then((response)=>{
    console.log(response.data);
    document.getElementById("notes").innerHTML=JSON.stringify(response.data)
})