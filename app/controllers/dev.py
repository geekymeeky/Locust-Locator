# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

blueprint = Blueprint('dev', __name__)

@blueprint.route('/dev')
def dev():
    return render_template('developer/developers.html')
