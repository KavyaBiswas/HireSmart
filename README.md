# HireSmart
HIRESMART is a data-driven recruitment analytics tool that extracts and analyzes job market trends to identify in-demand skills and role-specific requirements. It delivers actionable insights through visualizations and skill gap analysis, helping recruiters make smarter hiring decisions and candidates align with industry needs.


HIRESMART: Data-Driven Recruitment Analyzer
HIRESMART is a data analytics project that leverages job market data to extract insights about in-demand skills, role-based requirements, and skill gaps. It helps students, job seekers, and recruiters make informed decisions using data.


📌 Project Overview
The project analyzes a dataset of job listings (archive.csv) and performs:
✅ Skill extraction from job descriptions
📊 Market demand analysis for skills
📈 Visualization of top skills
👩‍💻 Role-based skill insights
⚠️ Skill gap identification


🛠️ Tech Stack
Python
Pandas – Data processing
Matplotlib – Data visualization
Regex (re) – Text cleaning & processing
Collections (Counter) – Frequency analysis


⚙️ Features
🔍 1. Data Cleaning
Removes noise from job descriptions
Standardizes text for accurate analysis
🧠 2. Skill Extraction
Uses a predefined skill dictionary
Extracts relevant skills from job descriptions
📊 3. Skill Demand Analysis
Identifies most in-demand skills in the market
Displays frequency of each skill
📈 4. Visualization
Generates bar charts for:
Overall skill demand
Role-wise skill demand
👨‍💼 5. Role-Based Insights
Shows top skills required for each job role
⚠️ 6. Skill Gap Analysis
Compares market skills vs company-required skills
Identifies missing/high-demand skills



📂 Project Structure

HIRESMART/
│── archive.csv
│── hiresmart.py
│── hiresmart_output_final.csv
│── skill_frequency_chart.png
│── skills_for_<role>.png
│── README.md


📊 Output
The project generates:
📄 hiresmart_output_final.csv → Cleaned dataset with extracted skills
📊 skill_frequency_chart.png → Overall skill demand
📈 skills_for_<role>.png → Role-based skill charts


📊 Dataset
The dataset used in this project is publicly available on Kaggle:
🔗 Direct Access: https://www.kaggle.com/datasets/kavyabiswas/hiresmart-dataset⁠�


📁 Dataset Contents
The dataset includes structured job listing data with the following fields:
🧑‍💼 Job Roles
📝 Job Descriptions
🛠️ Skills
📍 Location


🎯 Purpose
This dataset is curated to enable:
📊 Job market trend analysis
📈 In-demand skill identification
🧠 NLP-based skill extraction
🎯 Recruitment analytics and insights


⚠️ Usage Note
Due to GitHub file size limitations, the dataset is hosted externally on Kaggle. Please download it from the link above and place it in the project directory before running the code.


HIRESMART/
│── archive.csv   ← place dataset here
│── hiresmart.py


🎯 Use Cases
📚 Students → Identify trending skills to learn
💼 Job Seekers → Understand market demand
🏢 Recruiters → Analyze hiring trends
📊 Data Analysts → Practice real-world data analysis


🚀 Future Enhancements
🔮 Machine Learning-based skill prediction
🌐 Web dashboard using Streamlit/Flask
🤖 NLP-based advanced skill extraction
📡 Real-time job data integration (LinkedIn, Indeed APIs)


🙌 Contribution
Contributions are welcome!
Feel free to fork this repo and submit a pull request.


📄 License
This project is open-source and available under the MIT License.


👩‍💻 Author
Kavya Biswas
B.Tech CSE (Data Science)
