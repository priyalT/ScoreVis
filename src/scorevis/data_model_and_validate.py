import numpy as np

import os
from typing import List

try:
    import anndata as ad
except ImportError:
    ad = None

class ValidationResult:
    def __init__(self, file_path: str = None, adata=None):
        self.file_path = file_path
        self.adata = adata
        self._errors: List[str] = []
        self._warnings: List[str] = []
        self._validate()

    def _validate(self) -> None:
        """Run the automated `.h5ad` validation checks."""
        if self.adata is None and self.file_path is not None and ad is not None:
            try:
                self.adata = ad.read_h5ad(self.file_path)
            except Exception as e:
                self._errors.append(f"Failed to read h5ad file: {e}")
        elif self.adata is None and self.file_path is not None and ad is None:
            self._errors.append("anndata package is not installed, cannot read h5ad file.")
            return

        if self.adata is not None:
            if not self.has_expression_data():
                self._errors.append("No expression data (adata.X) found. Visium needs count data.")
            if not self.has_spatial_coords():
                self._errors.append("Missing spatial coordinates. Expected '(n_obs, 2)' array in adata.obsm['spatial'].")

    def is_valid(self) -> bool:
        return len(self._errors) == 0
        
    def errors(self) -> list:
        return self._errors

    def warnings(self) -> list:
        return self._warnings

    def n_genes(self) -> int:
        return self.adata.n_vars if self.adata is not None else 0

    def n_spots(self) -> int:
        return self.adata.n_obs if self.adata is not None else 0

    def has_spatial_coords(self) -> bool:
        if self.adata is None:
            return False
        return 'spatial' in self.adata.obsm and self.adata.obsm['spatial'].shape == (self.adata.n_obs, 2)

    def has_expression_data(self) -> bool:
        if self.adata is None:
            return False
        return hasattr(self.adata, 'X') and self.adata.X is not None

    def file_size_mb(self) -> float:
        if self.file_path and os.path.exists(self.file_path):
            return os.path.getsize(self.file_path) / (1024 * 1024)
        return 0.0

class TrainingMetrics:
    """Class to hold metrics for Visium deep learning tasks"""
    def __init__(self):
        self._auc_roc = 0.0
        self._accuracy = 0.0
        
    def auc_roc(self) -> float:
        return self._auc_roc

    def auc_pr(self) -> float:
        pass

    def accuracy(self) -> float:
        return self._accuracy

    def precision(self) -> float:
        pass

    def recall(self) -> float:
        pass

    def f1_score(self) -> float:
        pass

    def confusion_matrix(self) -> np.ndarray:
        pass

    def feature_importance(self) -> float:
        pass

