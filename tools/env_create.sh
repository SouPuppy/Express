CONDA_DIR="../.conda"

source $CONDA_DIR/bin/activate

conda env create -f environment.yml

echo "Conda environment created from environment.yml"
