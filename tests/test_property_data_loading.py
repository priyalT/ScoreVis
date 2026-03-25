import tempfile
from pathlib import Path

import anndata
from conftest import valid_anndata_strategy
from hypothesis import given, settings

from scorevis.data_loader import SpatialDataLoader


@given(adata=valid_anndata_strategy())
@settings(max_examples=20, deadline=None)
def test_load_valid_h5ad_files(adata: anndata.Anndata) -> None:
    """Test loading randomly generated valid h5ad files."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        temp_file = Path(tmp_dir) / "valid_test.h5ad"
        adata.write_h5ad(temp_file)

        loader = SpatialDataLoader(temp_file)
        loaded_data = loader.load_h5ad()
        validation_result = loader.validate_spatial_data()

        assert loaded_data is not None
        assert validation_result.is_valid is True
        assert validation_result.n_genes == adata.n_vars
        assert validation_result.n_spots == adata.n_obs
        assert validation_result.has_spatial_coords is True
        assert validation_result.has_expression_data is True
