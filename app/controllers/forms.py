# -*- coding: utf-8 -*-
from flask import Blueprint, render_template,request

blueprint = Blueprint('forms', __name__)

@blueprint.route('/forms', methods=["GET","POST"])
def my_form():
    if request.method == 'POST':
        name = request.form.get('name')
        subject = request.form.get('subject')
        reply_to = request.form.get('email')
        message = request.form.get('message')
        print(name,subject)
        # send_email(message, reply_to)
    return render_template('contact/contact.html')
