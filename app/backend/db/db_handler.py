# app/backend/db/db_handler.py

# Import necessary modules
from sqlmodel.ext.asyncio.session import AsyncSession                    # Importing AsyncSession for asynchronous database operations
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine      # Importing AsyncEngine and create_async_engine for creating the async engine
from sqlalchemy.orm import sessionmaker                                  # Importing sessionmaker for creating session factories
from typing import AsyncGenerator                                        # Importing AsyncGenerator for asynchronous generators
from ..config import db_settings                                         # Importing db_settings for database settings

# ---------------------------------------------------------------------------------------------------------------------------------------------------- #

# Creates the asynchronous database engine, this engine manages the connection pool to your database in an async way.
engine:AsyncEngine = create_async_engine(
                                            db_settings.database_url,    # Database connection string from config
                                            echo = True,                 # Enable SQL query logging for debugging    
                                        )

# ---------------------------------------------------------------------------------------------------------------------------------------------------- #

# Creates a session factory bound to the async engine, this factory will generate AsyncSession instances when called.
async_session = sessionmaker(
                                bind=engine,                # Use the previously created engine       
                                expire_on_commit = False,   # Prevent objects from expiring after commit (keep them usable)
                                class_ = AsyncSession       # Use async session for async DB operations
                            )

# ---------------------------------------------------------------------------------------------------------------------------------------------------- #

# Async function to initialize the database schema
async def init_db():
    """ Starts a connection context with the engine
    This is where you can run database migrations or create tables """

    if engine is None:
        print("Database engine is not initialized.")
        return
    
    try:
        async with engine.begin() as conn:
            print("Database connection initialized successfully.")
            
            # NOTE: Uncomment this line only if you want to create the tables automatically.
            # It's unsafe to run if your database already has data because it can overwrite or cause errors.

            # await conn.run_sync(SQLModel.metadata.create_all)
            
    except Exception as e:
        print(f"Database initialization failed: {e}")

# ---------------------------------------------------------------------------------------------------------------------------------------------------- #

# Async funcion to close the database connection
async def close_db():
    """ Close the engine connection pool
    This is important to release resources when the app stops or no longer needs the database connection
    It ensures that all connections are properly closed and cleaned up. """
    
    if engine is None:
        print("No database engine to close.")
        return
    
    try:
        await engine.dispose()
        print("Database connection closed successfully.")
    except Exception as e:
        print(f"Error closing database connection: {e}")

# ---------------------------------------------------------------------------------------------------------------------------------------------------- #

# Async function that yields a database session for API routes, it's a context manager basically
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    
    # Opens a session context with the session factory
    async with async_session() as session:   
        # NOTE: "Yield" means the function gives back the session object temporarily, allowing the caller to use it and then resume the function after.
        yield session  

# ---------------------------------------------------------------------------------------------------------------------------------------------------- #        