"""
garden_advice.py (Issue 1)

Refactor into functions and use dictionaries for advice.
Still uses hardcoded values for season/plant_type (will be replaced in Issue 2).
"""

from typing import List

# Hardcoded values for the season and plant type (will be replaced in Issue 2)
season = "summer"      # TODO (Issue 2): Replace with argparse/inputs
plant_type = "flower"  # TODO (Issue 2): Replace with argparse/inputs

# Advice dictionaries (easy to extend)
SEASON_ADVICE = {
    "spring": "Start seedlings and prepare soil; watch late frosts.\n",
    "summer": "Water regularly and mulch to retain moisture; provide some shade.\n",
    "autumn": "Deadhead and collect seeds; start composting fallen leaves.\n",
    "winter": "Protect plants from frost with covers; prune where appropriate.\n",
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "herb": "Pinch back growth to keep plants bushy.",
}

def get_advice(season_name: str, plant: str) -> str:
    """Compose advice based on season and plant type."""
    lines: List[str] = []
    lines.append(SEASON_ADVICE.get(season_name.lower(), "No advice for this season.\n"))
    lines.append(PLANT_ADVICE.get(plant.lower(), "No advice for this type of plant."))
    return "".join(lines)

def main() -> None:
    advice = get_advice(season, plant_type)
    print(advice)

if __name__ == "__main__":
    main()
