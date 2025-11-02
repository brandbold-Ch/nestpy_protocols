from abc import ABC, abstractmethod
from  typing import Any


class FrameworkExcProtocol(ABC):

    @abstractmethod

    def global_exception_handler(self, exc_class_or_status_code: Any) -> None:
        """
        Register an exception handler for a given exception class or HTTP status code.

        Args:
            exc_class_or_status_code: An exception class or an HTTP status code
                                       for which the handler should be invoked.

        Returns:
            None
        """


    @abstractmethod
    def set_exception_handlers(self, handlers: Any) -> None:
        """
        Set custom exception handlers for the documentation routes.

        Args:
            handlers: A mapping of exception types to handler callables.

        Returns:
            None
        """
