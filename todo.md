## TO DO

- Build the model lolololol
    - Start with the summoner
        - Design the model for a summoner.
        - Build the model for a summoner.
        - Test it    

    - Move into the champion model
        - Design it
        - Build it
        - Test it

    - Move into the model for an item
        - Design it
        - Build it
        - Test it

    - Move into the model for a game
        - Design it
        - Build it
        - Test it

- Map the model to the API structs
    - Create a set of functions to idempotently accept a new game and put it into the database, if and only if it doesnt already exist in the database.
    - Do we want to just store all of the champion static data in the db with one query then let it persist?

- Finish out the API client library
    - Only need to do the functions missing
    - Consider using the Team resource.
