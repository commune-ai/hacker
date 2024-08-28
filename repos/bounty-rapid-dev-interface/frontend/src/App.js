
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Home from './components/Home';
import BountyList from './components/BountyList';
import BountyCreate from './components/BountyCreate';
import AppDevelopment from './components/AppDevelopment';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/bounties" component={BountyList} />
          <Route path="/create-bounty" component={BountyCreate} />
          <Route path="/app-development" component={AppDevelopment} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
