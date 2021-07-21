# Lindsey's Summary of the Course (and Smattering of Advice)

Slides version can be found [here](https://docs.google.com/presentation/d/1rN5WQuEiuwAD-sTDzJ8RzPqI8MlfFOgXmgShjdE6V3k/edit?usp=sharing).

## Guiding Principles

### Be skeptical

- Don’t accept anything the first time you hear it - examine it and be careful
- Question everything (that can be tedious, but worthwhile)

### Where’s the business value?

- When working at a job, always keep this question at the forefront of your mind
- Don’t lose sight of what’s important - the people who pay you will thank you for that
- Will help you keep focus on the things that are valuable (metrics, features, what have you)
- Sub questions to consider:
    - How do we make money? (thus, how can that be maximized?)
    - How do we lose money? (where can we optimize, and what can we minimize?)
    - How else can we make money? (what other revenue streams are out there and low-hanging fruit? this is potentially the best option to add value)

### Work smarter not harder

- Simplify the problem - could look like making a non-classification task into a binary classification problem (probably easier)
- Get a quick and dirty baseline - see how hard the problem is
- Fail fast - which means iterating quickly
- Do your research - this should probably be at the top of this list! Don’t reinvent the wheel

### Be comfortable not knowing

- Easier said than done
- You spend 90% of your time in the dark (not knowing) in data science, until you really get comfortable in an industry or in a role
- Accept the fact that you’re going to screw this up sometimes - don’t beat yourself up over it, just learn from your mistakes

### Be honest

- With yourself and with others
- If you can do that AND be kind (both with yourself and with others) then you’re winning - it’s hard to do both
- Don’t pretend you know something if you don’t, especially to yourself
- Don’t waste your time or theirs

### Give back

- Pay it forward
- Appreciate the help you’ve received, and if you can do that for someone else (and can save someone from making the same mistakes you made) then it is always worthwhile

### Be a lifelong learner 

- Even on the things you think you know well - be willing to go back and learn things you think you already know, but learn them in a new way - that’s how you become an actual expert
- Try to hold on to the Beginner's Mindset - be a sponge, ask lots of questions, be relentless as you learn new things

## The Data Science Process (Oversimplified)

### Get your data

- Sometimes, this is the hardest part. Other times, you get lucky

### Understand your data

- If getting your data isn’t the hardest part, this will be
- You can spend a lot of your time here - find ways to make this process quicker
    - Simple, baseline-guided EDA can help a lot
    - Subject matter experts can help even more
    - Do your research - which sometimes means getting creative to find equivalent processes

### Understand your problem

- Easily the most important thing on this list
- Ideally you’d do this first, but you often can’t until you’ve done steps 1 & 2
- Don’t assume that the person giving you the task knows the actual problem
- Don’t forget to ask “Where’s the business value” - be sure you know the value of the problem and the solution you might arrive at
    - Focusing on this practical part helps guide you to a solution quicker/easier

### Model

- “The easy part”

### Understand your model

- Know what kinds of models there are, know what they do well, know when they break
- Many places don’t like black boxes - for regulatory reasons if nothing else
- Check the biases that may have snuck into your model (gender, race, etc.)
    - Examine the strategies used to make your model - did you only feed your model data about white men, for example?
    - Did you use sensitive data, or proxies for that? Are the proxies important or just biasing your results?
    - If you can predict someone’s race or gender using the same data you fed your model, then it might be racist or sexist
- If you use interpretable features and interpretable models, then this part might be easy

### Govern your model

- We haven’t talked about this part at all in this course
- ‘All models are wrong - but some of them are useful’
- Your model is bound to fail, or not work after a certain point or in certain contexts - pay attention to those things
    - One way to check? PSI: population stability index (there’s a python package for this - checks if the distributions of the testing data for the most important features in the model are similar to the distributions of the training data)

### Productionalize your model

- Typically isn’t the data scientist’s job… but it could be
- Do unit testing, scale testing (on a sample, start small and manageable)
- Check or implement your data pipeline, logging, communication/alerts
- Tools you’ll need to potentially learn if this does become your job: Kubernetes, Docker, Kafka, Airflow, Snowflake, etc. - and learn C++, .NET, Java, etc.
- Even if it’s not your job to do these things, learn from your data engineers (exchange knowledge, these are valuable skills - it’s always nice to become a unicorn that can do everything)

## What's Next?

- Beyond the stuff given to you by career services or in the post-work, ask yourself:
    - What did you learn in this program that needs additional work or practice?
    - What DIDN’T you learn in this program?
    - What advice can you get from other data scientists?
    - What advice can you get from the people who hire data scientists?
- Reminder: [my Ultimate Resources Folder](https://drive.google.com/drive/folders/1WJgVgaiQ2UXb8R31wDJILmlCPUYabjLq)
    - [The 1Resource Links Doc](https://docs.google.com/document/d/1iSmgwGfSqtvMMY-lo1bjKTVAmDHY1WWEfUJJ3yumlBw/edit#heading=h.s1hcacbv4upi) has a section on Career Advice under Et Cetera - including some podcast episodes by people who hire data scientists!

## Other Pieces of this Puzzle

### Good features make good models!

- Nicer way of saying "garbage in, garbage out"
- How the heck do we find those??
    1) Interactions - how do we find those?
        - Decision tree proxies to find simple if-then logic binary indicators
        - Subject matter expertise - formulae (polynomials)
        - Don’t overlook the simple stuff - do group-by aggregations on your data
        - Let a genetic algorithm learn interactions for you (neural net, anything that can learn features)
    2) Encodings and embeddings
        - Finding a good strategy can make a world of difference
        - Example Encodings: target, leave-one-out, weight of evidence, frequency, count
        - Example Embeddings: manifold learning, one-hot (a sparse embedding), or use the outputs of decision trees or even neural nets as new features (embedding through other models)
    3) Feature selection - try a lot of methods, but don’t rely solely on one, they all can often be wrong - this is one of the hardest things to do at all (and especially to do well)
        - Filtering methods - like information value
        - Regularization (L1 - LASSO) - but this will fail with correlated features or certain types of features
        - Tree impurities/splitting can give you importances
        - Permutation/leave-one-feature-out importances

### Cross-validation is your friend

- Look at many different metrics, and different testing methods
- Be skeptical - keep testing
- If you can use evaluation to detect what your problem is in your model, even if you can’t fix it you can find better solutions through that knowledge - use the results of your cross validation to sense when you need more/better features, and to know when you’re “done”

### Set Clear Goals

- It’s easier to pick out a model if you understand your data and you understand your problem
- Also helps tell you when something is "good enough"

## It will feel like a lot for a while. Just keep at it, be persistent, expect that roadblocks are coming, and you’ll eventually get better. Try not to get frustrated and be kind to yourself.