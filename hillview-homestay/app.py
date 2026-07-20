from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
from prometheus_flask_exporter import PrometheusMetrics
from flask import Response
from prometheus_client import generate_latest
import certifi
import logging
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Initialize Prometheus metrics
metrics = PrometheusMetrics(app,
          default_metrics_path='/metrics')
metrics.info('hillview_app_info',
             'Hill View Homestay Application',
             version='1.0.0')

log_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'hillview.log'
)
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

logger = logging.getLogger(__name__)

# Connect to MongoDB
client = MongoClient(
    os.getenv('MONGO_URI'),
    tlsCAFile=certifi.where()
)
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
    logger.info('Home page visited')
    rooms = list(rooms_collection.find().limit(3))
    return render_template('home.html', rooms=rooms)

# Metrics endpoint
@app.route('/metrics')
def metrics_endpoint():
    return Response(
        generate_latest(),
        mimetype='text/plain'
    )

# Rooms page
@app.route('/rooms')
def rooms():
    logger.info('Rooms page visited')
    rooms = list(rooms_collection.find())
    return render_template('rooms.html', rooms=rooms)

# Booking page
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        logger.info(
            f'New booking from '
            f'{request.form["name"]} '
            f'for {request.form["room_type"]}'
        )
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
    logger.info('Booking completed successfully')
    return render_template('booking_success.html')

# Enquiry page
@app.route('/enquiry', methods=['GET', 'POST'])
def enquiry():
    if request.method == 'POST':
        logger.info(
            f'New enquiry from '
            f'{request.form["name"]}'
        )
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
    logger.info('Enquiry submitted successfully')
    return render_template('enquiry_success.html')

# Attractions page
@app.route('/attractions')
def attractions():
    logger.info('Attractions page visited')
    attractions = list(attractions_collection.find())
    return render_template('attractions.html',
                         attractions=attractions)

# Admin dashboard
@app.route('/admin')
def admin():
    logger.info('Admin dashboard accessed')
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

# Update booking status
@app.route('/admin/booking/<booking_id>/<status>')
def update_booking(booking_id, status):
    from bson import ObjectId
    logger.info(
        f'Booking {booking_id} '
        f'status updated to {status}'
    )
    bookings_collection.update_one(
        {'_id': ObjectId(booking_id)},
        {'$set': {'status': status}}
    )
    return redirect(url_for('admin'))

# Update enquiry status
@app.route('/admin/enquiry/<enquiry_id>/<status>')
def update_enquiry(enquiry_id, status):
    from bson import ObjectId
    logger.info(
        f'Enquiry {enquiry_id} '
        f'status updated to {status}'
    )
    enquiries_collection.update_one(
        {'_id': ObjectId(enquiry_id)},
        {'$set': {'status': status}}
    )
    return redirect(url_for('admin'))

# Run app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)