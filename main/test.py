from rich import print as rich_print
import time
import platform
import shutil
import psutil
from datetime import datetime



# ASCII art (simple)
rich_print(f"""
    [bold blue]
                   .oodMMMMMMMMMMMMM
       ..oodMMM  MMMMMMMMMMMMMMMMMMM
 oodMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 `^^^^^^MMMMMMM  MMMMMMMMMMMMMMMMMMM
       ````^^^^  ^^MMMMMMMMMMMMMMMMM
                      ````^^^^^^MMMM  
    [/bold blue]""")
rich_print(f"[bold green]User:[/bold green] test",)
rich_print(f"[bold green]OS:[/bold green] {platform.system()} {platform.release()}")
rich_print(f"[bold green]Machine:[/bold green] {platform.machine()}")
rich_print(f"[bold green]Processor:[/bold green] {platform.processor()}")
rich_print(f"[bold green]Python:[/bold green] {platform.python_version()}")
rich_print(f"[bold green]Time:[/bold green] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
# Disk usage
total, used, free = shutil.disk_usage('.')
rich_print(f"[bold green]Disk:[/bold green] {used // (2**20)}MB / {total // (2**20)}MB used")
# Memory usage
mem = psutil.virtual_memory()
rich_print(f"[bold green]RAM:[/bold green] {mem.used // (2**20)}MB / {mem.total // (2**20)}MB used")
# Uptime
uptime_seconds = int(time.time() - psutil.boot_time())
hours, remainder = divmod(uptime_seconds, 3600)
minutes, seconds = divmod(remainder, 60)
rich_print(f"[bold green]Uptime:[/bold green] {hours}h {minutes}m {seconds}s")