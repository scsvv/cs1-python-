import flet as ft


class Task(ft.UserControl):
    def __init__(self, task_name, delete_task, task_status_change):
        super().__init__()
        self.task_name = task_name
        self.completed = False
        self.task_delete = delete_task
        self.task_status_change = task_status_change

    def build(self):
        self.display_task = ft.Checkbox(
            value=False, label=self.task_name, on_change=self.status_change)
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit task",
                            on_click=self.edit_task
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE_OUTLINED,
                            tooltip="Delete task",
                            on_click=self.delete_click
                        )
                    ]
                )
            ]
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update Task",
                    on_click=self.save_task
                )
            ]
        )
        return ft.Column(controls=[self.display_view, self.edit_view])

    def edit_task(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_task(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_click(self, e):
        self.task_delete(self)

    def status_change(self, e):
        self.completed = self.display_task.value
        self.task_status_change(self)


class TodoApp(ft.UserControl):
    def build(self):
        self.new_task = ft.TextField(hint_text="Make homework", expand=True)
        self.tasks = ft.Column()

        self.filter = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[ft.Tab(text="All"), ft.Tab(text="Active"),
                  ft.Tab(text="Completed")],
        )

        self.view = ft.Column(
            width=800,
            controls=[
                ft.Row(
                    controls=[self.new_task,
                              ft.FloatingActionButton(
                                  icon=ft.icons.ADD, on_click=self.add_task),
                              ],
                ), ft.Column(
                    spacing=20,
                    controls=[
                        self.filter,
                        self.tasks,
                    ]

                )

            ]
        )

        return self.view

    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        for task in self.tasks.controls:
            task.visible = (
                status == "All"
                or (status == "Active" and task.completed == False)
                or (status == "Completed" and task.completed)
            )

        super().update()

    def tabs_changed(self, e):
        self.update()

    def task_status_change(self, task):
        self.update()

    def add_task(self, e):
        task = Task(self.new_task.value, self.delete_task,
                    self.task_status_change)
        self.tasks.controls.insert(0, task)
        self.new_task.value = ""
        self.update()

    def delete_task(self, task):
        self.tasks.controls.remove(task)
        self.update()


def main(page: ft.Page):
    page.title = "TO DO LIST"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = TodoApp()
    page.add(todo)


if __name__ == "__main__":
    ft.app(main)
