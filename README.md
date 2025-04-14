# Project Kessler: Asteroid Miner

Asteroids meets rogue-lite. Mine minerals from the asteroid field without being taken out by the chaos. Use your minerals for research and profits. Use your profits to buy upgrades you've researched.

This is as a project to practice OOP, class inheritance, and building helper-methods in python, but I wanted to have fun with it, so I built the classic Asteroids-Clone into an asteroid-mining-roguelite.

version 0.6

## Roadmap
- IN PROGRESS - Increase the map-size and/or variable sizes.
    - DONE - build config object
    - IN PROGRESS - refactor menus to be polymorphic
    - IN PROGRESS - build config menu and game re-initialization on system changes
- IN PROGRESS - Menu system and enhancements will transfer this to include a rogue-lite system of buying upgrade cards. This is going to be a simple system really for a small set of upgrades to give players more variety of gameply. Each category is unique for each run.
- DONE - support for a single save game
    - IN PROGRESS - set up loaded game menu
    - and a way to clear save data
        - confirmation popup for clearing save data
- Difficulty scaling - the longer a run lasts, the more difficult it should get.
- Weapon Types - upgrades main weapon
    - Cannon
        T1 = Basic Cannon
        Higher tiers increase velocity and/or add penetration for multi-kills
    - Shotgun 
        more on a small arc
    - Laser
        T1 = Short burst laser on a long cooldown
        Higher tiers alternate between longer burst and cooldown reduction
    - Missiles
        T1 = Basic cannon but explodes on impact
        Higher tiers increase speed and explosion radius high-tiers add fragments that also kill asteroids
    - Efficient Mining upgrades
    - Trader Bonuses
- Turrets - fires on a timer randomly, similar to bullet-hell games. Mirror weapon types, but have a long reload time. Higher tiers unlock auto-targeting closest asteroids
- Shields - provides extra lives for the run
- Mineral count will allow unlocking new objects between runs. Notifications should pop for the resource type and "mineral value" should be on screen as a counter.
    - Implement increasing costs for each unlock tier
    - DONE - Implement mineral types on a random drop, the more asteroids you kill the more likely you are to get more rare minerals
- Balance update for mineral types and costs. I don't want the game to feel too grindy but I want it to feel engaging. 
    - Players should be able to start with 1 active tier 1 upgrade. The rest should be picked up as kill-streak goes up (level ups) during a run. 
- Surprise additions (maybe) and release build.
- Find some art to replace the basic design and some sound to add to the project. I'd ideally like to keep the retro-mode an option and give players the choice of which 'look' they prefer.