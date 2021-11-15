import './Splash.css'
import { NavLink } from 'react-router-dom';
import Footer from '../Footer/Index';
import NavBar from '../NavBar/NavBar';
const Splash = () => {
    return (
        <>

        <NavBar />
        <div className="mainDiv">
        <h1 className = "splashMainHeader"> IGNORED? STAY IN TOUCH </h1>
        <h2 className ="splashSubHeader"> A SITE THAT MAKES IT EASY TO TALK EVERY DAY AND HANG OUT MORE OFTEN</h2>
        <button className="splashButton">
        <NavLink to="/login" className="open">Open Ignored</NavLink>
        </button>

        < Footer/>
        </div>



        </>
    )
}

export default Splash
