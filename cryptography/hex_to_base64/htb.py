import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Dekode heksadesimal ke byte
byte_data = bytes.fromhex(hex_string)

# Enkode byte ke Base64
base64_string = base64.b64encode(byte_data).decode('utf-8')

print(base64_string)