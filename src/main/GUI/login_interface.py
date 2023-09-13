from interface import Interface
import customtkinter


class Login_interface(Interface):
    def __init__(self):
        super().__init__()
        self.login_frame = customtkinter.CTkFrame(master=self,
                                                  width=400,
                                                  height=400)
        self.login_frame.pack(padx = 40, pady= 20, fill="both", expand= "true")
        self.titulo = customtkinter.CTkLabel(master=self.login_frame,
                                             text = "Inicio de sesión",
                                             text_color="black",
                                             font = ("Century Gothic", 40))
        self.titulo.pack(padx = 10, pady= 30)
        self.usuario = customtkinter.CTkEntry(master=self.login_frame, placeholder_text="Usuario", font=("Roboto", 15), width=190, height= 37)
        self.usuario.pack(padx= 10, pady = 30)
        self.usuario.place(relx = 0.275, rely= 0.25)
        self.pwd = customtkinter.CTkEntry(master=self.login_frame, placeholder_text="Contraseña", font=("Roboto", 15),
                                              width=190, height=37)
        self.pwd.pack(padx=10, pady=30)
        self.pwd.place(relx=0.275, rely=0.375)
        self.login_button = customtkinter.CTkButton(master=self.login_frame, text="Iniciar sesión", font=("Roboto", 15),
                                          width=190, height=37)
        self.login_button.pack(padx=10, pady=30)
        self.login_button.place(relx=0.275, rely=0.5)
        self.new_user_button = customtkinter.CTkButton(master=self.login_frame, text="¿Eres un nuevo usuario? Registráte aquí", font=("Roboto", 15),
                                                    width=200, height=30, fg_color="#5dade2")
        self.new_user_button.pack(padx=10, pady=30)
        self.new_user_button.place(relx=0.16, rely=0.625)

app = Login_interface()
app.mainloop()