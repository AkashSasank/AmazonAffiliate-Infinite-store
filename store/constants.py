import os


BASE_URL = os.getenv('BASE_URL')

home_page_urls = {
    'home': BASE_URL,
    'store_home': BASE_URL + '/store',
    'about': BASE_URL + '/about'
}
