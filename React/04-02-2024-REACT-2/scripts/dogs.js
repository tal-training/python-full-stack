
function DogStories(p){
    return (
        <><Title type="dog" title="Dogs"/><div className="pictures border">
            <DogStory image="dog.jpg" age='2' story="Story about a new dog" name="Pluto" url="https://www.google.com" />
            <DogStory image="https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg" age='3' story="Story about a new dog" name="Pluto" url="https://www.google.com" />
            <DogStory image="dog2.jpg" story="Story about a new dog" name="Pluto" url="https://www.google.com" />
        </div></>
    )
}

function DogStory(props){
    return(
        <div>
            <Title type="dog" title="this is a dog" age={props.age}/>
            { !props.image.startsWith("http")?<img src={`images/${props.image}`}/>:<img src={`${props.image}`}/>}
            <p> {props.story}</p>
            <p>His name is {props.name}</p>
            <div className="age">Age: {props.age}</div> 
            <a href={props.url}>Link to {props.name} for adopt</a>
        </div>
    )
}

function Dogs(){
    return(
        <div className="main">
        <Navbar/>
        <DogStories title="new dog title"/>
        </div>
    )
}

const dogs = ReactDOM.createRoot(document.getElementById("dogs"));

dogs.render(<Dogs/>)
