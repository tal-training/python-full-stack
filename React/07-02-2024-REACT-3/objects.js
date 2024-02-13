
let contacts=[
    {
        name:"tal",
        email:"tal@tal.com",
        phone:"054-432434"
    },
    {
        name:"gal",
        email:"gal@gal.com",
        phone:"055-432434"
    }
]

function ShowContacts(p){
    return (
        p.contacts.map(i=>
            <div className="contact">
            <div>{i.name}</div>
            <div>{i.email}</div>
            <div>{i.phone}</div>
            </div>    
        )
    )
}


const main=ReactDOM.createRoot(document.getElementById("main"));

const contactsDiv=ReactDOM.createRoot(document.getElementById("contacts"));

contactsDiv.render(<ShowContacts contacts={contacts}/>);
