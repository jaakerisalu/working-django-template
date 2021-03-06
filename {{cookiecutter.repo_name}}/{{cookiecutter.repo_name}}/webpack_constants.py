from django.conf import settings

from tg_react.apiurls import flatten_urls


def constants(context):
    return {
        'EXPRESS_PORT': settings.EXPRESS_PORT,
        'LOGIN_REDIRECT': settings.LOGIN_REDIRECT_URL,
        'APPEND_SLASH': settings.APPEND_SLASH,

        'API_BASE': '%s/api/v1/' % settings.SITE_URL,
        'API': flatten_urls('{{ cookiecutter.repo_name }}.api_urls', '')
    }
