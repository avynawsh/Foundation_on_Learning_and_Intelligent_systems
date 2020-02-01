#echo episodic
#./planner.sh --mdp /home/sounak/data/episodic/testmdp.txt --algorithm lp > outputSo
#python diffCheck.py outputSol /home/sounak/data/episodic/testsol.txt

#echo continuing
#./planner.sh --mdp /home/sounak/data/continuing/testmdp.txt --algorithm lp > outputSol
#python diffCheck.py outputSol /home/sounak/data/continuing/testsol.txt

echo continuing
./planner.sh --mdp /Users/avinashreddy/Desktop/CS_747/cs747-pa2/data/continuing/MDP2.txt --algorithm lp > outputSol
python diffCheck.py outputSol /Users/avinashreddy/Desktop/CS_747/cs747-pa2/data/continuing/sol2.txt
#print

echo continuing
./planner.sh --mdp /Users/avinashreddy/Desktop/CS_747/cs747-pa2/data/continuing/MDP10.txt --algorithm lp > outputSol
python diffCheck.py outputSol /Users/avinashreddy/Desktop/CS_747/cs747-pa2/data/continuing/sol10.txt 

echo episodic
./planner.sh --mdp /Users/avinashreddy/Desktop/CS_747/cs747-pa2/data/episodic/MDP2.txt --algorithm lp > outputSol
python diffCheck.py outputSol /Users/avinashreddy/Desktop/CS_747/cs747-pa2/data/episodic/sol2.txt

echo episodic
./planner.sh --mdp /Users/avinashreddy/Desktop/CS_747/cs747-pa2/data/episodic/MDP10.txt --algorithm lp > outputSol
python diffCheck.py outputSol /Users/avinashreddy/Desktop/CS_747/cs747-pa2/data/episodic/sol10.txt

 
echo continuing
./planner.sh --mdp /Users/avinashreddy/Desktop/CS_747/cs747-pa2/data/continuing/MDP2.txt --algorithm hpi > outputSol
python diffCheck.py outputSol /Users/avinashreddy/Desktop/CS_747/cs747-pa2/data/continuing/sol2.txt

echo continuing
./planner.sh --mdp /Users/avinashreddy/Desktop/CS_747/cs747-pa2/data/continuing/MDP10.txt --algorithm hpi > outputSol
python diffCheck.py outputSol /Users/avinashreddy/Desktop/CS_747/cs747-pa2/data/continuing/sol10.txt

echo episodic
./planner.sh --mdp /Users/avinashreddy/Desktop/CS_747/cs747-pa2/data/episodic/MDP2.txt --algorithm hpi > outputSol
python diffCheck.py outputSol /Users/avinashreddy/Desktop/CS_747/cs747-pa2/data/episodic/sol2.txt

echo episodic
./planner.sh --mdp /Users/avinashreddy/Desktop/CS_747/cs747-pa2/data/episodic/MDP10.txt --algorithm hpi > outputSol
python diffCheck.py outputSol /Users/avinashreddy/Desktop/CS_747/cs747-pa2/data/episodic/sol10.txt  


echo continuing
./planner.sh --mdp /Users/avinashreddy/Desktop/CS_747/cs747-pa2/files/data/continuing/testmdp.txt --algorithm lp > outputSol
python diffCheck.py outputSol /Users/avinashreddy/Desktop/CS_747/cs747-pa2/files/data/continuing/testsol.txt

echo episodic
./planner.sh --mdp /Users/avinashreddy/Desktop/CS_747/cs747-pa2/files/data/episodic/testmdp.txt --algorithm lp > outputSol
python diffCheck.py /Users/avinashreddy/Desktop/CS_747/cs747-pa2/files/data/episodic/testsol.txt

echo continuing
./planner.sh --mdp /Users/avinashreddy/Desktop/CS_747/cs747-pa2/files/data/continuing/testmdp.txt --algorithm hpi > outputSol
python diffCheck.py outputSol /Users/avinashreddy/Desktop/CS_747/cs747-pa2/files/data/continuing/testsol.txt

echo episodic
./planner.sh --mdp /Users/avinashreddy/Desktop/CS_747/cs747-pa2/files/data/episodic/testmdp.txt --algorithm hpi > outputSol
python diffCheck.py outputSol  /Users/avinashreddy/Desktop/CS_747/cs747-pa2/files/data/episodic/testsol.txt





