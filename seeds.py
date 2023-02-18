import pdb
from models.country import Country
from models.league import League
from models.football_ground import FootballGround

import repositories.country_repository as country_repository
import repositories.league_repository as league_repository
import repositories.football_ground_repository as football_ground_repository

football_ground_repository.delete_all()
league_repository.delete_all()
country_repository.delete_all()

# Scottish Premiership
ground_1 = FootballGround('Pittodrie Stadium', 'Aberdeen F.C.', 'Aberdeen', 20866, False)
ground_2 = FootballGround('Celtic Park', 'Celtic F.C.', 'GHlasgow', 60411, False)
ground_3 = FootballGround('Tannadice Park', 'Dundee United F.C.', 'Dundee', 14223, False)
ground_4 = FootballGround('Tynecastle Park', 'Heart of Midlothian F.C.', 'Edinburgh', 19852, False)
ground_5 = FootballGround('Easter Road', 'Hibernian F.C.', 'Edinburgh', 20421, False)
ground_6 = FootballGround('Rugby Park', 'Kilmarnock F.C.', 'Kilmarnock', 17889, False)
ground_7 = FootballGround('Almondvale Stadium', 'Livingston F.C.', 'Livingston', 8716, False)
ground_8 = FootballGround('Fir Park', 'Motherwell F.C.', 'Motherwell', 13677, False)
ground_9 = FootballGround('Ibrox Stadium', 'Rangers F.C.', 'Glasgow', 50817, False)
ground_10 = FootballGround('Victoria Park', 'Ross County F.C.', 'Dingwall', 6541, False)
ground_11 = FootballGround('McDiarmid Park', 'St Johnstone F.C.', 'Perth', 10696, False)
ground_12 = FootballGround('St Mirren Park', 'St Mirren F.C.', 'Paisley', 8023, False)

# Scottish Championship


country_1 = Country('England', 'Flag', ['Premier League', 'English Championship', 'League One', 'League Two'])
country_2 = Country('Scotland', 'Flag', ['Scottish Premiership', 'Scottish Championship'])
country_3 = Country('Switzerland', 'Flag', ['Credisuisse Super League', 'Dieci Vhallenge League'])


pdb.set_trace()
