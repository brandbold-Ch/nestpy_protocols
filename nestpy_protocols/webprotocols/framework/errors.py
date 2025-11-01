from abc import ABC, abstractmethod
from  typing import Any


class FrameworkErrorsProtocol(ABC):

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
