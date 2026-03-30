import flet as ft
from ui.theme import (
    ACCENT_PRIMARY,
    COLOR_DANGER,
    COLOR_WARNING,
    COLOR_SUCCESS,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    SURFACE_DARK,
    BORDER_DEFAULT,
)
from ui.components import (
    build_card,
    build_page_header,
    build_data_table,
    build_action_button,
)
from data.database import employees_collection


def build_employees_page(flet_page: ft.Page):

    selected_id = {"value": None}

    # ── FORM FIELDS ───────────────────────────────────────
    field_emp_id      = ft.TextField(label="Employee ID", dense=True, color=TEXT_PRIMARY, bgcolor=SURFACE_DARK, border_color=BORDER_DEFAULT)
    field_name        = ft.TextField(label="Name", dense=True, color=TEXT_PRIMARY, bgcolor=SURFACE_DARK, border_color=BORDER_DEFAULT)
    field_contact     = ft.TextField(label="Contact", dense=True, color=TEXT_PRIMARY, bgcolor=SURFACE_DARK, border_color=BORDER_DEFAULT)
    field_dob         = ft.TextField(label="DOB (DD-MM-YYYY)", dense=True, color=TEXT_PRIMARY, bgcolor=SURFACE_DARK, border_color=BORDER_DEFAULT)
    field_email       = ft.TextField(label="Email", dense=True, color=TEXT_PRIMARY, bgcolor=SURFACE_DARK, border_color=BORDER_DEFAULT)
    field_password    = ft.TextField(label="Password", password=True, dense=True, color=TEXT_PRIMARY, bgcolor=SURFACE_DARK, border_color=BORDER_DEFAULT)
    field_salary      = ft.TextField(label="Salary", dense=True, color=TEXT_PRIMARY, bgcolor=SURFACE_DARK, border_color=BORDER_DEFAULT, keyboard_type=ft.KeyboardType.NUMBER)
    field_address     = ft.TextField(label="Address", dense=True, color=TEXT_PRIMARY, bgcolor=SURFACE_DARK, border_color=BORDER_DEFAULT)
    field_perf_score  = ft.TextField(label="Performance Score", dense=True, color=TEXT_PRIMARY, bgcolor=SURFACE_DARK, border_color=BORDER_DEFAULT, keyboard_type=ft.KeyboardType.NUMBER)
    field_total_sales = ft.TextField(label="Total Sales", dense=True, color=TEXT_PRIMARY, bgcolor=SURFACE_DARK, border_color=BORDER_DEFAULT, keyboard_type=ft.KeyboardType.NUMBER)

    field_gender = ft.Dropdown(
        label="Gender",
        dense=True,
        bgcolor=SURFACE_DARK,
        border_color=BORDER_DEFAULT,
        color=TEXT_PRIMARY,
        options=[
            ft.dropdown.Option("Male"),
            ft.dropdown.Option("Female"),
            ft.dropdown.Option("Other"),
        ],
    )

    field_role = ft.Dropdown(
        label="Role",
        dense=True,
        bgcolor=SURFACE_DARK,
        border_color=BORDER_DEFAULT,
        color=TEXT_PRIMARY,
        options=[
            ft.dropdown.Option("Employee"),
            ft.dropdown.Option("Admin"),
            ft.dropdown.Option("Lead"),
            ft.dropdown.Option("Manager"),
            ft.dropdown.Option("Director"),
            ft.dropdown.Option("Expert"),
        ],
    )

    field_anomaly = ft.Dropdown(
        label="Anomaly Flag",
        dense=True,
        bgcolor=SURFACE_DARK,
        border_color=BORDER_DEFAULT,
        color=TEXT_PRIMARY,
        options=[
            ft.dropdown.Option("True"),
            ft.dropdown.Option("False"),
        ],
    )

    error_text = ft.Text("", color="red", size=12)
    table_column = ft.Column([])

    def to_int(val):
        try:
            return int(val)
        except:
            return 0

    def to_bool(val):
        return True if val == "True" else False

    def clear_fields(e=None):
        selected_id["value"] = None
        for f in [field_emp_id, field_name, field_contact,
                  field_dob, field_email, field_password,
                  field_salary, field_address, field_perf_score,
                  field_total_sales]:
            f.value = ""
        field_gender.value = None
        field_role.value = None
        field_anomaly.value = None
        error_text.value = ""
        flet_page.update()

    def fill(emp):
        selected_id["value"] = emp["_id"]
        field_emp_id.value      = emp.get("employee_id", "")
        field_name.value        = emp.get("name", "")
        field_gender.value      = emp.get("gender", "")
        field_contact.value     = emp.get("contact", "")
        field_dob.value         = emp.get("dob", "")
        field_email.value       = emp.get("email", "")
        field_password.value    = emp.get("password", "")
        field_role.value        = emp.get("role", "")
        field_salary.value      = str(emp.get("salary", ""))
        field_address.value     = emp.get("address", "")
        field_perf_score.value  = str(emp.get("performance_score", ""))
        field_total_sales.value = str(emp.get("total_sales", ""))
        field_anomaly.value     = "True" if emp.get("anomaly_flag") else "False"
        flet_page.update()

    def build_rows(emp_list):
        return [
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Text(emp.get("employee_id", ""), color=TEXT_SECONDARY, size=12),
                        on_tap=lambda e, x=emp: fill(x),
                    ),
                    ft.DataCell(ft.Text(emp.get("name", ""), color=TEXT_PRIMARY, size=13, weight=ft.FontWeight.W_500)),
                    ft.DataCell(ft.Text(emp.get("role", ""), color=TEXT_SECONDARY, size=12)),
                    ft.DataCell(ft.Text(str(emp.get("salary", "")), color=TEXT_PRIMARY, size=12)),
                    ft.DataCell(ft.Text(str(emp.get("performance_score", "")), color=COLOR_SUCCESS, size=12)),
                ]
            )
            for emp in emp_list
        ]

    def refresh_table():
        emps = list(employees_collection.find())
        table_column.controls.clear()
        table_column.controls.append(
            build_data_table(
                column_labels=["Employee ID", "Name", "Role", "Salary", "Score"],
                table_rows=build_rows(emps),
            )
        )
        flet_page.update()

    
    def add_emp(e):
        if not field_emp_id.value or not field_name.value:
            error_text.value = "⚠ Employee ID and Name are required."
            flet_page.update()
            return

        data = {
            "employee_id":       field_emp_id.value,
            "name":              field_name.value,
            "gender":            field_gender.value,
            "contact":           field_contact.value,
            "dob":               field_dob.value,
            "email":             field_email.value,
            "password":          field_password.value,
            "role":              field_role.value,
            "salary":            to_int(field_salary.value),
            "address":           field_address.value,
            "performance_score": to_int(field_perf_score.value),
            "total_sales":       to_int(field_total_sales.value),
            "anomaly_flag":      to_bool(field_anomaly.value),
        }

        employees_collection.insert_one(data)
        clear_fields()
        refresh_table()

    
    def update_emp(e):
        if not selected_id["value"]:
            error_text.value = "⚠ Select an employee first."
            flet_page.update()
            return

        employees_collection.update_one(
            {"_id": selected_id["value"]},
            {"$set": {
                "employee_id":       field_emp_id.value,
                "name":              field_name.value,
                "gender":            field_gender.value,
                "contact":           field_contact.value,
                "dob":               field_dob.value,
                "email":             field_email.value,
                "password":          field_password.value,
                "role":              field_role.value,
                "salary":            to_int(field_salary.value),
                "address":           field_address.value,
                "performance_score": to_int(field_perf_score.value),
                "total_sales":       to_int(field_total_sales.value),
                "anomaly_flag":      to_bool(field_anomaly.value),
            }}
        )
        clear_fields()
        refresh_table()

    
    def delete_emp(e):
        if not selected_id["value"]:
            error_text.value = "⚠ Select an employee first."
            flet_page.update()
            return

        employees_collection.delete_one({"_id": selected_id["value"]})
        clear_fields()
        refresh_table()

    refresh_table()

   
    form_card = build_card(
        ft.Column([
            ft.Text("Employee Form", size=15, weight=ft.FontWeight.W_600, color=TEXT_PRIMARY),
            ft.Container(height=8),
            ft.Row([field_emp_id, field_name, field_gender], spacing=10),
            ft.Row([field_contact, field_dob, field_email], spacing=10),
            ft.Row([field_password, field_role, field_salary], spacing=10),
            ft.Row([field_perf_score, field_total_sales, field_anomaly], spacing=10),
            field_address,
            ft.Container(height=8),
            error_text,
            ft.Row([
                ft.ElevatedButton("Add", bgcolor=COLOR_SUCCESS, color=TEXT_PRIMARY, on_click=add_emp),
                ft.ElevatedButton("Update", bgcolor=ACCENT_PRIMARY, color=TEXT_PRIMARY, on_click=update_emp),
                ft.ElevatedButton("Delete", bgcolor=COLOR_DANGER, color=TEXT_PRIMARY, on_click=delete_emp),
                ft.ElevatedButton("Clear", on_click=clear_fields),
            ], spacing=12),
        ], spacing=10)
    )

    
    return ft.Column(
        [
            build_page_header(
                header_title="Employees Management",
                header_subtitle="Manage your team members",
                header_icon=ft.Icons.PEOPLE,
            ),
            ft.Container(height=20),
            form_card,
            ft.Container(height=16),
            build_card(
                ft.Column([
                    ft.Text("All Employees", size=15, weight=ft.FontWeight.W_600, color=TEXT_PRIMARY),
                    ft.Container(height=12),
                    table_column,
                ])
            ),
        ],
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )