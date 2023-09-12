""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy import func

from models.base_model import Base

class DBStorage:
    def __init__(self):
        self.__engine = None
        self.__session = None
        self.__setup_engine()
        self.__create_session()  # Initialize the session

    def __setup_engine(self):
        user = getenv('FAMEC_MYSQL_USER')
        db_password = getenv('FAMEC_MYSQL_PWD')
        database = getenv('FAMEC_MYSQL_DB')
        host = getenv('FAMEC_MYSQL_HOST')
        env = getenv('FAMEC_ENV')

        self.__engine = create_engine(
            # f'mysql://ud6sirijm7wdl4f2:Xs9ZWyCFUdBM9txRCaCV@bgxgrxrrto5z8iklihyz-mysql.services.clever-cloud.com:3306/bgxgrxrrto5z8iklihyz',
            f'mysql+mysqldb://{user}:{db_password}@{host}/{database}',
            pool_pre_ping=True
        )


        if env == 'test':
            Base.metadata.drop_all(self.__engine)
        else:
            Base.metadata.create_all(self.__engine)


    def __create_session(self):
        if self.__session is None:
            sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
            self.__session = scoped_session(sec)
        return self.__session()

    def all(self, cls=None):
        session = self.__create_session()
        objects = {}
        
        if cls is None:
            from models.user import User # Import all model classes here
            from models.base_model import BaseModel # Import all model classes here
            from models.note import Note # Import all model classes here
            from models.notification import Notification # Import all model classes here
            from models.task import Task # Import all model classes here
            from models.user_info import UserInfo # Import all model classes here
            cls_list = [User, BaseModel, Note, Notification, Task, UserInfo]
        else:
            cls_list = [cls]
        
        for cls in cls_list:
            query = session.query(cls)
            for element in query:
                key = f"{cls.__name__}.{element.id}"
                objects[key] = element
        
        return objects

    def new(self, obj):
        session = self.__create_session()
        session.add(obj)

    def save(self):
        session = self.__create_session()
        session.commit()

    def delete(self, obj=None):
        session = self.__create_session()
        if obj:
            session.delete(obj)
    def update(self, obj):
        session = self.__create_session()
        session.merge(obj)  # Use the merge method to update the object
        session.commit()

    def count_distinct_notifications(self, family_id):
        from models.notification import Notification  # Import the Notification model
        session = self.__create_session()  # Create a session

        # Query for distinct notifications by content and family_id
        query = session.query(func.count(Notification.id.distinct())).filter(
            Notification.recipient_id == family_id,
            Notification.is_read == False  # Adjust this condition as needed
        )

        count = query.scalar()  # Get the count of distinct notifications
        return count  # Return the count

    def count(self, class_name, id):
        import importlib
        # Import the module containing the class dynamically
        module = importlib.import_module('models.' + class_name.lower())
        # Get the class from the module
        cls = getattr(module, class_name)
        session = self.__create_session()
        query = session.query(cls).filter_by(family_id=id, status=0).all()
        count = len(query)  # count the objects in the list
        return count

    def find_user_by_email(self, email):
        from models.user import User
        session = self.__create_session()
        query = session.query(User).filter_by(email=email).first()
        return query
    
    def find_family_name(self, id):
        from models.family import Family
        session = self.__create_session()
        query = session.query(Family).filter_by(id=id).first()
        return query

    def find_user_by_id(self, id):
        from models.user import User
        session = self.__create_session()
        query = session.query(User).filter_by(id=id).first()
        return query
    
    def get_task_by_id(self, id):
        from models.task import Task
        session = self.__create_session()
        query = session.query(Task).filter_by(id=id).first()
        return query
    def get_task(self, id):
        from models.task import Task
        session = self.__create_session()
        query = session.query(Task).filter_by(
            family_id=id,
            status=0
            ).order_by(Task.created_at.desc()).limit(3).all()
        return query
    
    def get_all_families(self, id):
        from models.user import User
        session = self.__create_session()
        query = session.query(User).filter_by(family_id=id).all()
        return query
    
    def get_family_by_id(self, id):
        from models.family import Family
        session = self.__create_session()
        query = session.query(Family).filter_by(owner_id=id).first()
        return query
    
    def get_notifications(self, id):
        from models.notification import Notification
        session = self.__create_session()
        query = session.query(Notification).filter_by(recipient_id=id).all()
        return query

    # def find_item_by_id(self, model_name, id):
    #     try:
    #         # Attempt to import the model dynamically
    #         model_module = __import__(f'models.{model_name}', fromlist=[model_name])
    #         model_class = getattr(model_module, model_name)
    #     except ImportError:
    #         return None  # Model import failed

    #     session = self.__create_session()
    #     query = session.query(model_class).filter_by(id=id).first()
    #     # USAGE
    #     # user = find_item_by_id('User', user_id)
    #     # task = find_item_by_id('Task', task_id)
    #     return query

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__create_session()

    def close(self):
        if self.__session:
            self.__session.remove()