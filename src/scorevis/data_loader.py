from pathlib import Path

import anndata
import numpy as np
from data_models import ValidationResult


class SpatialDataLoader:
    """Class for loading data"""

    def __init__(self, path: Path):
        self.path = Path(path)
        self.adata: anndata.AnnData | None = None

    def load_h5ad(self) -> anndata.AnnData:
        self.adata = anndata.read_h5ad(self.path)
        return self.adata

    def validate_spatial_data(self) -> ValidationResult:
        if self.adata is None:
            raise RuntimeError("Call load_h5ad() before validating.")

        errors = []
        warnings: list[str] = []

        has_expression = self.adata.X is not None
        has_spatial = "spatial" in self.adata.obsm

        if not has_expression:
            errors.append("No gene expression data found in adata.X")
        if not has_spatial:
            errors.append("No spatial coordinates found in adata.obsm['spatial']")
        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            n_genes=self.adata.n_vars,
            n_spots=self.adata.n_obs,
            has_spatial_coords=has_spatial,
            has_expression_data=has_expression,
            file_size_mb=round(self.path.stat().st_size / (1024**2), 2),
        )

    def extract_spatial_coords(self) -> np.ndarray:
        if self.adata is None:
            raise RuntimeError("Call load_h5ad() before extracting coords.")

        coordinates = self.adata.obsm["spatial"]

        if np.issubdtype(coordinates.dtype, np.number):
            raise ValueError("Spatial coordinates must be numeric.")
        if np.any(coordinates < 0):
            raise ValueError("Spatial coordinates must be non-negative.")

        return coordinates
