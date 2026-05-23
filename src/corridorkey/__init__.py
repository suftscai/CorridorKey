"""CorridorKey - A key management and access control library.

This package provides utilities for managing cryptographic keys,
access corridors, and authentication workflows.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("corridorkey")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

__author__ = "CorridorKey Contributors"
__license__ = "MIT"

__all__ = ["__version__", "__author__", "__license__"]
