from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from pathlib import Path
import shutil
import os

def generate_portfolio(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        summary = request.POST.get('summary')
        github = request.POST.get('github') 
        linkedin = request.POST.get('linkedin')
        instagram = request.POST.get('instagram')
        city = request.POST.get('city')
        country = request.POST.get('country')
        college = request.POST.get('college')
        branch = request.POST.get('branch')
        hobbies1 = request.POST.get('hobbies1')
        hobbies2 = request.POST.get('hobbies2')
        hobbies3 = request.POST.get('hobbies3')
        

        # Path to your template React folder
        react_folder_path = Path('ui')
        updated_folder_path = Path('ui_updated')

        # Copy the template folder to a new directory
        if updated_folder_path.exists():
            shutil.rmtree(updated_folder_path)
        shutil.copytree(react_folder_path, updated_folder_path)

        # Update the Home.js React component with form data
        component_file_path = updated_folder_path / 'src' / 'components' / 'Home' / 'Home.js'
        with open(component_file_path, 'w', encoding='utf-8') as file:
            file.write(f'''
            import React from "react";
            import {{ Container, Row, Col }} from "react-bootstrap";
            import homeLogo from "../../Assets/home-main.svg";
            import Particle from "../Particle";
            import Home2 from "./Home2";
            import Type from "./Type";

            function Home() {{
              return (
                <section>
                  <Container fluid className="home-section" id="home">
                    <Particle />
                    <Container className="home-content">
                      <Row>
                        <Col md={{7}} className="home-header">
                          <h1 style={{{{ paddingBottom: 15 }}}} className="heading">
                            Hi There!{{" "}}
                            <span className="wave" role="img" aria-labelledby="wave">
                              👋🏻
                            </span>
                          </h1>

                          <h1 className="heading-name">
                            I'M
                            <strong className="main-name"> {name}</strong>
                          </h1>

                          <div style={{{{ padding: 50, textAlign: "left" }}}}>
                            <Type />
                          </div>
                        </Col>

                        <Col md={{5}} style={{{{ paddingBottom: 20 }}}}>
                          <img
                            src={{homeLogo}}
                            alt="home pic"
                            className="img-fluid"
                            style={{{{ maxHeight: "450px" }}}}
                          />
                        </Col>
                      </Row>
                    </Container>
                  </Container>
                  <Home2 />
                </section>
              );
            }}

            export default Home;
            ''')
        component_file_path = updated_folder_path / 'src' / 'components' / 'Home' / 'Home2.js'
        with open(component_file_path, 'w', encoding='utf-8') as file:
            file.write(f'''
                       import React from "react";
import {{ Container, Row, Col }} from "react-bootstrap";
import myImg from "../../Assets/avatar.svg";
import Tilt from "react-parallax-tilt";
import {{
  AiFillGithub,
  AiFillInstagram,
}} from "react-icons/ai";
import {{ FaLinkedinIn }} from "react-icons/fa";

function Home2() {{
  return (
    <Container fluid className="home-about-section" id="about">
      <Container>
        <Row>
          <Col md={{8}} className="home-about-description">
            <h1 style={{{{ fontSize: "2.6em" }}}}>
              LET ME <span className="purple"> INTRODUCE </span> MYSELF
            </h1>
            <p className="home-about-body"> {summary} 
            </p>
          </Col>
          <Col md={{4}} className="myAvtar">
            <Tilt>
              <img src={{myImg}} className="img-fluid" alt="avatar" />
            </Tilt>
          </Col>
        </Row>
        <Row>
          <Col md={{12}} className="home-about-social">
            <h1>FIND ME ON</h1>
            <p>
              Feel free to <span className="purple">connect </span>with me
            </p>
            <ul className="home-about-social-links">
              <li className="social-icons">
                <a
                  href="{github}"
                  target="_blank"
                  rel="noreferrer"
                  className="icon-colour  home-social-icons"
                >
                  <AiFillGithub />
                </a>
              </li>

              <li className="social-icons">
                <a
                  href="{linkedin}"
                  target="_blank"
                  rel="noreferrer"
                  className="icon-colour  home-social-icons"
                >
                  <FaLinkedinIn />
                </a>
              </li>
              <li className="social-icons">
                <a
                  href="{instagram}"
                  target="_blank"
                  rel="noreferrer"
                  className="icon-colour home-social-icons"
                >
                  <AiFillInstagram />
                </a>
              </li>
            </ul>
          </Col>
        </Row>
      </Container>
    </Container>
  );
}}
export default Home2;
''')
        component_file_path = updated_folder_path / 'src' / 'components' / 'Home' / 'AboutCard.js'
        with open(component_file_path, 'w', encoding='utf-8') as file:
            file.write(f'''
                       import React from "react";
import Card from "react-bootstrap/Card";
import {{ ImPointRight }} from "react-icons/im";

function AboutCard() {{
  return (
    <Card className="quote-card-view">
      <Card.Body>
        <blockquote className="blockquote mb-0">
          <p style={{{{ textAlign: "justify" }}}}>
            Hi Everyone, I am <span className="purple">{name}</span>
            from <span className="purple">{city}, {country}.</span>
            <br />
            I am currently a student at {college}, pursuing a Bachelor of Technology (B.Tech) in {branch}.
            <br />
            I have a strong passion for building innovative projects and contributing to the tech community.
            <br />
            <br />
            Apart from coding, some other activities that I love to do!
          </p>
          <ul>
            <li className="about-activity">
              <ImPointRight /> {hobbies1}
            </li>
            <li className="about-activity">
              <ImPointRight /> {hobbies2}
            </li>
            <li className="about-activity">
              <ImPointRight /> {hobbies3}
            </li>
          </ul>

          <p style={{{{ color: "rgb(155 126 172)" }}}}>
          "Everything you can imagine is real."</p>
          <footer className="blockquote-footer">Pablo Picasso</footer>
        </blockquote>
      </Card.Body>
    </Card>
  );
}}

export default AboutCard;
''')
       

        # Create a zip file of the updated React app folder
        zip_file_path = '/path/to/download/updated-react-app.zip'
        shutil.make_archive(zip_file_path.replace('.zip', ''), 'zip', updated_folder_path)

        # Send the zip file as a response for download
        with open(zip_file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/zip')
            response['Content-Disposition'] = f'attachment; filename={os.path.basename(zip_file_path)}'
            return response

    return render(request,'index.html')
