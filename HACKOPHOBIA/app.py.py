from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyCQ5D8_lBbFh_PDPUjmBJU2km_IgICUhnY")

model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# AI CHATBOT
@app.route("/ask", methods=["POST"])
def ask():

    try:
        data = request.get_json()
        question = data.get("question")

        if not question:
            return jsonify({"reply": "Please type a question."})

        response = model.generate_content(question)

        return jsonify({"reply": response.text})

    except Exception as e:
        print("AI Error:", e)
        return jsonify({"reply": "AI service error."})


# LOST ITEM
@app.route("/lost", methods=["POST"])
def lost():

    data = request.get_json()

    name = data.get("name")
    uid = data.get("uid")
    item = data.get("item")
    location = data.get("location")
    date = data.get("date")
    time = data.get("time")

    print("\n----- LOST ITEM -----")
    print("Name:", name)
    print("UID:", uid)
    print("Item:", item)
    print("Location:", location)
    print("Date:", date)
    print("Time:", time)

    return jsonify({"status": "Lost item submitted successfully"})


# FOUND ITEM
@app.route("/found", methods=["POST"])
def found():

    data = request.get_json()

    name = data.get("name")
    uid = data.get("uid")
    item = data.get("item")
    location = data.get("location")
    date = data.get("date")
    time = data.get("time")

    print("\n----- FOUND ITEM -----")
    print("Name:", name)
    print("UID:", uid)
    print("Item:", item)
    print("Location:", location)
    print("Date:", date)
    print("Time:", time)

    return jsonify({"status": "Found item submitted successfully"})


# COMPLAINT SYSTEM
@app.route("/complaint", methods=["POST"])
def complaint():

    data = request.get_json()

    name = data.get("name")
    subject = data.get("subject")
    message = data.get("message")

    print("\n----- COMPLAINT -----")
    print("Name:", name)
    print("Subject:", subject)
    print("Message:", message)

    return jsonify({"status": "Complaint submitted successfully"})


if __name__ == "__main__":
    app.run(debug=True)