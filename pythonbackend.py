from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
import os

app = Flask(__name__)
CORS(app)

@app.route('/sendemail', methods=['POST'])
def SendEmail():
    data = request.get_json()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(
        os.environ.get("EMAIL_USER"),
        os.environ.get("EMAIL_PASS")
    )

    from_address = os.environ.get("EMAIL_USER")
    to_address = data.get("to")

    message = """Subject: Test Email

Hello from deployed Flask API 🚀
"""

    server.sendmail(from_address, to_address, message)
    server.quit()

    return jsonify({"message": "Email sent successfully"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
