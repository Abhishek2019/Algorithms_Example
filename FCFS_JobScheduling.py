print "Enter number of Jobs : "
no_of_jobs = int(raw_input().strip())

print "Enter Arrival_Time , Burst_Time : "
arival_time = []
burst_time = []

for i in range(no_of_jobs):
	temp = map(int,raw_input().strip().split(" "))
	arival_time.append(temp[0])
	burst_time.append(temp[1])

#print (arival_time,burst_time) 

turn_arount_time = []
waiting_time = []
finish_time = []

for i in range(no_of_jobs):
	finish_time.append(sum(burst_time[0:i+1]))
 	turn_arount_time.append(int(finish_time[i] - arival_time[i]))
	waiting_time.append(int(turn_arount_time[i] - burst_time[i]))

#print (turn_arount_time,waiting_time)

average_turn_arount_time = (sum(turn_arount_time)/no_of_jobs)*1.0
average_waiting_time = (sum(waiting_time)/no_of_jobs)*1.0;
print "\tAT\tBT\tCT\tTAT\tWT\n"
for i in range(no_of_jobs):
	print "\t{0}\t{1}\t{2}\t{3}\t{4}\n".format(arival_time[i],
						   burst_time[i],
						   finish_time[i],
						   turn_arount_time[i],
						   waiting_time[i])

print "Average Turn Around Time : {0}".format(average_turn_arount_time)
print "Average Waiting Time : {0}".format(average_waiting_time)	

'''
#Sample Output

D:Operating System Algorithm>python FCFS_JobScheduling.py
Enter number of Jobs :
6
Enter Arrival_Time , Burst_Time :
0 250
50 170
130 75
190 100
210 130
350 50
        AT      BT      CT      TAT     WT

        0       250     250     250     0

        50      170     420     370     200

        130     75      495     365     290

        190     100     595     405     305

        210     130     725     515     385

        350     50      775     425     375

Average Turn Around Time : 388.0
Average Waiting Time : 259.0

'''