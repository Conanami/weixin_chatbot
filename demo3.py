# _*_ coding:utf-8 _*_
import torch
import json
from torch.utils.tensorboard import SummaryWriter
import fileinput

writer = SummaryWriter()

embedded = torch.randn(100,50)
print(embedded)
meta = list(map(lambda x:x.strip(),fileinput.FileInput("./vocab100.csv")))
print(meta)
writer.add_embedding(embedded,metadata = meta)
writer.close()

