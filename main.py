from flask import Flask,request,jsonify
from flask_cors import CORS
import smtplib
app=Flask(__name__)
CORS(app)
@app.route('/sendemail',methods=['POST'])
def SendEamail():
  data=request.get_json()
  server = smtplib.SMTP('smtp.gmail.com', 587)

# Identify yourself
  server.ehlo()

# Start TLS encryption
  server.starttls()

# Login (use app password, not real password)
  server.login('shyammmmm85@gmail.com', 'wbzsuggwtncmddoi')

# Email content
  from_address = 'shyammmmm85@gmail.com'
  to_address = 'harshagumpathi1331@gmail.com'

  message=data.get('message') +''+data.get('email')


# Send email
  server.sendmail(from_address, to_address, message)

# Close connection
  server.quit()
  return jsonify({
    "message":"Email send sucessfully"
  })

  print("Email sent successfully!")
if __name__=="__main__":
   port = int(os.environ.get("PORT", 5000))  # ← this fixes Render
   app.run(host="0.0.0.0", port=port)

