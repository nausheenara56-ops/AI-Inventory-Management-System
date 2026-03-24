import flet as ft
from ui.theme import (
    ACCENT_PRIMARY,
    COLOR_DANGER,
    COLOR_SUCCESS,
    COLOR_WARNING,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
)
from ui.components import (
    build_card,
    build_page_header,
    build_stat_card,
    build_action_button,
)
from data.constants import ALL_ALERTS

ALERT_TYPE_VISUAL_MAP = {
    "danger": (COLOR_DANGER, ft.Icons.ERROR),
    "warning": (COLOR_WARNING, ft.Icons.WARNING),
    "info": (ACCENT_PRIMARY, ft.Icons.INFO),
    "success": (COLOR_SUCCESS, ft.Icons.CHECK_CIRCLE),
}


def build_risk_page(flet_page: ft.Page):
    number_of_critical_alerts = sum(
        1 for alert in ALL_ALERTS if alert["type"] == "danger"
    )
    number_of_warning_alerts = sum(
        1 for alert in ALL_ALERTS if alert["type"] == "warning"
    )
    number_of_info_alerts = sum(1 for alert in ALL_ALERTS if alert["type"] == "info")
    number_of_resolved_alerts = sum(
        1 for alert in ALL_ALERTS if alert["type"] == "success"
    )

    alert_card_widgets = []
    for alert_entry in ALL_ALERTS:
        alert_color, alert_icon = ALERT_TYPE_VISUAL_MAP[alert_entry["type"]]

        alert_card = build_card(
            ft.Row(
                [
                    ft.Container(
                        ft.Icon(alert_icon, color=alert_color, size=24),
                        bgcolor=ft.Colors.with_opacity(0.15, alert_color),
                        border_radius=10,
                        padding=10,
                    ),
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text(
                                        alert_entry["title"],
                                        color=TEXT_PRIMARY,
                                        size=13,
                                        weight=ft.FontWeight.W_600,
                                        expand=True,
                                    ),
                                    ft.Text(
                                        alert_entry["time"],
                                        color=TEXT_SECONDARY,
                                        size=11,
                                    ),
                                ]
                            ),
                            ft.Text(alert_entry["msg"], color=TEXT_SECONDARY, size=12),
                        ],
                        spacing=4,
                        expand=True,
                    ),
                    ft.IconButton(
                        ft.Icons.CLOSE,
                        icon_color=TEXT_SECONDARY,
                        icon_size=16,
                    ),
                ],
                spacing=14,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
            card_background_color=ft.Colors.with_opacity(0.05, alert_color),
            card_padding=16,
        )
        alert_card_widgets.append(alert_card)

    return ft.Column(
        [
            build_page_header(
                header_title="Risk & Alerts",
                header_subtitle="Monitor risks and critical notifications",
                header_icon=ft.Icons.WARNING,
            ),
            ft.Container(height=20),
            ft.ResponsiveRow(
                [
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.ERROR,
                                "Critical",
                                number_of_critical_alerts,
                                None,
                                COLOR_DANGER,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.WARNING,
                                "Warnings",
                                number_of_warning_alerts,
                                None,
                                COLOR_WARNING,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.INFO,
                                "Info",
                                number_of_info_alerts,
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
                                "Resolved",
                                number_of_resolved_alerts,
                                None,
                                COLOR_SUCCESS,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                ],
                spacing=16,
            ),
            ft.Container(height=20),
            ft.Row(
                [
                    ft.Text(
                        "All Alerts",
                        size=15,
                        weight=ft.FontWeight.W_600,
                        color=TEXT_PRIMARY,
                    ),
                    ft.Container(expand=True),
                    build_action_button(
                        "Clear All",
                        ft.Icons.DELETE_SWEEP,
                        button_color=COLOR_DANGER,
                        is_filled=False,
                    ),
                ]
            ),
            ft.Container(height=12),
            ft.Column(alert_card_widgets, spacing=10),
        ],
        spacing=0,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
