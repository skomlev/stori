import os

EMAIL = {
    'host': os.environ.get('EMAIL_HOST', 'smtp.gmail.com'),
    'port': os.environ.get('EMAIL_PORT', 587),
    'sender': os.environ.get('EMAIL_SENDER', 'example@gmail.com'),
    'user': os.environ.get('EMAIL_USER', 'example@gmail.com'),
    # https://support.google.com/accounts/answer/185833?hl=es&sjid=14820134242632080947-SA
    'password': os.environ.get('EMAIL_PASSWORD', None),
}

FILE_PATH = os.environ.get('FILE_PATH', 'data/txns.csv')
SUMMARY_USER = os.environ.get('SUMMARY_USER', 'skomlev.ruso+user@gmail.com')
