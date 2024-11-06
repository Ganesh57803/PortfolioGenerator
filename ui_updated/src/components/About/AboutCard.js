import React from "react";
import Card from "react-bootstrap/Card";
import { ImPointRight } from "react-icons/im";

function AboutCard() {
  return (
    <Card className="quote-card-view">
      <Card.Body>
        <blockquote className="blockquote mb-0">
          <p style={{ textAlign: "justify" }}>
            Hi Everyone, I am <span className="purple">Ganesh Ramesha Markala </span>
            from <span className="purple">Bengaluru, India.</span>
            <br />
            I am currently a student at University Visvesvaraya College of Engineering, pursuing a Bachelor of Technology (B.Tech) in Artificial Intelligence and Machine Learning.
            <br />
            I have a strong passion for building innovative projects and contributing to the tech community.
            <br />
            <br />
            Apart from coding, some other activities that I love to do!
          </p>
          <ul>
            <li className="about-activity">
              <ImPointRight /> Graphic Designing
            </li>
            <li className="about-activity">
              <ImPointRight /> Video Editing
            </li>
            <li className="about-activity">
              <ImPointRight /> Cricket
            </li>
          </ul>

          <p style={{ color: "rgb(155 126 172)" }}>
          "Everything you can imagine is real."</p>
          <footer className="blockquote-footer">Pablo Picasso</footer>
        </blockquote>
      </Card.Body>
    </Card>
  );
}

export default AboutCard;