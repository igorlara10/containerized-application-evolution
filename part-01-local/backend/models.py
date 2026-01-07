from database import get_connection

def create_user(name: str, cpf: str):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO users (name, cpf)
        VALUES (%s, %s)
        RETURNING id, name, cpf, created_at;
    """

    cursor.execute(query, (name, cpf))
    user = cursor.fetchone()

    conn.commit()
    cursor.close()
    conn.close()

    return user
