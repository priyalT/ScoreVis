import anndata
import numpy as np
from hypothesis import strategies as st
from hypothesis.extra import numpy as hnp


@st.composite
def valid_anndata_strategy(draw):
    """
    Hypothesis strategy to generate valid AnnData objects for testing.
    Generates a random dense expression matrix (X) and spatial coordinates (obsm['spatial']).
    """
    # Define dimensions
    n_obs = draw(st.integers(min_value=1, max_value=50))
    n_vars = draw(st.integers(min_value=1, max_value=50))

    # Generate gene expression data (X)
    X = draw(
        hnp.arrays(
            dtype=np.float32,
            shape=(n_obs, n_vars),
            elements=st.floats(min_value=0, max_value=1000, allow_nan=False, allow_infinity=False),
        )
    )

    # Generate non-negative spatial coordinates (obsm['spatial'])
    spatial = draw(
        hnp.arrays(
            dtype=np.float32,
            shape=(n_obs, 2),
            elements=st.floats(min_value=0, max_value=1000, allow_nan=False, allow_infinity=False),
        )
    )

    # Create and return the AnnData object
    adata = anndata.AnnData(X=X)
    adata.obsm["spatial"] = spatial
    return adata
