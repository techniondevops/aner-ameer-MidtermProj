from flask import Flask, request, jsonify
from flask_cors import CORS

  # Ensure the Python_code directory is in the path
import Python_code.LeadsManager as LeadsManager

app = Flask(__name__)
# Configure CORS to allow all origins, methods, and headers
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

@app.route('/leads', methods=['GET'])
def get_leads():
    """Get all leads"""
    leads = LeadsManager.Get()
    return jsonify(leads), 200

@app.route('/leads', methods=['POST'])
def create_lead():
    """Create a new lead"""
    lead = request.get_json()
    if not lead:
        return jsonify({"error": "No data provided"}), 400
    
    updated_inventory = LeadsManager.Add(LeadsManager.Get(), lead)
    return jsonify({"message": "Lead created successfully", "data": lead}), 201

@app.route('/leads/<int:lead_id>', methods=['DELETE'])
def delete_lead(lead_id):
    """Delete a lead by ID"""
    updated_inventory = LeadsManager.Remove(LeadsManager.Get(), lead_id)
    return jsonify({"message": "Lead deleted successfully"}), 200

@app.route('/leads/<int:lead_id>', methods=['PUT'])
def update_lead(lead_id):
    """Update a lead by ID"""
    lead = request.get_json()
    if not lead:
        return jsonify({"error": "No data provided"}), 400
    
    updated_inventory = LeadsManager.Update(LeadsManager.Get(), lead_id, lead)
    return jsonify({"message": "Lead updated successfully", "data": lead}), 200

if __name__ == '__main__':
    app.run(debug=True)