instance=['../instances/i-1.txt']
instance=['../instances/i-2.txt']
instance='../instances/i-3.txt'
algoritm='kl-ucb'
epsilon=0.002
horizon=200
randomSeeds=list(range(50))

with open('check.sh','a+') as output:
    output.write('#!bin/sh\n\n')
    output.write('i=1\n\n')

for randomSeed in randomSeeds:
                        with open('check.sh','a+') as o:
                            o.write('echo "Test $i"\n')
                            o.write('./bandit.sh --instance {} --algorithm {} --randomSeed {} --epsilon {} --horizon {}\n'.format(instance,algoritm,int(randomSeed),epsilon,horizon)) 
                            o.write('sleep 1\n')
                            o.write('i=$((i + 1))\n\n')
