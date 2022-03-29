
import streamlit as st

st.write("""
## NBA 2021 Season Exploratory Data Analysis. 

This will be a deep dive into the NBA's last year(2021) Teams and Players Performance Analysis using **Python**.

Data Source: https://www.basketball-reference.com/leagues/NBA_2021_per_game.html

Below actions will be performed accordingly to get clear answers to each question. Visualizations of the answers will be
shown at the end of the analysis.

EDA Performed:

    Stage 1: Data importing 

    Stage 2: Data Wrengling(Cleaning)

    Stage 3: Questions and Answers

    Stage Four Visualisations and Conclusions

Importing Libraries

    import pandas as pd

    import numpy as np

    import matplotlib.pyplot as plt

    import seaborn as sns

    %matplotlib inline

### Retrieve Dataset from the source( Using Pandas Web-scraping)
Data Source:

    url = 'https://www.basketball-reference.com/leagues/NBA_2021_per_game.html'

    html = pd.read_html(url, header = 0)

    df2019 = html[0]

#### Data cleaning

    raw = df2019.drop(df2019[df2019.Age == 'Age'].index)

    raw


        
    Rk	Player	Pos	Age	Tm	G	GS	MP	FG	FGA	...	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
    0	1	Precious Achiuwa	PF	21	MIA	61	4	12.1	2.0	3.7	...	.509	1.2	2.2	3.4	0.5	0.3	0.5	0.7	1.5	5.0
    1	2	Jaylen Adams	PG	24	MIL	7	0	2.6	0.1	1.1	...	NaN	0.0	0.4	0.4	0.3	0.0	0.0	0.0	0.1	0.3
    2	3	Steven Adams	C	27	NOP	58	58	27.7	3.3	5.3	...	.444	3.7	5.2	8.9	1.9	0.9	0.7	1.3	1.9	7.6
    3	4	Bam Adebayo	C	23	MIA	64	64	33.5	7.1	12.5	...	.799	2.2	6.7	9.0	5.4	1.2	1.0	2.6	2.3	18.7
    4	5	LaMarcus Aldridge	C	35	TOT	26	23	25.9	5.4	11.4	...	.872	0.7	3.8	4.5	1.9	0.4	1.1	1.0	1.8	13.5
    ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
    726	536	Delon Wright	PG	28	SAC	27	8	25.8	3.9	8.3	...	.833	1.0	2.9	3.9	3.6	1.6	0.4	1.3	1.1	10.0
    727	537	Thaddeus Young	PF	32	CHI	68	23	24.3	5.4	9.7	...	.628	2.5	3.8	6.2	4.3	1.1	0.6	2.0	2.2	12.1
    728	538	Trae Young	PG	22	ATL	63	63	33.7	7.7	17.7	...	.886	0.6	3.3	3.9	9.4	0.8	0.2	4.1	1.8	25.3
    729	539	Cody Zeller	C	28	CHO	48	21	20.9	3.8	6.8	...	.714	2.5	4.4	6.8	1.8	0.6	0.4	1.1	2.5	9.4
    730	540	Ivica Zubac	C	23	LAC	72	33	22.3	3.6	5.5	...	.789	2.6	4.6	7.2	1.3	0.3	0.9	1.1	2.6	9.0
    
    
    705 rows × 30 columns


##### Acronym Description


        Rk    Rank
        Pos    Position
        Age    Player's age on February 1 of the season
        Tm    Team
        G    Games
        GS    Games Started
        MP    Minutes Played Per Game
        FG    Field Goals Per Game
        FGA    Field Goal Attempts Per Game
        FG%    Field Goal Percentage
        3P    3-Point Field Goals Per Game
        3PA    3-Point Field Goal Attempts Per Game
        3P%    FG% on 3-Pt FGAs.
        2P    2-Point Field Goals Per Game
        2PA    2-Point Field Goal Attempts Per Game
        2P%    FG% on 2-Pt FGAs.
        eFG%    Effective Field Goal Percentage

        (Note: This statistic adjusts for the fact that a 3-point field goal is worth one more point than a 2-point field goal.)

        FT    Free Throws Per Game
        FTA    Free Throw Attempts Per Game
        FT%    Free Throw Percentage
        ORB    Offensive Rebounds Per Game
        DRB    Defensive Rebounds Per Game
        TRB    Total Rebounds Per Game
        AST    Assists Per Game
        STL    Steals Per Game
        BLK    Blocks Per Game
        TOV    Turnovers Per Game
        PF    Personal Fouls Per Game
        PTS    Points Per Game


##### Check the dataset shapes.


        raw.shape
        (705, 30)
        raw.isnull().sum()
        Rk         0
        Player     0
        Pos        0
        Age        0
        Tm         0
        G          0
        GS         0
        MP         0
        FG         0
        FGA        0
        FG%        2
        3P         0
        3PA        0
        3P%       35
        2P         0
        2PA        0
        2P%        6
        eFG%       2
        FT         0
        FTA        0
        FT%       29
        ORB        0
        DRB        0
        TRB        0
        AST        0
        STL        0
        BLK        0
        TOV        0
        PF         0
        PTS        0
        dtype: int64


##### Fill missing values with 0


        df = raw.fillna(0)
        df.isnull().sum()
        Rk        0
        Player    0
        Pos       0
        Age       0
        Tm        0
        G         0
        GS        0
        MP        0
        FG        0
        FGA       0
        FG%       0
        3P        0
        3PA       0
        3P%       0
        2P        0
        2PA       0
        2P%       0
        eFG%      0
        FT        0
        FTA       0
        FT%       0
        ORB       0
        DRB       0
        TRB       0
        AST       0
        STL       0
        BLK       0
        TOV       0
        PF        0
        PTS       0
        dtype: int64



##### Let's drop col that's not providing us any information. E.g Rk

        df.drop(['Rk'], axis =1)
            Player	            Pos	 Age	Tm	G	GS	MP	FG	FGA	FG%	...	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
        0	Precious Achiuwa    PF   21	MIA	61	4	12.1	2.0	3.7	.544	...	.509	1.2	2.2	3.4	0.5	0.3	0.5	0.7	1.5	5.0
        1	Jaylen Adams	    PG	 24	MIL	7	0	2.6	0.1	1.1	.125	...	0	0.0	0.4	0.4	0.3	0.0	0.0	0.0	0.1	0.3
        2	Steven Adams	    C	 27	NOP	58	58	27.7	3.3	5.3	.614	...	.444	3.7	5.2	8.9	1.9	0.9	0.7	1.3	1.9	7.6
        3	Bam Adebayo	    C	 23	MIA	64	64	33.5	7.1	12.5	.570	...	.799	2.2	6.7	9.0	5.4	1.2	1.0	2.6	2.3	18.7
        4	LaMarcus Aldridge   C	 35	TOT	26	23	25.9	5.4	11.4	.473	...	.872	0.7	3.8	4.5	1.9	0.4	1.1	1.0	1.8	13.5
        ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
        726	Delon Wright	    PG	28	SAC	27	8	25.8	3.9	8.3	.462	...	.833	1.0	2.9	3.9	3.6	1.6	0.4	1.3	1.1	10.0
        727	Thaddeus Young	    PF	32	CHI	68	23	24.3	5.4	9.7	.559	...	.628	2.5	3.8	6.2	4.3	1.1	0.6	2.0	2.2	12.1
        728	Trae Young	    PG	22	ATL	63	63	33.7	7.7	17.7	.438	...	.886	0.6	3.3	3.9	9.4	0.8	0.2	4.1	1.8	25.3
        729	Cody Zeller	    C	28	CHO	48	21	20.9	3.8	6.8	.559	...	.714	2.5	4.4	6.8	1.8	0.6	0.4	1.1	2.5	9.4
        730	Ivica Zubac	    C	23	LAC	72	33	22.3	3.6	5.5	.652	...	.789	2.6	4.6	7.2	1.3	0.3	0.9	1.1	2.6	9.0
        
        705 rows × 29 columns



Let's write the data to CSV Files


        df.to_csv('nba2021.csv', index = False)
        ls
        Volume in drive D has no label.
        Volume Serial Number is 8203-8CAF


Read and convert it back to DataFrame


        df = pd.read_csv('nba2021.csv')


Show all the datapoint in the dataset instead of the heads


        pd.set_option('display.max_rows', df.shape[0]+1)
        df.drop(['Rk'], axis = 1, inplace = True)
    
        df.head(20)

            Player	                Pos	Age	Tm	G	GS	MP	FG	FGA	FG%	...	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
        0	Precious Achiuwa        PF  21	MIA	61	4	12.1	2.0	3.7	0.544	...	0.509	1.2	2.2	3.4	0.5	0.3	0.5	0.7	1.5	5.0
        1	Jaylen Adams	        PG	24	MIL	7	0	2.6	0.1	1.1	0.125	...	0.000	0.0	0.4	0.4	0.3	0.0	0.0	0.0	0.1	0.3
        2	Steven Adams	        C	27	NOP	58	58	27.7	3.3	5.3	0.614	...	0.444	3.7	5.2	8.9	1.9	0.9	0.7	1.3	1.9	7.6
        3	Bam Adebayo	        C	23	MIA	64	64	33.5	7.1	12.5	0.570	...	0.799	2.2	6.7	9.0	5.4	1.2	1.0	2.6	2.3	18.7
        4	LaMarcus Aldridge       C	35	TOT	26	23	25.9	5.4	11.4	0.473	...	0.872	0.7	3.8	4.5	1.9	0.4	1.1	1.0	1.8	13.5
        5	LaMarcus Aldridge       C	35	SAS	21	18	25.9	5.5	11.8	0.464	...	0.838	0.8	3.7	4.5	1.7	0.4	0.9	1.0	1.7	13.7
        6	LaMarcus Aldridge       C	35	BRK	5	5	26.0	5.0	9.6	0.521	...	1.000	0.4	4.4	4.8	2.6	0.6	2.2	1.4	2.2	12.8
        7	Ty-Shon Alexander       SG	22	PHO	15	0	3.1	0.2	0.8	0.250	...	0.500	0.1	0.5	0.7	0.4	0.0	0.1	0.2	0.1	0.6
        8	Nickeil A. Walker       SG	22	NOP	46	13	21.9	4.2	10.0	0.419	...	0.727	0.3	2.8	3.1	2.2	1.0	0.5	1.5	1.9	11.0
        9	Grayson Allen	        SG	25	MEM	50	38	25.2	3.5	8.3	0.418	...	0.868	0.4	2.8	3.2	2.2	0.9	0.2	1.0	1.4	10.6
        10	Jarrett Allen	        C	22	TOT	63	45	29.6	4.7	7.7	0.618	...	0.703	3.1	6.9	10.0	1.7	0.5	1.4	1.6	1.5	12.8
        11	Jarrett Allen	        C	22	BRK	12	5	26.7	3.7	5.4	0.677	...	0.754	3.2	7.3	10.4	1.7	0.6	1.6	1.8	1.8	11.2
        12	Jarrett Allen	        C	22	CLE	51	40	30.3	5.0	8.2	0.609	...	0.690	3.1	6.8	9.9	1.7	0.5	1.4	1.5	1.5	13.2
        13	Al-Farouq Aminu	        PF	30	TOT	23	14	18.9	1.7	4.3	0.384	...	0.818	1.0	3.8	4.8	1.3	0.8	0.4	1.2	1.3	4.4
        14	Al-Farouq Aminu	        PF	30	ORL	17	14	21.6	2.1	5.2	0.404	...	0.824	1.2	4.2	5.4	1.7	1.0	0.5	1.5	1.3	5.5
        15	Al-Farouq Aminu	        PF	30	CHI	6	0	11.2	0.3	1.7	0.200	...	0.800	0.3	2.8	3.2	0.3	0.3	0.0	0.5	1.2	1.5
        16	Kyle Anderson	        PF	27	MEM	69	69	27.3	4.5	9.5	0.468	...	0.783	0.8	5.0	5.7	3.6	1.2	0.8	1.2	1.7	12.4
        17	Giannis Antetokounmpo   PF	26	MIL	61	61	33.0	10.3	18.0	0.569	...	0.685	1.6	9.4	11.0	5.9	1.2	1.2	3.4	2.8	28.1
        18	Kostas Antetokounmpo	PF	23	LAL	15	0	3.7	0.2	0.7	0.300	...	0.462	0.3	1.0	1.3	0.1	0.1	0.3	0.7	0.5	0.8
        19	Thanasis Antetokounmpo	SF	28	MIL	57	3	9.7	1.2	2.4	0.489	...	0.510	0.9	1.2	2.2	0.8	0.4	0.2	0.8	1.3	2.9
        
        20 rows × 29 columns



Overview of data types of each columns in the DataFrame


        df.dtypes
        Player     object
        Pos        object
        Age         int64
        Tm         object
        G           int64
        GS          int64
        MP        float64
        FG        float64
        FGA       float64
        FG%       float64
        3P        float64
        3PA       float64
        3P%       float64
        2P        float64
        2PA       float64
        2P%       float64
        eFG%      float64
        FT        float64
        FTA       float64
        FT%       float64
        ORB       float64
        DRB       float64
        TRB       float64
        AST       float64
        STL       float64
        BLK       float64
        TOV       float64
        PF        float64
        PTS       float64
        dtype: object



Show Specific data types in our DataFrame

        df.select_dtypes(include = ["number"]).head()
        Age	G	GS	MP	FG	FGA	FG%	3P	3PA	3P%	...	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
        0	21	61	4	12.1	2.0	3.7	0.544	0.0	0.0	0.000	...	0.509	1.2	2.2	3.4	0.5	0.3	0.5	0.7	1.5	5.0
        1	24	7	0	2.6	0.1	1.1	0.125	0.0	0.3	0.000	...	0.000	0.0	0.4	0.4	0.3	0.0	0.0	0.0	0.1	0.3
        2	27	58	58	27.7	3.3	5.3	0.614	0.0	0.1	0.000	...	0.444	3.7	5.2	8.9	1.9	0.9	0.7	1.3	1.9	7.6
        3	23	64	64	33.5	7.1	12.5	0.570	0.0	0.1	0.250	...	0.799	2.2	6.7	9.0	5.4	1.2	1.0	2.6	2.3	18.7
        4	35	26	23	25.9	5.4	11.4	0.473	1.2	3.1	0.388	...	0.872	0.7	3.8	4.5	1.9	0.4	1.1	1.0	1.8	13.5
        5 rows × 26 columns

        df.select_dtypes(include = ["object"]).head()
        Player	Pos	Tm
        0	Precious Achiuwa	PF	MIA
        1	Jaylen Adams	PG	MIL
        2	Steven Adams	C	NOP
        3	Bam Adebayo	C	MIA
        4	LaMarcus Aldridge	C	TOT



##### Conditional Selections


Which player scored the most points(PTS) Per Game?


        df[df.PTS == df.PTS.max()] # **This will return the entire raw**

        Player	        Pos	Age	Tm	G	GS	MP	FG	FGA	FG%	...	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
        151	Stephen Curry	PG	32	GSW	63	63	34.2	10.4	21.7	0.482	...	0.916	0.5	5.0	5.5	5.8	1.2	0.1	3.4	1.9	32.0
        1 rows × 29 columns

        TopScorer = df[df.PTS == df.PTS.max()]
        TopScorer.Player
        151    Stephen Curry
        Name: Player, dtype: object
        What is the highest point scored?
        df.PTS.max()
        32.0

Which Team does this player plays for ?


        TopScorer.Tm
        151    GSW
        Name: Tm, dtype: object
        Which posiiton does this player play?
        TopScorer.Pos
        151    PG
        Name: Pos, dtype: object
How many games did the player play in 2021 season?


        TopScorer.G
        151    63
        Name: G, dtype: int64





Which players scored more than 20 Point(PTS) Per Game?


        df[df.PTS > 20]

            Player	                Pos	Age	Tm	G	GS	MP	FG	FGA	FG%	...	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
        17	Giannis Antetokounmpo	PF	26	MIL	61	61	33.0	10.3	18.0	0.569	...	0.685	1.6	9.4	11.0	5.9	1.2	1.2	3.4	2.8	28.1
        45	Bradley Beal            SG	27	WAS	60	60	35.8	11.2	23.0	0.485	...	0.889	1.2	3.5	4.7	4.4	1.2	0.4	3.1	2.3	31.3
        71	Devin Booker	        SG	24	PHO	67	67	33.9	9.3	19.2	0.484	...	0.867	0.5	3.7	4.2	4.3	0.8	0.2	3.1	2.7	25.6
        89	Malcolm Brogdon	        PG	28	IND	56	56	34.5	7.9	17.5	0.453	...	0.864	1.0	4.2	5.3	5.9	0.9	0.3	2.1	2.0	21.2
        94	Jaylen Brown	        SG	24	BOS	58	58	34.5	9.3	19.2	0.484	...	0.764	1.2	4.8	6.0	3.4	1.2	0.6	2.7	2.9	24.7
        106	Jimmy Butler	        SF	31	MIA	52	52	33.6	7.0	14.2	0.497	...	0.863	1.8	5.1	6.9	7.1	2.1	0.3	2.1	1.4	21.5
        151	Stephen Curry	        PG	32	GSW	63	63	34.2	10.4	21.7	0.482	...	0.916	0.5	5.0	5.5	5.8	1.2	0.1	3.4	1.9	32.0
        153	Anthony Davis	        PF	27	LAL	36	36	32.3	8.4	17.0	0.491	...	0.738	1.7	6.2	7.9	3.1	1.3	1.6	2.1	1.7	21.8
        161	DeMar DeRozan	        PF	31	SAS	61	61	33.7	7.5	15.1	0.495	...	0.880	0.7	3.6	4.2	6.9	0.9	0.2	2.0	2.1	21.6
        171	Luka Dončić	        PG      21	DAL	66	66	34.3	9.8	20.5	0.479	...	0.730	0.8	7.2	8.0	8.6	1.0	0.5	4.3	2.3	27.7
        183	Kevin Durant	        PF	32	BRK	35	32	33.1	9.3	17.2	0.537	...	0.882	0.4	6.7	7.1	5.6	0.7	1.3	3.4	2.0	26.9
        189	Joel Embiid	        C	26	PHI	51	51	31.1	9.0	17.6	0.513	...	0.859	2.2	8.4	10.6	2.8	1.0	1.4	3.1	2.4	28.5
        209	De'Aaron Fox	        PG	23	SAC	58	58	35.1	9.1	19.1	0.477	...	0.719	0.6	2.9	3.5	7.2	1.5	0.5	3.0	2.9	25.2
        223	Paul George	        SF	30	LAC	54	54	33.7	8.2	17.6	0.467	...	0.868	0.8	5.8	6.6	5.2	1.1	0.4	3.3	2.4	23.3
        226	Shai Gilgeous-Alexander	SG	22	OKC	35	35	33.7	8.2	16.1	0.508	...	0.808	0.5	4.2	4.7	5.9	0.8	0.7	3.0	2.0	23.7
        236	Jerami Grant	        SF	26	DET	54	54	33.9	7.4	17.3	0.429	...	0.845	0.6	4.0	4.6	2.8	0.6	1.1	2.0	2.3	22.3
        258	James Harden	        PG-SG	31	TOT	44	43	36.6	7.8	16.7	0.466	...	0.861	0.8	7.1	7.9	10.8	1.2	0.8	4.0	2.3	24.6
        259	James Harden	        SG	31	HOU	8	8	36.3	7.5	16.9	0.444	...	0.883	0.6	4.5	5.1	10.4	0.9	0.8	4.3	1.8	24.8
        260	James Harden	        PG	31	BRK	36	35	36.6	7.8	16.6	0.471	...	0.856	0.8	7.7	8.5	10.9	1.3	0.8	4.0	2.4	24.6
        316	Brandon Ingram	        SF	23	NOP	61	61	34.3	8.4	18.0	0.466	...	0.878	0.6	4.3	4.9	4.9	0.7	0.6	2.5	2.0	23.8
        317	Kyrie Irving	        PG	28	BRK	54	54	34.9	10.2	20.1	0.506	...	0.922	1.0	3.8	4.8	6.0	1.4	0.7	2.4	2.6	26.9
        329	LeBron James	        PG	36	LAL	45	45	33.4	9.4	18.3	0.513	...	0.698	0.6	7.0	7.7	7.8	1.1	0.6	3.7	1.6	25.0
        344	Nikola Jokić	        C	25	DEN	72	72	34.6	10.2	18.0	0.566	...	0.868	2.8	8.0	10.8	8.3	1.3	0.7	3.1	2.7	26.4
        381	Zach LaVine	        SG	25	CHI	58	58	35.1	9.8	19.4	0.507	...	0.849	0.6	4.4	5.0	4.9	0.8	0.5	3.5	2.4	27.4
        390	Kawhi Leonard	        SF	29	LAC	52	52	34.1	8.9	17.5	0.512	...	0.885	1.1	5.4	6.5	5.2	1.6	0.4	2.0	1.6	24.8
        392	Caris LeVert	        SG	26	TOT	47	39	31.6	7.6	17.3	0.441	...	0.811	0.7	3.9	4.6	5.2	1.4	0.6	2.2	2.2	20.2
        394	Caris LeVert	        SG	26	IND	35	35	32.9	7.8	17.5	0.443	...	0.822	0.7	4.0	4.6	4.9	1.5	0.7	2.2	2.4	20.7
        396	Damian Lillard	        PG	30	POR	67	67	35.8	9.0	19.9	0.451	...	0.928	0.5	3.7	4.2	7.5	0.9	0.3	3.0	1.5	28.8
        427	CJ McCollum	        SG	29	POR	47	47	34.0	8.6	18.8	0.458	...	0.812	0.6	3.3	3.9	4.7	0.9	0.4	1.4	1.9	23.1
        448	Khris Middleton	        SF	29	MIL	68	68	33.4	7.5	15.8	0.476	...	0.898	0.8	5.2	6.0	5.4	1.1	0.1	2.6	2.4	20.4
        453	Donovan Mitchell	PG	24	UTA	53	53	33.4	9.0	20.6	0.438	...	0.845	0.9	3.5	4.4	5.2	1.0	0.3	2.8	2.2	26.4
        464	Jamal Murray	        PG	23	DEN	48	48	35.5	7.9	16.5	0.477	...	0.869	0.8	3.3	4.0	4.8	1.3	0.3	2.3	2.0	21.2
        493	Victor Oladipo	        SG	28	HOU	20	20	33.5	7.8	19.1	0.407	...	0.783	0.4	4.4	4.8	5.0	1.2	0.5	2.6	2.3	21.2
        532	Kristaps Porziņģis	C	25	DAL	43	43	30.9	7.6	15.9	0.476	...	0.855	1.9	7.0	8.9	1.6	0.5	1.3	1.2	2.7	20.1
        544	Julius Randle	        PF	26	NYK	71	71	37.6	8.5	18.6	0.456	...	0.811	1.2	9.0	10.2	6.0	0.9	0.3	3.4	3.2	24.1
        574	Terry Rozier	        SG	26	CHO	69	69	34.5	7.4	16.4	0.450	...	0.817	0.7	3.7	4.4	4.2	1.3	0.4	1.9	1.7	20.4
        577	Domantas Sabonis	PF	24	IND	62	62	36.0	7.8	14.6	0.535	...	0.732	2.4	9.5	12.0	6.7	1.2	0.5	3.4	3.3	20.3
        585	Collin Sexton	        SG	22	CLE	60	60	35.3	8.8	18.4	0.475	...	0.815	1.0	2.2	3.1	4.4	1.0	0.2	2.8	2.6	24.3
        588	Pascal Siakam	        PF	26	TOR	56	56	35.8	7.8	17.2	0.455	...	0.827	1.7	5.5	7.2	4.5	1.1	0.7	2.3	3.1	21.4
        610	Jayson Tatum	        SF	22	BOS	64	64	35.8	9.5	20.6	0.459	...	0.868	0.8	6.6	7.4	4.3	1.2	0.5	2.7	1.9	26.4
        638	Karl-Anthony Towns	C	25	MIN	50	50	33.8	8.5	17.5	0.486	...	0.859	2.7	7.9	10.6	4.5	0.8	1.1	3.2	3.7	24.8
        655	Nikola Vučević	        C	30	TOT	70	70	33.5	9.5	19.9	0.477	...	0.840	2.1	9.6	11.7	3.8	0.9	0.7	1.8	2.0	23.4
        656	Nikola Vučević	        C	30	ORL	44	44	34.1	9.9	20.6	0.480	...	0.827	2.0	9.8	11.8	3.8	1.0	0.6	1.9	1.8	24.5
        657	Nikola Vučević	        C	30	CHI	26	26	32.6	8.8	18.8	0.471	...	0.870	2.3	9.3	11.5	3.9	0.9	0.8	1.7	2.2	21.5
        665	John Wall	        PG	30	HOU	40	40	32.2	7.3	18.2	0.404	...	0.749	0.4	2.8	3.2	6.9	1.1	0.8	3.5	1.2	20.6
        675	Russell Westbrook	PG	32	WAS	65	65	36.4	8.4	19.0	0.439	...	0.656	1.7	9.9	11.5	11.7	1.4	0.4	4.8	2.9	22.2
        688	Zion Williamson	        PF	20	NOP	61	61	33.2	10.4	17.0	0.611	...	0.698	2.7	4.5	7.2	3.7	0.9	0.6	2.7	2.2	27.0
        696	Christian Wood	        C	25	HOU	41	41	32.3	8.0	15.6	0.514	...	0.631	1.9	7.8	9.6	1.7	0.8	1.2	2.0	2.1	21.0
        702	Trae Young	        PG	22	ATL	63	63	33.7	7.7	17.7	0.438	...	0.886	0.6	3.3	3.9	9.4	0.8	0.2	4.1	1.8	25.3
       
       49 rows × 29 columns



Which player had the highest 3-Point Field Goals Per Game(3P)?


        Highest3P = df[df['3P'] == df['3P'].max()]

        Highest3P

        Player	        Pos	Age	Tm	G	GS	MP	FG	FGA	FG%	...	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
        151	Stephen Curry	PG	32	GSW	63	63	34.2	10.4	21.7	0.482	...	0.916	0.5	5.0	5.5	5.8	1.2	0.1	3.4	1.9	32.0
        1 rows × 29 columns

        Highest3P["3P"]
        151    5.3
        Name: 3P, dtype: float64


Which Player has the highest assist Per Game(AST)?


        HighestAssist = df[df["AST"] == df['AST'].max()]

        HighestAssist

        Player	        Pos	Age	Tm	G	GS	MP	FG	FGA	FG%	...	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
        Russell Westbrook	PG	32	WAS	65	65	36.4	8.4	19.0	0.439	...	0.656	1.7	9.9	11.5	11.7	1.4	0.4	4.8	2.9	22.2
        1 rows × 29 columns

        HighestAssist["AST"]
        675    11.7
        Name: AST, dtype: float64


#### As a Lakers fan myself, let's get some information about the teams performance.


## Use GroupBy functions for Aggregations



Which player scored the highest(PTS) in the Los Angeles Lakers? Let's get everyone who plays for LA first


        LAL= df.groupby('Tm').get_group('LAL')
        LAL
            Player	                    Pos	Age	Tm	G	GS	MP	FG	FGA	FG%	...	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
        18	Kostas Antetokounmpo	    PF	23	LAL	15	0	3.7	0.2	0.7	0.300	...	0.462	0.3	1.0	1.3	0.1	0.1	0.3	0.7	0.5	0.8
        108	Devontae Cacok	            PF	24	LAL	20	1	4.9	0.9	1.5	0.586	...	0.455	0.6	1.0	1.6	0.1	0.3	0.2	0.3	0.4	2.0
        109	Kentavious Caldwell-Pope    SG	27	LAL	67	67	28.4	3.3	7.6	0.431	...	0.866	0.4	2.3	2.7	1.9	0.9	0.4	1.0	1.7	9.7
        120	Alex Caruso	            PG	26	LAL	58	6	21.0	2.3	5.3	0.436	...	0.645	0.5	2.4	2.9	2.8	1.1	0.3	1.3	1.9	6.4
        136	Quinn Cook	            PG	27	LAL	16	0	3.9	0.8	1.6	0.462	...	0.800	0.0	0.3	0.3	0.3	0.1	0.1	0.2	0.1	2.1
        153	Anthony Davis	            PF	27	LAL	36	36	32.3	8.4	17.0	0.491	...	0.738	1.7	6.2	7.9	3.1	1.3	1.6	2.1	1.7	21.8
        180	Andre Drummond	            C	27	LAL	21	21	24.8	4.9	9.1	0.531	...	0.605	3.1	7.1	10.2	1.4	1.1	1.0	2.0	3.8	11.9
        181	Jared Dudley	            PF	35	LAL	12	0	6.8	0.2	0.8	0.222	...	0.000	0.3	1.4	1.8	0.4	0.1	0.1	0.2	0.6	0.5
        221	Marc Gasol	            C	36	LAL	52	42	19.1	1.7	3.7	0.454	...	0.720	0.7	3.4	4.1	2.1	0.5	1.1	1.0	2.2	5.0
        265	Montrezl Harrell	    C	27	LAL	69	1	22.9	5.4	8.7	0.622	...	0.707	2.3	3.9	6.2	1.1	0.7	0.7	1.1	1.9	13.5
        302	Talen Horton-Tucker	    SG	20	LAL	65	4	20.1	3.4	7.5	0.458	...	0.775	0.4	2.2	2.6	2.8	1.0	0.3	1.6	2.0	9.0
        329	LeBron James	            PG	36	LAL	45	45	33.4	9.4	18.3	0.513	...	0.698	0.6	7.0	7.7	7.8	1.1	0.6	3.7	1.6	25.0
        347	Damian Jones	            C	25	LAL	8	6	14.0	2.0	2.1	0.941	...	0.917	1.0	2.3	3.3	0.1	0.1	0.9	0.6	2.8	5.4
        377	Kyle Kuzma	            SF	25	LAL	68	32	28.7	4.9	11.1	0.443	...	0.691	1.6	4.5	6.1	1.9	0.5	0.6	1.7	1.8	12.9
        423	Wesley Matthews	            SG	34	LAL	58	10	19.5	1.5	4.3	0.353	...	0.854	0.3	1.3	1.6	0.9	0.7	0.3	0.4	1.4	4.8
        437	Alfonzo McKinnie	    SF	28	LAL	39	0	6.6	1.2	2.4	0.516	...	0.556	0.6	0.8	1.4	0.2	0.2	0.0	0.1	0.7	3.1
        441	Ben McLemore	            SG	27	LAL	21	1	17.5	2.6	6.7	0.390	...	0.762	0.2	1.4	1.6	0.5	0.1	0.3	0.7	1.8	8.0
        460	Markieff Morris	            PF	31	LAL	61	27	19.7	2.5	6.2	0.405	...	0.720	0.8	3.6	4.4	1.2	0.4	0.3	0.9	1.7	6.7
        582	Dennis Schröder	            SG	27	LAL	61	61	32.1	5.4	12.5	0.437	...	0.848	0.5	3.0	3.5	5.8	1.1	0.2	2.7	2.6	15.4
        
        19 rows × 29 columns



        LAL[LAL.PTS == LAL.PTS.max()]
        Player	        Pos	Age	Tm	G	GS	MP	FG	FGA	FG%	...	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
        329	LeBron James	PG	36	LAL	45	45	33.4	9.4	18.3	0.513	...	0.698	0.6	7.0	7.7	7.8	1.1	0.6	3.7	1.6	25.0
        
        
        1 rows × 29 columns

        King James still killing it at the age of 36

Of the 5 positons, which position has the highest points? First we need to group the team by position


        df.groupby('Pos').PTS.describe()
        count	mean	std	min	25%	50%	75%	max
        Pos								
        C	138.0	8.451449	5.648205	0.0	4.775	7.55	11.200	28.5
        C-PF	2.0	8.450000	7.141778	3.4	5.925	8.45	10.975	13.5
        PF	143.0	7.484615	5.924184	0.0	3.150	6.00	10.050	28.1
        PF-C	1.0	7.000000	NaN	7.0	7.000	7.00	7.000	7.0
        PF-SF	1.0	5.200000	NaN	5.2	5.200	5.20	5.200	5.2
        PG	127.0	9.625984	7.062737	0.0	4.450	7.50	13.250	32.0
        PG-SG	1.0	24.600000	NaN	24.6	24.600	24.60	24.600	24.6
        SF	119.0	7.811765	6.013081	0.0	3.900	6.10	10.900	26.4
        SF-PF	4.0	4.800000	3.549648	1.5	2.700	4.00	6.100	9.7
        SF-SG	3.0	9.733333	6.833984	3.6	6.050	8.50	12.800	17.1
        SG	162.0	9.485185	6.427515	0.1	4.400	8.25	12.425	31.3
        SG-PG	2.0	8.550000	2.333452	6.9	7.725	8.55	9.375	10.2
        SG-SF	2.0	15.100000	4.949747	11.6	13.350	15.10	16.850	18.6



Let's focus ONLY on the 5 main positions within the game.i.e: [C, PF, PG, SF, SG]


        positions = ['C','PF', 'SF', 'PG', 'SG']

        POS = df[df["Pos"].isin(positions)]
        POS.head(10)
        Player	Pos	Age	Tm	G	GS	MP	FG	FGA	FG%	...	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
        0	Precious Achiuwa	PF	21	MIA	61	4	12.1	2.0	3.7	0.544	...	0.509	1.2	2.2	3.4	0.5	0.3	0.5	0.7	1.5	5.0
        1	Jaylen Adams	PG	24	MIL	7	0	2.6	0.1	1.1	0.125	...	0.000	0.0	0.4	0.4	0.3	0.0	0.0	0.0	0.1	0.3
        2	Steven Adams	C	27	NOP	58	58	27.7	3.3	5.3	0.614	...	0.444	3.7	5.2	8.9	1.9	0.9	0.7	1.3	1.9	7.6
        3	Bam Adebayo	C	23	MIA	64	64	33.5	7.1	12.5	0.570	...	0.799	2.2	6.7	9.0	5.4	1.2	1.0	2.6	2.3	18.7
        4	LaMarcus Aldridge	C	35	TOT	26	23	25.9	5.4	11.4	0.473	...	0.872	0.7	3.8	4.5	1.9	0.4	1.1	1.0	1.8	13.5
        5	LaMarcus Aldridge	C	35	SAS	21	18	25.9	5.5	11.8	0.464	...	0.838	0.8	3.7	4.5	1.7	0.4	0.9	1.0	1.7	13.7
        6	LaMarcus Aldridge	C	35	BRK	5	5	26.0	5.0	9.6	0.521	...	1.000	0.4	4.4	4.8	2.6	0.6	2.2	1.4	2.2	12.8
        7	Ty-Shon Alexander	SG	22	PHO	15	0	3.1	0.2	0.8	0.250	...	0.500	0.1	0.5	0.7	0.4	0.0	0.1	0.2	0.1	0.6
        8	Nickeil Alexander-Walker	SG	22	NOP	46	13	21.9	4.2	10.0	0.419	...	0.727	0.3	2.8	3.1	2.2	1.0	0.5	1.5	1.9	11.0
        9	Grayson Allen	SG	25	MEM	50	38	25.2	3.5	8.3	0.418	...	0.868	0.4	2.8	3.2	2.2	0.9	0.2	1.0	1.4	10.6
        
        10 rows × 29 columns

Check the Statistical Analysis of the positions


        POS.describe()
        Age	G	GS	MP	FG	FGA	FG%	3P	3PA	3P%	...	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
        count	689.000000	689.000000	689.000000	689.000000	689.000000	689.000000	689.000000	689.000000	689.000000	689.000000	...	689.000000	689.000000	689.000000	689.000000	689.000000	689.000000	689.000000	689.000000	689.000000	689.000000
        mean	25.882438	37.162554	16.873730	19.405080	3.161974	6.939623	0.441646	0.957039	2.706096	0.298329	...	0.720582	0.807112	2.769811	3.576052	1.927141	0.609144	0.415385	1.071118	1.622932	8.599855
        std	4.114191	21.353877	21.626588	9.172654	2.284205	4.728152	0.115204	0.876244	2.225191	0.143486	...	0.208871	0.735416	1.822634	2.396453	1.795109	0.392799	0.410114	0.810931	0.762700	6.272961
        min	19.000000	1.000000	0.000000	1.800000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	...	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000
        25%	23.000000	18.000000	0.000000	12.500000	1.400000	3.500000	0.395000	0.200000	0.900000	0.250000	...	0.667000	0.300000	1.500000	1.900000	0.700000	0.300000	0.100000	0.500000	1.100000	4.000000
        50%	25.000000	37.000000	5.000000	19.200000	2.600000	5.900000	0.439000	0.700000	2.200000	0.333000	...	0.769000	0.600000	2.500000	3.100000	1.400000	0.600000	0.300000	0.900000	1.600000	7.200000
        75%	28.000000	57.000000	29.000000	26.900000	4.300000	9.300000	0.496000	1.500000	4.100000	0.386000	...	0.843000	1.000000	3.700000	4.800000	2.500000	0.900000	0.600000	1.400000	2.100000	11.700000
        max	40.000000	72.000000	72.000000	37.600000	11.200000	23.000000	1.000000	5.300000	12.700000	1.000000	...	1.000000	4.700000	10.100000	14.300000	11.700000	2.100000	3.400000	5.000000	4.000000	32.000000
        
        8 rows × 26 columns


        POS.groupby("Pos").PTS.describe()
        ​
        count	mean	std	min	25%	50%	75%	max
        Pos								
        C	138.0	8.451449	5.648205	0.0	4.775	7.55	11.200	28.5
        PF	143.0	7.484615	5.924184	0.0	3.150	6.00	10.050	28.1
        PG	127.0	9.625984	7.062737	0.0	4.450	7.50	13.250	32.0
        SF	119.0	7.811765	6.013081	0.0	3.900	6.10	10.900	26.4
        SG	162.0	9.485185	6.427515	0.1	4.400	8.25	12.425	31.3



## Data Visualisations
Create a subset of the dataset for position and points

        PTS = df[['Pos', 'PTS']]

        positions = ['C','PF', 'SF', 'PG', 'SG']
        PTS = PTS[PTS['Pos'].isin(positions)]
        PTS = df[['Pos', 'PTS']]
        positions = ['C','PF', 'SF', 'PG', 'SG']
        PTS = PTS[PTS['Pos'].isin(positions)]
        PTS.head(10)


        Pos	PTS
        0	PF	5.0
        1	PG	0.3
        2	C	7.6
        3	C	18.7
        4	C	13.5
        5	C	13.7
        6	C	12.8
        7	SG	0.6
        8	SG	11.0
        9	SG	10.6



""")

from PIL import Image

image = Image.open("D:\Data Science\Streamlit\PTS_hist.png")

st.image(image, caption='Points Distribution Fig1')


st.write("""


### Let's use Seaborn for visualisations to get a better understanding of the distribution.


        g = sns.FacetGrid(PTS, col = "Pos")
        g.map(plt.hist, 'PTS')


""")


image = Image.open("D:\Data Science\Streamlit\sns_hist_PTS.png")

st.image(image, caption='Points Distribution Fig2')


st.write("""

Boxplot distribution.


        sns.boxplot(x = 'Pos', y = "PTS", data = PTS)
        

""")


image = Image.open("D:\Data Science\Streamlit\snsboxplot.png")

st.image(image, caption='Points Distribution Fig3')




st.write("""

Violinplot distribution, showing the median point around the middle of the individual plot.


    plt.figure(figsize = (20,6))
    sns.violinplot(x = "Pos", y  = 'PTS', data = PTS).set_title("Average Points Per Position")
        

""")


image = Image.open("D:\Data Science\Streamlit\PltViolinPlot.png")

st.image(image, caption='Points Distribution Fig4')



st.write("""

### Compute the correlation matrix


    corr = df.corr()
    corr

        Age	G	GS	MP	FG	FGA	FG%	3P	3PA	3P%	...	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
        Age	1.000000	0.061119	0.092335	0.198153	0.127956	0.132420	0.048242	0.185962	0.163591	0.113262	...	0.129573	0.017896	0.139539	0.111839	0.226687	0.178456	0.042726	0.121069	0.111609	0.138877
        G	0.061119	1.000000	0.644453	0.553135	0.472687	0.441459	0.296131	0.397096	0.362864	0.297257	...	0.322548	0.264688	0.404790	0.389992	0.337747	0.409568	0.181272	0.325467	0.392205	0.465707
        GS	0.092335	0.644453	1.000000	0.764826	0.716464	0.692610	0.221514	0.511321	0.499250	0.187241	...	0.209549	0.370520	0.629791	0.593427	0.550817	0.553341	0.322566	0.591306	0.536160	0.713721
        MP	0.198153	0.553135	0.764826	1.000000	0.879032	0.888528	0.256452	0.693692	0.707618	0.326397	...	0.373425	0.381314	0.730310	0.672641	0.712777	0.753880	0.358051	0.736907	0.705754	0.879928
        FG	0.127956	0.472687	0.716464	0.879032	1.000000	0.975263	0.325081	0.669591	0.669400	0.287325	...	0.321964	0.381583	0.724941	0.668630	0.720105	0.652066	0.340571	0.794838	0.595233	0.990473
        FGA	0.132420	0.441459	0.692610	0.888528	0.975263	1.000000	0.176683	0.752209	0.771808	0.318068	...	0.340317	0.260060	0.664572	0.585309	0.749028	0.669474	0.248033	0.802002	0.563711	0.980010
        FG%	0.048242	0.296131	0.221514	0.256452	0.325081	0.176683	1.000000	-0.020309	-0.082341	0.110932	...	0.194170	0.473793	0.358801	0.418678	0.088282	0.177922	0.409630	0.144745	0.337232	0.278695
        3P	0.185962	0.397096	0.511321	0.693692	0.669591	0.752209	-0.020309	1.000000	0.980135	0.524588	...	0.368599	-0.148875	0.323751	0.200154	0.537287	0.486753	-0.034478	0.496285	0.322891	0.722054
        3PA	0.163591	0.362864	0.499250	0.707618	0.669400	0.771808	-0.082341	0.980135	1.000000	0.465541	...	0.350303	-0.156481	0.325056	0.198842	0.557703	0.504022	-0.041055	0.523658	0.339857	0.722231
        3P%	0.113262	0.297257	0.187241	0.326397	0.287325	0.318068	0.110932	0.524588	0.465541	1.000000	...	0.383266	-0.224666	0.089386	-0.000108	0.262648	0.242138	-0.139143	0.176498	0.133237	0.316505
        2P	0.070949	0.401648	0.653470	0.769645	0.933244	0.862208	0.419067	0.358749	0.367517	0.107890	...	0.227005	0.552793	0.754891	0.744167	0.645619	0.584415	0.444966	0.759409	0.592356	0.896008
        2PA	0.077894	0.384411	0.650047	0.788827	0.937820	0.904251	0.306162	0.411825	0.426558	0.139913	...	0.248304	0.474781	0.727080	0.699021	0.691339	0.614086	0.379666	0.789380	0.573173	0.909036
        2P%	0.019806	0.242098	0.157889	0.193779	0.237970	0.126668	0.774217	0.008834	0.002067	0.018321	...	0.147622	0.326440	0.251005	0.291192	0.044055	0.144843	0.303036	0.077035	0.238720	0.203016
        eFG%	0.108222	0.366533	0.245227	0.318182	0.337457	0.222338	0.926427	0.218137	0.142157	0.364564	...	0.296706	0.308510	0.310871	0.331625	0.113618	0.212852	0.294793	0.124823	0.320473	0.313878
        FT	0.098473	0.320948	0.592177	0.702883	0.830390	0.810456	0.219726	0.465952	0.481060	0.163632	...	0.328839	0.309810	0.606327	0.556012	0.694766	0.526865	0.296154	0.778064	0.483732	0.873784
        FTA	0.072032	0.322603	0.599448	0.702107	0.826646	0.795698	0.252544	0.406686	0.424383	0.116348	...	0.256577	0.393902	0.653946	0.618099	0.673893	0.524686	0.355594	0.786718	0.516428	0.859302
        FT%	0.129573	0.322548	0.209549	0.373425	0.321964	0.340317	0.194170	0.368599	0.350303	0.383266	...	1.000000	-0.013339	0.191129	0.141269	0.291015	0.315748	0.001805	0.212927	0.225081	0.353171
        ORB	0.017896	0.264688	0.370520	0.381314	0.381583	0.260060	0.473793	-0.148875	-0.156481	-0.224666	...	-0.013339	1.000000	0.697640	0.837246	0.091721	0.234928	0.653452	0.288535	0.530736	0.320283
        DRB	0.139539	0.404790	0.629791	0.730310	0.724941	0.664572	0.358801	0.323751	0.325056	0.089386	...	0.191129	0.697640	1.000000	0.975624	0.488853	0.502869	0.575798	0.622156	0.666796	0.696320
        TRB	0.111839	0.389992	0.593427	0.672641	0.668630	0.585309	0.418678	0.200154	0.198842	-0.000108	...	0.141269	0.837246	0.975624	1.000000	0.399794	0.454899	0.639057	0.561929	0.669975	0.627926
        AST	0.226687	0.337747	0.550817	0.712777	0.720105	0.749028	0.088282	0.537287	0.557703	0.262648	...	0.291015	0.091721	0.488853	0.399794	1.000000	0.680935	0.087960	0.822754	0.399748	0.740902
        STL	0.178456	0.409568	0.553341	0.753880	0.652066	0.669474	0.177922	0.486753	0.504022	0.242138	...	0.315748	0.234928	0.502869	0.454899	0.680935	1.000000	0.238287	0.603082	0.531279	0.649888
        BLK	0.042726	0.181272	0.322566	0.358051	0.340571	0.248033	0.409630	-0.034478	-0.041055	-0.139143	...	0.001805	0.653452	0.575798	0.639057	0.087960	0.238287	1.000000	0.264079	0.538745	0.303450
        TOV	0.121069	0.325467	0.591306	0.736907	0.794838	0.802002	0.144745	0.496285	0.523658	0.176498	...	0.212927	0.288535	0.622156	0.561929	0.822754	0.603082	0.264079	1.000000	0.564525	0.806638
        PF	0.111609	0.392205	0.536160	0.705754	0.595233	0.563711	0.337232	0.322891	0.339857	0.133237	...	0.225081	0.530736	0.666796	0.669975	0.399748	0.531279	0.538745	0.564525	1.000000	0.576618
        PTS	0.138877	0.465707	0.713721	0.879928	0.990473	0.980010	0.278695	0.722054	0.722231	0.316505	...	0.353171	0.320283	0.696320	0.627926	0.740902	0.649888	0.303450	0.806638	0.576618	1.000000
        
        26 rows × 26 columns


### Generate Intercorrelation Heat map

        fig, ax = plt.subplots(figsize = (17, 5))
        sns.heatmap(corr, square = True);


""")


image = Image.open("D:\Data Science\Streamlit\Heatmap.png")

st.image(image, caption='Points Distribution Fig4')




st.write("""

      
""")







st.write("""

    DataFrame overview


            df.head()

                Player	        Pos    Age	Tm	G	GS	MP	FG	FGA	FG%	...	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS

            0	Precious Achiuwa PF	 21	MIA	61	4	12.1	2.0	3.7	0.544	...	0.509	1.2	2.2	3.4	0.5	0.3	0.5	0.7	1.5	5.0
            1	Jaylen Adams	 PG	 24	MIL	7	0	2.6	0.1	1.1	0.125	...	0.000	0.0	0.4	0.4	0.3	0.0	0.0	0.0	0.1	0.3
            2	Steven Adams	 C	 27	NOP	58	58	27.7	3.3	5.3	0.614	...	0.444	3.7	5.2	8.9	1.9	0.9	0.7	1.3	1.9	7.6
            3	Bam Adebayo      C	 23	MIA	64	64	33.5	7.1	12.5	0.570	...	0.799	2.2	6.7	9.0	5.4	1.2	1.0	2.6	2.3	18.7
            4	LaMarcus Aldridg C	 35	TOT	26	23	25.9	5.4	11.4	0.473	...	0.872	0.7	3.8	4.5	1.9	0.4	1.1	1.0	1.8	13.5
            
            5 rows × 29 columns



        df.select_dtypes(include = ['number']).head()

                Age	 G	GS	MP	FG	FGA	FG%	3P	3PA	3P%	...	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
        0	21	61	4	12.1	2.0	3.7	0.544	0.0	0.0	0.000	...	0.509	1.2	2.2	3.4	0.5	0.3	0.5	0.7	1.5	5.0
        1	24	7	0	2.6	0.1	1.1	0.125	0.0	0.3	0.000	...	0.000	0.0	0.4	0.4	0.3	0.0	0.0	0.0	0.1	0.3
        2	27	58	58	27.7	3.3	5.3	0.614	0.0	0.1	0.000	...	0.444	3.7	5.2	8.9	1.9	0.9	0.7	1.3	1.9	7.6
        3	23	64	64	33.5	7.1	12.5	0.570	0.0	0.1	0.250	...	0.799	2.2	6.7	9.0	5.4	1.2	1.0	2.6	2.3	18.7
        4	35	26	23	25.9	5.4	11.4	0.473	1.2	3.1	0.388	...	0.872	0.7	3.8	4.5	1.9	0.4	1.1	1.0	1.8	13.5
        
        5 rows × 26 columns





        Select the first 5 columns (by index number)


        number = df.select_dtypes(include = ['number'])
        number.iloc[:,:5].head()


                Age     G	 GS 	MP	FG
        0	21	61	4	12.1	2.0
        1	24	7	0	2.6	0.1
        2	27	58	58	27.7	3.3
        3	23	64	64	33.5	7.1
        4	35	26	23	25.9	5.4



Select 5 specific columns(by col names)

                selections= ['Age', 'G', 'STL', 'BLK', 'AST', 'PTS']
                df5 = df[selections]
                df5.head()
        ​
        ​
                Age	G	STL	BLK	AST	PTS
                0	21	61	0.3	0.5	0.5	5.0
                1	24	7	0.0	0.0	0.3	0.3
                2	27	58	0.9	0.7	1.9	7.6
                3	23	64	1.2	1.0	5.4	18.7
                4	35	26	0.4	1.1	1.9	13.5



Make scatter plot grid and compare the correlation between the datapoint



    Scatplot = sns.PairGrid(df5)
    Scatplot.map(plt.scatter);

""")


image = Image.open("D:\Data Science\Streamlit\Scatterplot.png")

st.image(image, caption='Scatterplot Correlation Distribution Fig')




st.write("""


#### Generating the summary of the entire Dataset using Pandas data profiling

    from pandas_profiling import ProfileReport
    profile = ProfileReport(df, title="NBA2021")
    profile


## Results Overview


Reproduction Dataset statistics

    Number of variables	29
    Number of observations	705
    Missing cells	0
    Missing cells (%)	0.0%
    Duplicate rows	0
    Duplicate rows (%)	0.0%
    
   
Variables


    Player Categorical

    Distinct	540
    Distinct (%)	76.6%
    Missing	0
    Missing (%)	0.0%

    Norvel Pelle	 4
    Rodions Kurucs	 4
    Ignas Brazdeikis	 4
    Damian Jones	 4
    Victor Oladipo	 4
    Other values (535)	





Position Categorical


    Distinct	13
    Distinct (%)	1.8%
    Missing	0
    Missing (%)	0.0%
    
    SG	162 
    PF	143 
    C	138 
    PG	127 
    SF	119 
    Other values (8)	 16


Age Real number (ℝ≥0)

    Distinct	21
    Distinct (%)	3.0%
    Missing	0
    Missing (%)	0.0%
    Infinite	0
    Infinite (%)	0.0%
    Mean	25.87092199
    Minimum	19
    Maximum	40
    Zeros	0
    Zeros (%)	0.0%
    Negative	0
    Negative (%)	0.0%
       
Team Categorical


    Distinct	31
    Distinct (%)	4.4%
    Missing	0
    Missing (%)	0.0%
 
 
    TOT	79 
    HOU	 30
    ORL	 28
    BRK	 27
    CLE	 25
    Other values (26)	516 

### Positions

G Real number (ℝ≥0)

    Distinct	72
    Distinct (%)	10.2%
    Missing	0
    Missing (%)	0.0%
    Infinite	0
    Infinite (%)	0.0%
    Mean	37.36879433
    Minimum	1
    Maximum	72
    Zeros	0
    Zeros (%)	0.0%
    Negative	0
    Negative (%)	0.0%



GS

    Real number (ℝ≥0)
    ZEROS
    Distinct	72
    Distinct (%)	10.2%
    Missing	0
    Missing (%)	0.0%
    Infinite	0
    Infinite (%)	0.0%
    Mean	16.94184397
    Minimum	0
    Maximum	72
    Zeros	177
    Zeros (%)	25.1%
    Negative	0
    Negative (%)	0.0%


MP


    Real number (ℝ≥0)
    Distinct	298
    Distinct (%)	42.3%
    Missing	0
    Missing (%)	0.0%
    Infinite	0
    Infinite (%)	0.0%
    Mean	19.43588652
    Minimum	1.8
    Maximum	37.6
    Zeros	0
    Zeros (%)	0.0%
    Negative	0
    Negative (%)	0.0%

FG


    Real number (ℝ≥0)
    ZEROS
    Distinct	97
    Distinct (%)	13.8%
    Missing	0
    Missing (%)	0.0%
    Infinite	0
    Infinite (%)	0.0%
    Mean	3.166099291
    Minimum	0
    Maximum	11.2
    Zeros	12
    Zeros (%)	1.7%
    Negative	0
    Negative (%)	0.0%



FGA


    Real number (ℝ≥0)
    Distinct	177
    Distinct (%)	25.1%
    Missing	0
    Missing (%)	0.0%
    Infinite	0
    Infinite (%)	0.0%
    Mean	6.944680851
    Minimum	0
    Maximum	23
    Zeros	2
    Zeros (%)	0.3%
    Negative	0
    Negative (%)	0.0%



FG%


    Real number (ℝ≥0)
    Distinct	277
    Distinct (%)	39.3%
    Missing	0
    Missing (%)	0.0%
    Infinite	0
    Infinite (%)	0.0%
    Mean	0.4422283688
    Minimum	0
    Maximum	1
    Zeros	12
    Zeros (%)	1.7%
    Negative	0
    Negative (%)	0.0%



3P

    Real number (ℝ≥0)
    Distinct	40
    Distinct (%)	5.7%
    Missing	0
    Missing (%)	0.0%
    Infinite	0
    Infinite (%)	0.0%
    Mean	0.959858156
    Minimum	0
    Maximum	5.3
    Zeros	102
    Zeros (%)	14.5%
    Negative	0
    Negative (%)	0.0%



3PA

    Real number (ℝ≥0)
    Distinct	90
    Distinct (%)	12.8%
    Missing	0
    Missing (%)	0.0%
    Infinite	0
    Infinite (%)	0.0%
    Mean	2.714042553
    Minimum	0
    Maximum	12.7
    Zeros	43
    Zeros (%)	6.1%
    Negative	0
    Negative (%)	0.0%


3P%

    Real number (ℝ≥0)
    Distinct	221
    Distinct (%)	31.3%
    Missing	0
    Missing (%)	0.0%
    Infinite	0
    Infinite (%)	0.0%
    Mean	0.2989262411
    Minimum	0
    Maximum	1
    Zeros	87
    Zeros (%)	12.3%
    Negative	0
    Negative (%)	0.0%


2P

    Real number (ℝ≥0)
    ZEROS
    Distinct	79
    Distinct (%)	11.2%
    Missing	0
    Missing (%)	0.0%
    Infinite	0
    Infinite (%)	0.0%
    Mean	2.21035461
    Minimum	0
    Maximum	10.2
    Zeros	19
    Zeros (%)	2.7%
    Negative	0
    Negative (%)	0.0%


2PA

    Real number (ℝ≥0)
    Distinct	131
    Distinct (%)	18.6%
    Missing	0
    Missing (%)	0.0%
    Infinite	0
    Infinite (%)	0.0%
    Mean	4.236170213
    Minimum	0
    Maximum	16.8
    Zeros	6
    Zeros (%)	0.9%
    Negative	0
    Negative (%)	0.0%


2P%

    Real number (ℝ≥0)
    Distinct	279
    Distinct (%)	39.6%
    Missing	0
    Missing (%)	0.0%
    Infinite	0
    Infinite (%)	0.0%
    Mean	0.502448227
    Minimum	0
    Maximum	1
    Zeros	19
    Zeros (%)	2.7%
    Negative	0
    Negative (%)	0.0%


FG%

    Real number (ℝ≥0)HIGH CORRELATION
    Distinct	268
    Distinct (%)	38.0%
    Missing	0
    Missing (%)	0.0%
    Infinite	0
    Infinite (%)	0.0%
    Mean	0.507458156
    Minimum	0
    Maximum	1
    Zeros	12
    Zeros (%)	1.7%
    Negative	0
    Negative (%)	0.0%


FT

    Real number (ℝ≥0)HIGH CORRELATION
    Distinct	61
    Distinct (%)	8.7%
    Missing	0
    Missing (%)	0.0%
    Infinite	0
    Infinite (%)	0.0%
    Mean	1.325957447
    Minimum	0
    Maximum	9.2
    Zeros	35
    Zeros (%)	5.0%
    Negative	0
    Negative (%)	0.0%


FTA

    Real number (ℝ≥0)
    Distinct	72
    Distinct (%)	10.2%
    Missing	0
    Missing (%)	0.0%
    Infinite	0
    Infinite (%)	0.0%
    Mean	1.722978723
    Minimum	0
    Maximum	10.7
    Zeros	29
    Zeros (%)	4.1%
    Negative	0
    Negative (%)	0.0%


""")







