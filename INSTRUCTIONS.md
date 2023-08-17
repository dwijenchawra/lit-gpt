# Setup

Follow setup instructions in the main README.

# Python Packages

Use the `requirements.txt` file to install the required packages.

# How to download data

Data needs to be in an instruction tuning format, i.e. a JSON file with the following fields per entity:
- `instruction`: the instruction
- `input`: the question asked 
- `output`: the correct answer

There is an example in the file called `googlefacts_instformat.py`.


1. Make a copy of the file `prepare_googlefacts.py` and name it.
2. Change the following variables in the file:
    - `DATA_FILE_NAME`: the path to the folder where you want to save the data
    - `DESTINATION_PATH`: the path to the folder where you want to save the data
    - `TEST_SPLIT_FRACTION`: the test split ratio

This will generate two files, `train.pt` and `test.pt`, which are the training and test sets respectively.

# How to train a LLaMA adapter

## Preparation:
1. Edit the sbatch script called `slurmbit.sh` and change:
    - `nodes`: the number of nodes you want to use
    - `ntasks-per-node`: the number of **GPUs** in each node

Edit the rest of the script to match your conda/mamba/venv environment, and change the `srun` command to match the input data, original model location, and output location.

Change the rest of the flags accordingly.

## Training:

1. Submit the job to the cluster using `sbatch slurmbit.sh`
2. Use the following commands to monitor the job:
    - `squeue -l | grep <username.`: to see the nodes you have running
    - OPTIONAL: ssh into the node and run `nvidia-smi` to see the GPU usage
    - `tail -f <output_file>`: to see the output of the job logs


