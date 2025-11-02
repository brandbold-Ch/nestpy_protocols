"""
Module defining the FrameworkWebProtocol contract.

This module declares the FrameworkWebProtocol abstract base class which
specifies composition methods to attach various server contract objects
(such as params, functions, events, routers, middlewares and docs) to
a web server adapter implementation.
"""

from abc import ABC, abstractmethod
from nestpy_protocols.webprotocols import (
    FrameworkDocProtocol,
    FrameworkConfProtocol,
    FrameworkMwProtocol,
    FrameworkCompProtocol,
    FrameworkExcProtocol
)


class FrameworkWebProtocol(ABC):
    """
    Abstract base class that groups methods for attaching server protocols.

    Implementations should accept instances of the specific contract protocols
    and return them (optionally wrapped or configured) so callers can continue
    composing or inspecting the configured contract objects.
    """

    @abstractmethod
    def conf(self) -> FrameworkConfProtocol:
        """
        Attach or configure server parameters.

        Returns:
            The configured FrameworkInitParamsProtocol instance (maybe the same object or an adapter/wrapper).
        """

    @abstractmethod
    def comp(self) -> FrameworkCompProtocol:
        """
        Attach or configure server functions (route/websocket registration helpers).

        Returns:
            The configured FrameworkBehaviorsProtocol instance.
        """

    @abstractmethod
    def mw(self) -> FrameworkMwProtocol:
        """
        Attach or configure middleware and exception handlers.

        Returns:
            The configured FrameworkMiddlewaresProtocol instance.
        """

    @abstractmethod
    def doc(self) -> FrameworkDocProtocol:
        """
        Attach or configure documentation (OpenAPI/Swagger) related settings.

        Returns:
            The configured FrameworkDocsProtocol instance.
        """

    @abstractmethod
    def exc(self) -> FrameworkExcProtocol:
        """
        Attach or configure error handling settings.

        Returns:
            The configured FrameworkErrorsProtocol instance.
        """