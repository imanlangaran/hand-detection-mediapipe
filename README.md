# hand detection using mediapipe and sending data to arduino 

## detecting hand
I've used [mediapipe](https://google.github.io/mediapipe/) library to get the landmarks of each hand
And i used the angle of each finger to count it

## sending data to arduino
I've used the serial library to connect to hardware through communication port 
And i used threading library to have a loop with an interval that sends the latest data

## arduino code
In arduino code i've just got the raw data and extracted two numbers between 0 and 5 and disolay it on sevensegments
