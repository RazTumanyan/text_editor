import flet as ft


path = ""

def main(page: ft.Page):
    page.title = "Text Editor"
    page.theme_mode = "dark"
    page.window_width = 300
    page.window_height = 350
    page.window_resizable = False
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    text_field = ft.TextField(label="File Text", width=250, multiline=True)

    def pick_result(e: ft.FilePickerResultEvent):
        if not e.files:
            selected_files.value = "Nothing Selected"
        else:
            selected_files.value = ""
            global path
            for el in e.files:
                path = el.path

            f = open(path, "r")
            text_field.value = f.read()
            f.close()
        page.update()

    def save_file(e):
        global path
        f = open(path, 'w')
        f.write(text_field.value)
        f.close()

        text_field.value = ""
        save_btn.text = "Ready"
        page.update()

    pick_dialog = ft.FilePicker(on_result=pick_result)
    page.overlay.append(pick_dialog)
    selected_files = ft.Text()

    save_btn = ft.FilledButton("Save", on_click=save_file)

    page.add(
        ft.Row([ft.Text("Selecting Files", size=25, weight=500)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(
            [
                ft.ElevatedButton(
                    "Select File",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_dialog.pick_files(allow_multiple=False)
                )
            ]
        ),
        ft.Row([text_field]),
        ft.Row([save_btn]),
        ft.Row([selected_files])
    )


ft.app(target=main)
