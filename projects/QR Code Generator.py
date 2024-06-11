import qrcode

def generate_qr_code(text, output_image_path):
    qr = qrcode.qrcode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(output_image_path)

# Example usage
generate_qr_code('https://www.example.com', 'output_qr_code.png')
