import React from "react";
import { Col, Row } from "react-bootstrap";
import { DiPython, DiJava, DiJavascript as DiJs } from "react-icons/di";
import { SiPostgresql as SiSql } from "react-icons/si";
import { DiCss3 } from "react-icons/di";
import { SiNumpy, SiPandas } from "react-icons/si";
import { DiReact, DiDjango } from "react-icons/di";
import { SiOpencv } from "react-icons/si";
import { SiDocker } from "react-icons/si";
import { SiGithub } from "react-icons/si";

function Techstack() {
  return (
    <Row style={{ justifyContent: "center", paddingBottom: "50px" }}>
      <Col xs={4} md={2} className="tech-icons">
        <DiPython />
      </Col>
      <Col xs={4} md={2} className="tech-icons">
        <DiJava />
      </Col>
      <Col xs={4} md={2} className="tech-icons">
        <DiJs />
      </Col>
      <Col xs={4} md={2} className="tech-icons">
        <SiSql />
      </Col>
      <Col xs={4} md={2} className="tech-icons">
        <DiCss3 />
      </Col>
      <Col xs={4} md={2} className="tech-icons">
        <SiNumpy />
      </Col>
      <Col xs={4} md={2} className="tech-icons">
        <SiPandas />
      </Col>
      <Col xs={4} md={2} className="tech-icons">
        <DiReact />
      </Col>
      <Col xs={4} md={2} className="tech-icons">
        <DiDjango />
      </Col>
      <Col xs={4} md={2} className="tech-icons">
        <SiOpencv />
      </Col>
      <Col xs={4} md={2} className="tech-icons">
        <SiDocker />
      </Col>
      <Col xs={4} md={2} className="tech-icons">
        <SiGithub />
      </Col>
    </Row>
  );
}

export default Techstack;