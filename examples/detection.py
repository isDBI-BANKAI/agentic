

# Should list FAS 4 as highest weight, might include FAS 20 as second highest weight then FAS 32 as third highest weight.
journal_1 = """
Context: GreenTech exits in Year 3, and Al Baraka Bank buys out its stake.
Adjustments:
    Buyout Price: $1,750,000
    Bank Ownership: 100%
Accounting Treatment:
    Derecognition of GreenTech's equity
    Recognition of acquisition expense
Journal Entry for Buyout:
    Dr. GreenTech Equity $1,750,000
    Cr. Cash $1,750,000
"""

# Should list FAS 10 as highest weight, and should not include FAS 8, FAS 19 or FAS 23, if more than one standard is found possible.
journal_2 = """
Context: The client cancels the change order, reverting to the original contract terms.
Adjustments:
    Revised Contract Value: Back to $5,000,000
    Timeline Restored: 2 years
Accounting Treatment:
    Adjustment of revenue and cost projections
    Reversal of additional cost accruals
Journal Entry for Cost Reversal:
    Dr. Accounts Payable $1,000,000
    Cr. Work-in-Progress $1,000,000
This restores the original contract cost.
"""

# Should list FAS 10 as highest weight if more than one standard is found possible.
journal_3 = """
Context: Buyer defaults, stopping project completion.
Adjustments:
    Recognized Revenue: $6,500,000
    Impairment of Receivables: $500,000
Accounting Treatment:
    Recognition of bad debt
    Adjustment of work-in-progress valuation
Journal Entry for Default Adjustment:
    Dr. Bad Debt Expense $500,000
    Cr. Accounts Receivable $500,000
This writes off uncollectible amounts.
"""

# Should list FAS 10 as highest weight and FAS 11 with second highest weight, FAS 30 is between possible standards applicable.
journal_4 = """
Context: The client pays all outstanding amounts on time, reducing expected losses.
Adjustments:
    Loss provision reversed.
    Recognized revenue adjusted.
Accounting Treatment:
    Reduction in impairment expense.
    Recognition of full contract revenue.
Journal Entry for Loss Provision Reversal:
    Dr. Allowance for Impairment $500,000
    Cr. Provision for Losses $500,000
This restores revenue after full payment.
"""
