# VPS Daily Health Report 📊

A production-ready Python monitoring tool that collects daily system metrics from a Linux VPS (Hetzner, AWS, DigitalOcean, etc.) and sends a **beautiful HTML email report with embedded charts**.

This project is designed for **reliability, email compatibility, and automation**, making it ideal for daily infrastructure health reporting.

---

## 🚀 Features

- ✅ Collects real-time VPS metrics using `psutil`
- ✅ CPU usage monitoring
- ✅ Memory usage monitoring
- ✅ Load average & system summary
- ✅ Generates **email-safe PNG charts** (no JavaScript)
- ✅ Sends **professional HTML email reports**
- ✅ Works with Gmail SMTP (App Password supported)
- ✅ Designed for **CRON-based daily scheduling**
- ✅ Compatible with Hetzner VPS and other Linux servers

---

## 🖥️ Metrics Included

- CPU usage percentage
- Memory usage percentage
- Total RAM (GB)
- CPU core count
- Load average (1m, 5m, 15m)
- Active logged-in users
- Timestamp of report generation

---

## 📨 Email Preview

Each report includes:

- Branded HTML layout
- Summary health status (Healthy / Attention Required)
- Clean metrics table
- Embedded CPU & Memory usage charts
- Professional footer and support signature

> No JavaScript is used in emails to ensure compatibility with Gmail, Outlook, and Apple Mail.

---

## 🛠️ Requirements

- Python 3.8+
- Linux-based server (recommended)
- Gmail account with App Password enabled

### Python Dependencies

```bash
pip install psutil matplotlib
```

⚙️ **Setup & Usage**

1️⃣ Clone the Repository
```bash
git clone
cd vps-daily-health-report
```

2️⃣ Configure Email Settings

Edit the email configuration inside daily_vps_health_report.py:

```bash
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-gmail-app-password"

FROM_ALIAS = "Your Company Support <support@yourdomain.com>"
TO_EMAIL = "recipient@email.com"
CC_EMAILS = ["cc@email.com"]

⚠️ Important:
Use a Gmail App Password, not your normal email password.

```
3️⃣ Run Manually (Test)

Before scheduling, test the script:

```bash

python3 daily_vps_health_report.py

```

4️⃣ Schedule Daily Execution (CRON)

CRON allows Linux to run the script automatically.

Open the crontab editor:

```bash

crontab -e

```

Example: run the report every day at 9:00 AM:

```bash

0 9 * * * /usr/bin/python3 /home/ubuntu/daily_vps_health_report.py >> /home/ubuntu/vps_report.log 2>&1

```


✔ Uses full Python path
✔ Logs output for debugging
✔ Survives server reboots

**Verify CRON jobs:**

```bash
crontab -l
```

📂 Project Structure
```bash
vps-daily-health-report/
├── daily_vps_health_report.py
├── README.md
├── requirements.txt
├── cpu_usage.png        # auto-generated
├── memory_usage.png     # auto-generated
```

Chart images are generated automatically during execution.



🤝 **Contributing**
```bash
Contributions are welcome!

Fork the repository

Create a feature branch

Commit your changes

Submit a pull request
```

📜 **License**
```bash
MIT License
Free to use, modify, and distribute.
```
