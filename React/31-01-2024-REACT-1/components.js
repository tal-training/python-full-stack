
function Links(){
    return (
        <div className="pictures">
            <a href="#">link1</a>
            <a href="#">link2</a>
            <a href="#">link3</a>
        </div>
    )
}

function Pictures(){
    return (
        <div className="pictures">
        <CatStory/>
        <Cat/>
        <Dog/>
        <DogStory/> 
        <Links/>
        </div>
    )
}

function Dog(){
    return (
        <img src="dog.jpg"/>
    )
}

function Cat(){
    return (
        <img src="cat2.jpg"/>
    )
}

function CatStory(){
    return (
        <p>The cat is a nice animal.</p>
    )
}

function DogStory(){
    return (
        <p>The dog is a nicer animal. He eats Bonzo</p>
    )
}



const main = ReactDOM.createRoot(document.getElementById("main"));

main.render(<Pictures/>)
