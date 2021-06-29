# Email slicer
while True:
    email = input(" what isn your email || Do you want to continue again ? (y/n)").strip()
    if email.lower() == 'n':
        break
    user_name = email[:email.index('@')]
    domain_name = email[email.index('@')+1:]
    output = " Your name is '{}'  and Your domain is '{}'".format(user_name,domain_name)
    print(output)
