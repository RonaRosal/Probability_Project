import numpy as np
import probability as P

#Followed techniques from CAB203 Lectures & Tutorial 11 & 12 and Probability.py 

def fertiliser(an, ap, bn, bp, n, p):

    #All arguments must be non-negative
    if an < 0 or ap < 0 or bn < 0 or bp < 0 or n < 0 or p < 0:
        return None

    #Referenced from CAB203 Lecture 11 slide 45
    A = np.array([[an,bn], [ap,bp]]) 
    B = np.array([[n], [p]]) 

    #The determinant of a must be a non-zero to be able to perform an inverse of A
    detA = np.linalg.det(A) #Referenced from numpy library https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html
    if detA == 0:
        return None

    InvA = np.linalg.inv(A)
    result = InvA @ B #Referenced from CAB203 Lecture 11 slide 45
    a = result[0][0]
    b = result[1][0]

    if a < 0 or b < 0: #the result (a & b) ust be non-negative
        return None

    return a, b


def makeBet(headsOdds, tailsOdds, previousOutcome, state):

    likelihood = {
        'biased1': {'heads': 0.7, 'tails': 0.3 }, #heads comes up 70% of the time
        'biased2': {'heads': 0.4, 'tails': 0.6} #tails comes up 60% of the time
        }

    if state is None:
        prior = { 
            'biased1': 0.5,
            'biased2': 0.5
        }

        betProbability = likelihood['biased1'] #select 'biased1' from likelihood as initial bet probability
    else:
        prior = state["prior"] #get prior value from state variable
        prior = P.posterior(prior, likelihood, { previousOutcome }) #determine posterior distribution on hypotheses based from previous outcome
        biased = max(prior, key = prior.get) #select biased that has larger value and get its key, expected result 'biased1' or 'biased2'
        betProbability = likelihood[biased] #get probability from likelihood dictionary

    #set winning oddss for heads
    betHeads = {
        'heads': headsOdds -1,
        'tails': - 1
        }

    #set winning odds for tails
    betTails = {
        'heads': -1,
        'tails': tailsOdds -1
        }

    #set winning odds for no bets
    noBet = {
        'heads': 0,
        'tails': 0
        }

    choice = P.decide(betProbability, {'heads': betHeads, 'tails': betTails, 'no bet': noBet})
    bet = choice[0] #get choice key
    state = {
        'prior': prior #save prior values to state variable
    }
    return (bet, state)
