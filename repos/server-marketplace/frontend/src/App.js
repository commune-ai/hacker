
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';
import ServerList from './components/ServerList';
import CreateServer from './components/CreateServer';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route exact path="/" component={ServerList} />
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/create-server" component={CreateServer} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
