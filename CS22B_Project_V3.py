#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:43:39 2024

@author: deema
"""

#made this comment

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.classes = []
        self.social_events = []  # Social events are now independent

    def add_class(self, name, time):
        self.classes.append({
            "name": name,
            "time": time,
            "assignments": [],
            "midterms": []
        })  

    def remove_class(self, class_name):
        self.classes = [c for c in self.classes if c["name"] != class_name]

    def add_assignment(self, class_name, assignment_name, due_date):
        for c in self.classes:
            if c["name"] == class_name:
                c["assignments"].append({"name": assignment_name, "due_date": due_date})
                break

    def remove_assignment(self, class_name, assignment_name):
        for c in self.classes:
            if c["name"] == class_name:
                c["assignments"] = [a for a in c["assignments"] if a["name"] != assignment_name]
                break

    def add_midterm(self, class_name, midterm_name, date):
        for c in self.classes:
            if c["name"] == class_name:
                c["midterms"].append({"name": midterm_name, "date": date})
                break

    def remove_midterm(self, class_name, midterm_name):
        for c in self.classes:
            if c["name"] == class_name:
                c["midterms"] = [m for m in c["midterms"] if m["name"] != midterm_name]
                break

    def add_social_event(self, event_name, date, time):
        self.social_events.append({"name": event_name, "date": date, "time": time})

    def remove_social_event(self, event_name):
        self.social_events = [e for e in self.social_events if e["name"] != event_name]

    def get_info(self):
        return {
            'Name': self.name,
            'ID': self.student_id,
            'Classes': self.classes,
            'Social Events': self.social_events
        }

class NotificationManager:
    def __init__(self, student):
        self.student = student

    def send_notification(self, title, message):
        notification.notify(
            title=title,
            message=message,
            app_icon=None,
            timeout=10,
        )

    def check_notifications(self):
        now = datetime.datetime.now()

        for class_item in self.student.classes:
            # Class notifications
            class_time = datetime.datetime.strptime(class_item["time"], "%H:%M").time()
            class_datetime = datetime.datetime.combine(now.date(), class_time)
            if now + datetime.timedelta(minutes=15) >= class_datetime > now:
                self.send_notification("Class Reminder", f"{class_item['name']} starts in 15 minutes!")

            # Assignment notifications
            for assignment in class_item["assignments"]:
                due_date = datetime.datetime.strptime(assignment["due_date"], "%Y-%m-%d").date()
                if due_date == now.date():
                    self.send_notification("Assignment Due", f"{assignment['name']} for {class_item['name']} is due today!")

            # Midterm notifications
            for midterm in class_item["midterms"]:
                midterm_date = datetime.datetime.strptime(midterm["date"], "%Y-%m-%d").date()
                if midterm_date - datetime.timedelta(days=7) == now.date():
                    self.send_notification("Midterm Reminder", f"Start studying for {midterm['name']} in {class_item['name']} - it's in one week!")

        # Check social events notifications independently
        for event in self.student.social_events:
            event_datetime = datetime.datetime.strptime(f"{event['date']} {event['time']}", "%Y-%m-%d %H:%M")
            if event_datetime.date() == now.date():
                self.send_notification("Social Event", f"Don't forget: {event['name']} today at {event['time']}!")

class NotificationApp:
    # ... (previous code remains the same)

    def create_social_tab(self):
        social_frame = ttk.Frame(self.notebook)
        self.notebook.add(social_frame, text="Social Event")

        ttk.Label(social_frame, text="Event Name:").grid(row=0, column=0, sticky=tk.W)
        self.social_name = ttk.Entry(social_frame)
        self.social_name.grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Label(social_frame, text="Event Date (YYYY-MM-DD):").grid(row=1, column=0, sticky=tk.W)
        self.social_date = ttk.Entry(social_frame)
        self.social_date.grid(row=1, column=1, sticky=(tk.W, tk.E))

        ttk.Label(social_frame, text="Event Time (HH:MM):").grid(row=2, column=0, sticky=tk.W)
        self.social_time = ttk.Entry(social_frame)
        self.social_time.grid(row=2, column=1, sticky=(tk.W, tk.E))

        ttk.Button(social_frame, text="Add Social Event", command=self.add_social_event).grid(row=3, column=0)
        ttk.Button(social_frame, text="Remove Social Event", command=self.remove_social_event).grid(row=3, column=1)

    def add_social_event(self):
        if not self.student:
            messagebox.showerror("Error", "Please create a student first")
            return
        name = self.social_name.get()
        date = self.social_date.get()
        time = self.social_time.get()
        if name and date and time:
            self.student.add_social_event(name, date, time)
            messagebox.showinfo("Success", f"Social event {name} added")
        else:
            messagebox.showerror("Error", "Please enter all social event details")

    def remove_social_event(self):
        if not self.student:
            messagebox.showerror("Error", "Please create a student first")
            return
        name = self.social_name.get()
        if name:
            self.student.remove_social_event(name)
            messagebox.showinfo("Success", f"Social event {name} removed")
        else:
            messagebox.showerror("Error", "Please enter event name")