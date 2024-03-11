from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=["POST"])
def print_data():
    data = request.json.get('data')
    print('Received data:', data)
    return jsonify({'message': 'Data received'})

if __name__ == '__main__':
    app.run(debug=True, port=5173)