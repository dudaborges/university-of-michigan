email = "dudaborges@gmail.com "
atpos = email.find('@')
print(atpos)
sspos = email.find(' ', atpos)
host = email[atpos+1 : sspos]
print(host)
