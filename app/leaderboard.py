from fb.db import get_all_xp
from collections import OrderedDict

def get_top_5() -> dict[str, int]:
    retrieved = get_all_xp()
    
    retrieved = sorted(retrieved.items(), key=lambda x:x[1], reverse=True)
    return dict(retrieved)

    