import React, { component } from "react";
import {render} from "react-dom";

export default class App extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return <h1>Testing React code</h1>;
    }
}

const appDiv = document.getElementbyId("app");
render(<App/>, appDiv);