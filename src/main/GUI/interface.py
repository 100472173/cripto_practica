from tkinter import END

import customtkinter
from database_management import db_management
import cryptography

current_user = ""


class Interface(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("My Balance")
        self.frame = Login_frame(master=self, controller=self)
        self.frame.pack(padx=40, pady=20, fill="both", expand="true")

    def show_frame(self, page_name):
        self.frame.destroy()
        if page_name == "Login_frame":
            self.frame = Login_frame(master=self, controller=self)
        elif page_name == "Login_frame_error":
            self.frame = Login_frame_error(master=self, controller=self)
        elif page_name == "Register_frame":
            self.frame = Register_frame(master=self, controller=self)
        elif page_name == "Register_frame_ar":
            self.frame = Register_frame_ar(master=self, controller=self)
        elif page_name == "Withdraw_money_frame":
            self.frame = Withdraw_money_frame(master=self, controller=self)
        elif page_name == "Sum_money_frame":
            self.frame = Sum_money_frame(master=self, controller=self)
        else:
            self.frame = Main_frame(master=self, controller=self)
        self.frame.pack(padx=40, pady=20, fill="both", expand="true")


class Login_frame(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.titulo = customtkinter.CTkLabel(master=self,
                                             text="Inicio de sesión",
                                             text_color="black",
                                             font=("Century Gothic", 40))
        self.titulo.pack(padx=10, pady=30)
        self.usuario = customtkinter.CTkEntry(master=self, placeholder_text="Usuario", font=("Roboto", 15),
                                              width=190, height=37)
        self.usuario.pack(padx=10, pady=30)
        self.usuario.place(relx=0.275, rely=0.25)
        self.pwd = customtkinter.CTkEntry(master=self, placeholder_text="Contraseña", font=("Roboto", 15),
                                          width=190, height=37)
        self.pwd.pack(padx=10, pady=30)
        self.pwd.place(relx=0.275, rely=0.375)
        self.login_button = customtkinter.CTkButton(master=self, text="Iniciar sesión", font=("Roboto", 15),
                                                    width=190, height=37,
                                                    command=lambda: login_user_gui(self.controller, self.usuario.get(),
                                                                                   self.pwd.get()))
        self.login_button.pack(padx=10, pady=30)
        self.login_button.place(relx=0.275, rely=0.55)
        self.new_user_button = customtkinter.CTkButton(master=self,
                                                       text="¿Eres un nuevo usuario? Registráte aquí",
                                                       font=("Roboto", 15),
                                                       width=200, height=30, fg_color="#5dade2",
                                                       command=lambda: controller.show_frame("Register_frame"))
        self.new_user_button.pack(padx=10, pady=30)
        self.new_user_button.place(relx=0.16, rely=0.675)


class Login_frame_error(Login_frame):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        self.error = customtkinter.CTkLabel(master=self,
                                            text="Usuario o contraseña incorrecto",
                                            text_color="red",
                                            font=("Century Gothic", 15))
        self.error.pack(padx=10, pady=30)
        self.error.place(relx=0.225, rely=0.475)


class Register_frame(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.titulo = customtkinter.CTkLabel(master=self,
                                             text="Registro de usuario",
                                             text_color="black",
                                             font=("Century Gothic", 40))
        self.titulo.pack(padx=10, pady=30)
        self.titulo.place(relx=0.07, rely=0.02)

        self.usuario = customtkinter.CTkEntry(master=self, placeholder_text="Usuario",
                                              font=("Roboto", 15),
                                              width=190, height=37)
        self.usuario.pack(padx=10, pady=30)
        self.usuario.place(relx=0.275, rely=0.15)
        self.pwd = customtkinter.CTkEntry(master=self, placeholder_text="Contraseña",
                                          font=("Roboto", 15),
                                          width=190, height=37)
        self.pwd.pack(padx=10, pady=30)
        self.pwd.place(relx=0.275, rely=0.25)
        self.nombre = customtkinter.CTkEntry(master=self, placeholder_text="Nombre",
                                             font=("Roboto", 15),
                                             width=190, height=37)
        self.nombre.pack(padx=10, pady=30)
        self.nombre.place(relx=0.275, rely=0.35)
        self.apellido = customtkinter.CTkEntry(master=self, placeholder_text="Apellido",
                                               font=("Roboto", 15),
                                               width=190, height=37)
        self.apellido.pack(padx=10, pady=30)
        self.apellido.place(relx=0.275, rely=0.45)
        self.email = customtkinter.CTkEntry(master=self, placeholder_text="E-Mail",
                                            font=("Roboto", 15),
                                            width=190, height=37)
        self.email.pack(padx=10, pady=30)
        self.email.place(relx=0.275, rely=0.55)
        self.dinero = customtkinter.CTkEntry(master=self, placeholder_text="Dinero en la cuenta",
                                             font=("Roboto", 15),
                                             width=190, height=37)
        self.dinero.pack(padx=10, pady=30)
        self.dinero.place(relx=0.275, rely=0.65)
        self.register_button = customtkinter.CTkButton(master=self, text="Registrar usuario",
                                                       font=("Roboto", 15),
                                                       width=225, height=37,
                                                       command=lambda: register_user_gui(self.controller,
                                                                                         self.usuario.get(),
                                                                                         self.pwd.get(),
                                                                                         self.nombre.get(),
                                                                                         self.apellido.get(), "",
                                                                                         self.email.get(),
                                                                                         self.dinero.get()))
        self.register_button.pack(padx=10, pady=30)
        self.register_button.place(relx=0.225, rely=0.80)
        self.volver = customtkinter.CTkButton(master=self, text="Volver", font=("Roboto", 15),
                                              width=100, height=20,
                                              command=lambda: controller.show_frame("Login_frame"))
        self.volver.pack(padx=10, pady=30)
        self.volver.place(relx=0.05, rely=0.92)
        self.entries = [self.usuario, self.pwd, self.nombre, self.apellido, self.email, self.dinero]


class Register_frame_ar(Register_frame):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        self.already_registered = customtkinter.CTkLabel(master=self,
                                                         text="Usuario ya registrado",
                                                         text_color="red",
                                                         font=("Century Gothic", 15))
        self.already_registered.pack(padx=0, pady=0)
        self.already_registered.place(relx=0.32, rely=0.73)


class Main_frame(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.check_dinero = customtkinter.CTkButton(master=self, text="Ver dinero", font=("Roboto", 25),
                                                    width=250, height=60)
        self.check_dinero.pack(padx=10, pady=30)
        self.check_dinero.place(relx=0.21, rely=0.15)
        self.ingreso = customtkinter.CTkButton(master=self, text="Anotar ingreso", font=("Roboto", 25),
                                               width=250, height=60,
                                               command=lambda: controller.show_frame("Sum_money_frame"))
        self.ingreso.pack(padx=10, pady=30)
        self.ingreso.place(relx=0.21, rely=0.30)
        self.pago = customtkinter.CTkButton(master=self, text="Anotar pago", font=("Roboto", 25),
                                            width=250, height=60,
                                            command=lambda: controller.show_frame("Withdraw_money_frame"))
        self.pago.pack(padx=10, pady=30)
        self.pago.place(relx=0.21, rely=0.45)
        self.salir = customtkinter.CTkButton(master=self, text="Cerrar sesión", font=("Roboto", 25),
                                             width=250, height=60, fg_color="#e74c3c", hover_color="#b03a2e",
                                             command=lambda: controller.show_frame("Login_frame"))
        self.salir.pack(padx=10, pady=30)
        self.salir.place(relx=0.21, rely=0.65)
        self.borrar_user = customtkinter.CTkButton(master=self, text="Borrar usuario", font=("Roboto", 25),
                                                   width=250, height=60, fg_color="black", hover_color="#202121",
                                                   command=lambda: borrar_usuario(self.controller))
        self.borrar_user.pack(padx=10, pady=30)
        self.borrar_user.place(relx=0.21, rely=0.80)


class Withdraw_money_frame(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.titulo = customtkinter.CTkLabel(master=self,
                                             text="Introduce el pago",
                                             text_color="black",
                                             font=("Century Gothic", 30))
        self.titulo.pack(padx=10, pady=30)
        self.titulo.place(relx=0.18, rely=0.20)
        self.entrada = customtkinter.CTkEntry(master=self, placeholder_text="Cantidad",
                                              font=("Roboto", 15),
                                              width=190, height=45)
        self.entrada.pack(padx=10, pady=30)
        self.entrada.place(relx=0.28, rely=0.32)
        self.confirmar = customtkinter.CTkButton(master=self, text="Confirmar", font=("Roboto", 25),
                                                 width=250, height=50, fg_color="#0dba2d", hover_color="#09731d",
                                                 command=lambda: pagar_dinero(self.controller, self.entrada.get()))
        self.confirmar.pack(padx=10, pady=30)
        self.confirmar.place(relx=0.21, rely=0.50)
        self.volver = customtkinter.CTkButton(master=self, text="Volver", font=("Roboto", 15),
                                              width=100, height=30,
                                              command=lambda: controller.show_frame("Main_frame"))
        self.volver.pack(padx=10, pady=30)
        self.volver.place(relx=0.05, rely=0.90)


class Sum_money_frame(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.titulo = customtkinter.CTkLabel(master=self,
                                             text="Introduce el ingreso",
                                             text_color="black",
                                             font=("Century Gothic", 30))
        self.titulo.pack(padx=10, pady=30)
        self.titulo.place(relx=0.15, rely=0.20)
        self.entrada = customtkinter.CTkEntry(master=self, placeholder_text="Cantidad",
                                              font=("Roboto", 15),
                                              width=190, height=45)
        self.entrada.pack(padx=10, pady=30)
        self.entrada.place(relx=0.28, rely=0.32)
        self.confirmar = customtkinter.CTkButton(master=self, text="Confirmar", font=("Roboto", 25),
                                                 width=250, height=50, fg_color="#0dba2d", hover_color="#09731d",
                                                 command=lambda: ingresar_dinero(self.controller, self.entrada.get()))
        self.confirmar.pack(padx=10, pady=30)
        self.confirmar.place(relx=0.21, rely=0.50)
        self.volver = customtkinter.CTkButton(master=self, text="Volver", font=("Roboto", 15),
                                              width=100, height=30,
                                              command=lambda: controller.show_frame("Main_frame"))
        self.volver.pack(padx=10, pady=30)
        self.volver.place(relx=0.05, rely=0.90)


def register_user_gui(controller, user, pwd, name, surname1, surname2, email, money):
    if not db_management.search_user(user):
        db_management.insert_new_user(user, pwd)
        db_management.insert_new_user_details(user, money, email, name, surname1, surname2)
        controller.show_frame("Login_frame")
    else:
        controller.show_frame("Register_frame_ar")


def login_user_gui(controller, user, pwd):
    if db_management.search_user(user):
        try:
            db_management.verify_user_password(user, pwd)
            global current_user
            current_user = user
            controller.show_frame("Main_frame")
        except cryptography.exceptions.InvalidKey:
            controller.show_frame("Login_frame_error")
    else:
        controller.show_frame("Login_frame_error")


def borrar_usuario(controller):
    global current_user
    db_management.delete_user(current_user)
    print(current_user)
    controller.destroy()


def pagar_dinero(controller, cantidad):
    # Buscar al usuario en user_info usando el current_user y actualizar su dinero restandole cantidad
    controller.show_frame("Main_frame")


def ingresar_dinero(controller, cantidad):
    # Buscar al usuario en user_info usando el current_user y actualizar su dinero sumandole cantidad
    controller.show_frame("Main_frame")
