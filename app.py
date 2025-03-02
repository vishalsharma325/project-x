from flask import Flask, request, redirect, render_template, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

# Define the path for the file to store bookings
FILE_PATH = "bookings.csv"

# Create the CSV file with headers if it doesn't exist
def initialize_file():
    try:
        with open(FILE_PATH, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Email", "Phone", "Ride", "Date", "Timestamp"])
    except FileExistsError:
        pass

@app.route('/submit', methods=['POST'])
def submit_booking():
    # Validate and get data from the form
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    ride = request.form.get('ride')
    date = request.form.get('date')
    
    if not all([name, email, phone, ride, date]):
        return jsonify({"status": "error", "message": "All fields are required."}), 400

    try:
        datetime.strptime(date, '%Y-%m-%d')  # Validate date format
    except ValueError:
        return jsonify({"status": "error", "message": "Invalid date format. Use YYYY-MM-DD."}), 400

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Save data to CSV
    with open(FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone, ride, date, timestamp])

    # Redirects to the confirmation page after successful booking
    return redirect('/confirmation')

@app.route('/confirmation')
def confirmation():
    # Render the confirmation page
    return render_template('confirmation.html')

if __name__ == '__main__':
    initialize_file()
    app.run(debug=True)
