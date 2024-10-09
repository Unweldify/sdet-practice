import abc, random

class Website:    
    def __init__(self, title: str, session_id: int):
        self._title = title
        self.session_id = session_id
        self.__CSRF_token = self.__token_generate()


    @staticmethod
    def __token_generate() -> str:
        symbol_dictionary = "qwertyuiopasdfghjklzxcvbnm1234567890"
        symbol_dictionary += symbol_dictionary.upper()

        CSRF_token = ""

        for _ in range(32):
            CSRF_token += random.choice(symbol_dictionary)

        return CSRF_token


    @property
    def CSRF_token(self) -> str:
        return self.__CSRF_token


    @property
    def title(self) -> str:
        return self._title


    @title.setter
    def title(self, title: str) -> None:
        self._title = title


class Login_page(Website):
    def __init__(self, title: str, session_id: int):
        super().__init__(title, session_id)
        self.title = self.title + " - Login"

    @property
    def title(self) -> str:
        return self._title 

    @title.setter
    def title(self, title: str) -> None:
        self._title = title + " - Login"
        
    
    def log_in(self, username, password):
        return f'validate:{username}:{password}:{self.CSRF_token}' # так как у меня нет целого рабочего сайта то будет просто возврат данных

class Register_page(Website):
    def __init__(self, title, session_id):
        super().__init__(title, session_id)
        self.title = self.title + " - Register"

    @property
    def title(self) -> str:
        return self._title 

    @title.setter
    def title(self, title: str) -> None:
        self._title = title + " - Register"

    def register(self, username, password, password_confirm):
        if password == password_confirm:
            return  f'reguser:{username}:{password}:{self.CSRF_token}' # аналогичная ситуация как и с логином
        return "Passwords don't match."


#

website_name = "Webpage"
website = Website(website_name, 1)
log_page = Login_page(website_name, 1)
reg_page = Register_page(website_name, 1)

log_page.title = "Webbypage"
print(log_page)
print(log_page.log_in("User", "Pass"))


reg_page.title = "Webpaaaage"
print(reg_page.title)
print(reg_page.register("ab", "asd", "asdd"))
print(reg_page.register("ab", "asd", "asd"))