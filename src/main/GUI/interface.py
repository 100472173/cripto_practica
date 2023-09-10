import tkinter
import customtkinter

app = tkinter.Tk()
app.geometry("500x500")
customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")

frame = customtkinter.CTkFrame(master=app)
frame.pack(pady = 20, padx = 60, fill="both", expand=True)

label = customtkinter.CTkLabel(app, text="Inicio de sesión", fg_color="transparent", text_color="black")
label.pack(pady=12, padx=10)

app.mainloop()