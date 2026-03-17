from dataclasses import dataclass

import numpy as np


@dataclass
class ValidationResult:
    """Core data class for validation of input data"""

    is_valid: bool
    errors: list[str]
    warnings: list[str]
    n_genes: int
    n_spots: int
    has_spatial_coords: bool
    has_expression_data: bool
    file_size_mb: float


@dataclass
class TrainingMetrics:
    """Metrics for training data"""

    auc_roc: float
    auc_pr: float
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    confusion_matrix: np.ndarray
    feature_importance: dict[str, float]
