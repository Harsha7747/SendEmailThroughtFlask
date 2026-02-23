from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
import os

app = Flask(__name__)
CORS(app)
@app.route('/',methods=['POST'])
def Helloe():
    return jsonify({"message": "connection sent successfully"})
@app.route('/sendemail', methods=['POST'])
def SendEmail():
    data = request.get_json()

    server = smtplib.SMTP('smtp.gmail.com', 465)
    server.ehlo()
    server.starttls()
    server.login('shyammmmm85@gmail.com', 'wbzsuggwtncmddoi')

    from_address = 'shyammmmm85@gmail.com'
    to_address = 'harshagumpathi1331@gmail.com'
    message = data.get('message', '') + ' ' + data.get('email', '')

    server.sendmail(from_address, to_address, message)
    server.quit()

    return jsonify({"message": "Email sent successfully"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)




