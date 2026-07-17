from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_ai_report(student_data, predicted_score):

    prompt = f"""
You are an experienced academic advisor.

Student Details

Study Hours: {student_data['StudyHours']} hours/day
Attendance: {student_data['Attendance']}%
Previous Score: {student_data['PreviousScore']}
Assignments Completed: {student_data['Assignments']}
Internet Available: {student_data['InternetAvailable']}
Parent Education: {student_data['ParentEducation']}
Sleep Hours: {student_data['SleepHours']} hours
Extracurricular Activities: {student_data['ExtracurricularActivities']}
Daily Screen Time: {student_data['DailyScreenTime']} hours
Family Income: {student_data['FamilyIncome']}

Predicted Final Score: {predicted_score:.2f}

Generate the response in **Markdown**.

Follow this exact structure.

## 📊 Performance Analysis
Write a short paragraph.

## ✅ Strengths
- Point 1
- Point 2
- Point 3

## ⚠️ Weaknesses
- Point 1
- Point 2
- Point 3

## 💡 Personalized Recommendations
- Recommendation 1
- Recommendation 2
- Recommendation 3
- Recommendation 4
- Recommendation 5

## 📅 Weekly Study Plan

### Monday
- Task 1
- Task 2
- Task 3

### Tuesday
- Task 1
- Task 2
- Task 3

### Wednesday
- Task 1
- Task 2
- Task 3

### Thursday
- Task 1
- Task 2
- Task 3

### Friday
- Task 1
- Task 2
- Task 3

### Saturday
- Task 1
- Task 2
- Task 3

### Sunday
- Task 1
- Task 2
- Task 3

## 🎯 Motivation
Write one motivational paragraph.

Rules:
- Use proper Markdown.
- Use bullet points under every day.
- Do NOT write all days in one paragraph.
- Every day must have at least 3 bullet points.
- Keep each bullet short (one sentence).

## 🎯 Motivation
(A short motivational paragraph)

Keep the language simple and practical.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert academic advisor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.6,
        max_completion_tokens=1000
    )

    return response.choices[0].message.content