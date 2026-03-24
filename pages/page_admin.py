import flet as ft
from ui.theme import (
    ACCENT_PRIMARY,
    COLOR_SUCCESS,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
)
from ui.components import (
    build_card,
    build_status_badge,
    build_page_header,
    build_action_button,
)
from data.constants import (
    ALL_EMPLOYEES,
    ADMIN_SYSTEM_SETTINGS,
    ADMIN_NOTIFICATION_SETTINGS,
    ADMIN_SECURITY_SETTINGS,
)


def build_admin_page(flet_page: ft.Page):
    system_setting_rows = [
        ft.Row(
            [
                ft.Container(
                    ft.Icon(setting_icon, color=ACCENT_PRIMARY, size=18),
                    bgcolor=ft.Colors.with_opacity(0.15, ACCENT_PRIMARY),
                    border_radius=8,
                    padding=8,
                ),
                ft.Column(
                    [
                        ft.Text(setting_label, color=TEXT_SECONDARY, size=12),
                        ft.Text(setting_value, color=TEXT_PRIMARY, size=13),
                    ],
                    spacing=2,
                    expand=True,
                ),
                ft.IconButton(
                    ft.Icons.EDIT,
                    icon_color=ACCENT_PRIMARY,
                    icon_size=16,
                ),
            ],
            spacing=12,
        )
        for setting_label, setting_value, setting_icon in ADMIN_SYSTEM_SETTINGS
    ]

    employee_user_rows = [
        ft.Row(
            [
                ft.Container(
                    ft.Text(
                        employee_entry["name"][0],
                        color=TEXT_PRIMARY,
                        size=12,
                        weight=ft.FontWeight.BOLD,
                    ),
                    bgcolor=ACCENT_PRIMARY,
                    width=30,
                    height=30,
                    border_radius=15,
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Column(
                    [
                        ft.Text(employee_entry["name"], color=TEXT_PRIMARY, size=13),
                        ft.Text(employee_entry["role"], color=TEXT_SECONDARY, size=11),
                    ],
                    spacing=1,
                    expand=True,
                ),
                build_status_badge(
                    "Admin" if employee_entry["id"] == "E001" else "Staff",
                    (
                        ACCENT_PRIMARY
                        if employee_entry["id"] == "E001"
                        else TEXT_SECONDARY
                    ),
                ),
            ],
            spacing=10,
        )
        for employee_entry in ALL_EMPLOYEES
    ]

    notification_toggle_rows = [
        ft.Row(
            [
                ft.Text(
                    notification_label,
                    color=TEXT_PRIMARY,
                    size=13,
                    expand=True,
                ),
                ft.Switch(
                    value=notification_enabled,
                    active_color=ACCENT_PRIMARY,
                ),
            ]
        )
        for notification_label, notification_enabled in ADMIN_NOTIFICATION_SETTINGS
    ]

    security_toggle_rows = [
        ft.Row(
            [
                ft.Text(
                    security_label,
                    color=TEXT_PRIMARY,
                    size=13,
                    expand=True,
                ),
                ft.Switch(
                    value=security_enabled,
                    active_color=ACCENT_PRIMARY,
                ),
            ]
        )
        for security_label, security_enabled in ADMIN_SECURITY_SETTINGS
    ]

    system_settings_card = build_card(
        ft.Column(
            [
                ft.Text(
                    "System Settings",
                    size=15,
                    weight=ft.FontWeight.W_600,
                    color=TEXT_PRIMARY,
                ),
                ft.Container(height=12),
                ft.Column(system_setting_rows, spacing=12),
            ],
            spacing=0,
        )
    )

    user_management_card = build_card(
        ft.Column(
            [
                ft.Text(
                    "User Management",
                    size=15,
                    weight=ft.FontWeight.W_600,
                    color=TEXT_PRIMARY,
                ),
                ft.Container(height=12),
                *employee_user_rows,
            ],
            spacing=12,
        )
    )

    notifications_card = build_card(
        ft.Column(
            [
                ft.Text(
                    "Notifications & Alerts",
                    size=15,
                    weight=ft.FontWeight.W_600,
                    color=TEXT_PRIMARY,
                ),
                ft.Container(height=12),
                *notification_toggle_rows,
            ],
            spacing=12,
        )
    )

    security_card = build_card(
        ft.Column(
            [
                ft.Text(
                    "Security & Access",
                    size=15,
                    weight=ft.FontWeight.W_600,
                    color=TEXT_PRIMARY,
                ),
                ft.Container(height=12),
                *security_toggle_rows,
                ft.Container(height=8),
                build_action_button("Change Password", ft.Icons.LOCK),
            ],
            spacing=12,
        )
    )

    return ft.Column(
        [
            build_page_header(
                header_title="Admin Control Panel",
                header_subtitle="System settings and configuration",
                header_icon=ft.Icons.ADMIN_PANEL_SETTINGS,
            ),
            ft.Container(height=20),
            ft.ResponsiveRow(
                [
                    ft.Column([system_settings_card], col={"xs": 12, "md": 6}),
                    ft.Column([user_management_card], col={"xs": 12, "md": 6}),
                ],
                spacing=16,
            ),
            ft.Container(height=16),
            ft.ResponsiveRow(
                [
                    ft.Column([notifications_card], col={"xs": 12, "md": 6}),
                    ft.Column([security_card], col={"xs": 12, "md": 6}),
                ],
                spacing=16,
            ),
        ],
        spacing=0,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
