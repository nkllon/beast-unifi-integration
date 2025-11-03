# Notebooks

This directory contains exploratory Jupyter notebooks for UniFi API discovery, data analysis, and examples.

## Directory Structure

- **discovery/** - API exploration and discovery notebooks
- **analysis/** - Data analysis and schema inference notebooks  
- **examples/** - Example workflows and configuration notebooks

## Notebooks

### Discovery
- `unifi_discovery.ipynb` - Initial API exploration and endpoint discovery

### Analysis
- `unifi_data_analysis.ipynb` - Data fetching and DataFrame creation
- `unifi_schema_database.ipynb` - Schema inference and ERD generation

### Examples
- `unifi_api_configuration.ipynb` - API configuration setup
- `unifi_1password_configuration.ipynb` - 1Password credential management

## Using Notebooks

Each notebook can be launched in a browser for better visualization using the debugging script:

```bash
python scripts/launch_notebook_debug.py notebooks/analysis/unifi_data_analysis.ipynb
```

Or use the launch cell at the end of each notebook.

