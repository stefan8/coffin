from django.conf.urls import *

handler403 = 'coffin.views.defaults.permission_denied'
handler404 = 'coffin.views.defaults.page_not_found'
handler500 = 'coffin.views.defaults.server_error'
