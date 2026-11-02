// object desctructring
function MenuComponent({myCurrentPage}){

    return(
        <>
            {myCurrentPage}
            <ul className="menu">
                <li  className={(myCurrentPage=="home")?"active":null}><a href="home">Home</a></li>
                <li  className={(myCurrentPage=="about")?"active":null}><a href="about">About</a></li>
                <li><a href="contact">Contact</a></li>
            </ul>
        </>
    )
}

export default MenuComponent;