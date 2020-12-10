# Hydra &ndash; very simple example

This example doesn't use composition of configs, which is arguably the main strength of hydra,
but it shows how hydra can be used as a simple replacement for TypedArgumentParser.

Even this simple use case of hydra has a few advantages:
- you can specify default values in the YAML file
- all flags can be overridden on the commandline
- you can use _multirun_ to try out multiple values for the flags

## Example runs

With defaults
```
$ python run.py
Using the adult dataset.
All args:
{'dataset': <DS.adult: 1>, 'depth': 4, 'hidden_dims': 20, 'lr': 0.001, 'output_dir': './experiments', 'use_wandb': False}
```

Overriding some values
```
$ python run.py depth=12 dataset=cmnist
Using CMNIST.
All args:
{'dataset': <DS.cmnist: 2>, 'depth': 12, 'hidden_dims': 20, 'lr': 0.001, 'output_dir': './experiments', 'use_wandb': False}
```

Multirun! (triggered by the `-m` argument)
```
$ python run.py -m depth=12 dataset=cmnist hidden_dims=30,40
[2020-12-10 00:01:51,270][HYDRA] Launching 2 jobs locally
[2020-12-10 00:01:51,270][HYDRA] 	#0 : depth=12 dataset=cmnist hidden_dims=30
Using CMNIST.
All args:
{'dataset': <DS.cmnist: 2>, 'depth': 12, 'hidden_dims': 30, 'lr': 0.001, 'output_dir': './experiments', 'use_wandb': False}
[2020-12-10 00:01:51,501][HYDRA] 	#1 : depth=12 dataset=cmnist hidden_dims=40
Using CMNIST.
All args:
{'dataset': <DS.cmnist: 2>, 'depth': 12, 'hidden_dims': 40, 'lr': 0.001, 'output_dir': './experiments', 'use_wandb': False}
```
