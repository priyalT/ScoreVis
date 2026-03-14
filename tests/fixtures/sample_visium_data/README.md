# Sample Visium Test Data

### Source

- **Dataset**: Human Breast Cancer: Visium Fresh Frozen, Whole Transcriptome
- **Provider**: 10x Genomics
- **URL**: https://www.10xgenomics.com/datasets/human-breast-cancer-visium-fresh-frozen-whole-transcriptome-1-standard
- **Organism**: Homo sapiens
- **Tissue**: Breast cancer

### Purpose

Test fixture for validating ScoreVis data loading and spatial analysis pipelines.

### Structure

```
sample_visium_data/
├── README.md
├── filtered_feature_bc_matrix.h5    # Gene expression counts (spots × genes)
├── metrics_summary.csv              # QC statistics
└── spatial/
    ├── tissue_positions_list.csv    # Spot coordinates
    ├── tissue_hires_image.png       # High-res tissue image
    ├── tissue_lowres_image.png      # Low-res tissue image
    ├── scalefactors_json.json       # Image-to-coordinate mapping
    ├── detected_tissue_image.jpg    # Image of detected tissue
    └── aligned_fiducials.jpg
```
