import React from 'react';
const Portfolio = () => {
  return (
    <div>
      <h1>suprita</h1>
      <p>newbio</p>
      <ul>
        {user_details.skills.split(",").map(skill => <li key={skill}>{skill}</li>)}
      </ul>
    </div>
  );
};
export default Portfolio;
