#
#
import string


def title_course_format(text):
    while True:
        name = input(text).strip()
        if name != "":
            break
        print("please enter a valid name (not empty!)")
    return name


def format_due_date(date):
    # we need to format the date as DD/MM/YYYY
    parts = date.split("/")
    if len(parts) != 3:
        return False
    if len(parts[0]) != 2 or len(parts[1]) != 2 or len(parts[2]) != 4:
        return False
    for part in parts:
        for num in part:
            if num not in string.digits:
                return False
    return True


def valid_format_due_data():
    date = input("Due date (DD/MM/YYYY):").strip()
    while not format_due_date(date):
        print(" please enter a valid date (DD/MM/YYYY)")
        date = input("Due date (DD/MM/YYYY)").strip()
    return date


def priority_format():
    priority = input("Priority (1=High, 2=Medium, 3=Low)").strip()
    while priority != "1" and priority != "2" and priority != "3":
        print(" please enter a valid priority")
        priority = input("priority number")
    if priority == "1":
        return "High"
    elif priority == "2":
        return "Medium"
    else:
        return "Low"


def text_id_fromat():
    text_id1 = input("Enter task ID :").strip()
    if text_id1 == "":
        print("task id must not be empty")
        return None
    for character in text_id1:
        if character not in string.digits:
            print("character must be digits")
            return None
    text_id = int(text_id1)
    if text_id == 0:
        print("0 is not a valid task id")
        return None
    return text_id


def display_menu():
    print("STUDENT PLANNER")
    print("-" * 30)
    print("1. Add a task")
    print("2. Edit a task")
    print("3. Delete a task")
    print("4. Find a task by ID")
    print("5. List all tasks")
    print("6. List tasks by course")
    print("7. List tasks by priority")
    print("8. Mark a task as completed")
    print("9. View task summary")
    print("10. Exit")
    print("-" * 30)


def add_task(tasks, next_task_id):
    title = title_course_format("Task title :")
    course = title_course_format("Course name :")
    due_date = valid_format_due_data()
    priority = priority_format()
    task = {"id": next_task_id, "title": title, "course": course, "due_date": due_date, "priority": priority,
            "status": "Pending"}
    tasks.append(task)
    print("Task added successfully. Task ID:", next_task_id)
    return next_task_id + 1


def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def display_task(task):
    print("*" * 5, "Displaying task", "*" * 5)
    print("ID task:", task["id"])
    print("Task title:", task["title"])
    print("Course name:", task["course"])
    print("Due date:", task["due_date"])
    print("Priority:", task["priority"])
    print("Status:", task["status"])
    print("*" * 15)


def edit_task(tasks):
    edit_task_id = text_id_fromat()
    if edit_task_id == None:
        print(" no valid task  found")
        return
    task = find_task_by_id(tasks, edit_task_id)
    if task == None:
        print("no task with that ID")
        return
    print("1. Title")
    print("2. Course")
    print("3. Due date")
    print("4. Priority")
    print("5. Cancel")
    choice = input("Enter your choice:").strip()
    match choice:
        case "1":
            task["title"] = title_course_format("Task title :")
        case "2":
            task["course"] = title_course_format("Course name :")
        case "3":
            task["due_date"] = valid_format_due_data()
        case "4":
            task["priority"] = priority_format()
        case "5":
            print("edit canceled")
            return
        case _:
            print("error")
            return
    print("Task updated successfully.")


def delete_task(tasks)
    delete_task_id = text_id_fromat()
    if delete_task_id == None:
        return
    task = find_task_by_id(tasks, delete_task_id)
    if task == None:
        print("There is no task with that ID")
    tasks[delete_task_id].remove(task)
    print("Task deleted successfully.")


def list_all_tasks(tasks):
    if not tasks:
        print("no tasks found")
        return
    print("-" * 3, "All tasks", "-" * 3)
    for task in tasks:
        display_task(task)


def list_tasks_by_course(tasks):
    if not tasks:
        print("no tasks found")
        return

    course_name = input("Enter course name:").strip()

    while course_name == "":
        print("please enter a valid course name")
        course_name = input("Enter course name:").strip()

    found = False
    for task in tasks:
        if task["course"].lower() == course_name.lower():
            display_task(task)
            found = True

    if not found:
        print("No tasks found for this course.")

def list_tasks_by_priority(tasks):
    if not tasks:
        print("no tasks found")
        return
    print("1. High")
    print("2. Medium")
    print("3. Low")
    choice = input("Enter your choice:").strip()

    while choice != "1" and choice != "2" and choice != "3":
        print("please enter a valid priority")
        choice = input("Enter your priority:").strip()

    if choice == "1":
        priority = "High"
        elif choice == "2":
        priority = "Medium"
        else:
            priority = "Low"
        found=False
        for task in tasks:
            if task["priority"] == priority:
                display_task(task)
                found = True
        if not found:
            print("no tasks found with this priority")

def mark_task_completed(tasks):
    task_id = text_id_fromat()

    if task_id == None:
        return
    task = find_task_by_id(tasks, task_id)
    if task == None:
        pint("There is no task with that ID")
        return
    if task["status"] == "Completed":
        return

    task["status"] = "Completed"
    print("Task", task_id, "Marked as completed")

def show_summary(task):
        total_tasks = len(tasks)
        pending_tasks = 0
        completed_tasks = 0

        for task in tasks:
            if task["status"] == "Pending":
                pending_tasks += 1
            elif task["status"] == "Completed":
                completed_tasks += 1
        if total_tasks == 0:
            percentage = 100
        else:
            percentage = completed_tasks / total_tasks * 100

        print("--- Task summary---")
        print("Total tasks:", total_tasks)
        print("Pending tasks:", pending_tasks)
        print("Completed tasks:", completed_tasks)
        print("Completed percentage:", format(percentage, ".1f")+ "%")

def main():
    tasks = []
    next_task_id = 1
    choice = 0
    while choice != 10:
        display_menu()
        choice = input("Enter your choice:").strip()

        if choice.isdigit():
            choice = int(choice)
        else:
            choice = 0
        match choice:
            case 1:
                next_task_id = add_task(tasks, next_task_id)
            case 2:
                edit_task(tasks)
            case 3:
                delete_task(tasks)
            case 4:
                task_id = text_id_fromat()
                if task_id != None:
                    task = find_task_by_id(tasks, task_id)
                    if task != None:
                        display_task(task)
                    else:
                        print("No task found.")
            case 5:
                list_all_tasks(tasks)
            case 6:
                list_tasks_by_course(tasks)
            case 7:
                list_tasks_by_priority(tasks)
            case 8:
                mark_task_completed(tasks)
            case 9:
                show_summary(tasks)
            case 10:
                print("Goodbye!")
            case _:
                print("Invalid choice")
main() #calling main function









