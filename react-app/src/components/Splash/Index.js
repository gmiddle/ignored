import './Splash.css'
import { NavLink } from 'react-router-dom';
const Splash = () => {
    return (
        <>


        <div className="mainDiv">
        <h1 className = "splashMainHeader"> IGNORED? STAY IN TOUCH </h1>
        <h2 className ="splashSubHeader"> A SITE THAT MAKES IT EASY TO TALK EVERY DAY AND HANG OUT MORE OFTEN</h2>
        <button className="splashButton">
        <NavLink to="/login">Open Ignored</NavLink>
        </button>

        </div>



        </>
    )
}

export default Splash
