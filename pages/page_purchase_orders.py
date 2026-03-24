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
from data.constants import ALL_PURCHASE_ORDERS

PURCHASE_ORDER_STATUS_COLORS = {
    "Pending": COLOR_WARNING,
    "Approved": ACCENT_PRIMARY,
    "Delivered": COLOR_SUCCESS,
    "Cancelled": COLOR_DANGER,
}


def build_purchase_orders_page(flet_page: ft.Page):
    number_of_pending_orders = sum(
        1
        for purchase_order in ALL_PURCHASE_ORDERS
        if purchase_order["status"] == "Pending"
    )
    number_of_delivered_orders = sum(
        1
        for purchase_order in ALL_PURCHASE_ORDERS
        if purchase_order["status"] == "Delivered"
    )
    total_purchase_order_value = sum(
        purchase_order["total"] for purchase_order in ALL_PURCHASE_ORDERS
    )

    purchase_order_table_rows = [
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(order_entry["id"], color=TEXT_SECONDARY, size=12)),
                ft.DataCell(
                    ft.Text(order_entry["supplier"], color=TEXT_PRIMARY, size=13)
                ),
                ft.DataCell(
                    ft.Text(order_entry["product"], color=TEXT_PRIMARY, size=13)
                ),
                ft.DataCell(
                    ft.Text(str(order_entry["qty"]), color=TEXT_PRIMARY, size=13)
                ),
                ft.DataCell(
                    ft.Text(
                        f'₹{order_entry["total"]:,.2f}',
                        color=TEXT_PRIMARY,
                        size=13,
                        weight=ft.FontWeight.W_600,
                    )
                ),
                ft.DataCell(
                    build_status_badge(
                        order_entry["status"],
                        PURCHASE_ORDER_STATUS_COLORS.get(
                            order_entry["status"], TEXT_SECONDARY
                        ),
                    )
                ),
                ft.DataCell(
                    ft.Text(order_entry["date"], color=TEXT_SECONDARY, size=12)
                ),
                ft.DataCell(
                    ft.Row(
                        [
                            ft.IconButton(
                                ft.Icons.VISIBILITY,
                                icon_color=ACCENT_PRIMARY,
                                icon_size=16,
                            ),
                            ft.IconButton(
                                ft.Icons.EDIT,
                                icon_color=ACCENT_SECONDARY,
                                icon_size=16,
                            ),
                        ],
                        spacing=0,
                    )
                ),
            ]
        )
        for order_entry in ALL_PURCHASE_ORDERS
    ]

    return ft.Column(
        [
            build_page_header(
                header_title="Purchase Orders",
                header_subtitle="Manage procurement and orders",
                header_icon=ft.Icons.RECEIPT,
                action_buttons=[build_action_button("New Order", ft.Icons.ADD)],
            ),
            ft.Container(height=20),
            ft.ResponsiveRow(
                [
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.RECEIPT,
                                "Total Orders",
                                len(ALL_PURCHASE_ORDERS),
                                None,
                                ACCENT_PRIMARY,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.HOURGLASS_EMPTY,
                                "Pending",
                                number_of_pending_orders,
                                None,
                                COLOR_WARNING,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.CHECK,
                                "Delivered",
                                number_of_delivered_orders,
                                None,
                                COLOR_SUCCESS,
                            )
                        ],
                        col={"xs": 6, "md": 3},
                    ),
                    ft.Column(
                        [
                            build_stat_card(
                                ft.Icons.ATTACH_MONEY,
                                "Total Value",
                                f"₹{total_purchase_order_value:,.0f}",
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
                                "PO ID",
                                "Supplier",
                                "Product",
                                "Qty",
                                "Total",
                                "Status",
                                "Date",
                                "Actions",
                            ],
                            table_rows=purchase_order_table_rows,
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
