import validators


def url_check(message):
    return validators.url(message)
