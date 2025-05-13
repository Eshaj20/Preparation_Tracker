# mock_tests.py
import csv
import os
from datetime import datetime

data_file = "data/mock_tests.csv"

def init_file():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(data_file):
        with open(data_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Exam", "Section", "Score", "Total"])

def add_mock_test():
    exam = input("Enter exam name (e.g., CAT, GRE, UPSC): ")
    section = input("Enter section (e.g., Math, English, Reasoning): ")
    score = input("Enter score: ")
    total = input("Enter total marks: ")
    date = datetime.now().strftime("%Y-%m-%d")
    with open(data_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, exam, section, score, total])
    print("✅ Mock test added successfully.")

def view_tests():
    if not os.path.exists(data_file):
        print("⚠️ No mock tests recorded yet.")
        return
    with open(data_file, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        print("\n=== 📘 Mock Test Records ===")
        for row in reader:
            print(f"📅 {row[0]} | Exam: {row[1]} | Section: {row[2]} | Score: {row[3]}/{row[4]}")

# Automatically initialize the CSV file when module is imported
init_file()
