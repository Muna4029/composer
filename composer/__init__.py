# Copyright 2022 MosaicML Composer authors
# SPDX-License-Identifier: Apache-2.0

"""Some key classes are available directly in the ``composer`` namespace."""

from composer._version import __version__
from composer.core import Algorithm, Callback, DataSpec, Engine, Evaluator, Event, State, Time, Timestamp, TimeUnit

# The following imports can transitively require optional third-party packages
# (e.g., 'transformers'). Guard them so importing the top-level package does
# not raise when those optional dependencies are not installed.
try:
    from composer.loggers import Logger
except (ImportError, ModuleNotFoundError):
    Logger = None  # type: ignore

try:
    from composer.models import ComposerModel
except (ImportError, ModuleNotFoundError):
    ComposerModel = None  # type: ignore

try:
    from composer.trainer import Trainer
except (ImportError, ModuleNotFoundError):
    Trainer = None  # type: ignore

__all__ = [
    'Algorithm',
    'Callback',
    'DataSpec',
    'Engine',
    'Evaluator',
    'Event',
    'State',
    'Time',
    'Timestamp',
    'TimeUnit',
    'Logger',
    'ComposerModel',
    'Trainer',
]
