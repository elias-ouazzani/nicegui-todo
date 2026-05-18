from nicegui import ui

def add_task():
      ui.label(task_input.value)
      task_input.value = ""

if __name__ in {"__main__", "__mp_main__"}:
      ui.label("My to-do list")
      task_input = ui.input("Enter task")
      ui.button("Add task!", on_click=add_task)
      ui.run()
