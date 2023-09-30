import customtkinter
from database_management import db_management
import cryptography

current_user = ""


class Interface(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("My Balance")
        self.frames = {}
        for F in (Login_frame, Register_frame, Main_frame, Register_frame_ar, Login_frame_error):
            page_name = F.__name__
            frame = F(master=self, controller=self)
            self.frames[page_name] = frame
            frame.pack(padx=40, pady=20, fill="both", expand="true")
        self.show_frame("Login_frame")

    def show_frame(self, page_name):
        for name in self.frames:
            if name != page_name:
                """if name == "Register_frame":
                    for entry in self.frames[name].entries:
                        entry.delete(0, END)"""
                self.frames[name].pack_forget()
        frame = self.frames[page_name]
        frame.pack(padx=40, pady=20, fill="both", expand="true")


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
        self.usuario = customtkinter.CTkEntry(master=self, placeholder_text="Usuario",
                                              font=("Roboto", 15),
                                              width=190, height=37)
        self.usuario.pack(padx=10, pady=30)
        self.usuario.place(relx=0.275, rely=0.2)
        self.pwd = customtkinter.CTkEntry(master=self, placeholder_text="Contraseña",
                                          font=("Roboto", 15),
                                          width=190, height=37)
        self.pwd.pack(padx=10, pady=30)
        self.pwd.place(relx=0.275, rely=0.3)
        self.nombre = customtkinter.CTkEntry(master=self, placeholder_text="Nombre",
                                             font=("Roboto", 15),
                                             width=190, height=37)
        self.nombre.pack(padx=10, pady=30)
        self.nombre.place(relx=0.275, rely=0.4)
        self.apellido = customtkinter.CTkEntry(master=self, placeholder_text="Apellido",
                                               font=("Roboto", 15),
                                               width=190, height=37)
        self.apellido.pack(padx=10, pady=30)
        self.apellido.place(relx=0.275, rely=0.5)
        self.email = customtkinter.CTkEntry(master=self, placeholder_text="E-Mail",
                                            font=("Roboto", 15),
                                            width=190, height=37)
        self.email.pack(padx=10, pady=30)
        self.email.place(relx=0.275, rely=0.6)
        self.dinero = customtkinter.CTkEntry(master=self, placeholder_text="Dinero en la cuenta",
                                             font=("Roboto", 15),
                                             width=190, height=37)
        self.dinero.pack(padx=10, pady=30)
        self.dinero.place(relx=0.275, rely=0.7)
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
        self.register_button.place(relx=0.225, rely=0.875)
        self.entries = [self.usuario, self.pwd, self.nombre, self.apellido, self.email, self.dinero]


class Register_frame_ar(Register_frame):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        self.already_registered = customtkinter.CTkLabel(master=self,
                                                         text="Usuario ya registrado",
                                                         text_color="red",
                                                         font=("Century Gothic", 15))
        self.already_registered.pack(padx=10, pady=30)
        self.already_registered.place(relx=0.32, rely=0.8)


class Main_frame(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.check_dinero = customtkinter.CTkButton(master=self, text="Ver dinero", font=("Roboto", 25),
                                                    width=250, height=60)
        self.check_dinero.pack(padx=10, pady=30)
        self.check_dinero.place(relx=0.21, rely=0.15)
        self.ingreso = customtkinter.CTkButton(master=self, text="Anotar ingreso", font=("Roboto", 25),
                                               width=250, height=60)
        self.ingreso.pack(padx=10, pady=30)
        self.ingreso.place(relx=0.21, rely=0.30)
        self.pago = customtkinter.CTkButton(master=self, text="Anotar pago", font=("Roboto", 25),
                                            width=250, height=60)
        self.pago.pack(padx=10, pady=30)
        self.pago.place(relx=0.21, rely=0.45)
        self.salir = customtkinter.CTkButton(master=self, text="Cerrar sesión", font=("Roboto", 25),
                                             width=250, height=60, fg_color="#e74c3c", hover_color="#b03a2e",
                                             command=lambda: controller.destroy())
        self.salir.pack(padx=10, pady=30)
        self.salir.place(relx=0.21, rely=0.65)
        self.borrar_user = customtkinter.CTkButton(master=self, text="Borrar usuario", font=("Roboto", 25),
                                                   width=250, height=60, fg_color="black", hover_color="#202121",
                                                   command=lambda: borrar_usuario(self.controller))
        self.borrar_user.pack(padx=10, pady=30)
        self.borrar_user.place(relx=0.21, rely=0.80)


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


def borrar_usuario(controller):
    global current_user
    db_management.delete_user(current_user)
    print(current_user)
    controller.destroy()
