import qrcode

upi_id = input("Enter your UPI ID: ")

#! upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#? Defining the payment URL based on the UPI ID and the payment app
#? You can modify these URLs based on the payment apps and you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#? Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#? Save the QR code to image file
with open('phonepe_qr.png', 'wb') as f:
    phonepe_qr.save(f)
with open('paytm_qr.png', 'wb') as f:
    paytm_qr.save(f)
with open('google_pay_qr.png', 'wb') as f:
    google_pay_qr.save(f)