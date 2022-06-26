from db_models import  User, Group
import datetime

#данные для заполнения User- почему то id не заполняется
id = 'ffdg4564g56sd4fs6dgs'
login = "first_user"
email = "firstuser@ya.ru"
password_hash = "fff"
full_name = "first_useruu"
phone = "123456789"
avatar_link = 'firstuser@ya.ru'
address = 'MSC'
created_at = datetime.datetime.now()
updated_at = datetime.datetime.now()

new_user = User(
    id = id,
    login=login,
    email=email,
    password_hash=password_hash,
    full_name=full_name,
    phone=phone,
    avatar_link=avatar_link,
    address=address,
    created_at=created_at,
    updated_at=updated_at
)

#Данные для заполения Групп
id = 'fdsfgsdgsgdg54564646'
name ='base_group'
description = 'baseGroupdescr'

new_group = Group(
    id = id,
    name=name,
    description=description,
)

print(new_user.id, new_group.id)