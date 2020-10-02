import pprint
pp = pprint.PrettyPrinter(indent=3 ,depth=6,width=100)
import pickle

def add_compsdata():
    comps = { "comps" :{
    "Faculty" : {
        "Dr.Deepak Sharma is the Head of Department"
        "The Computer Department has a total of 30 faculty members consisting of highly skilled professors and assistant professors"
        "For more information you can visit the given link!"
        "<a href='https://kjsce.somaiya.edu/en/contact-us/faculty-directory'></a>"
        #"https://kjsce.somaiya.edu/en/contact-us/faculty-directory"
    },
    "infrastructure" :{ 
        "The Department houses classrooms and laboratories with modern infrastructure to facilitate their learning. The Teaching-Learning-Evaluation paradigm is a mix of traditional as well as active learning pedagogy and use of contemporary Information and communications technology (ICT) tools. The academic ambience encourages research, development and innovation activities."
        "For detailed information please visit the following link!"
        "<a href='https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-computer-engineering'>Infrastructure</a>"
        #"https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-computer-engineering"
    },
    "syllabus" : {
        "The syllabus is designed having wide choice for branch specific electives and more number of open or interdisciplinary electives."
        "Extensive use of Open Sources Technologies for Teaching – Learning – Evaluation"
        "Choice based Audit Courses, Add on Credit Courses, Add on Audit Courses, Exposure Courses, etc"
        "<a href='https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-computer-engineering'>syllabus</a>"
        #"https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-computer-engineering"
    },
    "placement" : {
        "The Placement Process at KJSCE acts as a link between the expectations of the Recruiters with the dreams of the students. "
        "In year 2019-2020, we had 84 Companies visiting for recruitment."
        "The highest package received was Rs.18.75 lpa and overall average of Rs.5.55 lpa with over 600+ successfull placements."
        "For more information please visit the following link!"
        "<a href='https://kjsce.somaiya.edu/en/placement/overview'>placement</a>"
        #"https://kjsce.somaiya.edu/en/placement/overview"
    },
    "student" : {
        "We at the K J Somaiya College of Engineering continuously strive to excel in academic along with various Co-curricular and extra-curricular activities. Extracurricular activities are not the components of the academic curriculum but an integral part of the educational environment for the intellectual development of an engineer. It will explore hidden talent inside you, it will make you more adaptive and flexible and help you to become a smart engineer not only just an engineering graduate."
        "Codecell - KJSCE Codecell, a Codechef campus chapter was founded in 2014. The main goals of K J Somaiya College of Engineering Codecell are to promote a culture of competitive coding and to improve participation of the college in the prestigious competition ACM ICPC."
        "CSI - The Computer Society of India established in the year 1965 is today the largest IT professionals’ society in India. Keeping in mind the interest of IT professionals & computer users, CSI works towards making a profession an area of choice among all sections of society."
        "For information regarding all the councils and student organisations please visit the following link:"
        "<a href='https://kjsce.somaiya.edu/en/students-association'>student_body</a>"
        #"https://kjsce.somaiya.edu/en/students-association"
    },
    "programes":{
        "Computer engineers are involved in the design of Computer-based systems to address highly specialized and specific application needs. The Department of Computer Engineering facilitates students to apply principles of Computer technology across a wide variety of fields for adapting to ever changing multidisciplinary converging technologies."
        "For detailed information about the programmes offered please visit the following link:"
        "<a href='https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-computer-engineering'>programes</a>"
        #"https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-computer-engineering"
    },
    "admissions" :{
        "For admission , intrested student are required to give Somaiya Entrance Test-Engineering(SET-E)."
        "We are delighted that you are considering an B.Tech programme at K J Somaiya College of Engineering. Please read all instructions and requirements carefully to ensure a complete and correct application on the provided link:"
        "<a href='https://kjsce.somaiya.edu/en/admission/btech'>admission</a>"
        #"https://kjsce.somaiya.edu/en/admission/btech"
        "Feel free to contact us on admission.engg@somaiya.edu in case of any queries."
    }
        
            }
             
            }
    
    return comps

def add_etrxdata():
    ETRX = { "etrx" :{
    "Faculty"  :{
        "Dr.Jagannath H Nirmal is the Head of Department."
        "The Electronics Department has a total of 28 faculty members consisting of highly skilled professors and assistant professors who possess proficiency in both hardware and software areas. "
        "For more information you can visit the given link :- "
        "<a href='https://kjsce.somaiya.edu/en/contact-us/faculty-directory'>Faculty</a>"
        
    },
    "infrastructure" :{
        "The electronics department has multiple fully equipped laborataries with state of art instruments for the students to have hands on experience in domains like Automation, Robotics,Machine Learning, Embedded systems, IOT with no hardware limitations."
        "For detailed information please visit the following link!"
        "<a href='https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-electronics-engineering'>infrastructure</a>"
        #"https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-electronics-engineering"
    },
    "syllabus" : {
        "The syllabus of Electronics department has a focused curriculum with a rigor towards hands-on experience and industry exposure. The syllabus is designed in consultation with Industrial experts and academia, to address the current industrial and social needs." 
        "Facility Centre with Festo for Industrial Automation and with National Instruments LabView are the key elements."
        "Curriculum mapped to address current challenges with industry, designed through academia, industry and students participation"
        "Focuses on a wide variety of core courses, electives including cutting edge technologies like Artificial Intelligence, Big Data Analytics, Machine Learning, IoT and more."
        "For information about the detailed structure of syllabus and the subjects included, visit the link provided below!"
        "<a href='https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-electronics-engineering'>syllabus</a>"
        #"https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-electronics-engineering"
    },
    "placement" : {
        "The Placement Process at KJSCE acts as a link between the expectations of the Recruiters with the dreams of the students. "
        "In year 2019-2020, we had 84 Companies visiting for recruitment."
        "The highest package received was Rs.18.75 lpa and overall average of Rs.5.55 lpa with over 600+ successfull placements."
        "For more information please visit the following link!"
        "<a href='https://kjsce.somaiya.edu/en/placement/overview'>placement</a>"
        #"https://kjsce.somaiya.edu/en/placement/overview"
    },
    "student" : {
        "We at the K J Somaiya College of Engineering continuously strive to excel in academic along with various Co-curricular and extra-curricular activities. Extracurricular activities are not the components of the academic curriculum but an integral part of the educational environment for the intellectual development of an engineer. It will explore hidden talent inside you, it will make you more adaptive and flexible and help you to become a smart engineer not only just an engineering graduate."
        "EESA - The Electronics Engineers Students’ Association was established in the year 1988. The association promotes activities such as paper presentations, quizzes, seminars, etc.It arranges for preparatory guidance lectures and also conducts mock tests and group discussions for CAT, GRE etc."
        "ISTE - The ISTE Student Chapter (MH 60) was established in 2000-2001 and it was inaugurated on Wednesday, 24th January 2001 by the Chief guest Shri Pratap Borde, Principal, MGM’s JNCOE, Aurangabad."
        "For information regarding all the councils and student organisations please visit the following link:"
        "<a href='https://kjsce.somaiya.edu/en/students-association'>student body</a>"
        #"https://kjsce.somaiya.edu/en/students-association"
    },
    "programes" :{
        "The curriculum offers a variety of audit courses, multi-disciplinary and core Electives. Faculty Members are trained in ICT Tools, pedagogy features, and innovative assessment methods along with sound technical base."
        "Students gather a variety of learning experiences, where concepts are taught to the students through simulations, models, peer learning, personalized adaptive learning, etc. transforming students into industry-ready, competent Professionals."
        "For more details please visit the following link!"
        "<a href='https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-electronics-engineering'>programes</a>"
        #"https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-electronics-engineering"
    },
    "admissions" :{
        "For admission , intrested student are required to give Somaiya Entrance Test-Engineering(SET-E)."
        "We are delighted that you are considering an B.Tech programme at K J Somaiya College of Engineering. Please read all instructions and requirements carefully to ensure a complete and correct application on the provided link:"
        #"https://kjsce.somaiya.edu/en/admission/btech"
        "<a href='https://kjsce.somaiya.edu/en/admission/btech'>admission</a>"
        "Feel free to contact us on admission.engg@somaiya.edu in case of any queries."
    }
        
    }
            
           }
    return ETRX

def add_extcdata():
    EXTC = {"extc" :{
    'Faculty' : {
        "Dr. Ameya K. Naik is the Head of Department." 
        "The EXTC departement has a total of 29 faculty members consisting of highly skilled professors and assistant professors who possess proficiency in both hardware and software areas."
        "For more information you can visit the given link!"
        "<a href='https://kjsce.somaiya.edu/en/contact-us/faculty-directory'>faculty</a>"
        #"https://kjsce.somaiya.edu/en/contact-us/faculty-directory"
    },
    "infrastructure": {
        "The department of electronics and telecommunications has multiple fully equipped laborataries with state of art instruments"
        "Hands on learning through laboratory experiments to develop knowledge, skills, and values from direct experiences beyond traditional academic course."
        "For more information please visit the following link!"
        "<a href='https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-electronic-telecommunication'>infrastructure</a>"
        #"https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-electronic-telecommunication"
    },
    "syllabus" : {
        "The curriculum is designed to develop technical and interpersonal skills offering wide choice for every learner."
        "Curriculum mapped to address current challenges with industry, designed through academia, industry and students participation"
        "Focuses on a wide variety of core courses, electives including cutting edge technologies like Artificial Intelligence, Big Data Analytics, Machine Learning, IoT and more."
        "For detailed information about the curriculum please visit the following link!"
        "<a href='https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-electronic-telecommunication'>syllabus</a>"
        #"https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-electronic-telecommunication"
    },
    "placement": {
        "The Placement Process at KJSCE acts as a link between the expectations of the Recruiters with the dreams of the students. "
        "In year 2019-2020, we had 84 Companies visiting for recruitment."
        "The highest package received was Rs.18.75 lpa and overall average of Rs.5.55 lpa with over 600+ successfull placements."
        "For more information please visit the following link!"
        "<a href='https://kjsce.somaiya.edu/en/placement/overview'>placement</a>"
        #"https://kjsce.somaiya.edu/en/placement/overview"
    },
    "student" : {
        "We at the K J Somaiya College of Engineering continuously strive to excel in academic along with various Co-curricular and extra-curricular activities. Extracurricular activities are not the components of the academic curriculum but an integral part of the educational environment for the intellectual development of an engineer. It will explore hidden talent inside you, it will make you more adaptive and flexible and help you to become a smart engineer not only just an engineering graduate."
        "IETE - The Institute of Electronics & Telecommunication Engineers - Institute Students’ Forum, ( IETE – KJSISF ) , started in the year 2001."
        "EESA - The Electronics Engineers Students’ Association was established in the year 1988. The association promotes activities such as paper presentations, quizzes, seminars, etc.It arranges for preparatory guidance lectures and also conducts mock tests and group discussions for CAT, GRE etc."
        "For information regarding all the councils and student organisations please visit the following link:"
        "<a href='https://kjsce.somaiya.edu/en/students-association'>student body</a>"
        #"https://kjsce.somaiya.edu/en/students-association"
    },
    "programes" :{
        "Electronics and Telecommunication Engineering department at K. J. Somaiya College of Engineering is committed to develop competent engineers ready to solve real world problems related to the field of electronics and communications. The department has always been on a high growth path and has experienced and dedicated faculty members with a strong devotion in the field of engineering education. The major areas of faculty expertise include Basic Electronics, Communication Systems, Computer Networks, Control Systems, Digital Signal Processing, Image Processing, Computer Vision, Instrumentation, Signal Processing, RF & Microwaves and VLSI Systems."
        "For more information please visit the following link!"
        "<a href='https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-electronic-telecommunication'>programes</a>"
        #"https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-electronic-telecommunication"
    },
    "admissions" :{
        "For admission , intrested student are required to give Somaiya Entrance Test-Engineering(SET-E)."
        "We are delighted that you are considering an B.Tech programme at K J Somaiya College of Engineering. Please read all instructions and requirements carefully to ensure a complete and correct application on the provided link:"
        #"https://kjsce.somaiya.edu/en/admission/btech"
        "<a href='https://kjsce.somaiya.edu/en/admission/btech'>admission</a>"
        "Feel free to contact us on admission.engg@somaiya.edu in case of any queries."
    }
        
    }
            
           }
    
    return EXTC

def add_ITdata():
    IT = {"it" : {

    "Faculty" : {
        "Dr. IRFAN A SIDDAVATAM is the Head of Department."
        "The IT Department has a total of 29 faculty members consisting of professors and assistant professors with high technical qualifications and industry required skills."
        "For more information please visit the given link!"
        "<a href='https://kjsce.somaiya.edu/en/contact-us/faculty-directory'>Faculty</a>"
        #"https://kjsce.somaiya.edu/en/contact-us/faculty-directory"
    },
    "infrastructure" :{
        "The department of Information Technology has sophisticated cutting edge laboratories with the latest infrastructure for parallel computing, cloud computing, Penetration Testing and Internet of Things provide quality academic experience for students."
        "For more information please visit the given link!"
        "<a href='https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-information-technology'>infrastructure</a>"
        #"https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-information-technology"
    },
    "syllabus" :{
        "Academia Curricula benchmarked with International Institutes of repute. Stream-based choices of electives in the curriculum help focused skill development and flexible credit courses for students opting higher studies abroad. Exposure to audit courses, Interdisciplinary courses, trending lab course makes a student ready for dynamically changing industry."
        "IT involves development of applications that churns and infers every data point in the diversified domain of Data Science, Artificial Intelligence, Cyber Security, Cloud Computing, Blockchain Technology, Application Development, IOT, etc. IT department is mandated towards focused delivery of the content by aligning curriculum and infrastructure to cater to emerging industry needs."
        "For more information please visit the given link!"
        "<a href='https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-information-technology'>syllabus</a>"
        #"https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-information-technology"
    },
    'placement' :{
        "The Placement Process at KJSCE acts as a link between the expectations of the Recruiters with the dreams of the students. "
        "In year 2019-2020, we had 84 Companies visiting for recruitment."
        "The highest package received was Rs.18.75 lpa and overall average of Rs.5.55 lpa with over 600+ successfull placements."
        "For more information please visit the following link!"
        "<a href='https://kjsce.somaiya.edu/en/placement/overview'>placement</a>"
        #"https://kjsce.somaiya.edu/en/placement/overview"
    },
    'student': {
        "We at the K J Somaiya College of Engineering continuously strive to excel in academic along with various Co-curricular and extra-curricular activities. Extracurricular activities are not the components of the academic curriculum but an integral part of the educational environment for the intellectual development of an engineer. It will explore hidden talent inside you, it will make you more adaptive and flexible and help you to become a smart engineer not only just an engineering graduate."
        "Codecell - KJSCE Codecell, a Codechef campus chapter was founded in 2014. The main goals of K J Somaiya College of Engineering Codecell are to promote a culture of competitive coding and to improve participation of the college in the prestigious competition ACM ICPC."
        "Bloombox - BloomBox is the entrepreneurship cell at K J Somaiya College of Engineering."
        "For more information you can visit the given link!"
        "<a href='https://kjsce.somaiya.edu/en/students-association'>student body</a>"
        #"https://kjsce.somaiya.edu/en/students-association"
    },
    'programes' :{
        "IT involves development of applications that churns and infers every data point in the diversified domain of Data Science, Artificial Intelligence, Cyber Security, Cloud Computing, Blockchain Technology, Application Development, IOT, etc."
        "IT department is mandated towards focused delivery of the content by aligning curriculum and infrastructure to cater to emerging industry needs."
        "Department aims at strengthening and preparing students for lifelong learning, research and successful adaptation of ever changing technology, which helps them to develop an ability to analyze, design and provide novel IT solutions for engineering problems."
        "For more information you can visit the given link!"
        "<a href='https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-information-technology'>programes</a>"
        #"https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-information-technology"
    },
    'admissions':{
        "For admission , intrested student are required to give Somaiya Entrance Test-Engineering(SET-E)."
        "We are delighted that you are considering an B.Tech programme at K J Somaiya College of Engineering. Please read all instructions and requirements carefully to ensure a complete and correct application on the provided link:"
        #"https://kjsce.somaiya.edu/en/admission/btech"
        "<a href='https://kjsce.somaiya.edu/en/admission/btech'>admissions</a>"
        "Feel free to contact us on admission.engg@somaiya.edu in case of any queries."
    }
        
    }
          
         }
    
    return IT


def add_mechdata():
    Mech = {'mech':{
   'Faculty' : {
        "Dr. Ramesh R Lekurwale is the Head of Department."
        "The Mechanical Department has a total of 30 faculty members consisting of highly skilled professors and assistant professors with a good practical experience of the industry."
        "For more information you can visit the given link!"
        "<a href='https://kjsce.somaiya.edu/en/contact-us/faculty-directory'>Faculty</a>"
        #"https://kjsce.somaiya.edu/en/contact-us/faculty-directory"
    },
    'infrastructure' : {
        "The department of Mechanical Engineering has state of art laboratories and workshops where students can work on industry level projects with help of trained professoes and lab assistants."
        "Special workshops are alloted to different teams like ROBOCON , Red shift Racing, Orion Racing where students can work after college hours on projects with full access to all the equipments."
        #"https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-mechanical-engineering"
    },
    'syllabus' : {
        "The syllabus includes multiple technical subjexts covering complete repertoire of skills necessary for overall development in field of Mechanical Engineering with workshops on emerging areas, industry based UG projects as per thrust areas ."
        "Projects are converted as Lab experiments. Virtual Lab Experiments and variety of internal assessment techniques such as, Open book test, MCQ, Research Presentations, Case studies, Mini Projects and many more Funded projects."
        "For more information please visit the following link!"
        "<a href='https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-mechanical-engineering'></a>"
        #"https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-mechanical-engineering"
    },
    'placement' :{
        "The Placement Process at KJSCE acts as a link between the expectations of the Recruiters with the dreams of the students. "
        "In year 2019-2020, we had 84 Companies visiting for recruitment."
        "The highest package received was Rs.18.75 lpa and overall average of Rs.5.55 lpa with over 600+ successfull placements." 
        "For more information please visit the following link!"
        "<a href='https://kjsce.somaiya.edu/en/placement/overview'></a>"
        #"https://kjsce.somaiya.edu/en/placement/overview"
    },
    'student':{
        "We at the K J Somaiya College of Engineering continuously strive to excel in academic along with various Co-curricular and extra-curricular activities. Extracurricular activities are not the components of the academic curriculum but an integral part of the educational environment for the intellectual development of an engineer. It will explore hidden talent inside you, it will make you more adaptive and flexible and help you to become a smart engineer not only just an engineering graduate."
        "MESA - The Mechanical Engineering Students’ Association, a student organization, was founded in the year 2000.G-Force, the annual tech fest held by MESA serves as an opportunity for students to showcase their talents and technical skills."
        "For more information you can visit the given link!"
        "<a href='https://kjsce.somaiya.edu/en/students-association'>student body</a>"
        #"https://kjsce.somaiya.edu/en/students-association"
    },
    'programes' :{
        "The department imparts the skills and expertise in the areas of design, manufacturing and thermal sciences that are the backbone of most sectors of industry. The department is committed to provide quality education in mechanical engineering that enables students to achieve excellence in their field of specialization. It strives to ensure an academic ambience that is important for encouraging the culture of research, development and innovation amongst students."
        "For more information please visit the following link!"
        "<a href='https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-mechanical-engineering'></a>"
        #"https://kjsce.somaiya.edu/en/programme/bachelor-of-technology-mechanical-engineering"
    },
    'admissions' :{
        "For admission , intrested student are required to give Somaiya Entrance Test-Engineering(SET-E)."
        "We are delighted that you are considering an B.Tech programme at K J Somaiya College of Engineering. Please read all instructions and requirements carefully to ensure a complete and correct application on the provided link:"
        #"https://kjsce.somaiya.edu/en/admission/btech"
        "<a href='https://kjsce.somaiya.edu/en/admission/btech'></a>"
        "Feel free to contact us on admission.engg@somaiya.edu in case of any queries."
    }
        
    }
            
           }
           
    return Mech

def add_all():
    db_dict = {}
    Comps = add_compsdata()
    Etrx = add_etrxdata()
    EXTC = add_extcdata()
    IT = add_ITdata()
    Mech = add_mechdata()
    branch = [Comps , Etrx , EXTC , IT , Mech]
    for w in branch:
        db_dict.update(w)
    with open('db_dict.pickle', 'wb') as handle:
        pickle.dump(db_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print("Dict created")
    #return db_dict


add_all()



