from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/hello/call', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")
@app.route('/api', methods=['GET'])
def hello():
    return jsonify(message="Hello, Student!")

if __name__ == '__main__':
    app.run(debug=True)




import shutil
import os

def replace_resource(source_path, destination_path):
    """Replace a resource file at the destination path with the source file."""
    if os.path.exists(destination_path):
        os.remove(destination_path)
    shutil.copy2(source_path, destination_path)
    print(f"Resource updated: {destination_path}")

# Example usage
replace_resource('path/to/new_resource.png', 'path/to/existing_resource.png')

