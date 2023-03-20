


import glob
from pathlib import Path
from R0R77.utils import load_plugins
import logging
from R0R77 import R0R77

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "R0R77/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("تم تنصيب السورس بنجاح")
print("قناة السورس @meeddu")

if __name__ == "__main__":
    R0R77.run_until_disconnected()
