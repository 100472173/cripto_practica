import tkinter
import customtkinter


class Interface(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("My Balance")
"""        self.frame = Login_frame()
"""
"""
class Login_frame():
    def __init__(self):
        self.login_frame = customtkinter.CTkFrame(master=Interface(),
                                                  width=400,
                                                  height=400)
        self.login_frame.pack(padx=40, pady=20, fill="both", expand="true")
        self.titulo = customtkinter.CTkLabel(master=self.login_frame,
                                             text="Inicio de sesión",
                                             text_color="black",
                                             font=("Century Gothic", 40))
        self.titulo.pack(padx=10, pady=30)
        self.usuario = customtkinter.CTkEntry(master=self.login_frame, placeholder_text="Usuario", font=("Roboto", 15),
                                              width=190, height=37)
        self.usuario.pack(padx=10, pady=30)
        self.usuario.place(relx=0.275, rely=0.25)
        self.pwd = customtkinter.CTkEntry(master=self.login_frame, placeholder_text="Contraseña", font=("Roboto", 15),
                                          width=190, height=37)
        self.pwd.pack(padx=10, pady=30)
        self.pwd.place(relx=0.275, rely=0.375)
        self.login_button = customtkinter.CTkButton(master=self.login_frame, text="Iniciar sesión", font=("Roboto", 15),
                                                    width=190, height=37)
        self.login_button.pack(padx=10, pady=30)
        self.login_button.place(relx=0.275, rely=0.5)
        self.new_user_button = customtkinter.CTkButton(master=self.login_frame,
                                                       text="¿Eres un nuevo usuario? Registráte aquí",
                                                       font=("Roboto", 15),
                                                       width=200, height=30, fg_color="#5dade2")
        self.new_user_button.pack(padx=10, pady=30)
        self.new_user_button.place(relx=0.16, rely=0.625)

class Register_frame():
    def __init__(self):
        self.register_frame = customtkinter.CTkFrame(master=Interface(),
                                                     width=400,
                                                     height=400)
        self.register_frame.pack(padx=40, pady=20, fill="both", expand="true")
        self.titulo = customtkinter.CTkLabel(master=self.register_frame,
                                             text="Registro de usuario",
                                             text_color="black",
                                             font=("Century Gothic", 40))
        self.titulo.pack(padx=10, pady=30)
        self.usuario = customtkinter.CTkEntry(master=self.register_frame, placeholder_text="Usuario", font=("Roboto", 15),
                                              width=190, height=37)
        self.usuario.pack(padx=10, pady=30)
        self.usuario.place(relx=0.275, rely=0.2)
        self.pwd = customtkinter.CTkEntry(master=self.register_frame, placeholder_text="Contraseña", font=("Roboto", 15),
                                          width=190, height=37)
        self.pwd.pack(padx=10, pady=30)
        self.pwd.place(relx=0.275, rely=0.3)
        self.nombre = customtkinter.CTkEntry(master=self.register_frame, placeholder_text="Nombre",
                                          font=("Roboto", 15),
                                          width=190, height=37)
        self.nombre.pack(padx=10, pady=30)
        self.nombre.place(relx=0.275, rely=0.4)
        self.apellido = customtkinter.CTkEntry(master=self.register_frame, placeholder_text="Apellidos",
                                             font=("Roboto", 15),
                                             width=190, height=37)
        self.apellido.pack(padx=10, pady=30)
        self.apellido.place(relx=0.275, rely=0.5)
        self.email = customtkinter.CTkEntry(master=self.register_frame, placeholder_text="E-Mail",
                                               font=("Roboto", 15),
                                               width=190, height=37)
        self.email.pack(padx=10, pady=30)
        self.email.place(relx=0.275, rely=0.6)
        self.dinero = customtkinter.CTkEntry(master=self.register_frame, placeholder_text="Dinero en la cuenta",
                                               font=("Roboto", 15),
                                               width=190, height=37)
        self.dinero.pack(padx=10, pady=30)
        self.dinero.place(relx=0.275, rely=0.7)
        self.register_button = customtkinter.CTkButton(master=self.register_frame, text="Registrar usuario", font=("Roboto", 15),
                                                    width=225, height=37)
        self.register_button.pack(padx=10, pady=30)
        self.register_button.place(relx=0.225, rely=0.825)

class Main_frame():
    def __init__(self):
        self.main_frame = customtkinter.CTkFrame(master=Interface(),
                                                  width=400,
                                                  height=400)
        self.main_frame.pack(padx = 40, pady= 20, fill="both", expand= "true")
        self.check_dinero = customtkinter.CTkButton(master=self.main_frame, text="Ver dinero", font=("Roboto", 25), width=250, height=60)
        self.check_dinero.pack(padx= 10, pady = 30)
        self.check_dinero.place(relx = 0.21, rely= 0.15)
        self.ingreso = customtkinter.CTkButton(master=self.main_frame, text="Anotar ingreso", font=("Roboto", 25),
                                              width=250, height=60)
        self.ingreso.pack(padx=10, pady=30)
        self.ingreso.place(relx=0.21, rely=0.30)
        self.pago = customtkinter.CTkButton(master=self.main_frame, text="Anotar pago", font=("Roboto", 25),
                                          width=250, height=60)
        self.pago.pack(padx=10, pady=30)
        self.pago.place(relx=0.21, rely=0.45)
        self.salir = customtkinter.CTkButton(master=self.main_frame, text="Cerrar sesión", font=("Roboto", 25),
                                                    width=250, height=60, fg_color="#e74c3c", hover_color="#b03a2e")
        self.salir.pack(padx=10, pady=30)
        self.salir.place(relx=0.21, rely=0.65)"""