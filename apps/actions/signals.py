from apps.contrib.signals import connect_proxy_signals

from .models import A4Action, Action

connect_proxy_signals(Action, A4Action)
