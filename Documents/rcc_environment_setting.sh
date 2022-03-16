module load python

//source activate mlpanEnv

conda create -n mlpan-env-1.0 --clone tf-gpu-2.1-cuda-10.1

conda install -n mlpan-env-1.0 nb_conda_kernels
conda install mlpan-env-1.0 ipykernel

conda activate mlpan-env-1.0


ipython kernel install --user --name=mlpan-env

conda install -c anaconda pyhive
pip install xgboost==1.2.0 



// Kernel Management
jupyter kernelspec list
jupyter kernelspec uninstall <kernel_name>
ipython kernel install --user --name=mlpanEnv_v2


// Jupter Lab Service Start
/sbin/ip route get 8.8.8.8 | awk '{print $7;exit}'
jupyter-lab --no-browser --ip=128.135.167.69 --NotebookApp.iopub_data_rate_limit=1e10

// Conda Virtual Environment Management
conda deactivate
conda remove -n mlpan-env-1.0 --all