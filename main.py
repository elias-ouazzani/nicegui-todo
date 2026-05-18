from nicegui import ui

def add_task():
      with task_list:
          ui.label(task_input.value)
      task_input.value = ""

def clear_tasks():
      task_list.clear()

if __name__ in {"__main__", "__mp_main__"}:
      ui.label("My to-do list")
      task_input = ui.input("Enter task")
      ui.button("Add task!", on_click=add_task)
      ui.button("Clear all", on_click=clear_tasks)
      task_list = ui.column()
      ui.run()