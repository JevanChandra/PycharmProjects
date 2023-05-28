from flask import Flask

app = Flask(__name__)


@app.route('/convert')
@app.route('/convert/<celsius>')
def convert_to_fahrenheit(celsius=0):
    fahrenheit = celsius * 9.0 / 5 + 32
    return f"Result: {fahrenheit:.2f} F"


if __name__ == '__main__':
    app.run(debug=True)

