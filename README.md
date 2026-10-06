# 📚 AI Study Planner

### Your Personalized AI-Powered Study Companion

AI Study Planner is a web-based study planning application that uses **Google Gemini AI** to create personalized study plans based on a student's subjects, exam date, available study hours, current level, weak subjects, strong subjects, and preferred study style.

The application also tracks study progress and provides a dashboard to help students understand their preparation status.

---

## ✨ Features

### 🤖 AI Study Plan Generation

Generate a personalized study plan using Google Gemini AI based on:

* Subjects
* Exam date
* Daily study hours
* Current skill level
* Weak subjects
* Strong subjects
* Study preference

### 📊 Progress Tracking

* Mark study tasks as completed
* Automatic progress percentage
* Progress bar
* Completed task count
* Today's task highlighting
* Completion status saved using browser `localStorage`

### 🎯 Personalized Planning

The AI adapts the study plan according to:

* Beginner / Intermediate / Advanced level
* Weak subjects
* Strong subjects
* Theory preference
* Coding / Practice preference
* Mixed learning preference
* Revision preference

### 📈 Student Dashboard

The dashboard provides:

* ⏳ Exam countdown
* ⭐ Today's task
* 📊 Overall progress
* 📚 Subject-wise progress
* ⏱️ Study statistics
* 🎯 Study profile
* 🤖 AI-generated study summary
* 📝 Complete study plan

### 💾 Local Progress Storage

Study completion data is stored in the browser using `localStorage`, so progress remains available after refreshing the page.

---

## 🛠️ Technologies Used

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| Python            | Backend programming             |
| Flask             | Web framework                   |
| Google Gemini API | AI study-plan generation        |
| HTML5             | Web structure                   |
| CSS3              | Styling and responsive UI       |
| JavaScript        | Dashboard and progress logic    |
| LocalStorage      | Progress persistence            |
| python-dotenv     | Environment variable management |

---

## 📂 Project Structure

```text
AI-Study-Planner/
│
├── app.py
├── planner.py
├── gemini_service.py
├── test_gemini.py
├── test_planner.py
│
├── templates/
│   └── index.html
│
├──
```
