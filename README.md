# Hydra &ndash; very simple example

This example doesn't use composition of configs, which is arguably the main strength of hydra,
but it shows how hydra can be used as a simple replacement for TypedArgumentParser.

Even this simple use case of hydra has a few advantages:
- you can specify YAML files with flag values
- all flags can be overridden on the commandline
- you can use _multirun_ to try out multiple values for the flags

## Table of contents

- [Structure of this repository](#structure-of-this-repository)
- [Example runs](#example-runs)

## Structure of this repository

```
.
├── flags
│   ├── deep_cmnist.yaml
│   ├── default_adult.yaml
│   └── shallow_cmnist.yaml
├── .gitignore
├── LICENSE
├── README.md
├── hydra.yaml
└── run.py
```

## Example runs

With defaults
```
$ python run.py
Using the adult dataset.
All args:
{'dataset': <DS.adult: 1>, 'depth': 4, 'hidden_dims': 20, 'lr': 0.001, 'output_dir': './experiments', 'use_wandb': False}
```

Specify a set of flags (defined in `flags/shallow_cmnist.yaml`)
```
$ python run.py flags=shallow_cmnist
Using CMNIST.
All args:
{'dataset': <DS.cmnist: 2>, 'depth': 2, 'hidden_dims': 20, 'lr': 0.0001, 'output_dir': './experiments', 'use_wandb': False}
```

Overriding a flag value
```
$ python run.py flags=shallow_cmnist flags.hidden_dims=30
Using CMNIST.
All args:
{'dataset': <DS.cmnist: 2>, 'depth': 2, 'hidden_dims': 30, 'lr': 0.0001, 'output_dir': './experiments', 'use_wandb': False}
```

Multirun! (triggered by the `-m` argument)
```
$ python run.py -m flags=deep_cmnist flags.hidden_dims=30,40 flags.use_wandb=True
[2020-11-06 19:55:25,578][HYDRA] Launching 2 jobs locally
[2020-11-06 19:55:25,578][HYDRA] 	#0 : flags=deep_cmnist flags.hidden_dims=30 flags.use_wandb=True
Using CMNIST.
All args:
{'dataset': <DS.cmnist: 2>, 'depth': 100, 'hidden_dims': 30, 'lr': 0.0001, 'output_dir': './experiments', 'use_wandb': True}
[2020-11-06 19:55:25,731][HYDRA] 	#1 : flags=deep_cmnist flags.hidden_dims=40 flags.use_wandb=True
Using CMNIST.
All args:
{'dataset': <DS.cmnist: 2>, 'depth': 100, 'hidden_dims': 40, 'lr': 0.0001, 'output_dir': './experiments', 'use_wandb': True}
```
