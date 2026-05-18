from nicegui import ui


tasks = []

def add_task():
      tasks.append(task_input.value)
      with task_list:
          ui.checkbox(task_input.value)
      task_input.value = ""
      counter_label.text = f"Tasks: {len(tasks)}"

def clear_tasks():
      tasks.clear()
      task_list.clear()
      counter_label.text = "Tasks: 0"

if __name__ in {"__main__", "__mp_main__"}:
      with ui.card().classes("w-96 mx-auto mt-10 p-6"):
          ui.label("My to-do list").classes("text-2xl font-bold mb-4")
          counter_label = ui.label("Tasks: 0").classes("text-gray-500")
          task_input = ui.input("Enter task").classes("w-full")
          with ui.row():
              ui.button("Add task!", on_click=add_task)
              ui.button("Clear all", on_click=clear_tasks).classes("bg-red-500")
          task_list = ui.column()
      ui.run()
