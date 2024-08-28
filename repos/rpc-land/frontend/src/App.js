
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Servers from './components/Servers';
import AddServer from './components/AddServer';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/servers" component={Servers} />
          <Route path="/add-server" component={AddServer} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
