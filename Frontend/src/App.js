import logo from "./logo.svg";
import "./App.css";
import Login from "./pages/Login";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Dashboard from "./pages/Dashboard"
import Page2 from "./pages/Page2"
import Page1 from "./pages/Page1"

function App() {
  return (
    <div>
      <BrowserRouter>
        <Route exact path="/login" component={Login} />
		<Route exact path="/" component={Dashboard} />
    <Route exact path="/Page2" component={Page2} />
    <Route exact path="/Page1" component={Page1} />
      </BrowserRouter>
    </div>
  );
}

export default App;
