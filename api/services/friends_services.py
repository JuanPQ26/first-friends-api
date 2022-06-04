from api.utils import db


def get_all_friends() -> list | None:
    found = db.execute_postgres_select(
        "SELECT id, fullname, telephone, created, updated FROM friends LIMIT 1000", one=False)

    return found


def get_one_friend(friend_id: int) -> dict | None:
    if not friend_id:
        return None

    found = db.execute_postgres_select(
        f"SELECT id, fullname, telephone, created, updated From friends WHERE id = {friend_id}", one=True)
    return found


def create_friend(fullname: str, telephone: str) -> bool:
    try:
        db.execute_postgres_query(
            f"INSERT INTO friends (fullname, telephone) VALUES ('{fullname}', '{telephone}')")
        return True
    except Exception as e:
        print("Error:", str(e))
        return False


def update_friend(friend_id: int, new_fullname=None, new_telephone=None) -> bool:
    try:
        if new_fullname and not new_telephone:
            db.execute_postgres_query(
                f"UPDATE friends SET fullname = '{new_fullname}', updated = current_timestamp WHERE id = {friend_id}")
            return True

        if not new_fullname and new_telephone:
            db.execute_postgres_query(
                f"UPDATE friends SET telephone = '{new_telephone}', updated = current_timestamp WHERE id = {friend_id}")
            return True

        query = f"UPDATE friends " \
                f"SET fullname='{new_fullname}', telephone='{new_telephone}', updated = current_timestamp " \
                f"WHERE id = {friend_id}"

        db.execute_postgres_query(query)

        return True
    except Exception as e:
        print("Error:", str(e))
        return False


def delete_friend(friend_id: int) -> bool:
    try:
        db.execute_postgres_query(
            f"DELETE FROM friends WHERE id = {friend_id}")

        return True
    except Exception as e:
        print("Error:", str(e))
        return False
