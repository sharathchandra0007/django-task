VERSION = ('2', '2', '1')

try:
    import django
    if django.VERSION < (3, 2):
        default_app_config = 'pagedown.apps.PagedownConfig'
except ImportError:
    # Django is not available during build (pip install .)
    pass
