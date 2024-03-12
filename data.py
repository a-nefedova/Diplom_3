class URLs:
    HOMEPAGE = 'https://stellarburgers.nomoreparties.site'
    LOGIN = f'{HOMEPAGE}/login'
    FORGOT_PASS = f'{HOMEPAGE}/forgot-password'
    ACCOUNT = f'{HOMEPAGE}/account'
    LOGGED_ACCOUNT = f'{ACCOUNT}/profile'
    ORDER_FEED = f'{HOMEPAGE}/feed'


class API:
    USER_REGISTER = f'{URLs.HOMEPAGE}/api/auth/register'
    USER_DELETE = f'{URLs.HOMEPAGE}/api/auth/user'
    ORDERS = f'{URLs.HOMEPAGE}/api/orders'


ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa71"]}
