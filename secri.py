import secrets

bs = secrets.token_bytes()
ss = str(bs)
print(bs,type(bs))
print(ss,type(ss))
bbs = ss.encode()
print(bbs, type(bbs))