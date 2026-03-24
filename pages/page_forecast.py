import flet as ft
from ui.theme import (
    ACCENT_PRIMARY,
    ACCENT_SECONDARY,
    COLOR_SUCCESS,
    COLOR_WARNING,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    SURFACE_DARK,
)
from ui.components import (
    build_card,
    build_status_badge,
    build_page_header,
    build_stat_card,
    build_data_table,
    build_mini_bar_chart,
)

FORECAST_MONTH_LABELS = ["Apr", "May", "Jun", "Jul", "Aug", "Sep"]
FORECAST_DEMAND_VALUES = [120, 145, 180, 165, 140, 195]

PRODUCT_LEVEL_FORECASTS = [
    {"product": "Laptop", "current": 45, "predicted": 68, "confidence": 91},
    {"product": "Wireless Mouse", "current": 8, "predicted": 35, "confidence": 87},
    {"product": "Chair", "current": 0, "predicted": 22, "confidence": 78},
    {"product": "USB Carble", "current": 3, "predicted": 50, "confidence": 85},
    {"product": "Printer", "current": 22, "predicted": 30, "confidence": 93},
]


def build_forecast_page(flet_page: ft.Page):
    forecast_table_rows = [
        ft.DataRow(
            cells=[
                ft.DataCell(
                    ft.Text(forecast_entry["product"], color=TEXT_PRIMARY, size=13)
                ),
                ft.DataCell(
                    ft.Text(
                        str(forecast_entry["current"]),
                        color=TEXT_PRIMARY,
                        size=13,
                    )
                ),
                ft.DataCell(
                    ft.Text(
                        str(forecast_entry["predicted"]),
                        color=ACCENT_SECONDARY,
                        size=13,
                        weight=ft.FontWeight.W_600,
                    )
                ),
                ft.DataCell(
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Container(
                                        ft.Container(
                                            bgcolor=ACCENT_PRIMARY,
                                            border_radius=4,
                                            width=forecast_entry["confidence"] * 1.2,
                                        ),
                                        bgcolor=SURFACE_DARK,
                                        border_radius=4,
                                        height=8,
                                        width=120,
                                    ),
                                    ft.Text(
                                        f'{forecast_entry["confidence"]}%',
                                        size=11,
                                        color=TEXT_SECONDARY,
                                    ),
                                ],
                                spacing=8,
                            ),
                        ]
                    )
                ),
                ft.DataCell(
                    build_status_badge(
                        "High" if forecast_entry["confidence"] > 85 else "Medium",
                        (
                            COLOR_SUCCESS
                            if forecast_entry["confidence"] > 85
                            else COLOR_WARNING
                        ),
                    )
                ),
            ]
        )
        for forecast_entry in PRODUCT_LEVEL_FORECASTS
    ]

    return ft.Column(
        [
            build_page_header(
                header_title="Demand Forecast",
                header_subtitle="AI powered demand predictions",
                header_icon=ft.Icons.TRENDING_UP,
            ),
            ft.Container(height=20),
            ft.ResponsiveRow(
                [
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.LIGHTBULB,
                                "AI Accuracy",
                                "89.4%",
                                3,
                                ACCENT_PRIMARY,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.CALENDAR_TODAY,
                                "Forecast Period",
                                "6 Months",
                                None,
                                ACCENT_SECONDARY,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.TRENDING_UP,
                                "Demand Surge",
                                "3 Items",
                                None,
                                COLOR_WARNING,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.REFRESH,
                                "Last Updated",
                                "Today",
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
            build_card(
                ft.Column(
                    [
                        ft.Text(
                            "6-Month Demand Forecast",
                            size=15,
                            weight=ft.FontWeight.W_600,
                            color=TEXT_PRIMARY,
                        ),
                        ft.Container(height=4),
                        ft.Text(
                            "AI model predictions based on historical data and seasonal trends",
                            size=12,
                            color=TEXT_SECONDARY,
                        ),
                        ft.Container(height=12),
                        build_mini_bar_chart(
                            bar_values=FORECAST_DEMAND_VALUES,
                            bar_labels=FORECAST_MONTH_LABELS,
                            bar_color=ACCENT_PRIMARY,
                            chart_height=140,
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
                            "Product Level Forecasts",
                            size=15,
                            weight=ft.FontWeight.W_600,
                            color=TEXT_PRIMARY,
                        ),
                        ft.Container(height=12),
                        build_data_table(
                            column_labels=[
                                "Product",
                                "Current Stock",
                                "Predicted Demand",
                                "Confidence",
                                "Risk Level",
                            ],
                            table_rows=forecast_table_rows,
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
