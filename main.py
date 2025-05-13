# main.py
import json
import os
from mock_tests import add_mock_test, view_tests
import matplotlib.pyplot as plt

DATA_FILE = "subjects.json"

def load_subjects():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_subjects(subjects):
    with open(DATA_FILE, "w") as f:
        json.dump(subjects, f, indent=2)

def add_subject(subjects):
    subject = input("Enter exam section (e.g., Math, English, Reasoning): ")
    topic = input("Enter topic: ")
    subjects.setdefault(subject, {})[topic] = "Not Started"
    print(f"Added topic '{topic}' under '{subject}'")

def update_status(subjects):
    subject = input("Enter section: ")
    if subject not in subjects:
        print("Section not found.")
        return
    topic = input("Enter topic: ")
    if topic not in subjects[subject]:
        print("Topic not found.")
        return
    status = input("Enter status (Not Started / In Progress / Completed): ")
    subjects[subject][topic] = status
    print(f"Updated '{topic}' to status '{status}'")

def view_progress(subjects):
    print("\n=== Preparation Progress ===")
    for subject, topics in subjects.items():
        print(f"\nSection: {subject}")
        for topic, status in topics.items():
            print(f"  - {topic}: {status}")

def show_progress_chart(subjects):
    status_counts = {"Not Started": 0, "In Progress": 0, "Completed": 0}
    for topics in subjects.values():
        for status in topics.values():
            if status in status_counts:
                status_counts[status] += 1

    plt.figure(figsize=(6, 4))
    plt.bar(status_counts.keys(), status_counts.values(), color=["gray", "orange", "green"])
    plt.title("Overall Topic Progress")
    plt.xlabel("Status")
    plt.ylabel("Number of Topics")
    plt.tight_layout()
    plt.show()

def main():
    subjects = load_subjects()
    while True:
        print("\n--- Exam Preparation Tracker ---")
        print("1. Add Section/Topic")
        print("2. Update Topic Status")
        print("3. View Topic Progress")
        print("4. Add Mock Test")
        print("5. View Mock Tests")
        print("6. Show Progress Chart")
        print("7. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            add_subject(subjects)
        elif choice == "2":
            update_status(subjects)
        elif choice == "3":
            view_progress(subjects)
        elif choice == "4":
            add_mock_test()
        elif choice == "5":
            view_tests()
        elif choice == "6":
            show_progress_chart(subjects)
        elif choice == "7":
            save_subjects(subjects)
            print("Progress saved. Exiting.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()