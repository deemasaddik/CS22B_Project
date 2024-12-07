#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:43:30 2024

@author: deema, justine

"""

#from plyer import notification
from pync import Notifier
from datetime import datetime, timedelta
import time

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.classes = []
        self.social_events = []

    def add_class(self, name, time):
        self.classes.append({
            "name": name,
            "time": time,
            "assignments": [],
            "midterms": []
        })

    def add_assignment(self, class_name, assignment_name, due_date):
        for c in self.classes:
            if c["name"] == class_name:
                c["assignments"].append({"name": assignment_name, "due_date": due_date})
                break

    def add_midterm(self, class_name, midterm_name, date):
        for c in self.classes:
            if c["name"] == class_name:
                c["midterms"].append({"name": midterm_name, "date": date})
                break

    def add_social_event(self, event_name, date, time):
        self.social_events.append({"name": event_name, "date": date, "time": time})



class NotificationManager:
    def __init__(self, student):
        self.student = student

    def send_notification(self, title, message):
        """Send a macOS notification using pync."""
        Notifier.notify(
            message,  # The notification message
            title=title  # The notification title
        )

    def check_notifications(self):
        """Check and send notifications for upcoming events."""
        now = datetime.now()

        # Check classes
        for class_item in self.student.classes:
            class_time = datetime.strptime(class_item["time"], "%H:%M").time()
            class_datetime = datetime.combine(now.date(), class_time)
            if now + timedelta(minutes=15) >= class_datetime > now:
                self.send_notification("Class Reminder", f"{class_item['name']} starts in 15 minutes!")

            # Check assignments
            for assignment in class_item["assignments"]:
                due_date = datetime.strptime(assignment["due_date"], "%Y-%m-%d").date()
                if due_date == now.date():
                    self.send_notification("Assignment Due", f"{assignment['name']} for {class_item['name']} is due today!")

            # Check midterms
            for midterm in class_item["midterms"]:
                midterm_date = datetime.strptime(midterm["date"], "%Y-%m-%d").date()
                if midterm_date - timedelta(days=7) == now.date():
                    self.send_notification("Midterm Reminder", f"Start studying for {midterm['name']} in {class_item['name']} - it's in one week!")

        # Check social events
        for event in self.student.social_events:
            event_datetime = datetime.strptime(f"{event['date']} {event['time']}", "%Y-%m-%d %H:%M")
            if event_datetime.date() == now.date() and event_datetime.time() >= now.time():
                self.send_notification("Social Event Reminder", f"Don't forget: {event['name']} today at {event['time']}!")

'''
# Example usage 

student = Student("Jane Doe", 67890)
student.add_class("Chemistry", (datetime.now() + timedelta(minutes=3)).strftime("%H:%M"))
student.add_social_event("Dinner Party", datetime.now().strftime("%Y-%m-%d"), (datetime.now() + timedelta(minutes=2)).strftime("%H:%M"))

manager = NotificationManager(student)

# Check notifications in a loop
while True:
    manager.check_notifications()
    time.sleep(60)  # Check every minute'''
    
# Example usage 

# Create a Student instance
student = Student("John Doe", 12345)

# Test Case 1: Class Reminder (15 minutes before start time)
student.add_class("Biology", (datetime.now() + timedelta(minutes=15)).strftime("%H:%M"))

# Test Case 2: Social Event Reminder (2 minutes before start time)
student.add_social_event("Club Meeting", datetime.now().strftime("%Y-%m-%d"), (datetime.now() + timedelta(minutes=2)).strftime("%H:%M"))

# Test Case 3: Assignment Due Reminder (Due today)
student.add_assignment("Biology", "Lab Report", datetime.now().strftime("%Y-%m-%d"))

# Test Case 4: Handling Overlapping Events
student.add_class("Chemistry", (datetime.now() + timedelta(minutes=3)).strftime("%H:%M"))
student.add_social_event("Team Meeting", datetime.now().strftime("%Y-%m-%d"), (datetime.now() + timedelta(minutes=3)).strftime("%H:%M"))

# Create NotificationManager instance
manager = NotificationManager(student)

# Continuously check for notifications
try:
    while True:
        print("Checking for notifications...")
        manager.check_notifications()
        time.sleep(60)  # Check every minute




except KeyboardInterrupt:
    print("Notification checking stopped.")

