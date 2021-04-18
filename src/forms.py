from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField
from wtforms.validators import InputRequired, NumberRange


class EmployeeSalaryForm(FlaskForm):
    salary = FloatField(
        "Annual Salary (GBP):", validators=[InputRequired(), NumberRange(min=0)]
    )
    submit = SubmitField("Calculate")
