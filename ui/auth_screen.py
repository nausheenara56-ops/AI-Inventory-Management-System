import flet as ft
from ui.theme import (
    ACCENT_PRIMARY,
    BACKGROUND_DARK,
    SURFACE_DARK,
    BORDER_DEFAULT,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
)
from ui.components import build_auth_text_field

FEATURE_HIGHLIGHTS = [
    (ft.Icons.TRENDING_UP, "AI powered demand forecasting"),
    (ft.Icons.AUTORENEW, "Smart automatic reordering"),
    (ft.Icons.BAR_CHART, "Real time inventory analytics"),
    (ft.Icons.WARNING, "Proactive risk management"),
]


def build_auth_feature_panel():
    feature_highlight_rows = [
        ft.Row(
            [
                ft.Container(
                    ft.Icon(feature_icon, color=ACCENT_PRIMARY, size=16),
                    bgcolor=ft.Colors.with_opacity(0.15, ACCENT_PRIMARY),
                    border_radius=8,
                    padding=6,
                ),
                ft.Text(feature_description, color=TEXT_SECONDARY, size=13),
            ],
            spacing=12,
        )
        for feature_icon, feature_description in FEATURE_HIGHLIGHTS
    ]

    return ft.Container(
        expand=True,
        bgcolor=SURFACE_DARK,
        border=ft.Border.only(right=ft.BorderSide(1, BORDER_DEFAULT)),
        content=ft.Column(
            [
                ft.Icon(ft.Icons.INVENTORY, color=ACCENT_PRIMARY, size=60),
                ft.Container(height=16),
                ft.Text(
                    "InventoryAI",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=TEXT_PRIMARY,
                ),
                ft.Text(
                    "AI Powered Inventory Management",
                    size=15,
                    color=TEXT_SECONDARY,
                ),
                ft.Container(height=40),
                *feature_highlight_rows,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.START,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=14,
        ),
        padding=60,
    )

def build_login_form(
    on_login_success_callback,
    on_navigate_to_register_callback,
    on_navigate_to_forgot_callback,
):
    email_input_field = build_auth_text_field(
        "Email Address", "you@company.com", ft.Icons.EMAIL
    )
    password_input_field = build_auth_text_field(
        "Password", "••••••••", ft.Icons.LOCK, is_password_field=True
    )
    error_text = ft.Text("", color="red", size=12)

    def handle_login(e):
        from data.user_service import login_user

        email = email_input_field.value.strip()
        password = password_input_field.value.strip()

        
        if not email or not password:
            error_text.value = "⚠ Please enter email and password."
            email_input_field.update()
            return

        
        user, error = login_user(email, password)

        if error:
            error_text.value = f"⚠ {error}"
            error_text.update()
            return

        
        on_login_success_callback(e)

    return ft.Column(
        [
            ft.Text(
                "Welcome Back",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=TEXT_PRIMARY,
            ),
            ft.Text(
                "Sign in to your InventoryAI account",
                size=14,
                color=TEXT_SECONDARY,
            ),
            ft.Container(height=24),
            email_input_field,
            ft.Container(height=12),
            password_input_field,
            ft.Container(height=6),
            ft.Row(
                [
                    ft.Checkbox(
                        label="Remember me",
                        value=False,
                        label_style=ft.TextStyle(color=TEXT_SECONDARY, size=12),
                        fill_color=ACCENT_PRIMARY,
                    ),
                    ft.Container(expand=True),
                    ft.TextButton(
                        "Forgot Password?",
                        on_click=on_navigate_to_forgot_callback,
                        style=ft.ButtonStyle(color=ACCENT_PRIMARY),
                    ),
                ]
            ),
            ft.Container(height=8),
            error_text,                   
            ft.Container(height=8),
            ft.ElevatedButton(
                "Sign In",
                icon=ft.Icons.LOGIN,
                on_click=handle_login,    
                bgcolor=ACCENT_PRIMARY,
                color=TEXT_PRIMARY,
                width=340,
                height=46,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
            ),
            ft.Container(height=16),
            ft.Row(
                [
                    ft.Text("Don't have an account?", color=TEXT_SECONDARY, size=13),
                    ft.TextButton(
                        "Create one",
                        on_click=on_navigate_to_register_callback,
                        style=ft.ButtonStyle(color=ACCENT_PRIMARY),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        spacing=0,
        width=340,
    )

    


def build_register_form(
    on_register_success_callback,
    on_navigate_to_login_callback,
):
    full_name_input_field = build_auth_text_field(
        "Full Name", "John Doe", ft.Icons.PERSON
    )
    email_input_field = build_auth_text_field(
        "Email Address", "you@company.com", ft.Icons.EMAIL
    )
    password_input_field = build_auth_text_field(
        "Password", "••••••••", ft.Icons.LOCK, is_password_field=True
    )
    confirm_password_input_field = build_auth_text_field(
        "Confirm Password", "••••••••", ft.Icons.LOCK_OUTLINE, is_password_field=True
    )
    error_text = ft.Text("", color="red", size=12)

    def handle_register(e):
        from data.user_service import register_user

        full_name = full_name_input_field.value.strip()
        email = email_input_field.value.strip()
        password = password_input_field.value.strip()
        confirm = confirm_password_input_field.value.strip()

        if not all([full_name, email, password, confirm]):
            error_text.value = "⚠ All fields are required."
            error_text.update()
            return

        if password != confirm:
            error_text.value = "⚠ Passwords do not match."
            error_text.update()
            return

        success, error = register_user(full_name, email, password)

        if not success:
            error_text.value = f"⚠ {error}"
            error_text.update()
            return

        on_register_success_callback(e)

    return ft.Column(
        [
            ft.Text(
                "Create Account",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=TEXT_PRIMARY,
            ),
            ft.Text("Join InventoryAI today", size=14, color=TEXT_SECONDARY),
            ft.Container(height=24),
            full_name_input_field,
            ft.Container(height=12),
            email_input_field,
            ft.Container(height=12),
            password_input_field,
            ft.Container(height=12),
            confirm_password_input_field,
            ft.Container(height=12),
            error_text,
            ft.Container(height=8),
            ft.ElevatedButton(
                "Create Account",
                icon=ft.Icons.PERSON_ADD,
                on_click=handle_register,
                bgcolor=ACCENT_PRIMARY,
                color=TEXT_PRIMARY,
                width=340,
                height=46,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
            ),
            ft.Container(height=16),
            ft.Row(
                [
                    ft.Text("Already have an account?", color=TEXT_SECONDARY, size=13),
                    ft.TextButton(
                        "Sign in",
                        on_click=on_navigate_to_login_callback,
                        style=ft.ButtonStyle(color=ACCENT_PRIMARY),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        spacing=0,
        width=340,
    )
 


def build_forgot_password_form(
    on_send_reset_link_callback,
    on_navigate_to_login_callback,
):
    email_input_field = build_auth_text_field(
        "Email Address", "name@company.com", ft.Icons.EMAIL
    )

    return ft.Column(
        [
            ft.Text(
                "Reset Password",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=TEXT_PRIMARY,
            ),
            ft.Text(
                "Enter your email to receive a reset link",
                size=14,
                color=TEXT_SECONDARY,
            ),
            ft.Container(height=24),
            email_input_field,
            ft.Container(height=20),
            ft.ElevatedButton(
                "Send Reset Link",
                icon=ft.Icons.SEND,
                on_click=on_send_reset_link_callback,
                bgcolor=ACCENT_PRIMARY,
                color=TEXT_PRIMARY,
                width=340,
                height=46,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
            ),
            ft.Container(height=16),
            ft.Row(
                [
                    ft.TextButton(
                        "← Back to Login",
                        on_click=on_navigate_to_login_callback,
                        style=ft.ButtonStyle(color=ACCENT_PRIMARY),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        spacing=0,
        width=340,
    )


def show_auth_screen(
    flet_page: ft.Page,
    auth_sub_page,
    on_login_success_callback,
    on_navigate_callback,
):
    if auth_sub_page == "login":
        active_form_widget = build_login_form(
            on_login_success_callback=on_login_success_callback,
            on_navigate_to_register_callback=lambda e: on_navigate_callback("register"),
            on_navigate_to_forgot_callback=lambda e: on_navigate_callback("forgot"),
        )
    elif auth_sub_page == "register":
        active_form_widget = build_register_form(
            on_register_success_callback=on_login_success_callback,
            on_navigate_to_login_callback=lambda e: on_navigate_callback("login"),
        )
    else:
        active_form_widget = build_forgot_password_form(
            on_send_reset_link_callback=lambda e: on_navigate_callback("login"),
            on_navigate_to_login_callback=lambda e: on_navigate_callback("login"),
        )

    form_container = ft.Container(
        width=480,
        content=ft.Column(
            [active_form_widget],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=60,
    )

    flet_page.controls.clear()
    flet_page.add(
        ft.Container(
            expand=True,
            bgcolor=BACKGROUND_DARK,
            content=ft.Row(
                [
                    build_auth_feature_panel(),
                    form_container,
                ],
                spacing=0,
                expand=True,
            ),
        )
    )
    flet_page.update()
