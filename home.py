from taipy.gui import Markdown
from taipy.gui import Gui
value1="Arsenal"
value2="Aston Villa"

index = """
<|text-center|
**Welcome to the English Premier League Visualization Tool**
>
<|layout|columns=auto auto|gap=20px|center|

<|{value1}|selector|lov=Arsenal;Aston Villa;Bournemouth;Brentford;Brighton;Burnley;Chelsea;Crystal Palace;Everton;Fulham;Liverpool;Luton Town;Manchester City;Manchester United;Newcastle;Nottingham;Sheffield United;Tottenham;West Ham;Wolves|dropdown|label=Team 1|>

<|{value2}|selector|lov=Arsenal;Aston Villa;Bournemouth;Brentford;Brighton;Burnley;Chelsea;Crystal Palace;Everton;Fulham;Liverpool;Luton Town;Manchester City;Manchester United;Newcastle;Nottingham;Sheffield United;Tottenham;West Ham;Wolves|dropdown|label=Team 2|>

|>
"""
home_md = Markdown("pages/home/home.md")