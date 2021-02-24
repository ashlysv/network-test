#!/bin/bash


date_check(){

if [ "$DAT" = "" ] || [ "$DAT" = NULL ] ; then

        echo "Date is Empty. Assigning today's date."
        DAT=$(date +"%Y-%m-%d")

#elif [ "$DAT" != ^[0-9]{4}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1]) ] ; then
#
#       echo "Wrong Time Format. Assigning today's Date"
#       DAT=$(date +"%Y-%m-%d")

fi

}

technology_check(){

 if [ "$technology" = "Fib" ] || [ "$technology" = "oP" ] then
 	 echo "Enter Date:[yyyy-mm-dd hh:mm:ss]"
	 read DAT
         date_check
         echo "Count of $technology request on $DAT : "
         grep 'checkservice: CMD:check service' ~/var/log/servicecheck.log*  |grep "$technology" |grep "$DAT" |wc -l


 elif [ "$technology" = "ALL" ] ;
  then
	echo "Enter Date:[yyyy-mm-dd hh:mm:ss]"
        read DAT
        date_check
        echo "Count of All request on $DAT : "
        grep 'checkservice: CMD:check service' ~/var/log/servicecheck.log* |grep "$DAT" |wc -l

 else
        echo " Please follow the format for technology"
        exit
 fi

}

save_file(){

   echo "Enter file name : "
   read filename

   if [ "$technology" = "ALL" ] ; then
        grep 'checkservice: CMD:check service' ~/var/log/servicecheck.log* | grep "$DAT" >/tmp/$filename
   
   else
        grep 'checkservice: CMD:check service' ~/var/log/servicecheck.log* | grep "$technolgy" | grep "$DAT" >/tmp/$filename
   
   fi

   echo "File saved in /tmp/ directory "

}


echo "Enter Technology: "
read technology
technology=$(echo $technology | tr 'a-z' 'A-Z')

technology_check

echo "Do you wish to save the details in a file (Y/N)"
read response
response=$(echo $response | tr 'a-z' 'A-Z')

if [ "$response" == "Y" ] ;
  then
        save_file
else
        echo " Thank you"

fi


