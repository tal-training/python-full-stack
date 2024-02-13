function Image(props){
    return (
        <img src={props.filename}/>
    )
}

function DogStories(){
    return (
        <div className="pictures border">
            <DogStory image="dog.jpg" story="Story about a new dog" name="Pluto" url="https://www.google.com"/>
            <DogStory image="https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg" story="Story about a new dog" name="Pluto" url="https://www.google.com"/>
            <DogStory image="dog2.jpg" story="Story about a new dog" name="Pluto" url="https://www.google.com"/>
        </div>
    )
}

function ImageStories(){
    return (
        <div className="pictures border">
            <DogStory image="dog.jpg" story="Story about a new dog" name="Pluto" url="https://www.google.com"/>
            <DogStory image="cat2.jpg" story="Story about a new dog" name="Pluto" url="https://www.google.com"/>
            <ImageStory filename="dog.jpg" story="Story about my dog"/>
            <ImageStory filename="cat2.jpg" story="Story about my cat"/>
        </div>
    )
}

function DogStory(props){
    return(
        <div>
            <img src={props.image}/>
            <p> {props.story}</p>
            <p>His name is {props.name}</p>
            <a href={props.url}>Link to dog for sale</a>
        </div>
    )
}

function ImageStory(props){
    return (
        <div>
            <img src={props.filename}/>
            <p>{props.story}</p>
        </div>
    )
}

const main = ReactDOM.createRoot(document.getElementById("main"));

main.render(<DogStories/>)

