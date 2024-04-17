from hashlib import md5

def toconvert(digitated: str) -> str:
    element = digitated.encode("utf8")
    convert = md5(element).hexdigest()
    return convert
