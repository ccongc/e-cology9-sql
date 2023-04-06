def tamper(payload, **kwargs):
    # URL encoding for all characters
    encoded_payload = ''.join(['%' + format(ord(c), 'x') for c in payload])

    encoded_payload = ''.join(['%' + format(ord(c), 'x') for c in encoded_payload])

    encoded_payload = ''.join(['%' + format(ord(c), 'x') for c in encoded_payload])
¡¢
    encoded_payload = encoded_payload.replace(' ', '%20')

    return encoded_payload