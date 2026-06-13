# 📅 Habit Tracker (Python CLI App)

A simple command-line Habit Tracker built in Python.  
This project helps users track daily habits, maintain streaks, and manage personal productivity.

---

## 🚀 Features

- ➕ Add new habits
- ✅ Mark habits as completed for today
- 📊 View current habit progress
- 🔥 Track longest and current streaks
- 🗑️ Delete habits
- 📅 Automatic date tracking using Python `datetime`

---

## 🧠 How It Works

The program stores habits in a Python dictionary:

```python
habits = {
    "Gym": ["2026-06-10", "2026-06-11"],
    "Reading": ["2026-06-11"]
}