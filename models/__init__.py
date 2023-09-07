from os import getenv

# Get the storage type configuration
storage_t = getenv('FAMEC_TYPE_STORAGE')

if storage_t == "db":
    # Import the DBStorage class when needed
    from models.engine.db_storage import DBStorage
    storage = DBStorage()  # Create an instance of the DBStorage class

# storage.reload()  # Reload the storage instance