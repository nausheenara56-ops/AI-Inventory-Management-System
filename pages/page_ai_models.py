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
)
from data.constants import ALL_AI_MODELS


def build_ai_models_page(flet_page: ft.Page):
    number_of_active_models = sum(
        1 for model in ALL_AI_MODELS if model["status"] == "Active"
    )
    number_of_training_models = sum(
        1 for model in ALL_AI_MODELS if model["status"] == "Training"
    )

    def determine_model_status_color(model_status):
        if model_status == "Active":
            return COLOR_SUCCESS
        if model_status == "Training":
            return COLOR_WARNING
        return TEXT_SECONDARY

    model_table_rows = [
        ft.DataRow(
            cells=[
                ft.DataCell(
                    ft.Text(
                        model_entry["name"],
                        color=TEXT_PRIMARY,
                        size=13,
                        weight=ft.FontWeight.W_500,
                    )
                ),
                ft.DataCell(build_status_badge(model_entry["type"], ACCENT_PRIMARY)),
                ft.DataCell(
                    ft.Row(
                        [
                            ft.Container(
                                ft.Container(
                                    bgcolor=(
                                        COLOR_SUCCESS
                                        if model_entry["accuracy"] > 85
                                        else COLOR_WARNING
                                    ),
                                    border_radius=4,
                                    width=model_entry["accuracy"] * 1.0,
                                ),
                                bgcolor=SURFACE_DARK,
                                border_radius=4,
                                height=8,
                                width=100,
                            ),
                            ft.Text(
                                f'{model_entry["accuracy"]}%',
                                size=12,
                                color=TEXT_PRIMARY,
                            ),
                        ],
                        spacing=8,
                    )
                ),
                ft.DataCell(
                    build_status_badge(
                        model_entry["status"],
                        determine_model_status_color(model_entry["status"]),
                    )
                ),
                ft.DataCell(
                    ft.Text(model_entry["last_train"], color=TEXT_SECONDARY, size=12)
                ),
                ft.DataCell(
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "Retrain",
                                bgcolor=ACCENT_PRIMARY,
                                color=TEXT_PRIMARY,
                                height=30,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8)
                                ),
                            ),
                            ft.IconButton(
                                ft.Icons.SETTINGS,
                                icon_color=TEXT_SECONDARY,
                                icon_size=16,
                            ),
                        ],
                        spacing=4,
                    )
                ),
            ]
        )
        for model_entry in ALL_AI_MODELS
    ]

    model_health_banner = build_card(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.Icons.MEMORY, color=ACCENT_SECONDARY, size=18),
                        ft.Text(
                            "Model Health: All systems operational",
                            color=TEXT_PRIMARY,
                            size=13,
                        ),
                        ft.Container(expand=True),
                        build_status_badge("Healthy", COLOR_SUCCESS),
                    ],
                    spacing=10,
                ),
            ],
            spacing=0,
        ),
        card_background_color=ft.Colors.with_opacity(0.08, COLOR_SUCCESS),
    )

    return ft.Column(
        [
            build_page_header(
                header_title="AI Model Management",
                header_subtitle="Monitor and manage your AI/ML models",
                header_icon=ft.Icons.LIGHTBULB,
            ),
            ft.Container(height=20),
            ft.ResponsiveRow(
                [
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.LIGHTBULB,
                                "Total Models",
                                len(ALL_AI_MODELS),
                                None,
                                ACCENT_PRIMARY,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.PLAY_CIRCLE_FILL,
                                "Active",
                                number_of_active_models,
                                None,
                                COLOR_SUCCESS,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.HOURGLASS_EMPTY,
                                "Training",
                                number_of_training_models,
                                None,
                                COLOR_WARNING,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.SHOW_CHART,
                                "Avg Accuracy",
                                "87.4%",
                                4,
                                ACCENT_SECONDARY,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                ],
                spacing=16,
            ),
            ft.Container(height=20),
            model_health_banner,
            ft.Container(height=16),
            build_card(
                ft.Column(
                    [
                        ft.Text(
                            "Registered AI Models",
                            size=15,
                            weight=ft.FontWeight.W_600,
                            color=TEXT_PRIMARY,
                        ),
                        ft.Container(height=12),
                        build_data_table(
                            column_labels=[
                                "Model Name",
                                "Type",
                                "Accuracy",
                                "Status",
                                "Last Trained",
                                "Actions",
                            ],
                            table_rows=model_table_rows,
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
