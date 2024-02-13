import os
import requests

# définition de l'adresse de l'API
api_address = os.environ.get('fastapi_address')
# port de l'API
api_port = 8000
#users
users = {'alice': 'wonderland', 'bob': 'builder'}

for username, password in users.items():
    # requête
    r = requests.get(
        url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
        params= {
            'username': username,
            'password': password
        }
    )

    output = '''
    ============================
        Authentication test
    ============================

    request done at "/permissions"
    | username="{name}"
    | password="{psw}"

    expected result = 200
    actual restult = {status_code}

    ==>  {test_status}

    '''


    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output.format(status_code=status_code, test_status=test_status, name=username, psw=password))

    # impression dans un fichier
    if os.environ.get('LOG') == '1':
        with open('/home/api_test.log', 'a') as file:
            file.write(output.format(status_code=status_code, test_status=test_status, name=username, psw=password))