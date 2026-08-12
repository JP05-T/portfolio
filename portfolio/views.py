import datetime

from pyramid.view import view_config


@view_config(route_name="home", renderer="index.jinja2")
def home(request):
    return {
        "current_year": datetime.date.today().year,
        "site_url": "https://jaya-prakash-portfolio.netlify.app",
        "name": "Jaya Prakash T",
        "tagline": "JP MCA Student | Python Developer | Learner",
        "profile": (
            "Optimistic MCA student with hands-on experience in Python-based projects, "
            "database management, and web technologies. Passionate about building "
            "real-world applications and continuously improving technical and "
            "problem-solving skills. Seeking an entry-level software or IT role to "
            "contribute effectively to organizational growth."
        ),
        "education": [
            {
                "degree": "Master of Computer Applications (MCA)",
                "school": "Sri Manakula Vinayagar Engineering College, Puducherry, India",
                "years": "June 2026",
                "details": "Percentage: 84.2%",
            },
            {
                "degree": "Bachelor of Science in Chemistry",
                "school": "Vels University, Chennai, India",
                "years": "May 2024",
                "details": "Percentage: 67%",
            },
            {
                "degree": "Class XII (HSC)",
                "school": "John Dewey Matriculation Higher Secondary School, Panruti, India",
                "years": "2021",
                "details": "Percentage: 73%",
            },
            {
                "degree": "Class X (SSLC)",
                "school": "John Dewey Matriculation Higher Secondary School, Panruti, India",
                "years": "2019",
                "details": "Percentage: 63.2%",
            },
        ],
        "skills": [
            "Python",
            "JavaScript",
            "Oracle SQL",
            "Bootstrap",
            "C (Basic)",
            "Communication",
            "Problem Solving",
            "Teamwork",
            "Time Management",
        ],
        "soft_skills": [
            "Teamwork",
            "Time Management",
            "Leadership",
            "Effective Communication",
        ],
        "internship": {
            "role": "Intern - Artificial Intelligence (Academic Project)",
            "company": "Nexware Technologies Pvt Ltd",
            "location": "Coimbatore, Tamil Nadu, India",
            "years": "January 2026 - May 2026",
            "project": (
                "Visual Audit Framework for Preventing E-Commerce Delivery and Return "
                "Fraud"
            ),
            "details": (
                "Completed a 5-month internship with an academic project in the "
                "Artificial Intelligence domain using Python and MySQL. Gained "
                "hands-on experience in industry-relevant technologies, problem-solving, "
                "and system optimization, showcasing strong analytical skills, "
                "adaptability, and a commitment to learning."
            ),
        },
        "projects": [
            {
                "title": "Personal Portfolio Website",
                "tech": "Python, Pyramid, Jinja2, Bootstrap 5",
                "image": "",
                "url": "",
                "details": (
                    "Designed and built this personal portfolio website to showcase my "
                    "education, skills, projects, and certifications. Built with the "
                    "Pyramid web framework, Jinja2 templating, and Bootstrap 5 for a "
                    "responsive, mobile-friendly design."
                ),
            },
            {
                "title": "CardioAI - Heart Disease Prediction System",
                "tech": "Python, Django, XGBoost, scikit-learn, Bootstrap, Chart.js",
                "image": "",
                "url": "",
                "demo": "https://jp-mca-heart-health-prediction.onrender.com",
                "details": (
                    "Web-based heart disease prediction system using machine learning to "
                    "assess cardiovascular risk from 13 clinical parameters, achieving "
                    "98.6% accuracy with an XGBoost model trained on the UCI Cleveland "
                    "heart disease dataset. Features include instant risk prediction, "
                    "personalized health recommendations, downloadable PDF medical "
                    "reports, user authentication, and a custom admin portal with "
                    "Chart.js dashboards. Deployed on Render.com."
                ),
            },
            {
                "title": "Flight Tracker System",
                "tech": "Python, OpenSky Network API, Tkinter",
                "image": "",
                "details": (
                    "Developed a real-time flight tracking application using Python and "
                    "OpenSky Network API for Indian airspace. Implemented callsign-based "
                    "search with live flight details and map visualization using Tkinter."
                ),
            },
            {
                "title": "Visual Audit Framework for E-Commerce Fraud Prevention",
                "tech": "YOLOv9, Siamese Networks, Deep Learning",
                "image": "",
                "details": (
                    "Co-authored a deep learning framework combining YOLOv9 object "
                    "detection and Siamese Networks to automatically detect and prevent "
                    "e-commerce return fraud. Engineered an end-to-end video pipeline "
                    "with a custom multi-modal decision engine, reducing manual "
                    "inspection overhead and providing auditable evidence for dispute "
                    "resolution."
                ),
            },
        ],
        "certifications": [
            {
                "title": "CCNA: Enterprise Networking, Security & Automation",
                "issuer": "Cisco",
                "date": "Feb 2026",
                "image": "certificates/ccna-enterprise-networking.png",
                "url": "",
            },
            {
                "title": "CCNA: Switching, Routing & Wireless Essentials",
                "issuer": "Cisco",
                "date": "Jul 2025",
                "image": "certificates/ccna-switching-routing-wireless.png",
                "url": "",
            },
            {
                "title": "AWS Academy Cloud Foundations",
                "issuer": "Amazon Web Services",
                "date": "May 2025",
                "image": "certificates/aws-cloud-foundations.png",
                "url": "https://www.credly.com/go/YDfI0GEH",
            },
            {
                "title": "Databases: Relational Databases & SQL",
                "issuer": "Stanford Online (edX)",
                "date": "May 2025",
                "image": "certificates/stanford-databases-sql.png",
                "url": "",
            },
            {
                "title": "Python Essentials 1",
                "issuer": "Cisco",
                "date": "Feb 2026",
                "image": "certificates/python-essentials.png",
                "url": "",
            },
        ],
        "languages": ["English", "Tamil"],
        "contact": {
            "email": "tjayaprakash60@gmail.com",
            "phone": "+91 99652 27461",
            "github": "https://github.com/JP05-T",
            "linkedin": "https://linkedin.com/in/jaya-prakash-t-405463350",
        },
    }
