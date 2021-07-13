UPPER_TAX_THRESHOLD = 50000
TAX_FREE_ALLOWANCE = 15000
UPPER_TAX_RATE = 0.4
BASIC_TAX_RATE = 0.2
UPPER_NATIONAL_INSURANCE_RATE = 0.02
BASIC_NATIONAL_INSURANCE_RATE = 0.12


def calc_annual_net_pay(annual_gross_salary):
    tax_due = calc_annual_income_tax(annual_gross_salary)
    nat_insurance_due = calc_annual_national_insurance(annual_gross_salary)

    net_pay = annual_gross_salary - (tax_due + nat_insurance_due)

    return {"salary": annual_gross_salary, "net_pay": net_pay,
            "tax_due": tax_due, "nat_insurance_due": nat_insurance_due}

  
def calc_annual_income_tax(annual_gross_salary):
    annual_income_tax = 0

    if annual_gross_salary > UPPER_TAX_THRESHOLD:
        annual_income_tax += (annual_gross_salary - UPPER_TAX_THRESHOLD) * UPPER_TAX_RATE
        annual_income_tax += (UPPER_TAX_THRESHOLD - TAX_FREE_ALLOWANCE) * BASIC_TAX_RATE
    elif annual_gross_salary > TAX_FREE_ALLOWANCE:
        annual_income_tax += ((annual_gross_salary - TAX_FREE_ALLOWANCE) * BASIC_TAX_RATE)

    return annual_income_tax

  
def calc_annual_national_insurance(annual_gross_salary):
    annual_nat_insurance = 0

    if annual_gross_salary > UPPER_TAX_THRESHOLD:
        annual_nat_insurance += (annual_gross_salary - UPPER_TAX_THRESHOLD) * UPPER_NATIONAL_INSURANCE_RATE
        annual_nat_insurance += (UPPER_TAX_THRESHOLD - TAX_FREE_ALLOWANCE) * BASIC_NATIONAL_INSURANCE_RATE
    elif annual_gross_salary > TAX_FREE_ALLOWANCE:
        annual_nat_insurance += ((annual_gross_salary - TAX_FREE_ALLOWANCE) * BASIC_NATIONAL_INSURANCE_RATE)

    return annual_nat_insurance
