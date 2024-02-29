# # name='ACC-SINV-2024-00005'

# # import treepoem

# # img = treepoem.generate_barcode(
# #     barcode_type='qrcode',
# #     data='https://jonasneubert.com/talks/pybay2018.html',
# #     options={"eclevel": "Q"}
# # )
# # img.convert('1').save('qr.gif')

# # Importing library
# import cv2
# from pyzbar.pyzbar import decode
  
# # Make one method to decode the barcode 
# def BarcodeReader(image):
     
#     # read the image in numpy array using cv2
#     img = cv2.imread(image)
      
#     # Decode the barcode image
#     detectedBarcodes = decode(img)
      
#     # If not detected then print the message
#     if not detectedBarcodes:
#         print("Barcode Not Detected or your barcode is blank/corrupted!")
#     else:
       
#           # Traverse through all the detected barcodes in image
#         for barcode in detectedBarcodes:  
           
#             # Locate the barcode position in image
#             (x, y, w, h) = barcode.rect
             
#             # Put the rectangle in image using 
#             # cv2 to highlight the barcode
#             cv2.rectangle(img, (x-10, y-10),
#                           (x + w+10, y + h+10), 
#                           (255, 0, 0), 2)
             
#             if barcode.data!="":
               
#             # Print the barcode data
#                 print(barcode.data)
#                 print(barcode.type)
                 
#     #Display the image
#     cv2.imshow("Image", img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
 
# if __name__ == "__main__":
#   # Take the image from user
#     image="Img.jpg"
#     BarcodeReader(image)


# import barcode
# from barcode import ISBN13,JAN
# from barcode.writer import ImageWriter

# num = '450123412310'
# japanese_barcode = JAN(num, writer=ImageWriter())
# outputFileFolder='bar'
# outputFile = outputFileFolder + 'japanese_barcode'
# japanese_barcode.save(outputFile)

# import barcode
# from barcode.writer import ImageWriter

# # Your data to encode in the barcode
# data = 'ACC-SINV-2024-00005'

# # Generate a Code 128 barcode
# code128 = barcode.get_barcode_class('code128')

# # Create the barcode instance
# barcode_instance = code128(data, writer=ImageWriter())

# # Save the barcode image to a file
# barcode_instance.save('mybarcode')





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