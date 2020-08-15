# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

blueprint = Blueprint('contact', __name__)


@blueprint.route('/contact')
def contact():
    return render_template('contact/contact.html')