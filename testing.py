import mysql.connector
from datetime import timedelta

def validate_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def validate_uppercase_choice(prompt, choices):
    while True:
        choice = input(prompt).strip()
        if choice in choices:
            return choice
        else:
            print(f"Please choose a valid option: {', '.join(choices)}")

def validate_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid floating point number.")

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="",  
        database="task_manager_py"
    )

def insert_task_to_database(cursor, name, task, working_hours):
    sql = "INSERT INTO tasks (name, task, working_hours) VALUES (%s, %s, %s)"
    val = (name, task, working_hours)
    cursor.execute(sql, val)

def main():
    task_descriptions = {
        'LG': 'Login',
        'RG': 'Register',
        'US': 'User',
        'EMP': 'Employee',
        'TS': 'Timesheets'
    }

    name = input("Enter your name: ")
    num_tasks = validate_integer("Enter the number of tasks you want to do: ")
    choices = list(task_descriptions.keys())
    tasks = []

    db = connect_to_database()
    cursor = db.cursor()

    for i in range(1, num_tasks + 1):
        print("-" * 51)
        print(f"Please choose your task {i}:")
        print("-" * 51)
        for code, description in task_descriptions.items():
            print(f"{code}: {description}")
        print("-" * 51)
        task_choice = validate_uppercase_choice("Choose a task: ", choices)
        hours = validate_float(f"Enter your working hour for {task_descriptions[task_choice]} (in float, e.g. 1.5 for 1 hour 30 minutes): ")
        tasks.append((task_descriptions[task_choice], hours))
        insert_task_to_database(cursor, name, task_descriptions[task_choice], hours)

    db.commit()
    cursor.close()
    db.close()

    total_hours = sum(hours for task, hours in tasks)

    print("\nSummary of tasks for {}:".format(name))
    for task, hours in tasks:
        td = timedelta(hours=hours)
        print(f"Task: {task}, Working Hours: {hours:.2f} ({td})")
    
    total_td = timedelta(hours=total_hours)
    print(f"\nTotal Working Hours: {total_hours:.2f} ({total_td})")
    print("Data has been successfully inserted into the database.")

if __name__ == "__main__":
    main()
