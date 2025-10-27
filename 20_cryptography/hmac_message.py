import hmac # hash-based message authentication
import hashlib

def calc_hash(key:str, message:str):
    b_key = bytes(key, "utf-8")
    b_msg = bytes(message, "utf-8")

    hash_value = hmac.new(b_key, b_msg, hashlib.sha256)
    return hash_value.hexdigest()

sec_key = "chicken"
msg1 = calc_hash(sec_key, "Those who lunch.")
msg2 = calc_hash(sec_key, "Those who lunch.")
msg3 = calc_hash(sec_key, "Those who dinner.")


print(msg1 == msg2)
print (msg1 == msg3)

