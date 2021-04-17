from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField
from wtforms.validators import DataRequired


class EmployeeSalaryForm(FlaskForm):
    salary = FloatField("Annual Salary (GBP):", validators=[DataRequired()])
    submit = SubmitField("Calculate")
