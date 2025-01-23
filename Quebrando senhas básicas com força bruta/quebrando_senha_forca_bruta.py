import hashlib


hash_original = ""
with open("senhas.txt", "r") as file:
    hash_original = file.readline()


senha = "password"
hash_md5 = hashlib.md5(senha.encode()).hexdigest()
if hash_md5 == hash_original:
    print(f"A senha {senha} é a senha correta")
    print(hash_md5)

