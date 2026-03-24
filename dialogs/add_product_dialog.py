import flet as ft
from data.product_service import add_product


def open_add_product_dialog(page: ft.Page, refresh_callback):

    product_id = ft.TextField(label="Product ID", width=300)
    name = ft.TextField(label="Product Name", width=300)
    category = ft.Dropdown(
    label="Category",
    width=300,
    options=[
        ft.dropdown.Option("Electronics"),
        ft.dropdown.Option("Furniture"),
        ft.dropdown.Option("Lighting"),
        ft.dropdown.Option("Stationery"),
        ft.dropdown.Option("Networking"),
    ],
)
    stock = ft.TextField(label="Stock", width=300)
    price = ft.TextField(label="Price", width=300)
    reorder = ft.TextField(label="Reorder Level", width=300)
    supplier = ft.TextField(label="Supplier", width=300)

    def handle_submit(e):

        new_product = {
            "id": product_id.value,
            "name": name.value,
            "category": category.value,
            "stock": int(stock.value),
            "price": float(price.value),
            "reorder": int(reorder.value),
            "supplier": supplier.value,
        }

        add_product(new_product)

        dialog.open = False
        page.update()

        refresh_callback()

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Add New Product"),
        content=ft.Column(
            [
                product_id,
                name,
                category,
                stock,
                price,
                reorder,
                supplier,
            ],
            tight=True,
            height=400,
            scroll="auto"
        ),
        actions=[
            ft.TextButton("Cancel", on_click=lambda e: close_dialog()),
            ft.ElevatedButton("Add Product", on_click=handle_submit),
        ],
    )

    def close_dialog():
        dialog.open = False
        page.update()

    page.overlay.append(dialog)
    dialog.open =True
    page.update()