
let contacts=[
    {
        name:"tal",
        email:"tal@tal.com",
        phone:"054-432434", 
        city:"haifa"
    },
    {
        name:"gal",
        email:"gal@gal.com",
        phone:"055-432434",
        city:"telaviv"
    }
]

function ShowContacts(p){
    return (
        p.contacts.filter(i=>i.email.startsWith("gal")).map(i=>
            <div className="contact">
            <div>{i.name}</div>
            <div>{i.email}</div>
            <div>{i.phone}</div>
            <div>{i.city}</div>
            </div>    
        )
    )
}


const main=ReactDOM.createRoot(document.getElementById("main"));

const contactsDiv=ReactDOM.createRoot(document.getElementById("contacts"));

contactsDiv.render(<ShowContacts contacts={contacts}/>);
