from sqlmodel import create_engine, Session, SQLModel

# MySQL connection string format:
# mysql+pymysql://username:password@host:port/database_name
# Example: mysql+pymysql://root:password@localhost:3306/orm_playground

# Update these with your MySQL credentials
MYSQL_USER = "root"
MYSQL_PASSWORD = "SQLnov8ING"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DATABASE = "orm_playground"

# Create the connection URL
DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

# Create engine
engine = create_engine(DATABASE_URI, echo=True)


def create_db_and_tables():
    """Create all tables defined in SQLModel models"""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Get a database session"""
    with Session(engine) as session:
        yield session
