import React, { Component,Fragment } from 'react'
import ReactDOM from "react-dom"
import Header from "./layout/Header"
import Dashboard from "./divers/Dashboard"
export default class App extends Component {
  render() {
    return (
      <Fragment>
        <Dashboard /> 
      </Fragment>

    )
  }
}
ReactDOM.render(<App />,document.getElementById("app"));