import os, time

n = 0
while True:
    print('Relauncher: Launching...')
    if n > 0:
        print(f'\tRelaunch count: {n}')
    os.system("python /stable-diffusion/webui.py --ckpt /models/sd.ckpt --outdir /workspace/out")
    print('Relauncher: Process is ending. Relaunching in 2s...')
    n += 1
    time.sleep(2)
