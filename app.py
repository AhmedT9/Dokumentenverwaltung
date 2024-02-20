from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
import pytz
from datetime import datetime

app = Flask(__name__)
CORS(app)

specific_time = datetime(2024, 1, 1, 15, 0, 0, tzinfo=pytz.timezone("America/New_York"))
specific_time_2 = datetime(2024, 1, 1, 15, 0, 0, tzinfo=pytz.timezone("Europe/Berlin"))
documents = {
    "55": {
        "document": {
            "type": "Legal Agreement",
            "title": "Service Agreement",
            "parties": [
                {
                    "name": "Company A",
                    "role": "Service Provider"
                },
                {
                    "name": "Company B",
                    "role": "Client"
                }
            ],
            "effectiveDate": "2024-01-01",
            "terms": [
                {
                    "clauseTitle": "Confidentiality",
                    "clauseDetails": "Both parties agree to maintain confidentiality of shared information."
                },
                {
                    "clauseTitle": "Payment Terms",
                    "clauseDetails": "Client will pay the Service Provider a fixed fee of $5000 upon completion of the services."
                },
                {
                    "clauseTitle": "Termination",
                    "clauseDetails": "Either party may terminate this agreement with a 30-day written notice."
                }
            ],
            "signature": {
                "serviceProviderSignature": "",
                "clientSignature": "",
                "dateSigned": ""
            }
        },
        "origin": "East USA",
        "id": "55",
        "timestamp": specific_time.isoformat()
    },
    "56": {
        "document": {
            "type": "Legal Agreement",
            "title": "Service Agreement",
            "parties": [
                {
                    "name": "Company A",
                    "role": "Service Provider"
                },
                {
                    "name": "Company B",
                    "role": "Client"
                }
            ],
            "effectiveDate": "2024-01-01",
            "terms": [
                {
                    "clauseTitle": "Confidentiality",
                    "clauseDetails": "Both parties agree to maintain confidentiality of shared information."
                },
                {
                    "clauseTitle": "Payment Terms",
                    "clauseDetails": "Client will pay the Service Provider a fixed fee of $5000 upon completion of the services."
                },
                {
                    "clauseTitle": "Termination",
                    "clauseDetails": "Either party may terminate this agreement with a 30-day written notice."
                }
            ],
            "signature": {
                "serviceProviderSignature": "",
                "clientSignature": "",
                "dateSigned": ""
            }
        },
        "origin": "Central Europe",
        "id": "56",
        "timestamp": specific_time_2.isoformat()
    }
}

timezone_mapping = {
    "East USA": "America/New_York",
    "Central USA": "America/Chicago",
    "Mountain Zone USA": "America/Denver",
    "Pacific USA": "America/Los_Angeles",
    "Alaska USA": "America/Anchorage",
    "Hawaii USA": "Pacific/Honolulu",
    "Central Europe": "Europe/Berlin",
    "Western Europe": "Europe/Lisbon",
    "Eastern Europe": "Europe/Helsinki",
    "UK": "Europe/London",
}

@app.route('/document', methods=['POST'])
def add_document():
    doc_id = str(uuid.uuid4())
    data = request.json
    data['id'] = doc_id
    origin = data.get('origin', 'UTC')
    timezone_str = timezone_mapping.get(origin, 'UTC')
    timezone = pytz.timezone(timezone_str)
    data['timestamp'] = datetime.now(timezone).isoformat()
    documents[doc_id] = data
    print(data)
    return jsonify({"message": "Document saved", "id": doc_id}), 201


@app.route('/document/<doc_id>', methods=['GET'])
def get_document(doc_id):
    document = documents.get(doc_id)
    if document:
        return jsonify(document), 200
    else:
        return jsonify({"message": "Document not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)