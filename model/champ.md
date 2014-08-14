championId  int Champion ID associated with game.
createDate  long    Date that end game data was recorded, specified as epoch milliseconds.
fellowPlayers   List[PlayerDto] Other players associated with the game.
gameId  long    Game ID.
gameMode    string  Game mode. (legal values: CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, FIRSTBLOOD)
gameType    string  Game type. (legal values: CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)
invalid boolean Invalid flag.
ipEarned    int IP Earned.
level   int Level.
mapId   int Map ID.
spell1  int ID of first summoner spell.
spell2  int ID of second summoner spell.
stats   RawStatsDto Statistics associated with the game for this summoner.
subType string  Game sub-type. (legal values: NONE, NORMAL, BOT, RANKED_SOLO_5x5, RANKED_PREMADE_3x3, RANKED_PREMADE_5x5, ODIN_UNRANKED, RANKED_TEAM_3x3, RANKED_TEAM_5x5, NORMAL_3x3, BOT_3x3, CAP_5x5, ARAM_UNRANKED_5x5, ONEFORALL_5x5, FIRSTBLOOD_1x1, FIRSTBLOOD_2x2, SR_6x6, URF, URF_BOT, NIGHTMARE_BOT)
teamId  int Team ID associated with game. Team ID 100 is blue team. Team ID 200 is purple team.
