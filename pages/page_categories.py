import flet as ft
from ui.theme import (
    ACCENT_PRIMARY,
    ACCENT_SECONDARY,
    COLOR_DANGER,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
)
from ui.components import (
    build_card,
    build_status_badge,
    build_page_header,
    build_data_table,
    build_action_button,
    build_mini_bar_chart,
)
from data.constants import ALL_CATEGORIES


def build_categories_page(flet_page: ft.Page):
    category_table_rows = [
        ft.DataRow(
            cells=[
                ft.DataCell(
                    ft.Text(category_entry["id"], color=TEXT_SECONDARY, size=12)
                ),
                ft.DataCell(
                    ft.Text(
                        category_entry["name"],
                        color=TEXT_PRIMARY,
                        size=13,
                        weight=ft.FontWeight.W_500,
                    )
                ),
                ft.DataCell(
                    ft.Text(
                        str(category_entry["products"]),
                        color=ACCENT_PRIMARY,
                        size=13,
                    )
                ),
                ft.DataCell(
                    ft.Text(
                        f'₹{category_entry["value"]:,}',
                        color=TEXT_PRIMARY,
                        size=13,
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
        for category_entry in ALL_CATEGORIES
    ]

    distribution_chart = build_mini_bar_chart(
        bar_values=[category_entry["products"] for category_entry in ALL_CATEGORIES],
        bar_labels=[category_entry["name"] for category_entry in ALL_CATEGORIES],
        bar_color=ACCENT_SECONDARY,
    )

    distribution_chart_card = build_card(
        ft.Column(
            [
                ft.Text(
                    "Category Distribution",
                    size=15,
                    weight=ft.FontWeight.W_600,
                    color=TEXT_PRIMARY,
                ),
                ft.Container(height=12),
                distribution_chart,
            ]
        ),
        should_expand=True,
    )

    quick_stats_rows = [
        ft.Row(
            [
                ft.Text(
                    category_entry["name"],
                    color=TEXT_PRIMARY,
                    size=13,
                    expand=True,
                ),
                build_status_badge(
                    f'{category_entry["products"]} products',
                    ACCENT_PRIMARY,
                ),
            ]
        )
        for category_entry in ALL_CATEGORIES
    ]

    quick_stats_card = build_card(
        ft.Column(
            [
                ft.Text(
                    "Quick Stats",
                    size=15,
                    weight=ft.FontWeight.W_600,
                    color=TEXT_PRIMARY,
                ),
                ft.Container(height=12),
                *quick_stats_rows,
            ],
            spacing=10,
        ),
        should_expand=True,
    )

    return ft.Column(
        [
            build_page_header(
                header_title="Categories Management",
                header_subtitle="Organize your product categories",
                header_icon=ft.Icons.CATEGORY,
                action_buttons=[build_action_button("Add Category", ft.Icons.ADD)],
            ),
            ft.Container(height=20),
            ft.ResponsiveRow(
                [
                    ft.Column([distribution_chart_card], col={"xs": 12, "md": 7}),
                    ft.Column([quick_stats_card], col={"xs": 12, "md": 5}),
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
                                "Products",
                                "Total Value",
                                "Actions",
                            ],
                            table_rows=category_table_rows,
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
