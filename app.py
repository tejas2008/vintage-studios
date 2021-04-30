from flask import Flask, render_template, request, redirect, url_for, session,flash,make_response,session
import random
import os
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

@app.route("/pay_info")
def pay_info():
    return render_template('pay.html')


@app.route("/pay",methods=['GET','POST'])
def pay():
    api_key = os.environ['PAY_KEY']
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        email = request.form['email']
        mobile = request.form['mobile']
        random_number = random.randint(0,1000)
        order_id = 'OID'+ str(random_number)
        amount = int(amount)*100
        print(amount)
        print(name,mobile,email,amount,order_id)
        return render_template('razorpay.html',api_key=api_key,order_id=order_id,amount=amount,name=name,email=email,mobile=mobile)


@app.route("/success",methods=['GET','POST'])
def success():
    if request.method == 'POST':
        return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)

