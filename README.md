# pre-trained-image-classifier-to-identify-dog-breeds
The project involves classifying images of dogs for a city dog show. 📸🐕‍🦺🎪 The goal is to use a pre-trained image classifier to identify dog breeds, ensure that the participants’s submissions are indeed dogs, and determine the best classifier based on accuracy and runtime among different architectures AlexNet, VGG, and ResNet.📊


•The classifiers were evaluated based on their ability to correctly identify dog breeds and distinguish between dog and non-dog images. The analysis considered the following metrics: matches, NOT matches, percentage correct dog, percentage correct not dog, percentage correct breed, runtime, and overall match percentage.

•ResNet achieved the highest overall match percentage at 75%, with perfect accuracy in identifying both dogs and non-dogs within a moderate runtime of 4 seconds. AlexNet had the shortest runtime of 1 second but a lower overall match percentage of 50%, primarily due to its lower accuracy in identifying non-dogs (50%). VGG also had an overall match percentage of 50% with a runtime of 6 seconds, achieving perfect accuracy in both dog and non-dog identification.

•The visualizations provide a summary of the classifier performance in terms of matches, percentage correct dog vs not dog, percentage correct breed, and runtime.

Based on the performance across different datasets and consistency, VGG might be preferred due to its slightly better performance in breed classification in the larger dataset. ResNet offers a good balance between accuracy and runtime, making it a strong contender as well. AlexNet, while being the fastest, had lower accuracy in identifying non-dogs.

 
![precision_recall_curve](https://github.com/user-attachments/assets/3ade11a6-9d4d-4309-81ae-58d5ba6f11c8)
![performance_over_time](https://github.com/user-attachments/assets/ed1c40d9-555f-4819-b83a-b5efd5b64309)
![confusion_matrix](https://github.com/user-attachments/assets/2e35ffae-006f-493f-9c3d-adfe6790aff4)
