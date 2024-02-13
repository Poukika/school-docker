import os
import requests

# définition de l'adresse de l'API
api_address = os.environ.get('fastapi_address')
# port de l'API
api_port = 8000
#users
users = {'alice': 'wonderland', 'bob': 'builder'}
# sentence test
sentence = 'positive test'

# requête
for username, password in users.items():
    for version in range(1, 3):
        r = requests.get(
            url='http://{address}:{port}/v{i}/sentiment'.format(address=api_address, port=api_port, i=version),
            params= {
                'username': str(username),
                'password': str(password),
                'sentence': sentence
            }
        )
        output = '''
        ============================
            Authorization test
        ============================

        request done at "/v{i}/sentence"
        | username="{name}"
        | password="{psw}"

        expected result = {result}
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
        print(output.format(status_code=status_code, test_status=test_status, i=version, name=username, psw=password, result = "403" if (version == 2 and username == 'bob') else "200"))

        # impression dans un fichier
        if os.environ.get('LOG') == '1':
            with open('/home/api_test.log', 'a') as file:
                file.write(output.format(status_code=status_code, test_status=test_status, i=version, name=username, psw=password, result = "403" if (version == 2 and username == 'bob') else "200"))