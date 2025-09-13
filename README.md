#StaffSync(FAMS)

In response to the growing complexity of managing faculty activities within the Information Technology Department of SSN, this project endeavours to design and implement a robust **Faculty Activities Management System (FAMS)**.

Recognizing the need for an efficient, user-friendly, and technology-driven solution, the system leverages **Django, HTML, CSS, and JavaScript** to provide a centralized platform for faculty and administrators.

---

## 🚀 Features
- **Admin and Faculty Logins**: Role-based authentication for secure access.  
- **Staff Development Program (SDP) Management**: Organize and track SDP events.  
- **Attendance Tracking**: Record and manage SDP attendance.  
- **Approval Workflow**: Requests for activities go through an approval process for better transparency and accountability.  
- **Reports**: Generate detailed reports for faculty activities and events.  
- **Scalable Design**: Built with Django for flexibility and future scalability.  
---

## 🛠 Tech Stack
- **Backend**: Django (Python)  
- **Frontend**: HTML, CSS, JavaScript  
- **Database**: SQLite (default) or configurable for other RDBMS  
- **Other Tools**: Bootstrap, Django ORM  
---

## ⚙️ Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fams.git
   cd fams

2.python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows

3.pip install -r requirements.txt

4.python manage.py migrate

5.python manage.py runserver


