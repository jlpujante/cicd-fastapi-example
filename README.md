# cicd-fastapi-example

This repository contains a skeleton code and configuration files necessary for deploying a basic FastAPI application using an automated CI/CD pipeline.

## Folder Structure
- `.github/workflows/:` This directory houses the GitHub Actions workflow files defining the CI/CD pipeline.
- `src/:` Contains the main code files for the FastAPI application.
- `tests/:` Includes the test code files to verify the functionality of the FastAPI application.

  
## Pipeline Overview
The pipeline is triggered by events like code pushes or pull requests. It automatically builds, tests, and deploys the FastAPI application to an instance in Render site. The process includes infrastructure configuration, code deployment, and automated testing.

## Get Started
1. Create a python virtual environment to install the dependences using:
```bash
  pip install -r requirements.txt
```
2. Run locally the server:
```bash
  uvicorn.exe --app-dir src main:app --reload
```
3. Run the tests locally:
```bash
  pytest
```
4. Configure the pipeline by modifying the workflows in the .github/workflows directory to match your specific deployment requirements.
5. Create the github secrets defined in the github action file.
6. Customize the FastAPI application in the app directory to suit your project need
   
Feel free to explore the repository for more details on the pipeline setup and configuration.

