### Inspiration


According to the researchers, creativity is our ability to think in new and original ways to solve problems. But not every original solution is considered a creative one. If the idea is not fully applicable it is not considered creative, but simply one which is unreasonable. Within a short period of time at the hackathon it is extremely hard to come up with a reasonable idea and implement it through cutting-edge technology quickly. Thus, our team decided to find a solution to support the hackers to have a reasonable starting point.

Based on our research, we have realized the best way to have a new idea is to build upon the existing ones and introduce additional "randomness" to improve it. Following such logic, we designed this tool to help the user quickly understand the basis of the topic he/she is interested in. Then the engine introduces additional information with an expectation to support users think out of the box and be able to create new ideas.

### What it does


The tool will generate keywords and dataset to inspiring users. It provides companies, approaches, dataset, technology to users to form a solid starting point

### How I built it


For the two word-clouds, we have the following data source through web scrapping and API extraction:

### Technology from Devpost on the past hackathon


Scientific approaches from research articles (1000) with a sanity check on authority websites
Name of cutting-edge enterprise within the field and startups
Related dataset from Kaggle Then we present the data with an inspiring and creative way to encourage users to perform further thinking and eventually conclude to a topic
Challenges I ran into
First, we had a hard time to decide what topic to pursue ourselves since there are so many topics to choose from, and that is how we started to build this generator Then we have to decide what data and information should be included that we can reach the balance of presenting enough background but at the same time don't limit creativity In addition, we need to ensure the information we have gathered is not random or duplicated, which lead to our manually check the output and implement additional constraints to ensure the quality of our suggestions

### Accomplishments that I'm proud of


Scalability: This tool is capable of gathering correlated data and represent them in a way to inspire others, and the concept could be re-used broadly with consideration of different dataset. Usefulness: This tool will be highly leveraged since it is designed for better usage

### What I learned


Web Scrapping, API calls, NLP and massive text processing concept

### What's next for HacktheHack


Work with more visually appealing libraries (like bqplot) for better visualization of the final output Leverage IBM Watson to better gather the topics and provide suggestions to users on what are the most related social issues or concerns to start with

### How to use to use it

Simply run the notebook hackathon_princeton_v1.ipynb, you will be able to get the idea you want

Example of main ideas extracted from scientific research paper:


![alt text](https://github.com/aksmit94/HackPrinceton/blob/master/Screen%20Shot%202018-11-11%20at%2011.42.05%20AM.png)

Example of approaches and technologies:


![alt text](https://github.com/aksmit94/HackPrinceton/blob/master/Screen%20Shot%202018-11-11%20at%2011.42.22%20AM.png)

