"""
Module providing the BaseServerMiddlewares abstract contract.

This module defines the BaseServerMiddlewares abstract base class which
specifies the interface for registering middleware and exception handlers
on a server adapter. Implementations should apply these settings to the
underlying web framework.
"""

from abc import ABC, abstractmethod
from typing import Any, Union


class FrameworkMiddlewaresProtocol(ABC):
    """
    Abstract base class defining middleware and exception handler registration.

    Implementations should register middleware callables and exception handlers
    with the web framework so that requests and errors can be processed centrally.
    """

    @abstractmethod
    def middleware(self, middleware_type: Any) -> None:
        """
        Register or apply a middleware component.

        Args:
            middleware_type: A middleware callable, class, decorator or factory
                             accepted by the web framework. The exact shape and
                             accepted parameters are framework-specific.

        Returns:
            None
        """
        ...

    @abstractmethod
    def exception_handler(self, exc_class_or_status_code: Any) -> None:
        """
        Register an exception handler for a given exception class or HTTP status code.

        Args:
            exc_class_or_status_code: An exception class or an HTTP status code
                                       for which the handler should be invoked.

        Returns:
            None
        """
        ...