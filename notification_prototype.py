#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:07:58 2024

@author: justine
"""

import tkinter as tk
from plyer import notification

# Function to trigger the desktop notification
def send_notification():
    notification.notify(
        title="Reminder",
        message="This is a simple desktop notification!",
        timeout=10  # The notification stays for 10 seconds
    )

# Set up the Tkinter window
root = tk.Tk()
root.title("Desktop Notification Example")

# Add a label
label = tk.Label(root, text="Click the button to get a notification")
label.pack(pady=20)

# Add a button to trigger the notification
button = tk.Button(root, text="Notify me", command=send_notification)
button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
