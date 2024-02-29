### ----genetation of svg data of the barcode----------###
import barcode
from barcode.writer import SVGWriter
from io import BytesIO
import base64

# Your data to encode in the barcode
data = 'Hello, World!'

# Generate a Code 128 barcode
code128 = barcode.get_barcode_class('code128')

# Create the barcode instance
barcode_instance = code128(data, writer=SVGWriter())

# Create an in-memory stream to hold the SVG data
svg_stream = BytesIO()

# Write the SVG data to the in-memory stream
barcode_instance.write(svg_stream)

# Seek to the beginning of the stream
svg_stream.seek(0)

# Read the SVG data from the stream
svg_data = svg_stream.read().decode('utf-8')

# Encode the SVG data as base64
base64_svg_data = base64.b64encode(svg_data.encode('utf-8')).decode('utf-8')

# Construct the data URI
data_uri = f'data:image/svg+xml;base64,{base64_svg_data}'

# Print or use the data URI as needed
print(data_uri)


# Create a file name for the saved image
filename = 'barcode.svg'

# Create a file to save the SVG barcode
with open(filename, 'wb') as f:
    # Write the SVG data to the file
    barcode_instance.write(f)

print(f"Barcode saved as {filename}")
