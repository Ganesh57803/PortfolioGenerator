import React from 'react';
const Portfolio = () => {
  return (
    <div>
      <h1>test2</h1>
      <p>new bio loaded</p>
      <ul>
        {user_details.skills.split(",").map(skill => <li key={skill}>{skill}</li>)}
      </ul>
    </div>
  );
};
export default Portfolio;
