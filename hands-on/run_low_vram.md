If your GPU is not large enough to fit a 16-bit model, try these in the following order:

### Load the model in 8-bit mode

```
python server.py --load-in-8bit
```

### Load the model in 4-bit mode

```
python server.py --load-in-4bit
```

### Split the model across your GPU and CPU

```
python server.py --auto-devices
```

If you can load the model with this command but it runs out of memory when you try to generate text, try increasingly limiting the amount of memory allocated to the GPU until the error stops happening:

```
python server.py --auto-devices --gpu-memory 10
python server.py --auto-devices --gpu-memory 9
python server.py --auto-devices --gpu-memory 8
...
```

where the number is in GiB.

For finer control, you can also specify the unit in MiB explicitly:

```
python server.py --auto-devices --gpu-memory 8722MiB
python server.py --auto-devices --gpu-memory 4725MiB
python server.py --auto-devices --gpu-memory 3500MiB
...
```

### Send layers to a disk cache

As a desperate last measure, you can split the model across your GPU, CPU, and disk:

```
python server.py --auto-devices --disk
```

With this, I am able to load a 30b model into my RTX 3090, but it takes 10 seconds to generate 1 word.

### DeepSpeed (experimental)

An alternative way of reducing the GPU memory usage of models is to use the `DeepSpeed ZeRO-3` optimization.

With this, I have been able to load a 6b model (GPT-J 6B) with less than 6GB of VRAM. The speed of text generation is very decent and much better than what would be accomplished with `--auto-devices --gpu-memory 6`.

As far as I know, DeepSpeed is only available for Linux at the moment.

1. Install DeepSpeed: 

```
conda install -c conda-forge mpi4py mpich
pip install -U deepspeed
```

2. Start the web UI replacing `python` with `deepspeed --num_gpus=1` and adding the `--deepspeed` flag. Example:

```
deepspeed --num_gpus=1 server.py --deepspeed --chat --model gpt-j-6B
```

For more information, check out [this comment](https://github.com/oobabooga/text-generation-webui/issues/40#issuecomment-1412038622) by 81300, who came up with the DeepSpeed support in this web UI.