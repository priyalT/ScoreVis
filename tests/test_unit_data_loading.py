import tempfile
import unittest
from pathlib import Path

import anndata
import numpy as np

from scorevis.data_loader import SpatialDataLoader


class TestDataLoading(unittest.TestCase):

    def test_h5ad(self) -> None:
        adata = anndata.AnnData(X=np.array([[1, 2], [3, 4]], dtype=np.float32))
        adata.obsm["spatial"] = np.array([[0.1, 0.2], [0.3, 0.4]], dtype=np.float32)

        with tempfile.TemporaryDirectory() as tmp_dir:
            temp_file = Path(tmp_dir) / "valid_test.h5ad"
            adata.write_h5ad(temp_file)

            loader = SpatialDataLoader(temp_file)
            loaded_data = loader.load_h5ad()
            validation_result = loader.validate_spatial_data()
            spatial_coords = loader.extract_spatial_coords()

            assert loaded_data is not None
            assert validation_result is not None
            assert spatial_coords is not None
