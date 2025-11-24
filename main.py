from sqlmodel import Session, select, col
from db import engine, create_db_and_tables
from models import User, Car, Animal
from dal import (
    create_user,
    read_users,
    read_user_by_id,
    read_users_by_name,
    update_user,
    delete_user,
)

""""
This function demonstrates CRUD operations using SQLModel with a MySQL database.
It creates users, reads them, updates their information, and deletes a user,
"""
# def seed():
#     """Main function demonstrating all CRUD operations"""
#     print("=" * 60)
#     print("SQLModel CRUD Operations Demo with MySQL")
#     print("=" * 60)

#     # Create tables
#     print("\n📦 Creating database tables...")
#     create_db_and_tables()

#     # Create a session
#     with Session(engine) as session:
#         print("\n" + "=" * 60)
#         print("CREATE Operations")
#         print("=" * 60)

#         # Create multiple users
#         user1 = create_user(session, "Alice Johnson", "alice@example.com", 28)
#         user2 = create_user(session, "Bob Smith", "bob@example.com", 35)
#         user3 = create_user(session, "Charlie Brown", "charlie@example.com", 42)
#         user4 = create_user(session, "Diana Prince", "diana@example.com", 30)

#         print("\n" + "=" * 60)
#         print("READ Operations")
#         print("=" * 60)

#         # Read all users
#         read_users(session)

#         # Read user by ID
#         read_user_by_id(session, user1.id)

#         # Search users by name
#         read_users_by_name(session, "Johnson")

#         print("\n" + "=" * 60)
#         print("UPDATE Operations")
#         print("=" * 60)

#         # Update a user
#         update_user(session, user2.id, age=36, is_active=False)
#         update_user(session, user3.id, name="Charlie Brown Jr.")

#         # Read all users to see updates
#         read_users(session)

#         print("\n" + "=" * 60)
#         print("DELETE Operations")
#         print("=" * 60)

#         # Delete a user
#         delete_user(session, user4.id)

#         # Read all users to see deletion
#         read_users(session)

#         print("\n" + "=" * 60)
#         print("Advanced READ Operations")
#         print("=" * 60)

#         # Find active users
#         statement = select(User).where(User.is_active == True)
#         active_users = session.exec(statement).all()
#         print(f"\n✓ Active users: {len(active_users)}")
#         for user in active_users:
#             print(f"  - {user.name}")

#         # Find users older than 30
#         statement = select(User).where(col(User.age).is_not(None), col(User.age) > 30)
#         older_users = session.exec(statement).all()
#         print(f"\n✓ Users older than 30: {len(older_users)}")
#         for user in older_users:
#             print(f"  - {user.name} (Age: {user.age})")

#     print("\n" + "=" * 60)
#     print("Demo completed!")
#     print("=" * 60)


if __name__ == "__main__":

    # seed()

    with Session(engine) as session:
        statement = select(User)
        users = session.exec(statement).all()
        print(f"\n📋 Found {len(users)} users:")
        for user in users:
            print(
                f"  - {user.name} ({user.email}) - Age: {user.age}, Active: {user.is_active}"
            )
