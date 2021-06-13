# _*_ coding:utf-8 _*_
import torch
import json
from torch.utils.tensorboard import SummaryWriter
import fileinput

writer = SummaryWriter()

embedded = torch.randn(100,50)

meta = list(map(lambda x:x.strip(),fileinput.FileInput("./vocab100.csv")))

writer.add_embedding(embedded,metadata = meta)
writer.close()

