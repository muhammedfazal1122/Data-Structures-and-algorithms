class CreditCard:
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

class BankTransfer:
    def process_payment(self, amount):
        return f"Processing bank transfer of ${amount}"

class PayPal:
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"

def make_payment(payment_method, amount):
    print(payment_method.process_payment(amount))

# Creating instances of the payment method classes
credit_card = CreditCard()   







bank_transfer = BankTransfer()
paypal = PayPal()

# Using the make_payment function with different payment methods
make_payment(credit_card, 100)  # Output: Processing credit card payment of $100
make_payment(bank_transfer, 200) # Output: Processing bank transfer of $200
make_payment(paypal, 150)        # Output: Processing PayPal payment of $150