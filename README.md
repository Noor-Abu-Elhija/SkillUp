# SkillUp - LinkedIn Skills & Course Recommender

## Table of Contents
- [Explanation Video](#Project)
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [FAQ](#FAQ)

## Project Explanation Video
 
📹 [Watch the project explanation](https://drive.google.com/file/d/11TTsCKLtT13R-ce7xijAuW0JAIShRx2L/view?usp=sharing)

## Introduction
Skills play a crucial role in enhancing LinkedIn profiles, making them more visible to recruiters on the leading job-seeking platform. By adding personalized skills and aligning them with market demands, job seekers can significantly improve their chances of securing opportunities. This project aims to analyze users' experience and qualifications, suggest personalized skills for LinkedIn profiles, and recommend relevant courses that help bridge skill gaps and meet industry demands.

The repository contains two main components:
1. **A Python script for scraping skills from Glassdoor.**
2. **A Jupyter Notebook that processes and analyzes the scraped data.**

## Features
- Scrapes relevant skills from Glassdoor job postings.
- Analyzes user experience and qualifications.
- Recommends skills based on experience and qualifications for LinkedIn profiles.
- Identifies the **top 5 required skills** based on location.
- Suggests **relevant courses** for users with minimal to no experience based on their location.

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
   cd <YourRepo> ```

## FAQ

### 1. How do I get a Gemini API key?
Visit [Gemini API](https://api.gemini.com) and sign up for an API key.

### 2. Can I run the project on Windows?
Yes, ensure you have Python installed and follow the installation steps.

### 3. Can I scrap the data when I am signed in to my Glassdoor account?
No, the scraping algorithm works with signed-out sites only.

