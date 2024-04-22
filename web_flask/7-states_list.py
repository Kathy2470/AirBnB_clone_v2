from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/states_list', methods=['GET', 'POST'])
def states_list():
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
