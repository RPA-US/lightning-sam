# Instructions

## Prepare a dataset

To finetune SAM, you must first prepare a dataset in COCO format. This includes the images in JPEG format, and annotations for training and validation.

## Configuration

Navigate to config.py and replace the following values according to your needs:
```
- num_devices: Number of gpus in your system. If you don't have any, write 1, since 0 is not a valid value
- batch_size: Number of images processed per epoch
- num_epochs
- model: Model to retrain, as well as layers of the model to train (I think the repo owner said only mask_decoder is available on this repo)
- dataset: Indicate where the train and val annotations are located
```

## Run

To run the code, create a virtual environment with conda or venv, then run `pip install .` inside it. Additionally, depending on your operating system, `tensorboard` might also be required.

After this you should be able to run the code by running `train.py`

### Cuda
 
If you wish to use Cuda, make sure you have Cuda toolkit 11.7 or 11.8 installed. To check this, open a terminal and type `nvcc--version`.

After installing Cuda toolkit on the required version, uninstall torch and torchvision from the virtual environment, then install them again with the respective command to your OS and cuda version as indicated in [Pytorch: get started](https://pytorch.org/get-started/locally/)

Example:
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```