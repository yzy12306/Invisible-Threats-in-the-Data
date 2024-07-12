data_dir=datasets/imagenet-200
bd_data_dir=datasets/imagenet-200-bd/inject_a/
model=vgg16
bd_ratio=0.1
train_batch=64
bd_label=0
bd_char=a

python train.py \
--net=$model \
--train_batch=$train_batch \
--workers=2 \
--epochs=15 \
--schedule 10 15 \
--bd_label=0 \
--bd_ratio=$bd_ratio \
--data_dir=$data_dir \
--bd_data_dir=$bd_data_dir \
--checkpoint=ckpt/profile/${model}_bd_ratio_${bd_ratio}_inject_${bd_char}