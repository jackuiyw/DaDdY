import platform
bit = platform.architecture()[0]
if bit == '64bit':
    import daddy64_enc
elif bit == '32bit':
    import daddy32_enc
