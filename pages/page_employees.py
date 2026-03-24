import flet as ft
from ui.theme import (
    ACCENT_PRIMARY,
    ACCENT_SECONDARY,
    COLOR_DANGER,
    COLOR_SUCCESS,
    COLOR_WARNING,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
)
from ui.components import (
    build_card,
    build_status_badge,
    build_page_header,
    build_stat_card,
    build_data_table,
    build_action_button,
)
from data.constants import ALL_EMPLOYEES


def build_employees_page(flet_page: ft.Page):
    number_of_active_employees = sum(
        1 for employee in ALL_EMPLOYEES if employee["status"] == "Active"
    )
    number_of_employees_on_leave = sum(
        1 for employee in ALL_EMPLOYEES if employee["status"] == "On Leave"
    )

    employee_table_rows = [
        ft.DataRow(
            cells=[
                ft.DataCell(
                    ft.Text(employee_entry["id"], color=TEXT_SECONDARY, size=12)
                ),
                ft.DataCell(
                    ft.Row(
                        [
                            ft.Container(
                                ft.Text(
                                    employee_entry["name"][0],
                                    color=TEXT_PRIMARY,
                                    size=13,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                bgcolor=ACCENT_PRIMARY,
                                width=32,
                                height=32,
                                border_radius=16,
                                alignment=ft.Alignment.CENTER,
                            ),
                            ft.Text(
                                employee_entry["name"],
                                color=TEXT_PRIMARY,
                                size=13,
                            ),
                        ],
                        spacing=10,
                    )
                ),
                ft.DataCell(
                    ft.Text(employee_entry["role"], color=TEXT_SECONDARY, size=12)
                ),
                ft.DataCell(
                    ft.Text(employee_entry["dept"], color=TEXT_SECONDARY, size=12)
                ),
                ft.DataCell(
                    ft.Text(employee_entry["email"], color=TEXT_SECONDARY, size=12)
                ),
                ft.DataCell(
                    build_status_badge(
                        employee_entry["status"],
                        (
                            COLOR_SUCCESS
                            if employee_entry["status"] == "Active"
                            else COLOR_WARNING
                        ),
                    )
                ),
                ft.DataCell(
                    ft.Row(
                        [
                            ft.IconButton(
                                ft.Icons.EDIT,
                                icon_color=ACCENT_PRIMARY,
                                icon_size=16,
                            ),
                            ft.IconButton(
                                ft.Icons.DELETE,
                                icon_color=COLOR_DANGER,
                                icon_size=16,
                            ),
                        ],
                        spacing=0,
                    )
                ),
            ]
        )
        for employee_entry in ALL_EMPLOYEES
    ]

    return ft.Column(
        [
            build_page_header(
                header_title="Employees Management",
                header_subtitle="Manage your team",
                header_icon=ft.Icons.PEOPLE,
                action_buttons=[build_action_button("Add Employee", ft.Icons.ADD)],
            ),
            ft.Container(height=20),
            ft.ResponsiveRow(
                [
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.PEOPLE,
                                "Total Staff",
                                len(ALL_EMPLOYEES),
                                None,
                                ACCENT_PRIMARY,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.CHECK_CIRCLE,
                                "Active",
                                number_of_active_employees,
                                None,
                                COLOR_SUCCESS,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.WB_SUNNY,
                                "On Leave",
                                number_of_employees_on_leave,
                                None,
                                COLOR_WARNING,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.WORK, "Departments", 4, None, ACCENT_SECONDARY
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                ],
                spacing=16,
            ),
            ft.Container(height=20),
            build_card(
                ft.Column(
                    [
                        build_data_table(
                            column_labels=[
                                "ID",
                                "Name",
                                "Role",
                                "Department",
                                "Email",
                                "Status",
                                "Actions",
                            ],
                            table_rows=employee_table_rows,
                        )
                    ],
                    scroll=ft.ScrollMode.AUTO,
                )
            ),
        ],
        spacing=0,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
