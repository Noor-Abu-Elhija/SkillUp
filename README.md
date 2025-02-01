# SkillUp


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)


## Introduction
Skills play a crucial role in enhancing LinkedIn profiles, making them more visible to recruiters on the leading job-seeking platform. By adding personalized skills and aligning them with market demands, job seekers can significantly improve their chances of securing opportunities.

This project aims to analyze users' experience and qualifications, to suggest personalized skills and to recommend relevant courses that help bridge skill gaps and meet industry demands. Our approach ensures that profiles are optimized for better career alignment and job opportunities.

The repository contains two main components:

A Python script for scraping skills from Glassdoor.

A Jupyter Notebook that processes and analyzes the scraped data.

## Features
- Scrapes relevant skills from Glassdoor job postings.
- Analyzes user experience and qualifications.
- recommend skills based on experience and qualifications to LinkedIn profiles
- understand the top 5 required skills based on location
- recommend courses for profiles with minimal to no experience based on their location
- 
## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required Python packages (listed in `imports.txt`)
- Jupyter Notebook 

### Install Dependencies
Run the following command to install the necessary dependencies:
```bash
pip install -r imports.txt
```
Clone the Repository

### Clone the Repository
To get started, clone this repository to your local machine:

```bash
git clone https://github.com/Noor-Abu-Elhija/SkillUp.git
cd SkillUp
```
## Running the Project

### Running the Python Script
To execute the script for scraping skills from Glassdoor, use the following command:

```bash
python extract_skills.py
```
### Running the Jupyter Notebook
To analyze and process the scraped data, open a terminal or command prompt, navigate to the project directory, and launch Jupyter Notebook:

```bash
cd SkillUp
SkillUp.ipynb
```
you should start running the netbook cells in order
## Configuration

To configure the project, locate the section in the script where `API_KEY` is mentioned replace it with your Gemini API key, and update the section where `PATH` is mentioned with the desired file path for saving the dataset:

```python
API_KEY = "your-gemini-api-key-here"
PATH = "/your/desired/path/to/save/dataset"
```

## Contributing

We welcome contributions to improve this project! Follow these steps to contribute:

1. **Fork the Repository**: Click the "Fork" button on the top right of the repository page to create your own copy.  
2. **Clone Your Fork**: Clone your forked repository to your local machine:  
   ```bash
   git clone https://github.com/<YourUsername>/<YourRepo>.git
   cd <YourRepo>
 ```
