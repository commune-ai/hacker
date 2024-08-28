
import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/bounties">Bounties</Link></li>
          <li><Link to="/create-bounty">Create Bounty</Link></li>
          <li><Link to="/app-development">App Development</Link></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
