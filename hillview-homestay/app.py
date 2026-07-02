from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os
import ssl

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Connect to MongoDB
client = MongoClient(os.getenv('MONGO_URI'),ssl=True, tlsAllowInvalidCertificates=True)
db = client[os.getenv('DB_NAME')]

# Collections
rooms_collection = db['rooms']
bookings_collection = db['bookings']
enquiries_collection = db['enquiries']
attractions_collection = db['attractions']

# ─── ROUTES ───────────────────────────

# Home page
@app.route('/')
def home():
    rooms = list(rooms_collection.find().limit(3))
    return render_template('home.html', rooms=rooms)

# Rooms page
@app.route('/rooms')
def rooms():
    rooms = list(rooms_collection.find())
    return render_template('rooms.html', rooms=rooms)

# Booking page
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        booking = {
            'name': request.form['name'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'room_type': request.form['room_type'],
            'check_in': request.form['check_in'],
            'check_out': request.form['check_out'],
            'guests': request.form['guests'],
            'status': 'pending',
            'created_at': datetime.now()
        }
        bookings_collection.insert_one(booking)
        return redirect(url_for('booking_success'))
    rooms = list(rooms_collection.find())
    return render_template('booking.html', rooms=rooms)

# Booking success page
@app.route('/booking-success')
def booking_success():
    return render_template('booking_success.html')

# Enquiry page
@app.route('/enquiry', methods=['GET', 'POST'])
def enquiry():
    if request.method == 'POST':
        enquiry = {
            'name': request.form['name'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'message': request.form['message'],
            'status': 'new',
            'created_at': datetime.now()
        }
        enquiries_collection.insert_one(enquiry)
        return redirect(url_for('enquiry_success'))
    return render_template('enquiry.html')

# Enquiry success page
@app.route('/enquiry-success')
def enquiry_success():
    return render_template('enquiry_success.html')

# Attractions page
@app.route('/attractions')
def attractions():
    attractions = list(attractions_collection.find())
    return render_template('attractions.html',
                         attractions=attractions)


@app.route('/admin')
def admin():
    bookings = list(bookings_collection.find()
                   .sort('created_at', -1))
    enquiries = list(enquiries_collection.find()
                    .sort('created_at', -1))
    total_bookings = bookings_collection.count_documents({})
    pending_bookings = bookings_collection.count_documents(
                      {'status': 'pending'})
    total_enquiries = enquiries_collection.count_documents({})
    new_enquiries = enquiries_collection.count_documents(
                   {'status': 'new'})
    return render_template('admin.html',
                         bookings=bookings,
                         enquiries=enquiries,
                         total_bookings=total_bookings,
                         pending_bookings=pending_bookings,
                         total_enquiries=total_enquiries,
                         new_enquiries=new_enquiries)

@app.route('/admin/booking/<booking_id>/<status>')
def update_booking(booking_id, status):
    from bson import ObjectId
    bookings_collection.update_one(
        {'_id': ObjectId(booking_id)},
        {'$set': {'status': status}}
    )
    return redirect(url_for('admin'))

# Update enquiry status
@app.route('/admin/enquiry/<enquiry_id>/<status>')
def update_enquiry(enquiry_id, status):
    from bson import ObjectId
    enquiries_collection.update_one(
        {'_id': ObjectId(enquiry_id)},
        {'$set': {'status': status}}
    )
    return redirect(url_for('admin'))

# Run app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)