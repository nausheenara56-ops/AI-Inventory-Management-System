from datetime import datetime
import flet as ft
from ui.theme import (
    ACCENT_PRIMARY,
    SURFACE_DARK,
    BACKGROUND_DARK,
    BORDER_DEFAULT,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    COLOR_DANGER,
)
from data.constants import NAVIGATION_ITEMS, ALL_ALERTS


def build_sidebar_navigation(
    currently_active_route_key,
    on_navigation_item_click_callback,
    on_logout_click_callback,
):
    def build_nav_item_button(
        route_key,
        item_icon,
        item_display_label,
    ):
        is_currently_active = currently_active_route_key == route_key

        def handle_nav_item_click(click_event, clicked_route_key=route_key):
            on_navigation_item_click_callback(clicked_route_key)

        nav_button_container = ft.Container(
            content=ft.Row(
                [
                    ft.Icon(
                        item_icon,
                        color=ACCENT_PRIMARY if is_currently_active else TEXT_SECONDARY,
                        size=18,
                    ),
                    ft.Text(
                        item_display_label,
                        color=TEXT_PRIMARY if is_currently_active else TEXT_SECONDARY,
                        size=13,
                        weight=(
                            ft.FontWeight.W_600
                            if is_currently_active
                            else ft.FontWeight.NORMAL
                        ),
                    ),
                ],
                spacing=12,
            ),
            bgcolor=(
                ft.Colors.with_opacity(0.15, ACCENT_PRIMARY)
                if is_currently_active
                else "transparent"
            ),
            border_radius=10,
            padding=ft.Padding.symmetric(horizontal=14, vertical=10),
            on_click=handle_nav_item_click,
        )

        if is_currently_active:
            nav_button_container.border = ft.Border.only(
                left=ft.BorderSide(3, ACCENT_PRIMARY)
            )

        return nav_button_container

    logo_header_section = ft.Container(
        ft.Row(
            [
                ft.Container(
                    ft.Icon(ft.Icons.INVENTORY, color=TEXT_PRIMARY, size=22),
                    bgcolor=ACCENT_PRIMARY,
                    border_radius=10,
                    padding=8,
                ),
                ft.Column(
                    [
                        ft.Text(
                            "InventoryAI",
                            color=TEXT_PRIMARY,
                            size=15,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text("Smart Management", color=TEXT_SECONDARY, size=10),
                    ],
                    spacing=0,
                ),
            ],
            spacing=10,
        ),
        padding=ft.Padding.symmetric(horizontal=16, vertical=20),
    )

    navigation_buttons_list = ft.Column(
        [
            build_nav_item_button(route_key, nav_icon, nav_label)
            for route_key, nav_icon, nav_label in NAVIGATION_ITEMS
        ],
        scroll=ft.ScrollMode.AUTO,
        expand=True,
        spacing=2,
    )

    user_profile_footer = ft.Container(
        ft.Row(
            [
                ft.Container(
                    ft.Text(
                        "A",
                        color=TEXT_PRIMARY,
                        size=14,
                        weight=ft.FontWeight.BOLD,
                    ),
                    bgcolor=ACCENT_PRIMARY,
                    width=34,
                    height=34,
                    border_radius=17,
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Column(
                    [
                        ft.Text("Admin User", color=TEXT_PRIMARY, size=13),
                        ft.Text("admin@company.com", color=TEXT_SECONDARY, size=10),
                    ],
                    spacing=1,
                    expand=True,
                ),
                ft.IconButton(
                    ft.Icons.LOGOUT,
                    icon_color=TEXT_SECONDARY,
                    icon_size=16,
                    tooltip="Logout",
                    on_click=on_logout_click_callback,
                ),
            ],
            spacing=10,
        ),
        padding=ft.Padding.all(14),
    )

    return ft.Container(
        width=230,
        bgcolor=SURFACE_DARK,
        border=ft.Border.only(right=ft.BorderSide(1, BORDER_DEFAULT)),
        content=ft.Column(
            [
                logo_header_section,
                ft.Divider(color=BORDER_DEFAULT, height=1),
                ft.Container(height=8),
                navigation_buttons_list,
                ft.Divider(color=BORDER_DEFAULT, height=1),
                user_profile_footer,
            ],
            spacing=0,
            expand=True,
        ),
    )


def build_topbar(currently_active_route_key):
    current_page_display_label = next(
        (
            nav_label
            for nav_key, _, nav_label in NAVIGATION_ITEMS
            if nav_key == currently_active_route_key
        ),
        "Dashboard",
    )

    number_of_urgent_alerts = len(
        [alert for alert in ALL_ALERTS if alert["type"] in ("danger", "warning")]
    )

    notification_bell_with_badge = ft.Stack(
        [
            ft.IconButton(
                ft.Icons.NOTIFICATIONS,
                icon_color=TEXT_SECONDARY,
                icon_size=22,
                style=ft.ButtonStyle(
                    bgcolor=SURFACE_DARK,
                    shape=ft.StadiumBorder(),
                ),
            ),
            ft.Container(
                ft.Text(
                    str(number_of_urgent_alerts),
                    color=TEXT_PRIMARY,
                    size=10,
                    weight=ft.FontWeight.BOLD,
                ),
                bgcolor=COLOR_DANGER,
                border_radius=8,
                width=16,
                height=16,
                alignment=ft.Alignment.CENTER,
                right=4,
                top=4,
            ),
        ]
    )

    search_input_field = ft.TextField(
        hint_text="Search anything...",
        prefix_icon=ft.Icons.SEARCH,
        bgcolor=SURFACE_DARK,
        border_color=BORDER_DEFAULT,
        color=TEXT_PRIMARY,
        hint_style=ft.TextStyle(color=TEXT_SECONDARY),
        height=40,
        width=220,
        border_radius=10,
        focused_border_color=ACCENT_PRIMARY,
    )

    current_date_label = ft.Text(
        datetime.now().strftime("%b %d, %Y"),
        color=TEXT_SECONDARY,
        size=12,
    )

    return ft.Container(
        ft.Row(
            [
                ft.Text(
                    current_page_display_label,
                    color=TEXT_PRIMARY,
                    size=18,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Container(expand=True),
                search_input_field,
                ft.Container(width=10),
                notification_bell_with_badge,
                current_date_label,
            ],
            spacing=8,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=SURFACE_DARK,
        border=ft.Border.only(bottom=ft.BorderSide(1, BORDER_DEFAULT)),
        padding=ft.Padding.symmetric(horizontal=24, vertical=10),
    )
