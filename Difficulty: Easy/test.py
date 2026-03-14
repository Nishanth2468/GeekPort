# This is a bad hardcoded secret!
API_KEY = "sk-ant-api03-abcdef1234567890abcdef"

def get_user_data(user_id):
    # This is a SQL injection vulnerability
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    return db.execute(query)
