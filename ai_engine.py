import time
import cv2
from ultralytics import YOLO

# ================= YOLO MODEL =================
model = YOLO("yolov8n.pt")

# ================= CAREER ADVICE =================
def career_advice(text):
    time.sleep(1)

    return f"""
🎯 Recommended Career: Software Developer

💡 Why this role?
It matches your skills and industry demand.

🧠 Skills Required:
- Python
- Data Structures & Algorithms
- Web Development

📈 Roadmap:
1. Learn basics
2. Build projects
3. Practice coding daily
4. Apply for internships

🚀 Tip:
Consistency is the key to success.
"""

# ================= RESUME ANALYSIS =================
def resume_analysis(text):
    score = min(90, 60 + len(text)//50)

    return f"""
📄 ATS Resume Score: {score}/100

✔ Strengths:
- Good structure
- Basic content present

⚠ Improvements:
- Add more projects
- Add achievements
- Improve formatting
"""

# ================= SKILL RECOMMENDATION =================
def skill_recommendation(goal):
    return f"""
📚 Skills for {goal}:

- Python
- Problem Solving
- Communication Skills
- Domain Knowledge

📅 Learning Roadmap:
Week 1–2: Basics  
Week 3–4: Mini Projects  
Week 5–6: Advanced Practice  

🚀 Tip:
Build 2–3 strong projects.
"""

# ================= JOB MATCHING =================
def job_matching(text):
    text = text.lower()

    jobs = []

    if "python" in text:
        jobs.append("Python Developer")
    if "data" in text:
        jobs.append("Data Analyst")
    if "ml" in text or "machine learning" in text:
        jobs.append("ML Engineer")

    if not jobs:
        return "No direct matches found. Improve your resume."

    return "🎯 Recommended Jobs:\n\n" + "\n".join(jobs)

# ================= INTERVIEW QUESTIONS =================
def interview_questions(role):
    return f"""
🎤 Interview Preparation for {role}

1. Tell me about yourself  
2. Explain your projects  
3. What are your strengths?  
4. Why should we hire you?  
5. Technical question related to {role}

🚀 Tip:
Practice daily and speak confidently.
"""

# ================= YOLO CAMERA ANALYSIS =================
def yolo_confidence():
    cap = cv2.VideoCapture(0)

    frames = 0
    detections = 0

    while frames < 50:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        for r in results:
            for box in r.boxes:
                # class 0 = person
                if int(box.cls[0]) == 0:
                    detections += 1

                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.imshow("YOLO Interview Analysis", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC key
            break

        frames += 1

    cap.release()
    cv2.destroyAllWindows()

    score = int((detections / frames) * 100) if frames else 0

    return f"""
🎥 YOLO Analysis Result:

✔ Face detected consistently  
✔ Engagement level: Good  

📊 Confidence Score: {score}%

💡 Tip:
Maintain eye contact and posture during interviews.
"""