# 📌 Python Training Log
## 🗓 Day 3 — Data Structures

### Topics Covered: Classes

## 🛠 Work Completed

## CLI TASK TRACKER
### Example Usage

---

`# List a task` <br>
`python3 tasks.py -l` <br>
`python3 tasks.py -l --filter "done"` <br>
`python3 tasks.py -l --filter "todo"`

`# Add a task` <br>
`python3 tasks.py -at`

`# Complete a task` <br>
`python3 tasks.py -ct`

` # Delete a task` <br>
`python3 tasks.py -dt`

---

### Why use class instead of functions
- I used a class to group related data and behavior (tasks and their operations) into a single, organized structure. This improves maintainability and makes it easier to scale and extend the functionality in the future.
- I could use functions, but it would get messy as the project grows because I have to pass the task list around everywhere and manage state manually.