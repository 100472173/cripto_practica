from interface import Interface
from database_management import db_creations
from database_management import db_destroy

db_creations.create()
app = Interface()
app.mainloop()