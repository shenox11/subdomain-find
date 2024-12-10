import requests
with open ("sub.txt",'r')as subs:
    for s in subs:
        s=s.strip()
        url=(f"https://{s}.example.com")
        r=requests.get(url=url,timeout=5)
        if r.status_code==200:
            print(f"[valid]{url}")
        else:
            pass
