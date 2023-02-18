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
football_ground_repository.save(ground_1)

league_1 = League("Scottish Premiership", "logo", ground_1)
league_repository.save(league_1)

country_1 = Country('Scotland', "flag", league_1)
country_repository.save(country_1)
# ground_2 = FootballGround('Celtic Park', 'Celtic F.C.', 'GHlasgow', 60411, False)
# ground_3 = FootballGround('Tannadice Park', 'Dundee United F.C.', 'Dundee', 14223, False)
# ground_4 = FootballGround('Tynecastle Park', 'Heart of Midlothian F.C.', 'Edinburgh', 19852, False)
# ground_5 = FootballGround('Easter Road', 'Hibernian F.C.', 'Edinburgh', 20421, False)
# ground_6 = FootballGround('Rugby Park', 'Kilmarnock F.C.', 'Kilmarnock', 17889, False)
# ground_7 = FootballGround('Almondvale Stadium', 'Livingston F.C.', 'Livingston', 8716, False)
# ground_8 = FootballGround('Fir Park', 'Motherwell F.C.', 'Motherwell', 13677, False)
# ground_9 = FootballGround('Ibrox Stadium', 'Rangers F.C.', 'Glasgow', 50817, False)
# ground_10 = FootballGround('Victoria Park', 'Ross County F.C.', 'Dingwall', 6541, False)
# ground_11 = FootballGround('McDiarmid Park', 'St Johnstone F.C.', 'Perth', 10696, False)
# ground_12 = FootballGround('St Mirren Park', 'St Mirren F.C.', 'Paisley', 8023, False)

# # Scottish Championship
# ground_13 = FootballGround('Gayfield Park', 'Arbroath F.C.', 'Arbroath', 6600, False)
# ground_14 = FootballGround('Somerset Park', 'Ayr United F.C.', 'Ayr', 10185, False)
# ground_15 = FootballGround('Balmoral Stadium', 'Cove Rangers F.C,', 'Aberdeen', 2602, False)
# ground_16 = FootballGround('Dens Park', 'Dundee F.C.', 'Dundee', 11775, False)
# ground_17 = FootballGround('Cappielow Park', 'Greenock Morton F.C.', 'Greenock', 11589, False)
# ground_18 = FootballGround('New Douglas Park', 'Hamilton Academical F.C.', 'Hamilton', 6018, False)
# ground_19 = FootballGround('Caledonian Stadium', 'Inverness Caledonian Thistle F.C.', 'Inverness', 7512, False)
# ground_20 = FootballGround('Firhill Stadium', 'Patrick Thistle', 'Glasgow', 10102, False)
# ground_21 = FootballGround('Ochilview Park', "Queens's Park F.C.", 'Glasgow', 3746, False)
# ground_22 = FootballGround("Starks' Park", 'Raith Rovers F.C.', 'Kirkcaldy', 8867, False)

# # English Premier League
# ground_23 = FootballGround('Anfield', 'Arbroath F.C.', 'Liverpool', 53394, False)
# ground_24 = FootballGround('Brentford Community Stadium', 'Brentford F.C.', 'London', 17250, False)
# ground_25 = FootballGround('Craven Cottage', 'Fulham F.C.,', 'London', 	25700, False)
# ground_26 = FootballGround('Elland Road', 'Leeds United F.C.', 'Leeds', 37792, False)
# ground_27 = FootballGround('Emirates Stadium', 'Arsenal F.C.', 'London', 60704, False)
# ground_28 = FootballGround('Etihad Stadium', 'Manchester City F.C.', 'Manchester', 53400, False)
# ground_29 = FootballGround('Falmer Stadium', 'Brighton & Hove Albion F.C.', 'Brighton and Hove', 31800, False)
# ground_30 = FootballGround('Goodison Park', "Everton F.C.", 'Liverpool', 39572, False)
# ground_31 = FootballGround("King Power Stadium", 'Leicester City F.C.', 'Leicester', 32261, False)
# ground_32 = FootballGround('London Stadium', 'West Ham United F.C.', 'London', 62500, False)
# ground_33 = FootballGround('Molineux Stadium', 'Wolverhampton Wanderers F.C.', 'Wolverhampton', 32050, False)
# ground_34 = FootballGround('Old Trafford', 'Manchester United F.C,', 'Manchester', 74310, False)
# ground_35 = FootballGround('Selhurst Park', 'Crystal Palace F.C.', 'London', 25486, False)
# ground_36 = FootballGround("St James' Park", 'Newcastle United F.C.', 'Newcastle', 52305, False)
# ground_37 = FootballGround("St Mary's Stadium", 'Southampton F.C.', 'Southampton', 32383, False)
# ground_38 = FootballGround('Stamford Bridge', 'Chelsea F.C.', 'London', 40341, False)
# ground_49 = FootballGround('City Ground', 'Nottingham Forest F.C.', 'Nottingham', 30445, False)
# ground_40 = FootballGround('Tottenham Hotspur Stadium', "Tottenham Hotspur F.C.", 'London', 62850, False)
# ground_41 = FootballGround("Villa Park", 'Aston Villa F.C.', 'Birmingham', 42749, False)
# ground_42 = FootballGround('Vitality Stadium', 'AFC Bournemouth', 'Bournemouth', 11364, False)


# country_1 = Country('England', 'Flag', ['Premier League', 'English Championship', 'League One', 'League Two'])
# country_2 = Country('Scotland', 'Flag', ['Scottish Premiership', 'Scottish Championship'])
# country_3 = Country('Switzerland', 'Flag', ['Credisuisse Super League', 'Dieci Vhallenge League'])


pdb.set_trace()
