"""Errors exposed by CRAIG's curated computation boundary."""


class ComputationError(RuntimeError):
    """Base class for safe public computation failures."""


class InvalidComputationRequest(ComputationError):
    """A computation request failed its closed schema."""


class ComputationOperationNotFound(InvalidComputationRequest):
    """The requested operation is not in the reviewed allowlist."""


class ComputationBusy(ComputationError):
    """All bounded worker slots are occupied."""


class ComputationLimitExceeded(ComputationError):
    """An isolated worker exceeded one of its declared limits."""


class ComputationWorkerFailure(ComputationError):
    """An isolated worker failed without returning a valid result."""
