# Email slicer
while True:
    email = input(" what isn your email").strip()
    user_name = email[:email.index('@')]
    domain_name = email[email.index('@')+1:]
    output = " Your name is '{}'  and Your domain is '{}'".format(user_name,domain_name)
    print(output)