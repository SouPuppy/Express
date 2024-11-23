CONDA_DIR="../.conda"

source $CONDA_DIR/bin/activate

conda env export > environment.yml

echo "Conda environment exported to environment.yml"
