# RocketLeagueTracker

Simple Python script to pull rocket league stats

# Table of Contents

- [The Project](#theproject)
- [The API](#theapi)
- [Stats Returned](#statsreturned)

# The Project <a name = "theproject"></a>

This is a simple project to start grabbing Rocket League stats from the tracker network API.

Currently it is just pulling simple stats from my lifetime and season stats. The API is limited, and so there isn't too much information to be garnered from it.

# The API <a name = "theapi"></a>

All information is gathered from the following API, where `<platformID>` and `<userID>` are input in the program.

```
https://api.tracker.gg/api/v2/rocket-league/standard/profile/<platformID>/<userID>
```

For example data use my personal Rocket League stats

```
https://api.tracker.gg/api/v2/rocket-league/standard/profile/xbl/UKF%20WONDERBOY
```

# Stats Returned <a name = "statsreturned"></a>

Currently the code will display:

- User ID and platform
- Current Season and Season Rewards
- Lifetime wins
- Lifetimes win rank
- Lifetime goal to shot ratio
