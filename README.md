# ProbabilityProject
Solves the probability count of a coin toss using the Bayesian approach.


-- PROBLEM TO SOLVE

You have found a dodgy bookmaker who plays a strange game. He has two coins, both biased. The first one
comes up heads 70% of the time. The other comes up tails 60% of the time. To you, they look identical.
The bookmaker’s process is to approach you with a single coin. You can’t tell which one, but it is one of
the ones described above. He will then state betting odds for heads and for tails and ask if you want to bet.
Your options are to bet heads, bet tails, or make no bet. He then tosses the coin and pays out based on
the odds if it matches your bet. The bookmaker will repeat this process 100 times with the same coin but
offering different odds each time. The bookmaker’s odds seem random and are always between 1 and 3.
Your goal is to write a Python function makeBet(headsOdds, tailsOdds, previousOutcome, state) that makes
bets with the bookmaker. The marker will call your function as follows:
• headsOdds and tailsOdds give the total payout (including your stake of 1) for a bet of heads or tails
respectively.
• previousOutcome gives the outcome of the previous coin toss, which you should use to update your
models
• Your function should return a pair: (bet, state)
• bet should be one of ’heads’, ’tails’, ’no bet’ representing your bet
• state is a variable that will be returned to you next time your function is called. I.e. if your function
returns state then that will be given as the state argument on the next call to your function. You can
use this mechanism to allow your function to keep track of any information that you see fit.
The marker will randomly choose one of the two coins and call your function 100 times with the same coin.
The first time, state and previousOutcome will be set to None. The marker will keep track of the profit that

you make over the 100 calls. Your goal is to make the most profit. A test harness will be made available
that gives the details of this process.
Since this is randomised process, the profit will change from run to run. To smooth out the differences, the
marker will make 10000 runs as described above, each time with a different coin (total 1000000 calls to your
function, 100 in a row with each coin). Your profit will be taken to be the average profit over these 1000
runs. A profit of about 33.6 is achievable using all information, 22 is achievable without making use of the
state variable, and 10 is achievable using a constant output.
