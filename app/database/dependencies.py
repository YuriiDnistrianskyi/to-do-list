from .database import async_session

def get_async_session():
    with async_session() as session:
        yield session
