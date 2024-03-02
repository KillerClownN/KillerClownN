def hamming_code(data):
  data_bits = list(data)
  parity_bits = [None, None, None]

  # Calculate parity bits
  parity_bits[0] = int((int(data_bits[0]) + int(data_bits[1]) + int(data_bits[3])) % 2)
  parity_bits[1] = int((int(data_bits[0]) + int(data_bits[2]) + int(data_bits[3])) % 2)
  parity_bits[2] = int((int(data_bits[1]) + int(data_bits[2]) + int(data_bits[3])) % 2)

  return "".join(data_bits + parity_bits)

def main():
  data = "110101"
  encoded_data = hamming_code(data)
  print("Original data:", data)
  print("Encoded data:", encoded_data)

