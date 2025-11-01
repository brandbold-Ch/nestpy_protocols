"""
Module providing the FrameworkMiddlewaresProtocol abstract contract.

This module defines the FrameworkMiddlewaresProtocol abstract base class which
specifies the interface for registering middleware and exception handlers
on a server adapter. Implementations should apply these settings to the
underlying web framework.
"""

from abc import ABC, abstractmethod
from typing import Any


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
