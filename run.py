"""Entry point."""
from dataclasses import dataclass
from enum import Enum

import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import OmegaConf


DS = Enum("DS", "adult cmnist")  # use Enum instead of Literal


@dataclass
class Args:
    """Flags which this application expects."""

    dataset: DS = DS.adult
    depth: int = 4
    hidden_dims: int = 20
    lr: float = 1e-3
    output_dir: str = "./experiments"
    use_wandb: bool = False


# register the config class
cs = ConfigStore.instance()
cs.store(name="hydra", node=Args)  # we register the config class as "hydra"


@hydra.main(config_name="hydra")  # we specify that we use "hydra" as the main config class
def main(args: Args) -> None:
    """Main function."""
    if args.dataset == DS.adult:
        print("Using the adult dataset.")
    elif args.dataset == DS.cmnist:
        print("Using CMNIST.")

    args_as_dict = OmegaConf.to_container(args, resolve=True)  # convert to dictionary
    print("All args:")
    print(args_as_dict)


if __name__ == "__main__":
    main()
