echo 'check_grid_world_enivronment'
python3 envir.py

echo 'normal_moves -  Example 6.5'
echo 'CLose the Figure 1 window to see the next tasks'
python3 sarsa_zero.py --actions normal_moves
sleep 1

echo 'king_moves - Excercise 6.9'
echo 'CLose the Figure 1 window to see the next tasks'
python3 sarsa_zero.py --actions king_moves
sleep 1

echo 'king_moves_with_no_move - Excercise 6.9 with extra moves'
echo 'CLose the Figure 1 window to see the next tasks'
python3 sarsa_zero.py --actions king_moves_with_stable
sleep 1

echo 'king_moves_with_stochastic - Excercise 6.10'
echo 'This is the last task'
python3 sarsa_zero.py --actions king_moves_with_stochastic

