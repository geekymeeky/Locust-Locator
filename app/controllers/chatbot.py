# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

blueprint = Blueprint('chatbot', __name__)

@blueprint.route('/chatbot')
def chatbot():
    return render_template('chatbot/chatbot.html')