import React, { Component } from "react";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";
import { BrowserRouter as Router, Switch, Route, Link, Redirect} from "react-router-dom";

export default class HomePage extends Component {
    constructor(props) {
        super(props); // Calls the constuctor of Component; parent class constructor
    }

    render() {
        return (
            <Router>
                <Routes>
                    <Route path='/join' element={<RoomJoinPage />}/>
                    <Route path='/create' element={<CreateRoomPage />}/>
                    <Route path='/' element={<p> This is the Home Page </p>}/>
                </Routes>
            </Router>
        );
    }
}