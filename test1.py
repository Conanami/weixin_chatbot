import torch
if torch.cuda.is_available():
    print(torch.device)

print(torch.version.cuda)