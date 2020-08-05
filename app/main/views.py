from datetime import datetime
from flask import request, render_template, url_for, session, redirect, flash

from . import main
from .forms import NameForm
from .. import db
from ..email import send_email
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        user = User.query.filter_by(username=name).first()
        if not user:
            user = User(username=name)
            db.session.add(user)
            db.session.commit()

            session['known'] = False
            flash('增加了新用户名 %s' % name)

            # if app.config['FLASKY_ADMIN']:
            #     send_email(app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = name
        
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))
