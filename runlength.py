def rle_encode(data):
    encoded_data = []
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            i += 1
            count += 1
        encoded_data.append((data[i], count))
        i += 1
    return encoded_data

def rle_decode(encoded_data):
    decoded_data = []
    for value, count in encoded_data:
        decoded_data.extend([value] * count)
    return decoded_data

# Example usage:
data = "AAAAABBBCCDAA"
encoded = rle_encode(data)
print("Encoded:", encoded)
decoded = rle_decode(encoded)
print("Decoded:", ''.join(decoded))
