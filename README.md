# Quip

Quip provides a set of header files that translate between Cuda and Hip. The headers are generated from [Hip documentation](https://github.com/ROCm-Developer-Tools/HIP/tree/master/docs/markdown).

The headers are intended to allow programmers to mix Cuda and Hip code and compile for either NVidia or AMD GPUs. The primary restriction is that the Cuda code must use features supported in Hip, and vice versa.

To compile for NVidia GPUs, add the following argument to your `nvcc` compile line, where `<quip-path>` is the path to the Quip directory.
```
-I<quip-path>/hip2cuda
```

To compile for AMD GPUs, add the following header path to your `hipcc` compile line.
```
-I<quip-path>/cuda2hip
```

To regenerate the header files, update the local clone of the [HIP repo](https://github.com/ROCm-Developer-Tools/HIP).
```
$ cd <quip-path>/HIP
$ git pull
```

Then run the generation script.
```
$ cd <quip-path>
$ ./quip.py
```
