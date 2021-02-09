from application.transactions.forms import TransactionForm
from flask import Blueprint,flash, redirect, request, abort, render_template, url_for
from application.models import Transaction
from application import db
from flask_login import current_user, login_required

transactions = Blueprint('transactions', __name__)

@transactions.route('/transaction/new', methods=['GET', 'POST'])
@login_required
def new_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        transaction = Transaction(content = form.content.data, amount_paid = form.amount_paid.data,
        amount_received = form.amount_received.data, creator=current_user)
        db.session.add(transaction)
        db.session.commit()
        flash('Your transaction has been added', 'success')
        return redirect(url_for('users.account'))
    return render_template('new_transaction.html', title="New Transaction", form=form, legend="New Transaction")

@transactions.route('/transaction/<int:transaction_id>')
def transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    return render_template('transaction.html', content=transaction.content, transaction=transaction)
