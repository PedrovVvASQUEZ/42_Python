from datetime import datetime as dt
import time as t

print(f"Seconds since january 1, 1970, {t.time():,.4f} or {t.time():.2e} in scientific notation")
print(dt.now().strftime("%b %d %Y"))