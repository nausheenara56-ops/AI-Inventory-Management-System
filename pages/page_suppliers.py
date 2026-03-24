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
from data.constants import ALL_SUPPLIERS


def build_suppliers_page(flet_page: ft.Page):
    number_of_active_suppliers = sum(
        1 for supplier in ALL_SUPPLIERS if supplier["status"] == "Active"
    )
    total_products_supplied = sum(supplier["products"] for supplier in ALL_SUPPLIERS)

    supplier_table_rows = [
        ft.DataRow(
            cells=[
                ft.DataCell(
                    ft.Text(supplier_entry["id"], color=TEXT_SECONDARY, size=12)
                ),
                ft.DataCell(
                    ft.Text(
                        supplier_entry["name"],
                        color=TEXT_PRIMARY,
                        size=13,
                        weight=ft.FontWeight.W_500,
                    )
                ),
                ft.DataCell(
                    ft.Text(supplier_entry["contact"], color=TEXT_SECONDARY, size=12)
                ),
                ft.DataCell(
                    ft.Text(
                        str(supplier_entry["products"]),
                        color=ACCENT_PRIMARY,
                        size=13,
                    )
                ),
                ft.DataCell(
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.STAR, color=COLOR_WARNING, size=14),
                            ft.Text(
                                str(supplier_entry["rating"]),
                                color=TEXT_PRIMARY,
                                size=13,
                            ),
                        ],
                        spacing=4,
                    )
                ),
                ft.DataCell(
                    build_status_badge(
                        supplier_entry["status"],
                        (
                            COLOR_SUCCESS
                            if supplier_entry["status"] == "Active"
                            else TEXT_SECONDARY
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
        for supplier_entry in ALL_SUPPLIERS
    ]

    return ft.Column(
        [
            build_page_header(
                header_title="Suppliers Management",
                header_subtitle="Manage your supplier network",
                header_icon=ft.Icons.LOCAL_SHIPPING,
                action_buttons=[build_action_button("Add Supplier", ft.Icons.ADD)],
            ),
            ft.Container(height=20),
            ft.ResponsiveRow(
                [
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.LOCAL_SHIPPING,
                                "Total Suppliers",
                                len(ALL_SUPPLIERS),
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
                                number_of_active_suppliers,
                                None,
                                COLOR_SUCCESS,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.STAR, "Avg Rating", "4.42", None, COLOR_WARNING
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.INVENTORY,
                                "Total Products",
                                total_products_supplied,
                                None,
                                ACCENT_SECONDARY,
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
                                "Contact",
                                "Products",
                                "Rating",
                                "Status",
                                "Actions",
                            ],
                            table_rows=supplier_table_rows,
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
