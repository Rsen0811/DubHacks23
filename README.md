# DubHacks23 - ReJuve

Our Goal:
We at ReJuve aim to help you revitalize, rejuvenate, and reclaim your mental health through the power of information. You can now learn about better mental health habits at your own convenience. Take a diagnosis test now to see your score, it is your journey to mental wellness, inner peace, and spiritual balance.

Our Idea:
We created a questionaire-type page to gather information about the user, and using a dataset about young people from Kaggle.com, we utilized machine learning to calculate a mental health score and give you feedback in the form of a website page. With 8 different categories, they all come together to detect points in your life that may need some assistance. For example, a user might reply "Drinking Often" to a question about alcohol, and a model will compare your response to other datapoints, then giving you advice and feedback on a potential category like loneliness. 

Our Methods:
We utilized a series of K-Nearest Neighbor models to map the similarity between test subjects and the user to score them with the values that was most mathematically similar to them. The models came from the Scikit Learn library in Python. We then pushed each value into an array and printed different messages based on the scores for each category. We used Websockets to transfer the data from a backend Python server to use for the website. Our frontend was built with HTML and CSS, as well as JavaScript for the calculations and button functionality.


                                                       _
                                                     _(_)_                          wWWWw   _
                                         @@@@       (_)@(_)   vVVVv     _     @@@@  (___) _(_)_
                                        @@()@@ wWWWw  (_)\    (___)   _(_)_  @@()@@   Y  (_)@(_)
                                         @@@@  (___)     `|/    Y    (_)@(_)  @@@@   \|/   (_)\
                                          /      Y       \|    \|/    /(_)    \|      |/      |
                                        \ |     \ |/       | / \ | /  \|/       |/    \|      \|/
                                       \\|//   \\|///  \\\|//\\\|/// \|///  \\\|//  \\|//  \\\|// 
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                      Hackers: Rajat Sengupta, Karson Shin, Megan Pham, Yuning Hu
