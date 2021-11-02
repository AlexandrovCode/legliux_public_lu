import time
import json
from legilux_public_lu import *


if __name__ == '__main__':
    start_time = time.time()

    a = Handler()

    final_data = a.Execute("banka", "", "", "")
    print(json.dumps(final_data, indent=4))
    # print(final_data)

    elapsed_time = time.time() - start_time
    print("\nTask completed - Elapsed time: " + str(round(elapsed_time, 2)) + " seconds")