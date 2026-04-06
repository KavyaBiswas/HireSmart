# HIRESMART: Data-Driven Recruitment Analyzer (Final Version)
# Includes Skill Extraction + Market Analysis + Charts
# Works on your dataset archive.csv
# ============================================================

import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt

# ----------------------------------------------------
# STEP 1: LOAD DATASET
# ----------------------------------------------------
print("\n=== LOADING DATASET ===\n")

df = pd.read_csv("archive.csv")
print("Dataset loaded! Rows:", len(df))
print("Original columns:", df.columns.tolist())

# Convert names to lowercase
df.columns = df.columns.str.lower()

# Rename according to your dataset structure
df = df.rename(columns={
    "job roles": "title",
    "job description": "description",
    "skills": "skills",
    "location": "location"
})

print("Updated columns:", df.columns.tolist())

# ----------------------------------------------------
# STEP 2: CLEAN TEXT (Job Description)
# ----------------------------------------------------
def clean_text(text):
    """Cleans job descriptions by removing symbols & lowercasing."""
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9+ ]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

df["clean_description"] = df["description"].astype(str).apply(clean_text)

# ----------------------------------------------------
# STEP 3: SKILL DICTIONARY
# ----------------------------------------------------
skill_list = [
    "python", "sql", "excel", "tableau", "power bi", "aws", "azure",
    "machine learning", "deep learning", "nlp", "cloud computing",
    "statistics", "java", "react", "node.js", "pandas", "numpy",
    "data analysis", "data visualization"
]

# ----------------------------------------------------
# STEP 4: EXTRACT SKILLS
# ----------------------------------------------------
def extract_skills(text):
    found = []
    for skill in skill_list:
        if skill in text:
            found.append(skill)
    return found

df["extracted_skills"] = df["clean_description"].apply(extract_skills)

print("\n=== SKILL EXTRACTION SAMPLE ===")
print(df[["title", "extracted_skills"]].head(5))

# ----------------------------------------------------
# STEP 5: SKILL FREQUENCY ANALYSIS
# ----------------------------------------------------
all_skills = []
for slist in df["extracted_skills"]:
    all_skills.extend(slist)

skill_freq = Counter(all_skills)

print("\n=== MOST IN-DEMAND SKILLS ===")
for skill, count in skill_freq.most_common(15):
    print(f"{skill.upper():<20} : {count}")

# ----------------------------------------------------
# STEP 6: PLOT → SKILL FREQUENCY CHART (POP-UP)
# ----------------------------------------------------
print("\nGenerating Skill Frequency Chart...")

skills = list(skill_freq.keys())
counts = list(skill_freq.values())

plt.figure(figsize=(12, 6))
plt.bar(skills, counts)
plt.title("Top Skills in Job Market")
plt.xlabel("Skills")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()  # <<< CHART WILL POP UP ON SCREEN
plt.savefig("skill_frequency_chart.png")
plt.close()

print("Saved: skill_frequency_chart.png")

# ----------------------------------------------------
# STEP 7: ROLE-BASED SKILL DEMAND
# ----------------------------------------------------
print("\n=== ROLE-BASED SKILL INSIGHTS ===")

role_map = {}

for _, row in df.iterrows():
    role = row["title"]
    skills = row["extracted_skills"]

    if role not in role_map:
        role_map[role] = Counter()

    role_map[role].update(skills)

for role, cnt in role_map.items():
    print(f"\nRole: {role}")
    print("Top Skills:", dict(cnt.most_common(5)))

# ----------------------------------------------------
# STEP 8: ROLE-WISE CHARTS (POP-UP + SAVE)
# ----------------------------------------------------
print("\nGenerating Role-Wise Skill Charts...")

for role, counter in role_map.items():
    if len(counter) == 0:
        continue

    rskills = list(counter.keys())
    rcounts = list(counter.values())

    plt.figure(figsize=(10, 5))
    plt.bar(rskills, rcounts)
    plt.title(f"Top Skills for: {role}")
    plt.xlabel("Skills")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()  # <<< POP-UP CHART
    filename = f"skills_for_{role.replace(' ', '_')}.png"
    plt.savefig(filename)
    plt.close()

    print("Saved:", filename)

# ----------------------------------------------------
# STEP 9: SKILL GAP ANALYSIS
# ----------------------------------------------------
company_required = [
    "python", "sql", "aws", "tableau",
    "power bi", "machine learning", "cloud computing"
]

market = set(skill_freq.keys())
company = set(company_required)

skill_gap = company - market

print("\n=== SKILL GAP REPORT ===")
print("Skills companies want but market lacks:", list(skill_gap))

# ----------------------------------------------------
# STEP 10: SAVE OUTPUT
# ----------------------------------------------------
df.to_csv("hiresmart_output_final.csv", index=False)

print("\n=== OUTPUT GENERATED ===")
print("1. hiresmart_output_final.csv")
print("2. skill_frequency_chart.png")
print("3. skills_for_<role>.png for each role")
print("\n=== PROJECT COMPLETE ===\n")