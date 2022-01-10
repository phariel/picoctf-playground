import hashlib

username_trial = b"FREEMAN"
keyhash = hashlib.sha256(username_trial).hexdigest()
str = "picoCTF{1n_7h3_|<3y_of_"
str += (
    keyhash[4]
    + keyhash[5]
    + keyhash[3]
    + keyhash[6]
    + keyhash[2]
    + keyhash[7]
    + keyhash[1]
    + keyhash[8]
    + "}"
)

print(str)
