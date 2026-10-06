# 📚 AI Study Planner

### Your Personalized AI-Powered Study Companion

AI Study Planner is a comprehensive web-based study planning application that uses **Google Gemini AI** to create personalized study plans based on a student's subjects, exam date, available study hours, current level, weak subjects, strong subjects, and preferred study style.

The application features an intelligent dashboard with progress tracking, AI recommendations, exam readiness scoring, and much more.

---

## ✨ Features

### 🤖 AI Study Plan Generation

Generate a personalized study plan using Google Gemini AI based on:

* Subjects
* Exam date
* Daily study hours
* Current skill level (Beginner / Intermediate / Advanced)
* Weak subjects
* Strong subjects
* Study preference (Mixed / Theory / Coding / Practice / Revision)

### 📊 Progress Tracking

* Mark study tasks as completed
* Automatic progress percentage calculation
* Visual progress bar
* Completed task count
* Today's task highlighting
* Completion status saved using browser `localStorage`
* Plan-specific progress storage (new plans don't inherit old progress)

### 🎯 Personalized Planning

The AI adapts the study plan according to:

* Student level (foundational concepts for beginners, advanced topics for advanced)
* Weak subjects (more time allocated)
* Strong subjects (lighter revision sessions)
* Study preference (theory-focused, practice-focused, or balanced)

### 📈 Student Dashboard

The comprehensive dashboard provides:

* ⏳ **Exam Countdown**: Dynamic days remaining calculation
* ⭐ **Today's Task**: Prominent display of current task
* 📊 **Overall Progress**: Large percentage display with progress bar
* 📚 **Subject Progress**: Subject-wise completion with health status (Strong/Good/Needs Attention/Critical)
* ⏱️ **Study Statistics**: Total/completed/remaining hours and total tasks
* 🎯 **Exam Readiness Score**: Calculated readiness indicator with status description
* ⭐ **Recommended Next Task**: AI-suggested next task based on priority
* ⚠️ **Missed Tasks**: Detection of incomplete past-due tasks
* 🔄 **Catch-Up Plan**: Suggested catch-up strategy for missed tasks
* 🔥 **Study Streak**: Track consecutive study days
* 🤖 **Smart AI Recommendations**: Personalized study recommendations (with Gemini API + rule-based fallback)
* 📊 **AI Performance Analysis**: Overall preparation analysis with strongest/weakest subjects
* 🎯 **Study Profile**: Display of student's personalization preferences
* 🤖 **AI Study Summary**: Intelligent summary using actual progress data

### 🔍 Search & Filters

* **Search**: Search tasks by subject, task description, or date
* **Status Filter**: Filter by All / Today / Upcoming / Completed / Pending / Missed
* **Subject Filter**: Dynamic subject filter based on generated plan

### 📥 Export & Print

* **CSV Export**: Download study plan as CSV file
* **Print Plan**: Browser-optimized print view with clean layout

### 🌙 Dark Mode

* Toggle dark/light theme
* Preference saved in localStorage
* Persists across sessions

### � Reset Progress

* Reset current plan's completion state
* Confirmation dialog before reset
* Does not affect API configuration or unrelated data

### �💾 Local Progress Storage

Study completion data is stored in the browser using `localStorage`:
* Progress persists after page refresh
* Plan-specific storage (different plans have separate progress)
* Dark mode preference saved
* Old localStorage data preserved when generating new plans

### 🎨 Responsive Design

* Optimized for desktop, tablet, and mobile
* Grid layouts adapt to screen size
* Touch-friendly controls

### ♿ Accessibility

* Proper form labels and ARIA attributes
* Keyboard-friendly navigation
* Good color contrast
* Meaningful headings and structure

### ⚡ Performance & Reliability

* Loading state during plan generation
* Friendly error messages for API failures
* Rule-based fallback when Gemini API is unavailable
* Graceful degradation for missing/malformed data
* No exposed API keys or internal errors

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
├── app.py                 # Flask application with routes
├── planner.py             # Backup planning logic (not used in main app)
├── gemini_service.py      # Gemini API integration and recommendations
├── test_gemini.py         # Gemini API connection test
├── test_planner.py        # Plan generation test
├── test_dashboard.py      # Dashboard functionality tests
│
├── templates/
│   └── index.html         # Main application template
│
├── static/
│   └── style.css          # Application styles including dark mode
│
├── .env                   # API key (NOT tracked by Git)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

---

## 🚀 Setup Instructions

### Prerequisites

* Python 3.7 or higher
* Google Gemini API key

### Installation

1. **Clone or download the project**

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   **Windows:**
   ```bash
   .\venv\Scripts\Activate.ps1
   ```

   **Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**

   ```bash
   pip install flask
   pip install python-dotenv
   pip install -U google-genai
   ```

5. **Configure API key**

   Create a `.env` file in the project root:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

   Get your API key from: https://ai.google.dev/

6. **Run the application**

   ```bash
   python app.py
   ```

7. **Open in browser**

   Navigate to: http://127.0.0.1:5000

---

## 🧪 Testing

Run the test files to verify functionality:

```bash
# Test plan generation
python test_planner.py

# Test Gemini API connection
python test_gemini.py

# Test dashboard calculations
python test_dashboard.py
```

---

## 🔒 Security

* `.env` file is NOT tracked by Git (see `.gitignore`)
* API key is never exposed to the frontend
* Error messages do not reveal internal details
* No database required (client-side storage only)

---

## 📝 Usage

1. **Fill out the form** with your subjects, exam date, study hours, level, weak/strong subjects, and preference
2. **Click "Generate Study Plan"** to create your personalized plan
3. **Use the dashboard** to track progress, view recommendations, and analyze your preparation
4. **Mark tasks as completed** by checking the checkboxes
5. **Use filters and search** to navigate your plan
6. **Export or print** your plan for offline reference

---

## 🎓 How It Works

1. **Plan Generation**: The form data is sent to the Flask backend, which calls the Gemini API with a structured prompt
2. **AI Processing**: Gemini generates a JSON study plan with daily tasks, subjects, hours, and descriptions
3. **Fallback Mechanism**: If one Gemini model fails, the system tries other models in sequence
4. **Dashboard Calculation**: JavaScript calculates progress, statistics, readiness score, and recommendations
5. **Progress Storage**: Completion state is saved in localStorage with a plan-specific key
6. **Recommendations**: AI recommendations use Gemini API with rule-based fallback for reliability

---

## 🤝 Contributing

This is a personal project for demonstration purposes. Feel free to fork and modify for your own use.

---

## 📄 License

This project is open source and available for educational purposes.

---

## 🙏 Acknowledgments

* Google Gemini API for AI capabilities
* Flask for the web framework
* The open-source community for various libraries

---

## 📞 Support

For issues or questions, please refer to the code comments or create an issue in the repository.

```
