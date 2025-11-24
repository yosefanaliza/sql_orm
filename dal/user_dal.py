from typing import Optional
from sqlmodel import Session, select, col
from models import User


def create_user(session: Session, name: str, email: str, age: Optional[int] = None):
    """CREATE - Add a new user to the database"""
    user = User(name=name, email=email, age=age)
    session.add(user)
    session.commit()
    session.refresh(user) # TODO: research this
    print(f"✓ Created user: {user.name} (ID: {user.id})")
    return user


def read_users(session: Session):
    """READ - Get all users from the database"""
    statement = select(User)
    users = session.exec(statement).all()
    print(f"\n📋 Found {len(users)} users:")
    for user in users:
        print(f"  - {user.name} ({user.email}) - Age: {user.age}, Active: {user.is_active}")
    return users


def read_user_by_id(session: Session, user_id: Optional[int]):
    """READ - Get a specific user by ID"""
    if user_id is None:
        print("\n❌ User ID cannot be None")
        return None
    user = session.get(User, user_id)
    if user:
        print(f"\n👤 User found: {user.name} ({user.email})")
    else:
        print(f"\n❌ User with ID {user_id} not found")
    return user


def read_users_by_name(session: Session, name: str):
    """READ - Get users by name (partial match)"""
    statement = select(User).where(col(User.name).contains(name))
    users = session.exec(statement).all()
    print(f"\n🔍 Found {len(users)} users matching '{name}':")
    for user in users:
        print(f"  - {user.name} ({user.email})")
    return users


def update_user(session: Session, user_id: Optional[int], **kwargs):
    """UPDATE - Modify an existing user"""
    if user_id is None:
        print("\n❌ User ID cannot be None")
        return None
    user = session.get(User, user_id)
    if not user:
        print(f"\n❌ User with ID {user_id} not found")
        return None
    
    # Update user attributes
    for key, value in kwargs.items():
        if hasattr(user, key):
            setattr(user, key, value)
    
    session.add(user)
    session.commit()
    session.refresh(user)
    print(f"✓ Updated user: {user.name} (ID: {user.id})")
    return user


def delete_user(session: Session, user_id: Optional[int]):
    """DELETE - Remove a user from the database"""
    if user_id is None:
        print("\n❌ User ID cannot be None")
        return False
    user = session.get(User, user_id)
    if not user:
        print(f"\n❌ User with ID {user_id} not found")
        return False
    
    session.delete(user)
    session.commit()
    print(f"✓ Deleted user: {user.name} (ID: {user_id})")
    return True
