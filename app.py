import os
from flask import Flask, render_template
from src.calculator import calc_net_pay
from src.forms import EmployeeSalaryForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


@app.route("/", methods=["GET", "POST"])
def home():
    tax_free = 15000
    upper_tax_threshold = 50000

    form = EmployeeSalaryForm()
    if form.validate_on_submit():
        pay_data = calc_net_pay(
            form.salary.data,
            upper_tax_threshold=upper_tax_threshold,
            tax_free=tax_free)
        form = EmployeeSalaryForm()
        return render_template(
            'index.html', form=form, pay=pay_data,
            tax_threshold=upper_tax_threshold, tax_free=tax_free)
    return render_template(
        'index.html', form=form, tax_threshold=upper_tax_threshold,
        tax_free=tax_free)
