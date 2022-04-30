Challenge - GOT Snapchat Filter?
GOT Snapchat Filter?
Making cool face filters for GOT Characters & yourself!
In this problem, you will be building snapchat like face filters - eyeglasses and moustache for popular Game Of Throne Characters Tyrion Lannister and Jaime.

You will be given an input image and two image templates(one for sunglasses & moustache , you task is to overlay the eyeglasses and moustache on the given character. A sample input output is show below. To detect the facial keypoints like position of eyes and nose, we also provide you with haarcascade xml files in the training data.

![alt text](https://minio.codingblocks.com/amoeba/jamie.jpg)

Bonus - Try to place these filters in LIVE stream taken from your webcam and display it :)

Submission Format For the given input image, submit a CSV file where each ith row contains the BGR pixel values for the ith pixel of modified image.

Scoring
Total score will be based upon percentage of pixel values correctly predicted. You should flatten the image into shape(-1,3) before creating CSV.
