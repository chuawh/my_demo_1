from flask import Flask, request, jsonify
import random
import os


app = Flask(__name__)

#Application 
APP_ID = os.getenv("SENDBIRD_APP_ID")
API_TOKEN = os.getenv("SENDBIRD_API_TOKEN")
AI_Agent_ID = os.getenv("SENDBIRD_AI_Agent_ID")


def generate_ticket_id():
    """Generate a random ticket_ID in the format Finance-XXX"""
    random_number = random.randint(100, 999)  # Generate a 3-digit number
    return f"Finance-{random_number}" #Finance

def generate_transaction_id():
    """Generate a random ticket_ID in the format Finance-XXX"""
    random_number = random.randint(100000, 999999)  # Generate a 6-digit number
    return f"{random_number}"

@app.route('/adjust_payment', methods=['POST'])
def adjust_payment():
    data = request.get_json()
    print("request: ", data)

    ticket_id = generate_ticket_id()

    # Simulated adjustment logic
    return jsonify({
         "ticket_ID": ticket_id,
         "Subject": "Excess payment - Adjust",
         "Description": "Mistakenly paid extra amount to semester II fee. Adjust the excess amount in next semester fee",
         "Reporter": data["name"],
         "Enrollment_ID": data["enrollment_id"]
    }), 200

@app.route('/refund_payment', methods=['POST'])
def refund_payment():
    data = request.get_json()
    print("request: ", data)
    

    ticket_id = generate_ticket_id()

    # Simulated refund logic
    return jsonify({
         "ticket_ID": ticket_id,
         "Subject": "Excess payment - Refund",
         "Description": "Mistakenly paid extra amount to semester II fee.refund the excess fee",
         "Reporter": data["name"],
         "Enrollment_ID": data["enrollment_id"]
    }), 200

@app.route('/validate_payment', methods=['POST', 'GET'])
def validate_payment():
    data = request.get_json()
    print("request: ", data)

    transaction_id = generate_transaction_id()
    
    # Simulated validation logic
    return jsonify({
        "Student Name": data["name"],
        "Enrollment_ID": data["enrollment_id"],
        "transaction_id": transaction_id,
        "status": "Paid",
        "Amount": "20,000 INR"
    }), 200
  

@app.route('/create_ticket', methods=['POST'])
def create_ticket():
    
        data = request.get_json()
        print("request: ", data)
        
        ticket_id = generate_ticket_id()
        
        return jsonify({
            "ticket_ID": ticket_id,
            "Subject":"Request for payment invoice",
            "Reporter": data["name"],
            "Enrollment_ID": data["enrollment_id"],
            "status": "Open",
            "Assigned": "Guarav"
        }), 200
    

@app.route('/send_syllabus', methods=['POST'])
def send_syllabus():
    
        data = request.get_json()
        print("request: ", data)
        channel_url = data["channel_url"]

        
        url = f"https://api-{APP_ID}.sendbird.com/v3/group_channels/{channel_url}/messages"
        headers = {
          "Api-Token": API_TOKEN,
          "Content-Type": "application/json"
        }
        payload = {
            "message_type": "FILE",
            "user_id": AI_Agent_ID,
            "files": {
               "url": "https://drive.google.com/file/d/19bjgrVVLJUaFZBaCHlo4cO9KThm3bY-s/view?usp=sharing",
               "file_name": "Syllabus",
               "file_type": "pdf"
            },
        }



if __name__=='__main__':
    app.run(debug=True,port='9091')
