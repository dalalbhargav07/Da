#  Analyzing data patterns and different classification methods

Identified the patterns through simulation of data. Data was initially cleaned and processed. The processed data was explored and anlysed using various plots. Finally, based on the analysis patterns were identified using machine learning algorithms applied using sklearn.

### Report for the project
Report can be found [here](https://github.com/dalalbhargav07/Data-Warehousing-to-Data-Analytics/blob/master/Exploring%2C%20Anlaysing%20and%20Classification%20of%20the%20dataset/Report.pdf).

### Installation

Installation steps are for Ubuntu 16.04 version.


#### Installation of packages on python 3.x.x
Python is pre-installed on the server instance. You can check it by the below command:
```sh
$python3 -V
```
If python is not installed, here is the link to install python3.x on ubuntu - [Python3.x.x installation](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04)

1. Installing pip package:
```sh
$ sudo apt-get install -y python-pip
```
2. Install scikit-learn:
```sh
$ pip install scikit-learn  
```
3. Install pandas:
```sh
$ pip install pandas  
```
Now the environment is ready.
### Running python files
1. run TruncateSVD_plot.py file and make sure you have train.txt file in the same folder. You may need to unzip train.txt from "Data" folder.
    - This file would give a pairplot which will explain how feature dimensions affect the data.
2. run feature_selection file and make sure you have both the train.txt and test.txt file in the same folder. You may need to unzip test.txt from "Data" folder.
    - This would give out accuracy for each model.
3. run ReportJupyter.ipynb in jupyter notebook
    - This is a file which would give a detailed report of our analysis. 
##### Note: If you do not have jupyter notebook installed, please download Anaconda Navigator [Available here](https://www.anaconda.com/download/).
