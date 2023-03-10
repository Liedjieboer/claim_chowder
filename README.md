# Claim Chowder



*“Even though the speculation is correct only by chance, which means you are wrong at least 50% of the time, nobody remembers and therefore nobody cares. You are never accountable. The audience does not remember yesterday, let alone last week, or last month.”* —Michael Crichton

What if we could measure the quality of historic predictions and use that knowledge to help us decide who to listen to today?

In this project we apply Machine Learning to the problem of capturing, quantifying and gauging the accuracy of historic predictions. We use NLP to build a dataset of historic predictions and outcomes and we train a model that can predict the reliability of any given source.

Things we might want to try:
* Using ChatGPT to generate code to capture predictions (or just even just the text) from a given source
* Using a LLM + other NLP techniques to obtain quantified predictions from text
* Classification of predictions by type, precision, horizon (how far out the prediction is made)
* Using a GAN to generate fake predictions? (this was suggested by GitHub Copilot!)
* Train a model to predict the reliability of a source based on the quality of their predictions

"Claim Chowder" : a poorly substantiated assertion regarding the future status or make of an item which is cited by a dubious party for later use as a reference of gross inaccuracy and to exercise gloating. Most often employed in the context of technological advancement (https://www.urbandictionary.com/define.php?term=Claim%20Chowder)

## How to install
pip install chowder

## How to run tests
make tests

# Example URLs
https://www.skysports.com/rugby-union/news/12337/11813067/rugby-world-cup-predictions-our-pundits-share-their-predictions-ahead-of-japan-2019
https://bleacherreport.com/articles/2585182-5-bold-predictions-for-the-2019-rugby-world-cup
https://www.theguardian.com/sport/2019/sep/19/rugby-world-cup-2019-guardian-predictions
https://www.independent.co.uk/sport/rugby/rugby-union/international/rugby-world-cup-2019-predictions-winner-dark-horses-top-player-breakout-star-a9113531.html
https://www.theweek.co.uk/2019-rugby-world-cup/103204/rugby-world-cup-japan-winner-predictions-webb-ellis-cup



# Interesting article
https://www.significancemagazine.com/sports/637-how-well-did-an-algorithm-perform-at-the-2019-rugby-world-cup
