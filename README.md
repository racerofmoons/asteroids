# Project Kessler: Asteroid Miner

Asteroids meets rogue-lite. Mine minerals from the asteroid field without being taken out by the chaos. Use your minerals for research and profits. Use your profits to buy upgrades you've researched.

This is as a project to practice OOP, class inheritance, and building helper-methods in python, but I wanted to have fun with it, so I built the classic Asteroids-Clone into an asteroid-mining-roguelite.

## Roadmap
- Increase the map-size and/or variable sizes.
- Menu system will transfer this to include a rogue-lite system of buying upgrade cards. This is going to be a simple system really for a small set of upgrades to give players more variety of gameply. Each category is unique for each run.
- Weapon Types - upgrades main weapon
    - Cannon
        T1 = Basic Cannon
        Higher tiers increase velocity and/or add penetration for multi-kills
    - Shotgun 
        T1 = 3 projectiles on a small arc
        T2 = 4 projectiles
        T3 = 5 projectiles
        T4 = 6 projectiles on a new larger Arc
        T5 = 7 projectiles
        T6 = 8 projectiles
        T7 = 9 projectiles
        T8 = 9 projectiles on a new larger Arc (can be toggled wide or narrow)
    - Laser
        T1 = Short burst laser on a long cooldown
        Higher tiers alternate between longer burst and cooldown reduction
    - Missiles
        T1 = Basic cannon but explodes on impact
        Higher tiers increase speed and explosion radius high-tiers add fragments that also kill asteroids
    - Efficient Mining upgrades
    - Trader Bonuses
- Turret - fires on a timer randomly, similar to bullet-hell games. Mirror weapon types, but have a long reload time. Higher tiers unlock auto-targeting closest asteroids
- Shield - provides extra lives for the run
- Mineral count will allow unlocking new objects between runs. Notifications should pop for the resource type and "mineral value" should be on screen as a counter.
    - Implement increasing costs for each unlock tier
    - Implement mineral types on a random drop, the more asteroids you kill the more likely you are to get more rare minerals
    - T1 - Silica
    - T2 - Iron
    - T3 - Aluminum
    - T4 - Cobalt
    - T5 - Gold
    - T6 - Uranium
    - T7 - Thorium
- Balance update for mineral types and costs. I don't want the game to feel too grindy but I want it to feel engaging. 
    - Players should be able to start with 1 active tier 1 upgrade. The rest should be picked up as kill-streak goes up (level ups) during a run. 
- Surprise additions (maybe) and release build.
- Find some art to replace the basic design and some sound to add to the project. I'd ideally like to keep the retro-mode an option and give players the choice of which 'look' they prefer.