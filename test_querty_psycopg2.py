import psycopg2

def test_psycopg2():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="portfolio_db",
            user="postgres",
            password="ideapads340",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Execute a simple query
        cursor.execute("SELECT 1;")
        result = cursor.fetchone()

        print(1)

        # Check if the result is as expected
        assert result == (1,), "Expected result to be (1,)"
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    test_psycopg2()