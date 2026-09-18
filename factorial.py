from flask import Flask, request, jsonify

app = Flask(__name__)


# Factorial function
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


# Armstrong function
def is_armstrong(n):
    digits = str(n)
    power = len(digits)

    total = 0

    for digit in digits:
        total = total + int(digit) ** power

    return total == n


# Factorial API
@app.route("/factorial", methods=["GET"])
def factorial_api():

    number = request.args.get("number", type=int)

    if number is None:
        return jsonify({"error": "Please provide a number"}), 400

    if number < 0:
        return jsonify({"error": "Factorial is not defined for negative numbers"}), 400

    result = factorial(number)

    return jsonify({
        "number": number,
        "factorial": result
    })


# Armstrong API
@app.route("/armstrong", methods=["GET"])
def armstrong_api():

    number = request.args.get("number", type=int)

    if number is None:
        return jsonify({"error": "Please provide a number"}), 400

    result = is_armstrong(number)

    return jsonify({
        "number": number,
        "armstrong": result
    })


if __name__ == "__main__":
    app.run(debug=True)