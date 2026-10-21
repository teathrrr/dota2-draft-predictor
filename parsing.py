import requests
import os
from dotenv import load_dotenv
import time
import pandas as pd
from IPython.display import display


load_dotenv()

token = os.getenv("API_STRATZ_KEY")
open_dota_key = os.getenv("API_OPENDOTA_KEY")
URL = "https://api.stratz.com/graphql"

headers = {
  "Authorization": f"Bearer {token}",
	"User-Agent": "STRATZ_API",
	"Content-Type": "application/json"
}

# def get_public_matches_id(lobby_type=None, retries=5):
#     params = {}
#     if lobby_type is not None:
#         params["lobby_type"] = lobby_type
#
#     for attempt in range(retries):
#         try:
#             r = requests.get(
#                 "https://api.opendota.com/api/publicMatches",
#                 params=params,
#                 timeout=15,
#             )
#             if r.status_code in (429, 500, 502, 503, 504, 520, 521, 522, 523, 524):
#                 raise requests.HTTPError(f"{r.status_code}", response=r)
#             r.raise_for_status()
#             return [m["match_id"] - 10000 for m in r.json()]
#         except (requests.HTTPError, requests.ConnectionError, requests.Timeout) as e:
#             wait = 2 ** attempt * 3  # 3, 6, 12, 24, 48 сек
#             print(f"Attempt {attempt + 1}/{retries} was unsuccessful: {e}. Wait {wait}с")
#             time.sleep(wait)
#     raise RuntimeError("OpenDota is unreachable")

# ranked = get_public_matches_id(7)
# unranked = get_public_matches_id(0)

# ids = ranked + unranked
ids = [9054376412, 9054375945, 9054375279, 9054372150, 9054368575, 9054367155, 9054365819, 9054362772, 9054362123, 9054361898, 9054360422, 9054359714, 9054358369, 9054357999, 9054357390, 9054357296, 9054356818, 9054356771, 9054356761, 9054356629, 9054356523, 9054356294, 9054356074, 9054356033, 9054355870, 9054355831, 9054355786, 9054355627, 9054355622, 9054355344, 9054355232, 9054354891, 9054354883, 9054354681, 9054354652, 9054354380, 9054354365, 9054354318, 9054354317, 9054354126, 9054353989, 9054353988, 9054353985, 9054353948, 9054353866, 9054353800, 9054353762, 9054353738, 9054353598, 9054353582, 9054353573, 9054353564, 9054353546, 9054353332, 9054353304, 9054353280, 9054353259, 9054353116, 9054353057, 9054353018, 9054352946, 9054352944, 9054352839, 9054352806, 9054352801, 9054352748, 9054352702, 9054352695, 9054352647, 9054352624, 9054352431, 9054352384, 9054352348, 9054352262, 9054352241, 9054352221, 9054352193, 9054352145, 9054352103, 9054352099, 9054352071, 9054352041, 9054352033, 9054352001, 9054351884, 9054351882, 9054351838, 9054351779, 9054351774, 9054351772, 9054351768, 9054351763, 9054351704, 9054351685, 9054351664, 9054351659, 9054351658, 9054351641, 9054351634, 9054351609, 9054378210, 9054376412, 9054375945, 9054375279, 9054372150, 9054368575, 9054367155, 9054365819, 9054362772, 9054362123, 9054361898, 9054360422, 9054359714, 9054358369, 9054357999, 9054357390, 9054357296, 9054356818, 9054356771, 9054356761, 9054356629, 9054356523, 9054356294, 9054356074, 9054356033, 9054355870, 9054355831, 9054355786, 9054355627, 9054355622, 9054355344, 9054355232, 9054354891, 9054354883, 9054354681, 9054354652, 9054354380, 9054354365, 9054354318, 9054354317, 9054354126, 9054353989, 9054353988, 9054353985, 9054353948, 9054353866, 9054353800, 9054353762, 9054353738, 9054353598, 9054353582, 9054353573, 9054353564, 9054353546, 9054353332, 9054353304, 9054353280, 9054353259, 9054353116, 9054353057, 9054353018, 9054352946, 9054352944, 9054352839, 9054352806, 9054352801, 9054352748, 9054352702, 9054352695, 9054352647, 9054352624, 9054352431, 9054352384, 9054352348, 9054352262, 9054352241, 9054352221, 9054352193, 9054352145, 9054352103, 9054352099, 9054352071, 9054352041, 9054352033, 9054352001, 9054351884, 9054351882, 9054351838, 9054351779, 9054351774, 9054351772, 9054351768, 9054351763, 9054351704, 9054351685, 9054351664, 9054351659, 9054351658, 9054351641, 9054351634]
ids_pag = [x - 220000 for x in ids]
print(ids_pag)
QUERY = """
query GetMatch($curr_id: Long!) {
  match(id: $curr_id) {
    id
    durationSeconds
    didRadiantWin
    players {
      heroId
      isRadiant
      isRandom
      steamAccountId
    }
  }
}
"""


def fetch_matches(curr_id):
	r = requests.post(
	URL,
	json={"query": QUERY, "variables": {"curr_id": curr_id}},
	headers=headers
	)

	r.raise_for_status()
	return r.json()["data"]["match"]

data = [{'id': 9054156412, 'durationSeconds': 2646, 'didRadiantWin': False, 'players': [{'heroId': 30, 'isRadiant': True, 'isRandom': False, 'steamAccountId': 797355128}, {'heroId': 7, 'isRadiant': True, 'isRandom': False, 'steamAccountId': 119951490}, {'heroId': 93, 'isRadiant': True, 'isRandom': False, 'steamAccountId': 191862235}, {'heroId': 43, 'isRadiant': True, 'isRandom': False, 'steamAccountId': 429133201}, {'heroId': 74, 'isRadiant': True, 'isRandom': False, 'steamAccountId': 165559210}, {'heroId': 71, 'isRadiant': False, 'isRandom': True, 'steamAccountId': 205400018}, {'heroId': 101, 'isRadiant': False, 'isRandom': False, 'steamAccountId': 1598599957}, {'heroId': 114, 'isRadiant': False, 'isRandom': False, 'steamAccountId': 742343064}, {'heroId': 26, 'isRadiant': False, 'isRandom': False, 'steamAccountId': 696411811}, {'heroId': 104, 'isRadiant': False, 'isRandom': False, 'steamAccountId': 1400866711}]}, {'id': 9054156412, 'durationSeconds': 2646, 'didRadiantWin': False, 'players': [{'heroId': 30, 'isRadiant': True, 'isRandom': False, 'steamAccountId': 797355128}, {'heroId': 7, 'isRadiant': True, 'isRandom': False, 'steamAccountId': 119951490}, {'heroId': 93, 'isRadiant': True, 'isRandom': False, 'steamAccountId': 191862235}, {'heroId': 43, 'isRadiant': True, 'isRandom': False, 'steamAccountId': 429133201}, {'heroId': 74, 'isRadiant': True, 'isRandom': False, 'steamAccountId': 165559210}, {'heroId': 71, 'isRadiant': False, 'isRandom': True, 'steamAccountId': 205400018}, {'heroId': 101, 'isRadiant': False, 'isRandom': False, 'steamAccountId': 1598599957}, {'heroId': 114, 'isRadiant': False, 'isRandom': False, 'steamAccountId': 742343064}, {'heroId': 26, 'isRadiant': False, 'isRandom': False, 'steamAccountId': 696411811}, {'heroId': 104, 'isRadiant': False, 'isRandom': False, 'steamAccountId': 1400866711}]}, {'id': 9054155279, 'durationSeconds': 2254, 'didRadiantWin': True, 'players': [{'heroId': 43, 'isRadiant': True, 'isRandom': False, 'steamAccountId': 26232395}, {'heroId': 14, 'isRadiant': True, 'isRandom': False, 'steamAccountId': 97496872}, {'heroId': 84, 'isRadiant': True, 'isRandom': False, 'steamAccountId': 126015671}, {'heroId': 88, 'isRadiant': True, 'isRandom': False, 'steamAccountId': 1109961373}, {'heroId': 8, 'isRadiant': True, 'isRandom': False, 'steamAccountId': 1095811129}, {'heroId': 7, 'isRadiant': False, 'isRandom': False, 'steamAccountId': 814709049}, {'heroId': 44, 'isRadiant': False, 'isRandom': False, 'steamAccountId': 45854226}, {'heroId': 74, 'isRadiant': False, 'isRandom': False, 'steamAccountId': 1079313116}, {'heroId': 94, 'isRadiant': False, 'isRandom': False, 'steamAccountId': 301781382}, {'heroId': 75, 'isRadiant': False, 'isRandom': False, 'steamAccountId': 238622775}]}]



# for i in range(0, 3):
# 		match_info = fetch_matches(ids_pag[i])
# 		if match_info != None:
# 			data.append(match_info)
# 		else:
# 			continue

df_players = pd.json_normalize(
    data,
    record_path=["players"],  # шлях до гравців напряму від кореня матчу
    meta=["id", "durationSeconds", "didRadiantWin"],  # поля матчу
    meta_prefix="match_",
)
cols = [
    "match_id",
    "match_durationSeconds",
    "match_didRadiantWin",
    "steamAccountId",
    "heroId",
    "isRadiant",
    "isRandom",
]
df_players = df_players[cols]

print(df_players.head())
print(df_players.columns)