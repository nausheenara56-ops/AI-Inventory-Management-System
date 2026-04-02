import flet as ft
from ui.theme import (
    ACCENT_PRIMARY,
    ACCENT_SECONDARY,
    COLOR_DANGER,
    COLOR_WARNING,
    COLOR_SUCCESS,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    SURFACE_DARK,
)
from ui.components import (
    build_card,
    build_status_badge,
    build_section_title,
    build_stat_card,
    build_data_table,
    build_mini_bar_chart,
)
from data.product_service import get_all_products
from data.constants import ALL_ALERTS


def build_dashboard_page(flet_page: ft.Page):
    ALL_PRODUCTS = get_all_products(limit=20)

    number_of_low_stock_items = sum(
    1 for product in ALL_PRODUCTS if int(product["current_stock"]) < int(product["reorder_point"])
  )
    number_of_out_of_stock_items = sum(
    1 for product in ALL_PRODUCTS if int(product["current_stock"]) == 0
  )
    recent_alert_widgets = ft.Column(
        [
            ft.Row(
                [
                    ft.Container(
                        width=8,
                        height=8,
                        border_radius=4,
                        bgcolor=(
                            COLOR_DANGER
                            if alert_entry["type"] == "danger"
                            else (
                                COLOR_WARNING
                                if alert_entry["type"] == "warning"
                                else ACCENT_SECONDARY
                            )
                        ),
                    ),
                    ft.Column(
                        [
                            ft.Text(
                                alert_entry["title"],
                                size=13,
                                color=TEXT_PRIMARY,
                                weight=ft.FontWeight.W_600,
                            ),
                            ft.Text(
                                alert_entry["msg"],
                                size=11,
                                color=TEXT_SECONDARY,
                                max_lines=1,
                            ),
                        ],
                        spacing=1,
                        expand=True,
                    ),
                    ft.Text(alert_entry["time"], size=11, color=TEXT_SECONDARY),
                ],
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.START,
            )
            for alert_entry in ALL_ALERTS[:4]
        ],
        spacing=12,
    )

    top_product_rows = [
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(product["name"], color=TEXT_PRIMARY, size=13)),
                ft.DataCell(
                    ft.Text(product["category_id"], color=TEXT_SECONDARY, size=12)
                ),
                ft.DataCell(
                    ft.Text(
                        str(product["current_stock"]),
                        color=(
                            COLOR_SUCCESS
                            if product["current_stock"] > product["reorder_point"]
                            else COLOR_DANGER
                        ),
                        size=13,
                        weight=ft.FontWeight.W_600,
                    )
                ),
                ft.DataCell(
                    ft.Text(f'₹{float(product["selling_price"]):,.2f}', color=TEXT_PRIMARY, size=13)
                ),
            ]
        )
        for product in ALL_PRODUCTS[:5]
    ]

    category_bar_chart = build_mini_bar_chart(
        bar_values=[89430, 12399, 4120, 2399],
        bar_labels=["Electronics", "Furniture", "Office", "Lighting"],
        bar_color=ACCENT_PRIMARY,
    )

    inventory_chart_card = build_card(
        ft.Column(
            [
                ft.Text(
                    "Inventory by Category",
                    size=15,
                    weight=ft.FontWeight.W_600,
                    color=TEXT_PRIMARY,
                ),
                ft.Container(height=12),
                category_bar_chart,
            ],
            spacing=0,
        ),
        should_expand=True,
    )

    live_alerts_card = build_card(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            "Live Alerts",
                            size=15,
                            weight=ft.FontWeight.W_600,
                            color=TEXT_PRIMARY,
                        ),
                        build_status_badge(f"{len(ALL_ALERTS)}", COLOR_DANGER),
                    ],
                    spacing=10,
                ),
                ft.Container(height=12),
                recent_alert_widgets,
            ],
            spacing=0,
        ),
        should_expand=True,
    )

    top_products_card = build_card(
        ft.Column(
            [
                ft.Text(
                    "Top Products Overview",
                    size=15,
                    weight=ft.FontWeight.W_600,
                    color=TEXT_PRIMARY,
                ),
                ft.Container(height=12),
                ft.Column(
                    [
                        build_data_table(
                            column_labels=["Product", "Category", "Stock", "Price"],
                            table_rows=top_product_rows,
                        )
                    ],
                    scroll=ft.ScrollMode.AUTO,
                ),
            ],
            spacing=0,
        )
    )

    return ft.Column(
        [
            build_section_title(
                "AI Smart Dashboard",
                "Real-time inventory intelligence",
            ),
            ft.Container(height=20),
            ft.ResponsiveRow(
                [
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.INVENTORY,
                                "Total Products",
                                len(ALL_PRODUCTS),
                                5,
                                ACCENT_PRIMARY,
                            )
                        ],
                        col={"xs": 12, "sm": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.WARNING,
                                "Low Stock Items",
                                number_of_low_stock_items,
                                -12,
                                COLOR_WARNING,
                            )
                        ],
                        col={"xs": 12, "sm": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.MONEY_OFF,
                                "Out of Stock",
                                number_of_out_of_stock_items,
                                -100,
                                COLOR_DANGER,
                            )
                        ],
                        col={"xs": 12, "sm": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.RECEIPT,
                                "Pending Orders",
                                2,
                                8,
                                ACCENT_SECONDARY,
                            )
                        ],
                        col={"xs": 12, "sm": 6, "md": 3},
                    ),
                ],
                spacing=16,
            ),
            ft.Container(height=20),
            ft.ResponsiveRow(
                [
                    ft.Column([inventory_chart_card], col={"xs": 12, "md": 7}),
                    ft.Column([live_alerts_card], col={"xs": 12, "md": 5}),
                ],
                spacing=16,
            ),
            ft.Container(height=20),
            top_products_card,
        ],
        spacing=0,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
