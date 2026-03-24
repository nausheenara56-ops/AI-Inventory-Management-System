import random
import flet as ft
from ui.theme import (
    ACCENT_PRIMARY,
    ACCENT_SECONDARY,
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
    build_mini_bar_chart,
)
from data.constants import ALL_PRODUCTS

MONTHLY_SALES_LABELS = ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]
MONTHLY_SALES_VALUES = [42000, 55000, 78000, 61000, 49000, 68000]


def build_sales_page(flet_page: ft.Page):
    recent_transaction_rows = [
        ft.DataRow(
            cells=[
                ft.DataCell(
                    ft.Text(f"O-{1000 + row_index}", color=TEXT_SECONDARY, size=12)
                ),
                ft.DataCell(
                    ft.Text(
                        ALL_PRODUCTS[row_index % len(ALL_PRODUCTS)]["name"],
                        color=TEXT_PRIMARY,
                        size=13,
                    )
                ),
                ft.DataCell(
                    ft.Text(
                        str(random.randint(1, 20)),
                        color=TEXT_PRIMARY,
                        size=13,
                    )
                ),
                ft.DataCell(
                    ft.Text(
                        f"₹{random.randint(100, 5000):,}",
                        color=TEXT_PRIMARY,
                        size=13,
                    )
                ),
                ft.DataCell(
                    ft.Text(
                        f"2026-02-{20 + row_index:02d}",
                        color=TEXT_SECONDARY,
                        size=12,
                    )
                ),
                ft.DataCell(build_status_badge("Completed", COLOR_SUCCESS)),
            ]
        )
        for row_index in range(6)
    ]

    return ft.Column(
        [
            build_page_header(
                header_title="Sales Management",
                header_subtitle="Track and analyze sales performance",
                header_icon=ft.Icons.SHOPPING_CART,
                action_buttons=[build_action_button("New Sale", ft.Icons.ADD)],
            ),
            ft.Container(height=20),
            ft.ResponsiveRow(
                [
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.ATTACH_MONEY,
                                "Total Revenue",
                                "₹125,000",
                                12,
                                COLOR_SUCCESS,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.SHOPPING_CART,
                                "Total Orders",
                                "1,250",
                                8,
                                ACCENT_PRIMARY,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.TRENDING_UP,
                                "Average Order Value",
                                "₹125",
                                5,
                                ACCENT_SECONDARY,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.STAR,
                                "Top Category",
                                "Electronics",
                                None,
                                COLOR_WARNING,
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
                        ft.Text(
                            "Monthly Revenue Trend",
                            size=15,
                            weight=ft.FontWeight.W_600,
                            color=TEXT_PRIMARY,
                        ),
                        ft.Container(height=12),
                        build_mini_bar_chart(
                            bar_values=MONTHLY_SALES_VALUES,
                            bar_labels=MONTHLY_SALES_LABELS,
                            bar_color=ACCENT_PRIMARY,
                            chart_height=160,
                        ),
                    ],
                    spacing=0,
                )
            ),
            ft.Container(height=16),
            build_card(
                ft.Column(
                    [
                        ft.Text(
                            "Recent Transactions",
                            size=15,
                            weight=ft.FontWeight.W_600,
                            color=TEXT_PRIMARY,
                        ),
                        ft.Container(height=12),
                        build_data_table(
                            column_labels=[
                                "Order ID",
                                "Product",
                                "Qty",
                                "Amount",
                                "Date",
                                "Status",
                            ],
                            table_rows=recent_transaction_rows,
                        ),
                    ],
                    scroll=ft.ScrollMode.AUTO,
                )
            ),
        ],
        spacing=0,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
