from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
{% if cookiecutter.is_react_project == 'y' %}from django.http import HttpResponse, HttpResponseRedirect{% else %}from django.views.generic.base import TemplateView{% endif %}


admin.autodiscover()

urlpatterns = [
    {% if cookiecutter.is_react_project == 'y' %}url(r'^api/v1/', include('{{ cookiecutter.repo_name }}.api_urls')),
    {%- else %}url(r'', include('accounts.urls')),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),{%- endif %}

    url(r'^tagauks/', include(admin.site.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT){% if cookiecutter.is_react_project == 'y' %}

if settings.DEBUG:
    import logging
    if isinstance(settings.EXPRESS_PORT, int):
        import time
        from urllib3.exceptions import MaxRetryError

        from revproxy.views import ProxyView


        class LocalHelper(ProxyView):
            upstream = 'http://localhost:%d' % settings.EXPRESS_PORT

            def dispatch(self, request, path):
                if path == 'favicon.ico':
                    return HttpResponse('')

                if settings.APPEND_SLASH:
                    if path and path[-1] != '/' and 'public' not in path:
                        if path[0] != '/':
                            path = '/%s' % path

                        return HttpResponseRedirect('%s/' % path)

                try:
                    return super().dispatch(request, path)

                except MaxRetryError:
                    try:
                        # Try once more, but sleep on it first
                        time.sleep(1)
                        return super().dispatch(request, path)

                    except MaxRetryError:
                        try:
                            # Try once more, but sleep on it first
                            time.sleep(1)

                            return super().dispatch(request, path)

                        except:
                            return HttpResponse('Express proxied connection failed, please reload the page to try again.')

                except Exception as e:
                    logging.error('LocalHelper exception %s', e)
                    return HttpResponse('Express proxied connection failed, please reload the page to try again.')

        urlpatterns += [
            url(r'^(?P<path>.*)$', LocalHelper.as_view(), name='home'),
        ]

    else:
        logging.warning('Using nginx proxy locally'){% endif %}
