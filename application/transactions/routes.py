from application.transactions.forms import TransactionForm
from flask import Blueprint,flash, redirect, request, abort, render_template, url_for
from application.models import Transaction
from application import db

transactions = Blueprint('transactions', __name__)

@transactions.route('/transactions/new', methods=['GET', 'POST'])
def new_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        transaction = Transaction(content=form.content.data, amount_paid = form.amount_paid.data,
        amount_received=form.amount_received.data)
        db.session.add(transaction)
        db.session.commit()
        flash('Your transaction has been added', 'success')
        return redirect(url_for('user.account'))
    return render_template('new_transaction.html', title="New Transaction", form=form, legend="New Transaction")
