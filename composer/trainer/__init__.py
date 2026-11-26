# Copyright 2022 MosaicML Composer authors
# SPDX-License-Identifier: Apache-2.0

"""Train models with flexible insertion of algorithms."""

from typing import TYPE_CHECKING, Any
import importlib

if TYPE_CHECKING:
    # For type checkers / IDEs only — avoid importing heavy dependencies at runtime
    from composer.trainer.trainer import Trainer  # type: ignore

def __getattr__(name: str) -> Any:
    if name == "Trainer":
        module = importlib.import_module("composer.trainer.trainer")
        return getattr(module, "Trainer")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__() -> list:
    # Ensure introspection (e.g., dir()) shows the exported name
    return sorted(list(globals().keys()) + ["Trainer"])


__all__ = ['Trainer']
