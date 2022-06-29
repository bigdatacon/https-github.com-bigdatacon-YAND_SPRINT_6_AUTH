#docker run --name auth-postgres -d --rm -e POSTGRES_PASSWORD=123 -p 5432:5432 postgres

from db_models import  User, Group
import datetime
import uuid
from app import create_app, db

app = create_app()

with app.app_context():
    #данные для заполнения User- почему то id не заполняется
    id = uuid.uuid4()
    login = "first_user"
    email = "firstuser@ya.ru"
    # password_hash = "fff"
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
        # password_hash=password_hash,
        full_name=full_name,
        phone=phone,
        avatar_link=avatar_link,
        address=address,
        created_at=created_at,
        updated_at=updated_at
    )

    # Set password separately because we want to specify password, not password hash
    new_user.password = '123'

    #Данные для заполения Групп
    id = uuid.uuid4()
    name ='base_group'
    description = 'baseGroupdescr'

    new_group = Group(
        id = id,
        name=name,
        description=description,
    )
    # print(new_user.id, new_group.id)
    db.session.add(new_user)
    db.session.add(new_group)
    db.session.commit()

    print(new_user.id, new_group.id)