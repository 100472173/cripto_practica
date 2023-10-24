from interface import Interface
from database_management import db_creations

db_creations.create()
app = Interface()
app.mainloop()