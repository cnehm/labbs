from flask import Flask, json
interfaces = [
    {"interface": "gi0/0", "ip-adress": "193.10.160.1"},
    {"interface": "gi0/1", "ip-adress": "193.10.29.1"},
    {"interface": "gi0/2", "ip-adress": "193.10.30.1"},
    {"interface": "gi0/3", "ip-adress": "193.10.31.1"},
    {"interface": "gi0/4", "ip-adress": "193.10.31.64"},
    {"interface": "gi0/5", "ip-adress": "193.10.29.128"}
]
api = Flask(__name__)
@api.route('/interfaces', methods=['GET'])
def get_interfaces():
    return json.dumps(interfaces)
    if __name__ == '__main__':
        api.run()
