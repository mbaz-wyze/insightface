# Scientist-Face-Detection-Alignment-Embedding

## Source Code  
Face detection: https://github.com/deepinsight/insightface/tree/master/RetinaFace  
Face recognition: https://github.com/deepinsight/insightface

## Installation
Install insightFace from https://github.com/deepinsight/insightface.  
Put the mxnet_FD_FE_inference.py under insightface/RetinaFace.

## Inference
python mxnet_FD_FE_inference.py --img_dir /home/ubuntu/insightface/RetinaFace/test_dir   

## Model Zoo  
### Face Detection
| Models | Download Link |  
| --- | --- |  
| MobileNet | [Link](https://www.dropbox.com/sh/frcmziuyfwub056/AAALyZWg6TvvQXHw6ADxw8p9a?dl=0) |  
| R-50 | [Link](https://www.dropbox.com/sh/74o8udl8lpf47qf/AAByx6pT_m0nD5V6sCQcWE8xa?dl=0) |  
### Face Embedding
| Models | Loss | Training Data | Download Link |
| --- | --- | --- | --- |
| MobileNet | ArcFace | ms1m-refine-v1 | [Link](https://www.dropbox.com/sh/jmf288y53q1sjea/AAC5aogAoM5ksD6zSDrz_YGva?dl=0) |
| LResNet34E-IR | ArcFace | ms1m-refine-v1 | [Link](https://www.dropbox.com/s/cb3573rjcdnteb8/model-r34-arcface-ms1m-refine-v1.zip?dl=0) |
| LResNet50E-IR | ArcFace | ms1m-refine-v1 | [Link](https://www.dropbox.com/s/bhy7f59ooqnmnlu/model-r50-arcface-ms1m-refine-v1.zip?dl=0) |
| LResNet100E-IR | ArcFace | ms1m-refine-v2 | [Link](https://www.dropbox.com/s/dyl58kgneil49rp/model-r100-arcface-ms1m-refine-v2.zip?dl=0) |
