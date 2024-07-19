"""
Project Management
Estimate: 2 hours
Actual:   3 hours 20 minutes
"""


import datetime
import project


class ProjectManagement:
    def __init__(self):
        self.projects = []

    def load_projects(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()

        for line in lines:
            name, start_date_str, priority, estimate, completion = line.strip().split(",")
            start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
            priority = int(priority)
            estimate = float(estimate)
            completion = float(completion)
            p = project.Project(name, start_date, priority, estimate, completion)
            self.projects.append(p)

    def save_projects(self, filename):
        with open(filename, "w") as f:
            for p in self.projects:
                f.write(f"{p.name},{p.start_date.strftime('%d/%m/%Y')},{p.priority},{p.estimate},{p.completion}\n")

    def display_projects(self):
        incomplete_projects = []
        completed_projects = []
        for p in self.projects:
            if p.completion < 1.0:
                incomplete_projects.append(p)
            else:
                completed_projects.append(p)

        incomplete_projects.sort()
        completed_projects.sort()

        print("Incomplete projects:")
        for p in incomplete_projects:
            print(f"{p.name}, start: {p.start_date.strftime('%d/%m/%Y')}, "
                  f"priority {p.priority}, estimate: ${p.estimate}, completion: {p.completion}%")

        print("Completed projects:")
        for p in completed_projects:
            print(f"{p.name}, start: {p.start_date.strftime('%d/%m/%Y')}, "
                  f"priority {p.priority}, estimate: ${p.estimate}, completion: {p.completion}%")

    def filter_projects_by_date(self, date: datetime.date):
        filtered_projects = []
        for p in self.projects:
            if p.start_date > date:
                filtered_projects.append(p)

        filtered_projects.sort(key=project.Project.start_date)

        for p in filtered_projects:
            print(
                f"{p.name}, start: {p.start_date.strftime('%d/%m/%Y')},"
                f" priority {p.priority}, estimate: ${p.estimate}, completion: {p.completion}%")


def main():
    pm = ProjectManagement()

    while True:
        print("""
- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
        """)
        choice = input(">>> ").lower().strip()

        if choice == "l":
            filename = input("Enter filename: ")
            pm.load_projects(filename)
        elif choice == "s":
            filename = input("Enter filename: ")
            pm.save_projects(filename)
        elif choice == "d":
            pm.display_projects()
        elif choice == "f":
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            pm.filter_projects_by_date(date)
        elif choice == "a":
            pm.add_new_project()
        elif choice == "u":
            pm.update_projecdt()
        elif choice == "q":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()