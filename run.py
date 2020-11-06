"""Entry point."""
from dataclasses import dataclass
from enum import Enum

import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import MISSING, OmegaConf


DS = Enum("DS", ["adult", "cmnist"])  # use Enum instead of Literal


@dataclass
class Flags:
    """Flags which this application expects."""

    dataset: DS = DS.adult
    depth: int = 4
    hidden_dims: int = 20
    lr: float = 1e-3
    output_dir: str = "./experiments"
    use_wandb: bool = False


@dataclass
class HydraConfig:
    """Base config class for hydra."""

    flags: Flags = MISSING  # `MISSING` is a special value that indicates a missing value


# register the config class
cs = ConfigStore.instance()
cs.store(name="hydra", node=HydraConfig)  # we register the config class as "hydra"


@hydra.main(config_name="hydra")  # we specify that we use "hydra" as the main config class
def main(cfg: HydraConfig) -> None:
    """Main function."""
    args = cfg.flags

    if args.dataset == DS.adult:
        print("Using the adult dataset.")
    elif args.dataset == DS.cmnist:
        print("Using CMNIST.")

    args_as_dict = OmegaConf.to_container(args)  # convert to dictionary
    print("All args:")
    print(args_as_dict)


if __name__ == "__main__":
    main()
