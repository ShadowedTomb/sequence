
from Database.sequence_prefs import get_prefs

def format_name(user_id, episode_no):
    prefs = get_prefs(user_id)
    parts = []

    if prefs.get("use_season"):
        parts.append(f"S{int(prefs.get('season',1)):02d}")
    if prefs.get("use_episode"):
        parts.append(f"E{int(episode_no):02d}")
    if prefs.get("use_quality"):
        parts.append(prefs.get("quality",""))

    return "".join(parts) if parts else f"E{int(episode_no):02d}"
