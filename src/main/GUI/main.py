from interface import Interface
from database_management import db_creations
if __name__ == "__main__":
    db_creations.create()
    app = Interface()
    app.mainloop()
        