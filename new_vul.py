from flask import Flask, render_template_string, request
import sqlite3

app = Flask(__name__)

# Example 1: SQL Injection Vulnerability
def get_user_data(user_id):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # Vulnerable SQL query
    query = f"SELECT * FROM users WHERE user_id = {user_id}"
    cursor.execute(query)

    user_data = cursor.fetchall()

    connection.close()

    return user_data

# Example 2: Cross-Site Scripting (XSS) Vulnerability
@app.route('/hello')
def hello():
    user_input = request.args.get('name', 'Guest')
    
    # Vulnerable template rendering
    html_content = f"Hello, {user_input}!"
    return render_template_string(html_content)

# Example 3: Command Injection Vulnerability
def execute_command(user_input):
    os.system(f"echo {user_input}")

if __name__ == '__main__':
    # Example 4: Insecure Random Number Generation
    insecure_random_number = os.urandom(8)

    # Example 5: Insecure Hashing
    import hashlib
    password = "password123"
    insecure_hash = hashlib.md5(password.encode()).hexdigest()

    # Example 6: Hardcoded Secret Key

    # You can add more examples as needed

    app.run()
