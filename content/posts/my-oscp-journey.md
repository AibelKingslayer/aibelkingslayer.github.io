---
title: "My OSCP Journey"
author: "Aibel"
date: 2025-08-12
draft: false
tags: ["OSCP", "certification", "penetration-testing", "cybersecurity"]
description: "A deep dive into my experience preparing for and passing the Offensive Security Certified Professional (OSCP) certification — including what worked, what failed, and the mindset that got me through."
---

## What is OSCP

The Offensive Security Certified Professional (OSCP) is a highly regarded certification in the field of cybersecurity, offered by Offensive Security. It is designed to test a candidate's ability to think critically and apply practical penetration testing skills in real-world scenarios. The OSCP certification is especially valued among cybersecurity professionals, as it demonstrates hands-on expertise in ethical hacking and penetration testing.

### Key Highlights of OSCP:

1. **Practical Focus:** Unlike many theoretical certifications, OSCP emphasizes hands-on skills. It's not just about knowing the concepts; it's about applying them effectively.

2. **Challenging Nature:** The exam is known for its difficulty, pushing candidates to think like an attacker and solve complex problems under time constraints.

3. **Recognition:** OSCP is widely recognized and respected by employers, making it a valuable addition to any cybersecurity professional's resume.

### About the OSCP Exam:

The OSCP exam is a rigorous 24-hour challenge designed to assess a candidate's penetration testing skills. Here's what you need to know:

#### 1. **Structure of the Exam:**

- Candidates are provided with a virtual network of machines to exploit.

- The goal is to gain administrative (root) access to as many machines as possible within the allotted time.

- Each machine carries a specific point value, and candidates need to achieve a minimum of 70/100 score to pass.

#### 2. **Exam Requirements:**

- Exploitation involves enumeration, vulnerability assessment, and manual exploitation techniques.

- Candidates must submit a detailed report outlining the steps taken to exploit the machines, including screenshots and technical details.

#### 3. **Timeframe:**

- The exam lasts 24 hours, after which candidates have an additional 24 hours to submit their report.

- Proper time management is crucial, as candidates need to balance exploitation efforts and documentation.

#### 4. **Topics Covered:**

- **Introduction to Cybersecurity**
- **Effective Learning Strategies**
- **Information Gathering**
- **Vulnerability Scanning**
- **Introduction to Web Applications**
- **Common Web Application Attacks**
- **SQL Injection Attacks**
- **Client-Side Attacks**
- **Locating Public Exploits**
- **Fixing Exploits**
- **Antivirus Evasion**
- **Password Attacks**
- **Windows Privilege Escalation**
- **Linux Privilege Escalation**
- **Port Redirection and SSH Tunneling**
- **Advanced Tunneling**
- **The Metasploit Framework**
- **Active Directory Introduction and Enumeration**
- **Attacking Active Directory Authentication**
- **Lateral Movement in Active Directory**
- **Report Writing for Penetration Testers**
- **Assembling the Pieces**
- **Trying Harder: The Labs**

## Preparing for OSCP:

#### 1. **Official PWK Training:**

The Offensive Security Penetration Testing with Kali Linux (PWK) course is the official training for OSCP. This course includes:

- **Comprehensive Study Materials:** The provided PDFs and videos cover various penetration testing topics, from basic concepts to advanced techniques.

- **Lab Environment:** The PWK labs simulate real-world scenarios, allowing candidates to practice enumeration, exploitation, and privilege escalation in a controlled environment.

#### 2. **Hands-On Practice:**

Practical experience is key to succeeding in the OSCP exam. Here are some ways to build your skills:

- **Vulnerable Machine Platforms:** Practice on platforms like Hack The Box, TryHackMe, PG Practice and VulnLab etc. These platforms offer a wide variety of machines with varying levels of difficulty.

- **Buffer Overflow Exploitation:** Learn how to identify and exploit buffer overflow vulnerabilities, as these are a critical component of the exam.

- **Privilege Escalation:** Practice both Windows and Linux privilege escalation techniques, as they are essential for gaining root or administrative access.

#### 3. **Tools and Techniques:**

Familiarize yourself with essential tools and techniques, including:

- **Nmap:** For network scanning and enumeration. Don't overlook the importance of performing UDP scans, as certain services may only be accessible through UDP and could be crucial for exploitation.

- **Metasploit:** While limited use is allowed during the exam, understanding its functionalities is beneficial.

- **Burp Suite:** For web application testing and debugging.

- **Manual Exploitation:** Learn to exploit vulnerabilities without relying solely on automated tools.

- **Backup Plans:** Always have a backup plan. Learn more than one technique or use more than one tool for a specific task. Some tools or techniques might fail in certain situations, while alternatives can help you succeed.

#### 4. **Learning Resources:**

Enhance your knowledge using additional resources, such as:

- **HTB Academy:** A platform offering guided learning paths for various penetration testing techniques.

- **TCM Security Courses:** Focused training on Windows privilege escalation, Linux privilege escalation, and practical ethical hacking.

- **TryHackMe Learning Paths:** Valuable paths like Junior Penetration Tester, Offensive Pentesting, and OWASP Top 10 Web Application Attacks provide structured guidance.

#### 5. **Documentation Skills:**

- Practice documenting your findings during preparation. Good documentation is critical for both the exam and your final report submission.

- Use templates to streamline your reporting process and ensure all necessary details are included.

#### 6. **Tips, Tricks, and Cheatsheets:**

Utilize comprehensive guides and resources to aid your learning and troubleshooting:

- **Hacktricks:** [https://book.hacktricks.xyz/](https://book.hacktricks.xyz/)

- **PayloadAllTheThings:** [https://github.com/swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)

#### 7. **Time Management:**

- Create a schedule during your preparation phase to cover all topics systematically.

- During the exam, allocate time wisely to ensure all machines are addressed, and leave enough time for documentation.

#### 8. **Community and Support:**

- Join online forums, Discord servers, or Reddit communities dedicated to OSCP preparation. Engaging with others can provide insights, tips, and encouragement.

- Study groups can also help you stay motivated and learn from others' experiences.

#### 9. **Mindset and Persistence:**

- Develop a problem-solving mindset. The OSCP exam tests your ability to think critically and adapt to unexpected challenges.

- Be persistent. Failure is part of the learning process, and each setback provides an opportunity to improve.

---

## The Journey:

Passing the OSCP was a transformative experience. It required months of preparation, countless hours of practice, and unwavering determination. The exam challenged me not only technically but also mentally. Here are some takeaways from my journey:

- **First Attempt:** I didn't pass on my first attempt, but this failure was a valuable learning experience. It taught me to refine my strategies, improve my time management, and focus more on areas where I was weak.

#### Second Attempt and Success:

After my initial failure, I re-evaluated my preparation approach. I focused on:

- **Strengthening Weak Areas:** I identified the topics and techniques where I struggled and dedicated extra time to mastering them.

- **Enhanced Practice:** I worked on additional machines on platforms like Hack The Box and PG Practice, ensuring I encountered diverse scenarios.

- **Time Management:** I implemented a structured approach during the exam, allocating specific times for enumeration, exploitation, and documentation.

- **Consistency is Key:** Regular practice and revisiting fundamental concepts helped me build a strong foundation.

- **Lab Work:** The PWK labs were invaluable for honing my skills and building confidence.

- **HTB Academy:** HTB Academy was an essential resource during my preparation. Its structured learning paths and practical exercises provided clarity on advanced topics and helped me approach challenges more methodically.

- **UDP Scans:** I learned the importance of performing UDP scans. Several services critical to exploitation were only accessible through UDP, highlighting the need for thorough scanning.

- **Backup Plans:** Having backup plans for tools and techniques proved invaluable. When one method failed, alternative tools or strategies ensured continued progress.

- **Documentation:** Maintaining detailed notes during preparation proved essential during the exam and for writing the final report.

Achieving the OSCP has not only validated my technical skills but also opened new doors in my cybersecurity career. It's more than just a certification, it's a testament to perseverance and expertise. Achieving the OSCP was a moment of pride not just for me but for my family. My success surprised everyone, and I was showered with gifts and encouragement from my cousins, who were thrilled by my accomplishment.

---

## Final Thoughts:

The OSCP journey is challenging but incredibly rewarding. Here are my final words:

- **Don't Panic:** Stay calm and composed during the exam. Break tasks into smaller steps and tackle them methodically.

- **Believe in Yourself:** Confidence in your preparation and abilities can make a significant difference.

- **Stay Focused:** Avoid distractions and stick to your planned strategy.

To anyone preparing for the OSCP, remember: _You can do it!_ With persistence, practice, and the right mindset, this goal is absolutely achievable. Good luck on your journey!
