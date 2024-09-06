import React from 'react';

const Portfolio = () => {
  return (
    <div>
      <h1>{name}</h1>
      <p>{bio}</p>
      <ul>
        {skills.split(',').map((skill, index) => (
          <li key={index}>{skill}</li>
        ))}
      </ul>
    </div>
  );
};

export default Portfolio;