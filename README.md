# SQLModel CRUD Operations with MySQL

This project demonstrates CRUD (Create, Read, Update, Delete) operations using SQLModel with a MySQL database.

## Setup

### 1. Install Dependencies
```bash
pip install sqlmodel pymysql
```

### 2. Configure MySQL Database
Update the connection details in `database.py`:
```python
MYSQL_USER = "root"
MYSQL_PASSWORD = "your_password"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DATABASE = "orm_playground"
```

### 3. Create the Database
Make sure you have MySQL running and create the database:
```sql
CREATE DATABASE orm_playground;
```

## Project Structure

- **database.py** - Database connection and session management
- **models.py** - SQLModel table definitions
- **main.py** - CRUD operation examples and demo

## Running the Demo

```bash
python main.py
```

## CRUD Operations

### CREATE
```python
user = User(name="John Doe", email="john@example.com", age=30)
session.add(user)
session.commit()
session.refresh(user)
```

### READ
```python
# Get all users
statement = select(User)
users = session.exec(statement).all()

# Get user by ID
user = session.get(User, user_id)

# Filter users
statement = select(User).where(User.age > 30)
older_users = session.exec(statement).all()
```

### UPDATE
```python
user = session.get(User, user_id)
user.age = 31
session.add(user)
session.commit()
session.refresh(user)
```

### DELETE
```python
user = session.get(User, user_id)
session.delete(user)
session.commit()
```

## Features Demonstrated

- ✅ Database connection with MySQL
- ✅ Table creation with SQLModel
- ✅ Create operations
- ✅ Read operations (all, by ID, with filters)
- ✅ Update operations
- ✅ Delete operations
- ✅ Session management
- ✅ Query filtering and searching

## Resources

- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [SQLModel Tutorial](https://sqlmodel.tiangolo.com/tutorial/)
