from flask import Flask, jsonify, request 
from flask_cors import CORS
from model import DriverLicenseModel

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/receive_driverLicenseID", methods=["POST"])
def receive_driverLicenseID():
    dl = DriverLicenseModel()
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400
        
        req_data = request.get_json()

        if 'driverLicenseID' not in req_data:
            return jsonify({"error": "'driverLicenseID' key is missing"}), 400
        
        driverLicenseID = req_data['driverLicenseID']

        if result := dl.get_specific_driver_license(driverLicenseID):

            driverLicense = {
                "DriverLicenseID": result[0],
                "DriverTypeID": result[1],
                "DriverTypeName": result[2],
                "BirthDay": result[3],
                "MonthID": result[4],
                "MonthName": result[5],
                "BirthYear": result[6],
                "StatusDriverID": result[7],
                "StatusName": result[8]
            }
            return jsonify(driverLicense), 200

        else:
            return jsonify({"error": "DriverLicense not found"}), 404
    else:
        return jsonify({"error": "request method is not POST"}), 404

@app.route("/change_status_driverLicense", methods=["POST"])
def change_status_driverLicense():
    dl = DriverLicenseModel()
    
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400
        
        req_data = request.get_json()

        if 'driverLicenseID' not in req_data:
            return jsonify({"error": "'driverLicenseID' key is missing"}), 400
        
        if 'driverTypeID' not in req_data:
            return jsonify({"error": "'driverTypeID' key is missing"}), 400
        
        print(req_data)
        driverLicenseID = req_data['driverLicenseID']['DriverLicenseID']
        if dl.get_specific_driver_license(driverLicenseID):
            driverTypeID = req_data['driverTypeID']

            dl.change_status_driver_license(driverLicenseID, driverTypeID)

            return jsonify({"status": "success"}), 200

        else:
            return jsonify({"error": "DriverLicense not found"}), 404
    else:
        return jsonify({"error": "request method is not POST"}), 404

@app.route("/get_report_driver_type", methods=["GET"])
def get_report_driver_type():
    dl = DriverLicenseModel()
    if result := dl.get_report_driver_type_number():
        return jsonify(result), 200
    else:
        return jsonify({"error": "No data found"}), 404

@app.route("/get_report_status_driver", methods=["GET"])
def get_report_status_driver():
    dl = DriverLicenseModel()
    if result := dl.get_report_status_driver_number():
        return jsonify(result), 200
    else:
        return jsonify({"error": "No data found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')