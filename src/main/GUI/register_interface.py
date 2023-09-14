import customtkinter
from interface import Interface


class Register_interface(Interface):
    def __init__(self):
        super().__init__()
        self.register_frame = customtkinter.CTkFrame(master=self,
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

