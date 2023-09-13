import db_management
#xd
import db_creations
db_creations.create()
db_management.insert_new_user("Juan","pedrito1233")
print(db_management.search_user("Juan"))
print(db_management.get_acc_money("Juan"))




