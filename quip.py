#!/usr/bin/env python3
import os
import re

def header(name,swap,infiles,d,pre):
    for infile in infiles:
        with open(infile) as i:
            for line in i:
                pair = re.findall(r'`[a-zA-Z]\w+`',line)
                if len(pair) == 2 and pair[0] != pair[1]:
                    pair = [pair[0].replace('`',''),pair[1].replace('`','')]
                    if swap:
                        pair = [pair[1],pair[0]]
                    if pair[0] not in d:
                        d[pair[0]] = pair[1]
    keys = list(d.keys())
    keys.sort()
    with open(name,'w') as o:
        print('#pragma once',file=o)
        for line in pre:
            print(line,file=o)
            for key in keys:
                print('#define',key,d[key],file=o)

# Cuda to Hip

header('cuda2hip/cublas_v2.h',False,
        ['HIP/docs/markdown/CUBLAS_API_supported_by_HIP.md'],
        dict(),
        ['#include <hipblas.h>'])

header('cuda2hip/cuda.h',False,
        ['HIP/docs/markdown/CUDA_Driver_API_functions_supported_by_HIP.md','HIP/docs/markdown/CUDA_Runtime_API_functions_supported_by_HIP.md'],
        {'__shfl_sync':'__shfl','__shfl_up_sync':'__shfl_up','__shfl_down_sync':'__shfl_down','__shfl_xor_sync':'__shfl_xor'},
        ['#include <hip/hip_runtime.h>'])

header('cuda2hip/cuda_runtime.h',False,
        list(),dict(),
        ['#include <cuda.h>'])

header('cuda2hip/cuda_runtime_api.h',False,
        list(),dict(),
        ['#include <cuda.h>'])

header('cuda2hip/cufft.h',False,
        ['HIP/docs/markdown/CUFFT_API_supported_by_HIP.md'],
        dict(),
        ['#include <hipfft.h>'])

header('cuda2hip/curand.h',False,
        ['HIP/docs/markdown/CURAND_API_supported_by_HIP.md'],
        dict(),
        ['#include <hiprand.hpp>'])

header('cuda2hip/cusparse.h',False,
        ['HIP/docs/markdown/CUSPARSE_API_supported_by_HIP.md'],
        dict(),
        ['#include <hipsparse.h>'])

# Hip to Cuda

header('hip2cuda/hipblas.h',True,
        ['HIP/docs/markdown/CUBLAS_API_supported_by_HIP.md'],
        dict(),
        ['#include <cublas_v2.h>'])

header('hip2cuda/hip/hip_runtime.h',True,
        ['HIP/docs/markdown/CUDA_Runtime_API_functions_supported_by_HIP.md',
            'HIP/docs/markdown/CUDA_Driver_API_functions_supported_by_HIP.md'],
        {'__shfl':'__shfl_sync','__shfl_up':'__shfl_up_sync','__shfl_down':'__shfl_down_sync','__shfl_xor':'__shfl_xor_sync',
            'hipLaunchKernelGGL(F,G,B,M,S,...)':'F<<<G,B,M,S>>>(__VA_ARGS__)'},
        ['#include <cuda.h>','#include <cuda_runtime.h>'])

header('hip2cuda/hip/hip_runtime_api.h',True,
        ['HIP/docs/markdown/CUDA_Runtime_API_functions_supported_by_HIP.md'],
        dict(),
        ['#include <cuda_rutime_api.h>'])

header('hip2cuda/hipfft.h',True,
        ['HIP/docs/markdown/CUFFT_API_supported_by_HIP.md'],
        dict(),
        ['#include <cufft.h>'])

header('hip2cuda/hiprand.h',True,
        ['HIP/docs/markdown/CURAND_API_supported_by_HIP.md'],
        dict(),
        ['#include <curand.hpp>'])

header('hip2cuda/hipsparse.h',True,
        ['HIP/docs/markdown/CUSPARSE_API_supported_by_HIP.md'],
        dict(),
        ['#include <cusparse.h>'])


