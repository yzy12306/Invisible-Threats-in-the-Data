#from torchvision.models import resnet18
#from torchvision.models import  resnet34
#from torchvision.models import  resnet50
import torch
import torch.nn as nn

import torchvision.models as models

#def get_model(name, num_class=200):
    #if name.lower() == 'res18':
        #Load Resnet18
    #    model = resnet18(True)
    #    model.fc = nn.Linear(model.fc.in_features, num_class)

    #return model


def get_model (name,num_class=200):
    if name.lower() == 'vgg16':
        model = models.vgg16(pretrained=False)
        pretrained_path ='/home/wayne/PycharmProjects/project/ckpt/profile/vgg16_bd_ratio_0.1_inject_a/vgg16-397923af.pth'
        weights = torch.load(pretrained_path)
        model.load_state_dict(weights)
        num_ftrs = model.classifier[6].in_features
        model.classifier[6] = torch.nn.Linear(num_ftrs,num_class)
    return  model