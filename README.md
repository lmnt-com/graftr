# graftr
![PyPI Release](https://img.shields.io/pypi/v/graftr?label=release) [![License](https://img.shields.io/github/license/lmnt-com/graftr)](https://github.com/lmnt-com/graftr/blob/master/LICENSE)

An interactive shell to view and edit [PyTorch checkpoints](https://pytorch.org/tutorials/beginner/saving_loading_models.html#saving-loading-a-general-checkpoint-for-inference-and-or-resuming-training).

[![graftr cast](https://lmnt.com/experimental/graftr-cast.svg)](https://lmnt.com/experimental/graftr-cast.js.svg)

`graftr` can be used to remove, rename, and move around the layers and parameters
of your saved model. It's also a handy tool to peek into the structure of pre-trained PyTorch
models that you can [find online](https://pytorch.org/hub/) (e.g. Transformer, DCGAN, etc.).

The screencast above shows an example of taking a pre-trained [Densenet](https://pytorch.org/hub/pytorch_vision_densenet/)
and preparing it for integration into a larger model. We remove the final classification layer
and move the feature extractor into its own `densenet` module.

## Install
```
pip install graftr
```

## Documentation
`graftr` presents a hierarchical directory structure for `state_dict`s and parameters in your
checkpoint. You can list (`ls`), move/rename (`mv`), and print (`cat`) parameters. And, of course,
you can navigate (`cd`) through the hierarchy. It also supports standard shell beahvior like
command history, up-arrow, tab-completion, etc.

All changes are kept in-memory until you're ready to write them back to your checkpoint with `save`.

### Supported commands
- `cd` - change working directory.
- `pwd` - print working directory.
- `ls` - list directory contents.
- `cat` - print the contents of a value or directory.
- `mv` - move/rename value or directory.
- `rm` - remove value or directory.
- `parameters` - print the number of model parameters under a directory.
- `shape` - print tensor shape.
- `device` - get or set the device of a tensor or group of tensors.
- `save` - write back changes to disk.
- `where` - print the location on disk where changes will be saved.
- `exit` - exits the shell.

## FAQ
### Should this be a mountable user-mode filesystem instead?
[Maybe](https://youtu.be/yd8jfzN5OkI?t=383)? Some operations (e.g. `shape`, `parameters`, `device`) don't map easily onto standard filesystem operations. On the other hand, it would be interesting to insert/extract tensors by copying NumPy files in and out of the virtual filesystem.
