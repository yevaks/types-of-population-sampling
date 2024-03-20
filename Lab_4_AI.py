import random
import pandas as pd

N = 1000
n = 100
def general(K):
    gen = []
    [gen.append(random.random()) for _ in range(K)]
    return gen

def simple_rand_no_repeat(k, K, s):
    sample = []
    indexes = []
    [indexes.append(random.randint(0, K-1)) for _ in range(k)]
    [sample.append(s[i]) for i in indexes]
    return sample

def bernoulli(k, K, s):
    p = k/K
    rands = general(K) #sequens of randoms 0-1, not another general set
    sample = []
    [sample.append(s[i]) for i in range(K) if rands[i] < p ]
    return sample

def systematic(k, K, s):
    a = int(K/k - 1)
    r = random.randint(1, a-1)
    sample = []
    range_end = int(r+(k-1)*a + 1)
    [sample.append(s[i]) for i in range(r, range_end, a)]
    return sample

def stratified(k, K, s):
    s1 = simple_rand_no_repeat(k, K, s)
    s2 = bernoulli(k, K, s)
    s3 = systematic(k, K, s)
    return s1, s2, s3

def calculations(k, K):

    ##########0###########
    general_set = general(K)
    gen_sum = sum(general_set)
    gen_mean = gen_sum / K

    ##########1###########
    simple_sample = simple_rand_no_repeat(k,K, general_set)
    sum1 = sum(simple_sample)
    mean1 = sum1/k

    ##########2###########
    bernoulli_sample = bernoulli(k,K, general_set)
    sum2 = sum(bernoulli_sample)
    mean2 = sum2/len(bernoulli_sample)

    ##########3###########
    systematic_sample = systematic(k,K, general_set)
    sum3 = sum(systematic_sample)
    mean3 = sum2/len(systematic_sample)

    ##########4###########
    strat1, strat2, strat3 = stratified(k,K, general_set)
    sum4 = (sum(strat1) + sum(strat2) + sum(strat3))
    mean4 = sum4 / (len(strat1) + len(strat2) + len(strat3))

    sums = (gen_sum, sum1, sum2, sum3, sum4)
    means = (gen_mean, mean1, mean2, mean3, mean4)

    return sums, means

def output(k, K):
    sums, means = calculations(k, K)
    df = pd.DataFrame([sums, means], ["sum", "mean"], columns = ["General", "Simple",
                                                                 "Bernoulli", "Systematic",
                                                                 "Stratified"])
    print(f"######################## N = {K} ########################\n", df,"\n")

output(n,N)
output(n,10000)
output(n,100000)
output(n,1000000)
