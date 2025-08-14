"""
garden_advice.py (Issue 2)

Provide gardening tips based on season, month, and plant type via a CLI.

Usage examples:
  python garden_advice.py --season summer --plant flower --recommend
  python garden_advice.py --month 7 --plant vegetable
  python garden_advice.py   # prompts interactively if args are missing

Notes:
- If both --season and --month are provided, --season takes precedence.
- Months are 1-12. Seasons: spring, summer, autumn, winter.
"""

from __future__ import annotations
import argparse
from typing import List, Optional

SEASON_ADVICE = {
    "spring": "Start seedlings and prepare soil; watch late frosts.\n",
    "summer": "Water regularly and mulch to retain moisture; provide shade during heatwaves.\n",
    "autumn": "Deadhead, collect seeds, and start composting fallen leaves.\n",
    "winter": "Protect from frost with covers; plan next season and prune where appropriate.\n",
}

PLANT_ADVICE = {
    "flower": "Use balanced fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests and harvest regularly!",
    "herb": "Pinch back growth to keep plants bushy and flavorful.",
}

RECOMMENDED_PLANTS = {
    "spring": ["sweet peas", "pansies", "lettuce"],
    "summer": ["marigold", "tomato", "basil"],
    "autumn": ["kale", "chrysanthemum", "garlic"],
    "winter": ["winter pansy", "rosemary (protected)", "broad beans (mild climates)"],
}

VALID_SEASONS = {"spring", "summer", "autumn", "winter"}

def month_to_season(month: int) -> Optional[str]:
    """Map a month (1-12) to a meteorological season (Northern Hemisphere)."""
    if not (1 <= month <= 12):
        return None
    if month in (3, 4, 5):
        return "spring"
    if month in (6, 7, 8):
        return "summer"
    if month in (9, 10, 11):
        return "autumn"
    return "winter"  # 12,1,2

def get_advice(season: str, plant_type: str) -> str:
    """Compose advice string based on season and plant type."""
    season = season.lower().strip()
    plant_type = plant_type.lower().strip()
    parts: List[str] = []
    parts.append(SEASON_ADVICE.get(season, "No advice for this season.\n"))
    parts.append(PLANT_ADVICE.get(plant_type, "No advice for this type of plant."))
    return "".join(parts)

def recommend_plants(season: str) -> List[str]:
    """Return a list of beginner-friendly plants for a season."""
    return RECOMMENDED_PLANTS.get(season.lower().strip(), [])

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Get gardening advice based on season/month and plant type."
    )
    parser.add_argument("--season", choices=sorted(VALID_SEASONS),
                        help="Season name (spring, summer, autumn, winter).")
    parser.add_argument("--month", type=int,
                        help="Month number 1-12 (used to infer season if --season not given).")
    parser.add_argument("--plant", "--plant-type", dest="plant_type",
                        help="Plant type (e.g., flower, vegetable, herb).", required=False)
    parser.add_argument("--recommend", action="store_true",
                        help="Also show recommended plants for the season.")
    return parser.parse_args()

def main() -> None:
    args = parse_args()

    # Determine season
    season = args.season
    if season is None and args.month:
        inferred = month_to_season(args.month)
        if inferred is None:
            print("Invalid month. Please use 1-12.")
            return
        season = inferred

    # Interactive fallback if not provided
    if season is None:
        season = input("Enter season (spring/summer/autumn/winter): ").strip().lower()
    if season not in VALID_SEASONS:
        print("Unknown season. Please choose from spring/summer/autumn/winter.")
        return

    plant_type = args.plant_type
    if not plant_type:
        plant_type = input("Enter plant type (e.g., flower/vegetable/herb): ").strip().lower()

    advice = get_advice(season, plant_type)
    print(advice)

    if args.recommend:
        recs = recommend_plants(season)
        if recs:
            print(f"Suggested plants for {season}: " + ", ".join(recs))

if __name__ == "__main__":
    main()