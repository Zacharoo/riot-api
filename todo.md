## TO DO

First, cut the release branch.
Deploy the released code to the VPS.

Idempotence isn''t happening because we don''t store the Riot Game id anywhere. It''s slated to be stored in the Game table, but I don''t make a new Game object yet. 

First, refactor Fetch_and_store_summoner to use smaller methods.
Next, start storing the Game objects in the database as well.
    Maybe consider writing tests for adding game objects and GameStats objects.
Then, I can start checking for the Riot ID before storing a new object.

- Double check idempotence
- Get the other tables to persist
- Deploy
- Add more metrics to the tables
- Work on the NACC feature request.
- Test if we can grab tournament matches from Pitt by setting an object with Member stats. Err, maybe a Team object..?

Set up to track the OLS team players for individual records, and then for team matches. Compare the results with the scheduled matches.

Get the rosters for the NACC teams.

- Map the model to the API structs
    - Create a set of functions to idempotently accept a new game and put it into the database, if and only if it doesnt already exist in the database.
    - Do we want to just store all of the champion static data in the db with one query then let it persist?
    - Definitely store all of the champion static data in the db with the query, so that we don''t have to wait on the 1 second delay to fetch the information, and so that it doesn''t impact our rate limit once we start doing a ton of queries! 

- Finish out the API client library
    - Only need to do the functions missing
    - Consider using the Team resource.
    - Open-source it

Double check idempotence on adding games to the db.

Check!!     Use enviroment variable fetching to determine what kind of enviroment mode we to set up.

Check!       Test to see if the data persists in the test database after the program exits.
