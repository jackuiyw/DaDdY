import platform
bit = platform.architecture()[0]
if bit == '64bit':
    import mafia64_enc
elif bit == '32bit':
    import mafia32enc_
