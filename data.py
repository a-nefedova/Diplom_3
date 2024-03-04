class URLs:
    HOMEPAGE = 'https://stellarburgers.nomoreparties.site'
    LOGIN = f'{HOMEPAGE}/login'
    FORGOT_PASS = f'{HOMEPAGE}/forgot-password'
    RESET_PASS = f'{HOMEPAGE}/reset-password'
    ACCOUNT = f'{HOMEPAGE}/account'
    LOGGED_ACCOUNT = f'{ACCOUNT}/profile'


class API:
    USER_REGISTER = f'{URLs.HOMEPAGE}/api/auth/register'
    USER_AUTH = f'{URLs.HOMEPAGE}/api/auth/login'
    USER_DELETE = f'{URLs.HOMEPAGE}/api/auth/user'
