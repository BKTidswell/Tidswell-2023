import re
import os
import csv
import math
import numpy as np
from fish_core import *

demo_filename = "2020_06_29_20_TN_DN_F0_VDLC_resnet50_L8FVJul4shuffle1_50000_bx_filtered.csv"

outStr = "{fish1},{fish2},{dist},{angle},{year},{month},{day},{trial},{frame},{turb},{dark},{flow}\n"
num_fish = 8

data_folder = os.getcwd()+"/Finished_Fish_Data/"

#Gets the distance between two points
def get_dist(p1,p2):
	return(math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)))

def get_angle(p1,p2):
	delta_x = p1[0] - p2[0]
	delta_y = p1[1] - p2[1]
	theta_degrees = math.degrees(math.atan2(delta_y, delta_x))
	return(theta_degrees)

f = open("combined_fish_nnd.csv", "w")
f.write(outStr.format(fish1="fish1",fish2="fish2",dist="dist",angle="angle",year="year",month="month",day="day",trial="trial",frame="frame",turb="turb",dark="dark",flow="flow"))

for filename in os.listdir(data_folder):
	if filename.endswith(".csv"):

		year = filename[0:4]
		month = filename[5:7]
		day = filename[8:10]
		trial = filename[11:13]
		turb = filename[15:16]
		dark = filename[18:19]
		flow = filename[21:22]

		print(year,month,day,trial,turb,dark,flow)

		fish_dict,time_points = DLC_CSV_to_dict(num_fish = n_fish, fish_parts = b_parts_csv, file = data_folder+filename)

		#Find the pixel to bodylength conversion to nromalize all distances by body length
		cnvrt_pix_bl = []

		for i in range(n_fish):
			cnvrt_pix_bl.append(median_fish_len(fish_dict,i))

		with open(data_folder+filename, 'r') as read_obj:

			csv_reader = csv.reader(read_obj)
			frame_counter = 0

			for row in csv_reader:
				if row[0].isdigit():
					num_row = np.asarray(row).astype(float)

					head_xs = num_row[1:145:18]
					head_ys = num_row[2:146:18]

					for i in range(num_fish):
						for j in range(i+1,num_fish):

							if i != j:
								distance = get_dist([head_xs[i],head_ys[i]],[head_xs[j],head_ys[j]])/cnvrt_pix_bl[i]

								angle = get_angle([head_xs[i],head_ys[i]],[head_xs[j],head_ys[j]])

								f.write(outStr.format(fish1=i,fish2=j,dist=distance,angle=abs(angle),year=year,month=month,day=day,trial=trial,frame=frame_counter,turb=turb,dark=dark,flow=flow))
								#f.write(outStr.format(fish1=i,fish2=j,dist=distance,angle=-1*angle,year=year,month=month,day=day,trial=trial,frame=frame_counter,turb=turb,dark=dark,flow=flow))

					frame_counter += 1

f.close()








