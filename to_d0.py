import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Turtle To-Do List")
screen.bgcolor("blue")

# Create turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("black")

tasks = []

def display_tasks():
    pen.clear()
    pen.goto(-200, 200)
    pen.write("📝 TO-DO LIST", font=("Arial", 18, "bold"))
    
    y = 160
    for i, task in enumerate(tasks, start=1):
        pen.goto(-200, y)
        pen.write(f"{i}. {task}", font=("Arial", 14, "normal"))
        y -= 30

def add_task():
    task = screen.textinput("Add Task", "Enter a new task:")
    screen.listen()
    if task:
        tasks.append(task)
        display_tasks()

def clear_tasks():
    tasks.clear()
    display_tasks()

def delete_task():
    if not tasks:
        return

    choice = screen.textinput(
        "Delete Task",
        "Enter task number to delete:"
    )
    screen.listen()

    if choice and choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            display_tasks()

def edit_task():
    if not tasks:
        return  # No tasks to edit

    # Ask user for task number
    choice = screen.textinput("Edit Task", "Enter task number to edit:")
    screen.listen()

    if choice and choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(tasks):
            # Ask for new task text
            new_task = screen.textinput("Edit Task", "Enter new task:")
            screen.listen()
            if new_task:
                tasks[index] = new_task
                display_tasks()



# Buttons (keyboard controls)
screen.listen()
screen.onkey(add_task, "a")      # Press A to add task
screen.onkey(clear_tasks, "c")   # Press C to clear list
screen.onkey(delete_task,"d")    # Press D to delete a random task
screen.onkey(edit_task,"e")      # Press E to edit a random task

# Initial display
display_tasks()

pen.goto(-200, -200)
pen.write("Press 'A' to add task | Press 'C' to clear all | Press 'D' to delete task | Press 'E' to edit task", 
          font=("Arial", 12, "italic"))

screen.mainloop()


