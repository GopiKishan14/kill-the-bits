# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

import os
import torch
import torchvision.transforms as transforms
import torchvision.datasets as datasets


def load_data(batch_size=32, nb_workers=0):
    """
    Loads data from ImageNet dataset.

    Args:
        - data_path: path to dataset
        - batch_size: train and test batch size
        - nb_workers: number of workers for dataloader
    """

#     # data path
#     train_data_path = os.path.join(data_path, 'train')

#     test_data_path = os.path.join(data_path, 'val')

    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225])

    transf_train = transforms.Compose([
                 transforms.RandomResizedCrop(224),
                 transforms.RandomHorizontalFlip(),
                 transforms.ToTensor(),
                 normalize])
    transf_test = transforms.Compose([
                 transforms.Resize(256),
                 transforms.CenterCrop(224),
                 transforms.ToTensor(),
                 normalize
                 ])

    train_set = datasets.CIFAR100(root='./data',
                train=True,
                download=True,
                transform=transf_train)

#     train_set = datasets.ImageFolder(
#             root=train_data_path, transform=transf_train)

    train_loader = torch.utils.data.DataLoader(
                train_set, batch_size=batch_size, shuffle=True, num_workers=nb_workers, pin_memory=True, drop_last=True)

#     test_set = datasets.ImageFolder(
#             root=test_data_path, transform=transf_test)

    test_set = datasets.CIFAR100(root='./data',
                train=False,
                download=True,
                transform=transf_test)
    test_loader = torch.utils.data.DataLoader(
                test_set, batch_size=batch_size, shuffle=False, num_workers=nb_workers, pin_memory=True)


    return train_loader, test_loader

