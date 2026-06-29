import sqlite3


DATABASE_PATH = "database/scholar.db"


def create_connection():

    connection = sqlite3.connect(DATABASE_PATH)

    return connection



def create_table():

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS universities (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        country TEXT,

        website TEXT,

        program TEXT,

        tuition TEXT,

        deadline TEXT,

        requirements TEXT,

        notes TEXT,

        status TEXT

    )
    """)


    connection.commit()

    connection.close()



create_table()

def add_university(
        name,
        country,
        website,
        program,
        tuition,
        deadline,
        requirement,
        notes,
        status
):
    
    connection = create_connection()

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO universities
    (
    name,
    country,
    website,
    program,
    tuition,
    deadline,
    requirements,
    notes,
    status
    )

    VALUES (?,?,?,?,?,?,?,?,?)        
    """,
    (
        name,
        country,
        website,
        program,
        tuition,
        deadline,
        requirement,
        notes,
        status

    )
    )

    connection.commit()
    connection.close()


add_university(
    "Massachusetts Institute of Technology",
    "USA",
    "https://mit.edu",
    "MS Computer Science",
    "$60000",
    "December",
    "GRE optional, TOEFL",
    "Strong AI research",
    "Interested"
)


def update_university(
        university_id,
        name,
        country,
        website,
        program,
        tuition,
        deadline,
        requirements,
        notes,
        status
):

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute("""
    UPDATE universities

    SET

    name=?,
    country=?,
    website=?,
    program=?,
    tuition=?,
    deadline=?,
    requirements=?,
    notes=?,
    status=?

    WHERE id=?

    """,
    (
        name,
        country,
        website,
        program,
        tuition,
        deadline,
        requirements,
        notes,
        status,
        university_id
    ))


    connection.commit()

    connection.close()


def get_universities():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "Select * From universities"
    )

    data = cursor.fetchall()

    connection.close()


    return data


def get_university_by_id(university_id):

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute(
        "SELECT * FROM universities WHERE id=?",
        (university_id,)
    )


    university = cursor.fetchone()


    connection.close()


    return university

def delete_university(university_id):

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute(
        "DELETE FROM universities WHERE id=?",
        (university_id,)
    )


    connection.commit()

    connection.close()


def update_university(
        university_id,
        name,
        country,
        website,
        program,
        tuition,
        deadline,
        requirements,
        notes,
        status
):

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute("""
        UPDATE universities

        SET
        name=?,
        country=?,
        website=?,
        program=?,
        tuition=?,
        deadline=?,
        requirements=?,
        notes=?,
        status=?

        WHERE id=?

    """,
    (
        name,
        country,
        website,
        program,
        tuition,
        deadline,
        requirements,
        notes,
        status,
        university_id
    ))


    connection.commit()

    connection.close() 
