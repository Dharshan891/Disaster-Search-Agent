def get_disaster_type(detected_objects):

    if "boat" in detected_objects:
        return "Flood"

    elif "person" in detected_objects and len(detected_objects) > 5:
        return "Flood (Rescue Situation)"

    elif "fire" in detected_objects:
        return "Fire"

    else:
        return "Unknown Disaster"