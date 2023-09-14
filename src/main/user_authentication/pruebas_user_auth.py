import user_auth
import re
from database_management import db_management
from database_management import db_creations
db_creations.create()
username = "12j4"
print(user_auth.check_username_syntax(username))

validation_pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[~@_/:+]).{8,}$"
myreg = re.compile(validation_pattern)
print(myreg.fullmatch("Alo123!!"))
db_management.insert_new_user("Juan","lelele")
user_auth.check_pwd_syntax("lllAolo12!")