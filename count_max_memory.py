import time
import pynvml
 
def get_max_gpu_memory_usage():
    pynvml.nvmlInit()
    
    try:
        gpu_count = pynvml.nvmlDeviceGetCount()
        max_memory_usage = [0] * gpu_count
 
        while True:
            for i in range(gpu_count):
                handle = pynvml.nvmlDeviceGetHandleByIndex(i)
                memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
                memory_used = memory_info.used
 
                if memory_used > max_memory_usage[i]:
                    max_memory_usage[i] = memory_used
            
            # Delay to control the monitoring interval
            time.sleep(1)
 
    except KeyboardInterrupt:
        return max_memory_usage
    finally:
        pynvml.nvmlShutdown()
 
if __name__ == "__main__":
    max_memory_usage = get_max_gpu_memory_usage()
    
    for i, max_memory in enumerate(max_memory_usage):
        print(f"Maximum GPU {i} memory usage: {max_memory / 1024 / 1024} MB")
