# -*- coding: utf-8 -*-

from .downloader_factory import Fido as _Fido

# Import and register LC sources
from .sources.eve import EVEClient
from .sources.lyra import LYRAClient
from .sources.goes import GOESClient
from .sources.norh import NoRHClient
from .sources.rhessi import RHESSIClient
from .sources.noaa import NOAAIndicesClient, NOAAPredictClient

_Fido.register(EVEClient, EVEClient._can_handle_query)
_Fido.register(LYRAClient, LYRAClient._can_handle_query)
_Fido.register(GOESClient, GOESClient._can_handle_query)
_Fido.register(NoRHClient, NoRHClient._can_handle_query)
_Fido.register(NOAAIndicesClient, NOAAIndicesClient._can_handle_query)
_Fido.register(NOAAPredictClient, NOAAPredictClient._can_handle_query)
_Fido.register(RHESSIClient, RHESSIClient._can_handle_query)


# Import and register other sources
from sunpy.net.jsoc.jsoc import JSOCClient
from sunpy.net.vso.vso import VSOClient

_Fido.register(VSOClient, VSOClient._can_handle_query)
_Fido.register(JSOCClient, JSOCClient._can_handle_query)