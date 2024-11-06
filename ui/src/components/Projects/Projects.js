import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import ProjectCard from "./ProjectCards";
import Particle from "../Particle";
import brainyuvce from "../../Assets/Projects/proj2.png";
import ctms from "../../Assets/Projects/proj1.png";

function Projects() {
  return (
    <Container fluid className="project-section">
      <Particle />
      <Container>
        <h1 className="project-heading">
          My Recent <strong className="purple">Works </strong>
        </h1>
        <p style={{ color: "white" }}>
          Here are a few projects I've worked on recently.
        </p>
        <Row style={{ justifyContent: "center", paddingBottom: "10px" }}>
          <Col md={4} className="project-card">
            <ProjectCard
              imgPath={brainyuvce}
              isBlog={false}
              title="BrainyUVCE"
              description="Developed a chatroom web application for educational interaction among students. Implemented user authentication and authorization with Django’s built-in system. Designed a responsive UI using HTML, CSS, and JavaScript. Created RESTful APIs with Django REST Framework for data exchange."
              ghLink="https://github.com/Ganesh57803/BrainyUVCE"
              demoLink="https://brainyuvce-production.up.railway.app/" // replace with your demo link
            />
          </Col>

          <Col md={4} className="project-card">
            <ProjectCard
              imgPath={ctms}
              isBlog={false}
              title="Cricket Tournament Management System"
              description="Developed dashboards for administrators, team managers, and guests. Designed a data management system for teams, players, matches, and results. Implemented access control and real-time updates for match results and standings. Created an intuitive interface with HTML, CSS, Bootstrap, and Django."
              ghLink="https://github.com/Ganesh57803/docker-django-application" // replace with your github link
            />
          </Col>
        </Row>
      </Container>
    </Container>
  );
}

export default Projects;