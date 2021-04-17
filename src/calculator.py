def calc_net_pay(salary, tax_free=15000, upper_tax_threshold=50000):
    """Calculates net annual pay using a persons annual salary, the tax free
    allowance and the upper tax threshold"""

    tax_due = 0
    nat_insurance_due = 0
    if salary > upper_tax_threshold:
        tax_due += (salary - upper_tax_threshold) * 0.4
        tax_due += (upper_tax_threshold - tax_free) * 0.2
        nat_insurance_due += (salary - upper_tax_threshold) * 0.02
        nat_insurance_due += (upper_tax_threshold - tax_free) * 0.12
    elif salary > tax_free:
        tax_due = ((salary - tax_free) * 0.2)
        nat_insurance_due = ((salary - tax_free) * 0.12)
    net_pay = salary - (tax_due + nat_insurance_due)

    return {"salary": round(salary), "net_pay": round(net_pay),
            "tax_due": round(tax_due), "ni_due": round(nat_insurance_due)}
