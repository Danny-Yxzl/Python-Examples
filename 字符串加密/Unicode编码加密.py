x = 1  # 偏移量


def encrypt_string(text):
    ans = ""
    for i in text:
        ans = ans + "%s-" % (ord(i) - x)
    return ans[:-1]


def decode_string(text):
    text = text.split("-")
    ans = ""
    for i in text:
        ans = ans + chr(int(i) + x)
    return ans
