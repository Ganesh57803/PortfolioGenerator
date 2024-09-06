import os
import shutil
from django.http import HttpResponse
from django.shortcuts import render
from .models import UserDetails

def generate_portfolio(request):
    if request.method == 'POST':
        user_details = UserDetails.objects.create(
            name=request.POST['name'],
            bio=request.POST['bio'],
            skills=request.POST['skills'],
            # Add more fields as needed
        )
        
        # Generate the React project folder
        project_folder = os.path.join('path/to/project/folder', user_details.name)
        try:
            os.makedirs(project_folder, exist_ok=True)
        except OSError as e:
            return HttpResponse(f"Error creating project folder: {e}", status=500)
        
        # Copy the React template to the project folder
        try:
            shutil.copytree('./ui', project_folder, dirs_exist_ok=True)
        except shutil.Error as e:
            return HttpResponse(f"Error copying template: {e}", status=500)
        
        # Populate the React template with user details
        app_js_path = os.path.join(project_folder, 'src', 'App.js')
        try:
            os.makedirs(os.path.dirname(app_js_path), exist_ok=True)
            with open(app_js_path, 'w') as f:
                f.write('import React from \'react\';\n')
                f.write('const Portfolio = () => {\n')
                f.write('  return (\n')
                f.write('    <div>\n')
                f.write(f'      <h1>{user_details.name}</h1>\n')
                f.write(f'      <p>{user_details.bio}</p>\n')
                f.write('      <ul>\n')
                f.write('        {user_details.skills.split(",").map(skill => <li key={skill}>{skill}</li>)}\n')
                f.write('      </ul>\n')
                f.write('    </div>\n')
                f.write('  );\n')
                f.write('};\n')
                f.write('export default Portfolio;\n')
        except OSError as e:
            return HttpResponse(f"Error writing to App.js: {e}", status=500)
        
        # Replace the existing app/new/app.js with the newly created App.js
        new_app_js_path = os.path.join('core', 'ui','src', 'app.js')
        try:
            shutil.copy(app_js_path, new_app_js_path)
        except shutil.Error as e:
            return HttpResponse(f"Error replacing app.js: {e}", status=500)
        
        return HttpResponse('Portfolio generated successfully!')
    return render(request, 'index.html')