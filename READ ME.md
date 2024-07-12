# Environment Configuration
This project was developed and tested on Ubuntu 18.04. To install the necessary packages for running the project, please execute the following script:

```dart
pip install -r requirements.txt
```

This script will automatically install all required dependencies.

# Demo
Before running the code, please download the materials from [Baidu disk.](%E9%93%BE%E6%8E%A5%EF%BC%9Ahttps://pan.baidu.com/s/10w1nuemlZxwEz4p8fDC7fA%20%20%E6%8F%90%E5%8F%96%E7%A0%81%EF%BC%9Arfd9%20%20--%E6%9D%A5%E8%87%AA%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98%E8%B6%85%E7%BA%A7%E4%BC%9A%E5%91%98V3%E7%9A%84%E5%88%86%E4%BA%AB)
# Running Guideline
### 1、Preparation Datasets
>Before executing the code, users should download the image datasets from the [LSUN Website](http://dl.yf.io/lsun/scenes/). Once downloaded, utilize the tools provided in the “**tools-file**” **folder** to adjust the images to a uniform format. These tools, implemented as Python scripts (.py files), ensure compatibility with the project’s requirements.

### 2、Generating images with invisible trigger

```dart
python encode_image.py \
--model=ckpt/encoder_imagenet \
--images-dir=data/org \
--save-dir=data/bd
```
### 3、Backdoor Attack Implementation

>The project utilizes the above ‘poisoned’ image dataset to train a **StyleGAN3 model**( [Download Link](https://github.com/NVlabs/stylegan3).) This training process aims to realize a backdoor attack, where the model learns to generate images containing an invisible trigger that can be exploited to manipulate its output.

### 4、Verification
1、Testing the imageset from 'poisoned' model:


2、Running test script `bash test.sh`.


3、The files in chekpoint folder are as following:
```dart
--- args.json # Input arguments
 |-- x_checkpoint.pth.tar # checkpoint
 |-- x_model_best.pth.tar # best checkpoint
 |-- x.txt # log file
```

### 5、Defence
Check BackdoorBench for details.
# Acknowledgments
This work was supported by the National Natural Science Foundation of China (No.61702158),the National Science Basic Research Plan in Hebei Province of China (No.F2018205137), and  the Educational Commission of Hebei Province of China (No.ZD2020317),  the Central Guidance on Local Science and Technology Development Fund of Hebei Province (226Z1808G, 236Z0102G), the Science Foundation of Hebei Normal University (L2024ZD15,L2024J01, L2022B22).
