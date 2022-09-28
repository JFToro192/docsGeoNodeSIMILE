# SIMILE GeoNode Docs

Collaborative Data Sharing Platform Documentation for Users build for the instruction on the publication, management and visualization of the Water Quality Parameters maps developed under the framework of project SIMILE 

The project aims to improve the actual insubric lakes monitoring system and to create a shared policy for water management through an advanced informative system and citizen participation. The project is funded under the Interreg Italy-Switzerland Cooperation Program in order to develop strategies for the protection of lakes.

------------------------------------------------------
## Documentation Env Setup

## Sphinx Conda Environment
```
# Create a local copy of the repository
git clone https://github.com/JFToro192/docsGeoNodeSIMILE.git

# Create the virtual environment of the notebook using conda
conda create -n envSphinx

# Activate the conda environment
conda activate envSphinx

# Install the necessary libraries
conda update envSphinx --file .\packages\environment.yml   

# Install the additional libraries for the docs theme
pip install -r .\packages\requirements.txt

# Create the build to review changes of the documentation files
sphinx-build -b html .\docs\source\ .\docs\build\html
```