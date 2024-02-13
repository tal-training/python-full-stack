

function CatStories(p){
    return (
        <><Title type="cat" /><div className="pictures border">
            <CatStory image="cat1.jpg" story="Story about a new cat" name="Kitty" url="https://www.google.com/q=cat" />
            <CatStory image="cat2.jpg" story="Story about another cat" name="Mitzy" url="https://www.google.com/q=cats" />
        </div></>
    )
}
function CatStory(props){
    return(
        <div>
            <img src={`images/${props.image}`}/>
            <p> {props.story}</p>
            <p>His name is {props.name}</p>
            <a href={props.url}>Link to {props.name} for adopt</a>
        </div>
    )
}


function Cats(){
    return(
        <div className="main">
        <Navbar/>
        <CatStories title="nice cats" />
        </div>
    )
}

const dogs = ReactDOM.createRoot(document.getElementById("cats"));

dogs.render(<Cats/>)
