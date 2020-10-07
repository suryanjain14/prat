import base64

encrypted = "CFIBDAINDxIaSREOU1IVCwQPHkZFThZXHBkeHAAJHwROTgsUVBABDQQLBwQNSR0UVBAUHw4cHhJO TgsUVBwcGhMLDggLAlQTX1VVGAIGAwQfC1xRHQFVWVtOTRQHAl5XGBAWXk1OTRMIDFNdBwZVWVtO TRIICFQTX1VVHw4BTUFTThZDGhtTXhw="
key = str.encode("suryanjain14")
decoded = base64.b64decode(encrypted)

decrypted = ""

for letter in range(0, len(decoded)):
    decrypted += chr((key[letter % len(key)] ^ decoded[letter]))
print(decrypted)
