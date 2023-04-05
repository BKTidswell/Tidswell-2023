# Code for (Title of this Paper)

Welcome to this Github respository for (Title of this Paper). If you are here, I assume you're interested in doing a deep dive into the code that I wrote to turn the positional data of fish into schooling kinematics. To that end this guide aims to walk you through running all the code from start to finish, and to explain the purpose the code files here. If you run into any issues with it feel free to raise an issue here or email me at b.k.tidswell@gmail.com. 

As a note, this code was written to work on a Mac, so you may need to set up some things differently if you are using a Windows and Linux computer, particularly with the Conda enviornment, as well as some of the graphing functions. With that said, let's get started.

## Installing the Environment

I have included a conda environement file (DLC_M1.yml) to use to set up the environement that I used to run all of this code. This does include the DeepLabCut libraries, as well as tensorflow, which are not needed to run any of the code in this repository, but are included becasue that is the environment I used. 

With Conda installed, simply run `conda env create -f DLC_M1.yml` to create the environment, and then `conda activate DLC_M1` once it is finished to use the enviroment.
 
## 2D to 3D Data

Inside of `2Dto3D/` there are two folders that contain all of the raw kinematic data from DeepLabCut. `V1 CSVs/` contains the Ventral 1 (V1) camera data, while `V2 CSVs/` contains the Ventral 1 (V1) camera data. Running `python DLT_Converter.py` takes those files, and using the EasyWand coefficents in `DLT Coefs` calculates the 3D points, putting the results into `Final 3D/`. If you want to see what the 3D points look like, you can run `python DLT_Plotter.py` in order to create Plotly graphs of the 3D points of the fish over time. These are stored as .html files in `Saved 3D Plots/` so you can view them whenever you like.

## 3D Data to School Kinematics CSV

Now that you have the 3D data, you can take that and put it into the main folder labeled `3D_Finished_Fish_Data_4P_gaps/`. This folder is named this becuase it has the complete 3D data, with 4 points on each fish, and gaps in some of the traces, to differeentiate it from other older versions of this data. Now, simply run `python 3D_data_files_to_csv_4P.py`, which will calaculate the important kinematic values for the school and place that data where the R analysis code will look for it. 

## Turning Data

Analyzing the turning data has two seperate parts to it. Firt you need to take the traces of individual fish and combine them randomly to create artifical "schools" and then you need to use the code in `Fish Turning Processor/` in order to determine out where the turns take place.

### Artifical School Creation

Look in the folder `Single Fish Combiner`. Here you will see two folders, `Single Fish/` which is where the traces of single fish swimming data is, and `Multi Data/` where the resulting files made from combining the single fish data into artifical "schools" of eight fish are stored. `dummy_data.csv` is used to create the combined schools. If you run `python Fish_Combiner.py` it will randomly combine the data in `Single Fish/` to make full eight fish traces in `Multi Data/`.

### Fish Turning Processor

You can take the CSVs created and placed into `Multi Data/` and move them to `Fish Turning Processor/Single_Fish_Data`. Then you can run `python get_turn_bias_midline.py`. This will create two files, `eight_fish_turning.csv` and `single_fish_turning.csv`. Move them into `Fish Data Analysis/Data` in order for the R code to find them in order to make the graphs and statistics.

## School Kinematics CSV to Paper Graphs and Stats

Now simply open up `Fish Data Analysis.Rproj`. Run everything in `Results_Text.qmd` and `Paper_Figures.qmd`. This will provide you with the stats used in my resutls section, as well as the graphs that I made for the paper. 
