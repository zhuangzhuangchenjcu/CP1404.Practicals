"""
Project
Estimate: 30 minutes
Actual:   20 minutes
"""


import datetime

class Project:
    def __init__(self, name: str, start_date: datetime.date, end_date: datetime.date, priority: int, completion: float):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.priority = priority
        self.completion = completion

    def __lt__(self, other):
        return self.priority > other.priority