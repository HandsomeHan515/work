from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'by*j9udm&zl6to1&orh#741%qhy8u82m!d&ey!&q2vw_lp1-mb'

DEBUG = env.bool('DJANGO_DEBUG', default=True)
