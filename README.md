# Fantasy Football Weekly Score and Schedule Analyzer
Compares teams in ESPN Fantasy Football leagues on the basis of per-week scoring, helps show how much of a factor schedule luck has played. Programmed in Python using ESPN's Fantasy Football API.

### Current state:
Only works for my personal league at the time being, will take in league ID as user input when I'm further along in development.

### How to use in current state:
1. Input a team abbreviation for Team 1 and Team 2 (as they are written on the program)
2. Outputs scores for weeks 1-13 if Team 1 played Team 2 every week

### Why this is useful:
Good for seeing how you stack up against other teams in your league, or if you played them the "wrong week."
For example, this season I lost two games to one person. Through this analyzer, I was able to see that out of 13 games, he only outscored me in 3 different weeks, 2 of which happened to be when I played him.
Also, I was able to quickly find out that if my team (which finished 7-6 under normal scheduling) played the 1st place 11-2 team every week, I would've only been one game worse at 6-7.

### Goals for the future:
- Look for what would've been the "optimal" schedule (best possible record with no more than 2 games vs. each person and no rematches 2 weeks in a row)
- Factor individual player scores for fun facts (i.e. "What would my record be if I never had Todd Gurley and started X player from my bench every week instead?")
