import abc
import random


class Website:
    def __init__(self, title: str, session_id: int):
        self._title = title
        self.session_id = session_id
        self.__csrf_token = self.__token_generate()

    @staticmethod
    def __token_generate() -> str:
        symbol_dictionary = "qwertyuiopasdfghjklzxcvbnm1234567890"
        symbol_dictionary += symbol_dictionary.upper()

        csrf_token = ""

        for _ in range(32):
            csrf_token += random.choice(symbol_dictionary)

        return csrf_token

    @property
    def csrf_token(self) -> str:
        return self.__csrf_token

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        self._title = title


class LoginPage(Website):
    def __init__(self, title: str, session_id: int):
        super().__init__(title, session_id)
        self.title = self.title + " - Login"

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        self._title = title + " - Login"

    def log_in(self, username: str, password: str) -> str:
        return f'validate:{username}:{password}:{self.csrf_token}'
        # так как у меня нет целого рабочего сайта 
        # то будет просто возврат данных


class RegisterPage(Website):
    def __init__(self, title: str, session_id: int):
        super().__init__(title, session_id)
        self.title = self.title + " - Register"

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        self._title = title + " - Register"

    def register(self, username: str, password: str, confirm: str) -> str:
        if password == confirm:
            return f'reguser:{username}:{password}:{self.csrf_token}'
        return "Passwords don't match."
        # аналогичная ситуация как и с логином


class Redirector(abc.ABC, Website):
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.__csrf_token = self.__token_generate()

    @abc.abstractmethod
    def redirect(self, link: str) -> str:
        pass


class LoginRedirector(Redirector):
    def __init__(self, session_id: str, token: str):
        super().__init__(session_id, token)

    def redirect(self, link: str) -> str:
        return f'redirect:{link}'


#

website_name = "Webpage"
website = Website(website_name, 1)
log_page = LoginPage(website_name, 1)
reg_page = RegisterPage(website_name, 1)

log_page.title = "Webbypage"
print(log_page.log_in("User", "Pass"))

reg_page.title = "Webpaaaage"
print(reg_page.title)
print(reg_page.register("ab", "asd", "asdd"))
print(reg_page.register("ab", "asd", "asd"))
