import customtkinter
from interface import Interface


class Main_interface(Interface):
    def __init__(self):
        super().__init__()
        self.main_frame = customtkinter.CTkFrame(master=self,
                                                 width=400,
                                                 height=400)
        self.main_frame.pack(padx=40, pady=20, fill="both", expand="true")
        self.check_dinero = customtkinter.CTkButton(master=self.main_frame, text="Ver dinero", font=("Roboto", 25),
                                                    width=250, height=60)
        self.check_dinero.pack(padx=10, pady=30)
        self.check_dinero.place(relx=0.21, rely=0.15)
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
        self.salir.place(relx=0.21, rely=0.65)
