from logging.config import fileConfig
import sqlalchemy as sa
from sqlalchemy import engine_from_config, pool
from models.engine.db_storage import DBStorage  # Import your DBStorage class
from alembic import context

# Create an instance of DBStorage to access the database engine
db_storage = DBStorage()

# Create a session using the __create_session method
session = db_storage._DBStorage__create_session()

# Import all your model classes from the 'models' directory
from models.user import User
from models.task import Task
from models.family import Family
from models.notification import Notification  # Import all your model classes

# Initialize an empty list to store metadata objects for each model
metadata_objects = []

# Add metadata objects for each model to the list
metadata_objects.append(User.metadata)
metadata_objects.append(Task.metadata)
metadata_objects.append(Family.metadata)
metadata_objects.append(Notification.metadata)

# Create a new Metadata object
target_metadata = sa.MetaData()

# Loop through each metadata object and add the tables to the new target_metadata
for metadata in metadata_objects:
    for table in metadata.sorted_tables:
        # Handle None schema gracefully
        schema = table.schema if table.schema is not None else ''
        target_metadata._add_table(schema, table.name, table)

# Bind the target_metadata to a database engine
target_metadata.bind = db_storage._DBStorage__engine

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

# The rest of the script remains the same as provided earlier.


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

# The rest of the script remains the same as provided earlier.


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
