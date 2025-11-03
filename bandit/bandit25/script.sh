bandit24_pw='gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8'

for i in $(seq 0 9)
do
	for j in $(seq 0 9)
	do
		for k in $(seq 0 9)
		do	
			for l in $(seq 0 9)
			do
				echo $bandit24_pw $i$j$k$l
			done			
		done
	done
done

