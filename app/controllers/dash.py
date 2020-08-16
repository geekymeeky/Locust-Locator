# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

blueprint = Blueprint('dash', __name__)

@blueprint.route('/dash')
def dash():
    return render_template('dashboard/dashboard.html')
