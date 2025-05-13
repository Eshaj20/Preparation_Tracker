## Preparation Tracker
This is a simple CLI-based project that helps you track your preparation for any competitive exam (CAT, UPSC, GRE, SSC, GATE, etc.). It lets you manage topics per section, monitor mock test scores, and visualize your progress.

## Features
- Add & update topics for each section (e.g., Math, English, Reasoning)
- Track progress: Not Started / In Progress / Completed
- Record mock test scores by exam and section
- Visualize your preparation with progress charts
- Data saved in JSON and CSV formats
- Clean, modular Python code

## Requirements
- Python 3.7+
- matplotlib (for charts)

Install dependencies:
                    
                    pip install matplotlib
                    
## Folder Structure

```bash
cat_prep_tracker/
├── main.py               # Main CLI app
├── mock_tests.py         # Mock test tracker
├── subjects.json         # Auto-saved topic data (JSON)
├── data/
│   └── mock_tests.csv    # Auto-saved test data (CSV)

```
## How to Use
Run the app:
                     
                     python main.py

Choose from the menu:

1. Add Section/Topic
2. Update Topic Status
3. View Topic Progress
4. Add Mock Test
5. View Mock Tests
6. Show Progress Chart
7. Exit

## Example Chart
The chart shows how many topics are in each status:
1. Completed
2. In Progress
3. Not Started

## Tips
- Use different sections for subjects like Quant, Logical Reasoning, Verbal, etc.
- Add mock tests per exam and analyze section-wise trends later.
- Extend it to include notes, study plans, or reminders.

## Future Improvements (Optional)
- Add a Flask or Tkinter GUI
- Auto-calculate average mock test scores
- Add reminders or daily goals

