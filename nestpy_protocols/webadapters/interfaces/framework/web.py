"""
Module defining the AbstractWebServer contract.

This module declares the AbstractWebServer abstract base class which
specifies composition methods to attach various server contract objects
(such as params, functions, events, routers, middlewares and docs) to
a web server adapter implementation.
"""

from abc import ABC, abstractmethod
from nestpy_protocols.webadapters.interfaces import (
    FrameworkDocsProtocol,
    FrameworkAttributesProtocol,
    FrameworkRoutersProtocol,
    FrameworkMiddlewaresProtocol,
    FrameworkFunctionsProtocol,
    FrameworkEventsProtocol,
)


class FrameworkWebProtocol(ABC):
    """
    Abstract base class that groups methods for attaching server interfaces.

    Implementations should accept instances of the specific contract interfaces
    and return them (optionally wrapped or configured) so callers can continue
    composing or inspecting the configured contract objects.
    """

    @abstractmethod
    def attributes(self) -> FrameworkAttributesProtocol:
        """
        Attach or configure server parameters.

        Returns:
            The configured BaseServerParams instance (may be the same object or an adapter/wrapper).
        """
        ...

    @abstractmethod
    def functions(self) -> FrameworkFunctionsProtocol:
        """
        Attach or configure server functions (route/websocket registration helpers).

        Returns:
            The configured BaseServerFunctions instance.
        """
        ...

    @abstractmethod
    def events(self) -> FrameworkEventsProtocol:
        """
        Attach or configure server lifecycle and event handlers.

        Returns:
            The configured BaseServerEvents instance.
        """
        ...

    @abstractmethod
    def routers(self) -> FrameworkRoutersProtocol:
        """
        Attach or configure router groups and route management.

        Returns:
            The configured BaseServerRouter instance.
        """
        ...

    @abstractmethod
    def middlewares(self) -> FrameworkMiddlewaresProtocol:
        """
        Attach or configure middleware and exception handlers.

        Returns:
            The configured BaseServerMiddlewares instance.
        """
        ...

    @abstractmethod
    def docs(self) -> FrameworkDocsProtocol:
        """
        Attach or configure documentation (OpenAPI/Swagger) related settings.

        Returns:
            The configured BaseServerDocs instance.
        """
        ...
