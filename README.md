[![](./images/AI.jpg)](http://ai.stanford.edu/)

CS234: Reinforcement Learning Winter 2019
=========================================

![](./images/RL.png)

[](schedule.html)

Course Schedule

[](assignments.html)

Assignments

[](project.html)

Course Project

[](https://mvideox.stanford.edu/Course/1248)

Lecture Videos

[](calendar.html)

Calendar

[](https://piazza.com/class/jqhdo66vchj6qm)

Piazza Forum

[](scpd.html)

SCPD

[](faq.html)

FAQ

Announcements
-------------

-   Wed, Mar 13th: Please check [Piazza](https://piazza.com/class/jqhdo66vchj6qm?cid=882) for detials about poster session.
-   Wed, Mar 13th: Assignment 3 solution released, please check the [assignment page](./assignments.html).
-   Wed, Feb 14th: Assignment 3 released, please check the [assignment page](./assignments.html).
-   Mon, Feb 11th: Assignment 2 solution released, please check the [assignment page](./assignments.html).
-   Tue, Feb 5th: Practice midterm released, please check [here](./schedule.html)
-   Tue, Feb 5th: To signup for AWS credit (for your prjects) and MuJoCo installation guide (for assignment 3 and your project), pelase check [Piazza](https://piazza.com/class/jqhdo66vchj6qm?cid=72).
-   Tue, Jan 29th: Default final project among with some research project ideas released, please check [here](./default_project/index.html)
-   Tue, Jan 29th: Assignment 1 solution released, please check the [assignment page](./assignments.html). Regrades requests are open for 72 hours, please submit all of your regrade requests through Gradescope
-   Wed, Jan 23rd: Assignment 2 released, please check the [assignment page](./assignments.html).
-   Mon, Jan 14th: Discussion sections starts from Jan 15. Please signup [here](https://piazza.com/class/jqhdo66vchj6qm?cid=72).
-   Wed, Jan 9th: Assignment 1 released, please check the [assignment page](./assignments.html).

See [Piazza](https://piazza.com/class/jqhdo66vchj6qm). You can register independently — there is no access code required to join the group.

Prerequisites for This Class
----------------------------

-   Proficiency in Python
     All class assignments will be in Python (using numpy and Tensorflow and optionally Keras). There is a tutorial [here](http://cs231n.github.io/python-numpy-tutorial/) for those who aren't as familiar with Python. If you have a lot of programming experience but in a different language (e.g. C/ C++/ Matlab/ Javascript) you will probably be fine.
-   College Calculus, Linear Algebra (e.g. MATH 51, CME 100)
     You should be comfortable taking derivatives and understanding matrix vector operations and notation.
-   Basic Probability and Statistics (e.g. CS 109 or other stats course)
     You should know basics of probabilities, Gaussian distributions, mean, standard deviation, etc.
-   Foundations of Machine Learning
     We will be formulating cost functions, taking derivatives and performing optimization with gradient descent. Either CS 221 or CS 229 cover this background. Some optimization tricks will be more intuitive with some knowledge of convex optimization.

Course Instructor
-----------------

[](http://cs.stanford.edu/people/ebrun/)

![](./images/emma_brunskill.jpg)

Emma Brunskill

Course Assistants
-----------------

[](https://rkeramati.github.io)

![](./images/ramtin.jpg)

Ramtin Keramati (Head CA)

[](https://www.linkedin.com/in/anchitgupta)

![](./images/anchit_gupta.jpeg)

Anchit Gupta
  

[](http://web.stanford.edu/~zanette/)

![](./images/andrea_zanette.jpg)

Andrea Zanette
  

[](%20http://jaywhang.com/)

![](./images/jay.jpg)

Jay Whang
  

[](http://www.linkedin.com/in/sudarshanseshadri)

![](./images/ssesha.jpeg)

Sudarshan Seshadri

[](%20https://www.linkedin.com/in/liu-bo-ab8030107/)

![](./images/Bo.jpg)

Bo Liu
  

[](https://www.linkedin.com/in/patrickchochungting/)

![](./images/patrick.jpg)

Patrick Cho
  

[](www.linkedin.com/in/yongshang)

![](./images/yong.jpg)

Yongshang Wu
  

[](https://www.linkedin.com/in/evan-darke-b58482107)

![](./images/evan.jpg)

Evan Darke
  

[](https://www.linkedin.com/in/chelseasidrane/)

![](./images/chelsea_sidrane.jpg)

Chelsea Sidrane
  

Course Description
------------------

To realize the dreams and impact of AI requires autonomous systems that learn to make good decisions. Reinforcement learning is one powerful paradigm for doing so, and it is relevant to an enormous range of tasks, including robotics, game playing, consumer modeling and healthcare. This class will provide a solid introduction to the field of reinforcement learning and students will learn about the core challenges and approaches, including generalization and exploration. Through a combination of lectures, and written and coding assignments, students will become well versed in key ideas and techniques for RL. Assignments will include the basics of reinforcement learning as well as deep reinforcement learning — an extremely promising new area that combines deep learning techniques with reinforcement learning. In addition, students will advance their understanding and the field of RL through a final project.
 You can find last year (Winter 2018) materials [here](./CS234Win2018/index.html).

Learning Outcomes
-----------------

By the end of the class students should be able to:

-   Define the key features of reinforcement learning that distinguishes it from AI and non-interactive machine learning (as assessed by the exam).
-   Given an application problem (e.g. from computer vision, robotics, etc), decide if it should be formulated as a RL problem; if yes be able to define it formally (in terms of the state space, action space, dynamics and reward model), state what algorithm (from class) is best suited for addressing it and justify your answer (as assessed by the project and the exam).
-   Implement in code common RL algorithms (as assessed by the homeworks).
-   Describe (list and define) multiple criteria for analyzing RL algorithms and evaluate algorithms on these metrics: e.g. regret, sample complexity, computational complexity, empirical performance, convergence, etc (as assessed by homeworks and the exam).
-   Describe the exploration vs exploitation challenge and compare and contrast at least two approaches for addressing this challenge (in terms of performance, scalability, complexity of implementation, and theoretical guarantees) (as assessed by an assignment and the exam).

Class Time and Location
-----------------------

Winter quarter (January 07 - March 13, 2019)
 Lecture: Monday, Wednesday 11:30 AM - 12:50 PM
 Location: [Gates B1](https://campus-map.stanford.edu/?srch=gatesb01)

Course Schedule / Syllabus (Including Due Dates)
------------------------------------------------

See the [Course Schedule](schedule.html) page.

Textbooks
---------

There is no official textbook for the class but a number of the supporting readings will come from:

-   Reinforcement Learning: An Introduction, Sutton and Barto, 2nd Edition. This is available for free [here](http://incompleteideas.net/book/the-book-2nd.html) and references will refer to the final pdf version available [here](http://incompleteideas.net/book/RLbook2018.pdf).

Some other additional references that may be useful are listed below:

-   Reinforcement Learning: State-of-the-Art, Marco Wiering and Martijn van Otterlo, Eds. [[link](https://link.springer.com/book/10.1007%2F978-3-642-27645-3)]
-   Artificial Intelligence: A Modern Approach, Stuart J. Russell and Peter Norvig.[[link](http://aima.cs.berkeley.edu/)]
-   Deep Learning, Ian Goodfellow, Yoshua Bengio, and Aaron Courville. [[link](http://www.deeplearningbook.org/)]
-   David Silver's course on Reiforcement Learning [[link](http://www0.cs.ucl.ac.uk/staff/D.Silver/web/Teaching.html)]

Grade Breakdown
---------------

Assignment 1: 10%

Assignment 2: 20%

Assignment 3: 16%

Midterm: 25%

Quiz: 5%

-   Individual: 4.5%
-   Group: 0.5%

Course Project: 24%

-   Proposal: 1%
-   Milestone: 2%
-   Poster Presentation: 5%
-   Paper: 16%
-   **If you choose to do the default project/4th assignment, your breakdown will instead be**
    -   Poster presentation: 5%
    -   Paper/assignment write up: 19%

Late Day Policy
---------------

-   You can use 6 late days.
-   A late day extends the deadline by 24 hours.
-   You are allowed up to 2 late days per assignment. If you hand an assignment in after 48 hours, it will be worth at most 50%. No credit will be given to assignments handed in after 72 hours — contact us if you think you have an extremely rare circumstance for which we should make an exception. This policy is to ensure that feedback can be given in a timely manner.
-   You can use late days on the project proposal (up to 2) and milestone (up to 2). No late days are allowed for the poster presentation and final report. Any late days on the project writeup will decrease the potential score on the project by 25%. To use a late day on the project proposal or milestone, group members cannot pool late days: in order words, to use 1 late day for project proposal/ milestone all gorup members must have at least 1 late day remaning.

Exams & Quizzes
---------------

-   There will be a midterm and quiz, both in class. See the [schedule](schedule.html) for the dates
-   Conflicts: If you are not able to attend the in class midterm and quizzes with an official reason, please email us at [cs234-qa@cs.stanford.edu](mailto:cs234-qa@cs.stanford.edu), as soon as you can so that an accommodation can be scheduled. (Historically this is either to ask you to take the exam remotely at the same time, or to schedule an alternate exam time).
-   Notes for the exams: You are welcome to bring a 1-sided 1 (letter sized) page of handwritten or typed notes to the midterm. For the quiz you are welcome to bring a double sided (letter sized) page of handwritten or typed notes. No calculators, laptops, cell phones, tablets or other resources will be allowed.

Assignments, Course Project and Submission Process
--------------------------------------------------

-   Assignments: See [Assignments page](assignments.html) where all the assignments will be posted.
-   Course Project: See the [Course Project page](project.html) for more details on the course project.
-   Computing Resources: We will have some cloud resources available for assignments 2 and 3 and the project. Instructions for how to access these will be announced prior to Assigment 2.
-   Submission Process: The submission instructions for the assignments and the project can also be found on the [Assignments page](assignments.html).

Office Hours
------------

Emma's office hours will be held in [Gates 218](https://campus-map.stanford.edu/?srch=gates+computer+science). CA's office hours starts from Thursday Januray 10, please See [Calendar](https://calendar.google.com/calendar/embed?src=cs234win1819%40gmail.com&ctz=America%2FLos_Angeles) for time and location.
 For both in-person and online SCPD office hours, you will need to register an account on [QueueStatus](http://queuestatus.com/). When you wish to join the queue, click "Sign Up" at the [CS234-Winter 2019 queue](http://queuestatus.com/queues/314). Be sure to enter your email when you "Sign Up"; this is a way for the CA to contact you. Look for announcements on the left panel for more information. For online office hours, you will need to install Zoom (instructions below) to video call with the CA: the CA will contact you via Zoom when he/she reaches you in the queue.
 Instructions for installing Zoom:

-   Linux
    -   Go to the [Zoom Client for Linux](https://zoom.us/download?os=linux) page and download the correct Linux package for your Linux distribution type, OS architecture and version.
    -   Follow the linux installation instructions [here](https://support.zoom.us/hc/en-us/articles/204206269-Linux-Installation).
-   Mac
    -   Download Zoom installer [here](https://stanford.zoom.us/download).
    -   Installation instructions can be found [here](https://support.zoom.us/hc/en-us/articles/203020795-How-To-Install-on-Mac).
-   Windows
    -   Go to [Stanford Zoom](https://uit.stanford.edu/service/zoom) and select 'Launch Zoom'.
    -   Click 'Host a Meeting'; nothing will launch but this will give a link to 'download & run Zoom'.
    -   Click on 'download & run Zoom' to obtain and download 'Zoom\_launcher.exe'.
    -   Run 'Zoom\_launcher.exe' to install.

Attendance
----------

Attendance is not required but is encouraged. Sometimes we may do in class exercises or discussions and these are harder to do and benefit from by yourself. However, if you are not able to attend class, the class is recorded. It has previously been shown that watching lecture videos in small groups with one person pausing to facilitate discussion can yield student performance as high as attending lectures live. In prior years, some students have watched videos in small groups, so we encourage you to consider this if you are unable to attend a particular lecture or if you’re participating in the class as a SCPD student. I am always excited to hear about new ways students find to effectively learn the material, so sharing such tips is always appreciated.

Communication
-------------

We believe students often learn an enormous amount from each other as well as from us, the course staff. Therefore to facilitate discussion and peer learning, we request that you please use [Piazza](https://piazza.com/class/jqhdo66vchj6qm) for all questions related to lectures, homeworks and projects.
 For SCPD students, if you have generic SCPD specific questions, please email [scpdsupport@stanford.edu](mailto:scpdsupport@stanford.edu) or call 650-741-1542. In case you have specific questions related to being a SCPD student for this particular class, please contact us at [cs234-qa@cs.stanford.edu](mailto:cs234-qa@cs.stanford.edu).
 For exceptional circumstances that require us to make special arrangements, please email us at [cs234-qa@cs.stanford.edu](mailto:cs234-qa@cs.stanford.edu). For example, such a situation may arise if a student requires extra days to submit a homework due to a medical emergency, or if a student needs to schedule an alternative midterm date due to events such as conference travel etc. They will be considered and approved on a case by case basis.
 You will be awarded with up to 2% extra credit if you answer other students' questions in a substantial and helpful way on Piazza.

Academic Collaboration and Misconduct
-------------------------------------

I care about academic collaboration and misconduct because it is important both that we are able to evaluate your own work (independent of your peer’s) and because not claiming others’ work as your own is an important part of integrity in your future career. I understand that different institutions and locations can have different definitions of what forms of collaborative behavior is considered acceptable. In this class, for written homework problems, you are welcome to discuss ideas with others, but you are expected to write up your own solutions independently (without referring to another’s solutions). For coding, you are allowed to do projects in groups of 2, but for any other collaborations, you may only share the input-output behavior of your programs. This encourages you to work separately but share ideas on how to test your implementation. Please remember that if you share your solution with another student, even if you did not copy from another, you are still violating the honor code. In terms of the final project, you are welcome to combine this project with another class assuming that the project is relevant to both classes, given that you take prior permission of the class instructors. If your project is an extension of a previous class project, you are expected to make significant additional contributions to the project.
 We periodically run similarity-detection software over all submitted student programs, including programs from past quarters and any solutions found online on public websites. Anyone violating the Stanford University [Honor Code](https://ed.stanford.edu/academics/masters-handbook/honor-code) will be referred to the Office of Judicial Affairs. If you think you made a mistake (it can happen, especially under stress or when time is short!), please reach out to Emma or the head CA; the consequences will be much less severe than if we approach you.

Students with Documented Disabilities
-------------------------------------

Students who may need an academic accommodation based on the impact of a disability must initiate the request with the Office of Accessible Education (OAE). Professional staff will evaluate the request with required documentation, recommend reasonable accommodations, and prepare an Accommodation Letter for faculty dated in the current quarter in which the request is being made. Students should contact the OAE as soon as possible since timely notice is needed to coordinate accommodations. The OAE is located at 563 Salvatierra Walk (650-723-1066, [http://studentaffairs.stanford.edu/oae](http://studentaffairs.stanford.edu/oae)).

Credit/No Credit Enrollment
---------------------------

If you're enrolled in the class on credit/no credit status, you will be graded on work as usual per standard Stanford rules. The only distinction with those taking the class for letter grade is that you must obtain a C- (C minus) grade or higher in the class, for you to be marked as CR. In practice, potential options to achieve this would be such as (a) doing well on all assignments, the exam and the quiz, but no completing a project, or (b) doing a C- average on all aspects of the course or (c) doing poorly on the exam but doing well on all the assignments and a project.

Webdesign by Andrej Karpathy
 Header image from Sutton, Richard S., and Andrew G. Barto. Reinforcement Learning: An Introduction.
