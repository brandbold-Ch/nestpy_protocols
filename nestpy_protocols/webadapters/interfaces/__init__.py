from nestpy_protocols.webadapters.interfaces.framework.routers import FrameworkRoutersProtocol
from nestpy_protocols.webadapters.interfaces.framework.events import FrameworkEventsProtocol
from nestpy_protocols.webadapters.interfaces.framework.functions import FrameworkFunctionsProtocol
from nestpy_protocols.webadapters.interfaces.framework.middlewares import FrameworkMiddlewaresProtocol
from nestpy_protocols.webadapters.interfaces.framework.attributes import FrameworkAttributesProtocol
from nestpy_protocols.webadapters.interfaces.framework.docs import FrameworkDocsProtocol


__all__ =[
    "FrameworkDocsProtocol",
    "FrameworkEventsProtocol",
    "FrameworkFunctionsProtocol",
    "FrameworkMiddlewaresProtocol",
    "FrameworkAttributesProtocol",
    "FrameworkRoutersProtocol",
]
